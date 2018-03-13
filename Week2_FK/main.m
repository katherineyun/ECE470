function main()
    disp('Program started');
    % vrep=remApi('remoteApi','extApi.h'); % using the header (requires a compiler)
    vrep=remApi('remoteApi'); % using the prototype file (remoteApiProto.m)
    vrep.simxFinish(-1); % just in case, close all opened connections
    clientID=vrep.simxStart('127.0.0.1',19997,true,true,5000,5);

    if (clientID>-1)
        disp('Connected to remote API server');
        
        %start simulation
        vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot);
        
        M = [0 0 -1 0; 0 1 0 0.192; 1 0 0 0.692; 0 0 0 1];
        
        s1 = skew_4([0;0;1],[0;0;0.152]);
        s2 = skew_4([-1;0;0],[0;0.12;0.152]);
        s3 = skew_4([-1;0;0],[0;0.12;0.396]);
        s4 = skew_4([-1;0;0],[0;0.27;0.609]);
        s5 = skew_4([0;0;1],[0;0.11;0.609]);
        s6 = skew_4([-1;0;0],[0;0.11;0.692]);
       
        ss1 = skew_6(s1);
        ss2 = skew_6(s2);
        ss3 = skew_6(s3);
        ss4 = skew_6(s4);
        ss5 = skew_6(s5);
        ss6 = skew_6(s6);

        theta1 = [50;-60;110;-120;-90;60];
        theta2 = [-50;-80;130;-130;-90;10];
        theta3 = [80;40;-30;60;-70;80];
        
        
        %==================================================================
        %First Configuration
        %==================================================================
        
        %Compute forward kinematics
        T = FK(ss1,ss2,ss3,ss4,ss5,ss6, M, theta3);
        disp(T);
        
        %Get rotation matrix and position vector
        R = [T(1,1) T(1,2) T(1,3); T(2,1) T(2,2) T(2,3); T(3,1) T(3,2) T(3,3)];
        p = [T(1,4);T(2,4); T(3,4)];
        
        %Convert rotation matrix to euler engles
        a = rotm2eul(R);
        
        
        %move robot to first configuration
        move_robot(vrep,clientID,theta3);
        pause(1);
        
        %==================================================================
        %Creat Dummy object
        %==================================================================
        vrep.simxCreateDummy(clientID, 0.05, [], vrep.simx_opmode_blocking);
        pause(0.5);
        [result, dummy_handle] = vrep.simxGetObjectHandle(clientID, 'Dummy', vrep.simx_opmode_blocking);
        if result ~= vrep.simx_return_ok
          disp('could not get dummy handle');
        end
        
        %Move dummy according to given pose
        vrep.simxSetObjectPosition(clientID,dummy_handle,-1,p,vrep.simx_opmode_oneshot);
        pause(1);

        vrep.simxSetObjectOrientation(clientID,dummy_handle,-1,a,vrep.simx_opmode_oneshot);
        pause(2);
        
        
        %==================================================================
        %End of Simulation
        %==================================================================
        %stop simulation
        vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot);
       
        % Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
        vrep.simxGetPingTime(clientID);

        % Now close the connection to V-REP:    
        vrep.simxFinish(clientID);
    else
        disp('Failed connecting to remote API server');
    end
    
    disp('Program ended');
end
