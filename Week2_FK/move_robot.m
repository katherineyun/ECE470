function move_robot(vrep,clientID, theta)
    for i = 1:6
        [result, joint_handle] = vrep.simxGetObjectHandle(clientID, strcat('UR3_joint',num2str(i)), vrep.simx_opmode_blocking);
        
        if result ~= vrep.simx_return_ok
            disp(strcat('could not get joint',num2str(i),' handle'));
        end
        
        vrep.simxSetJointTargetPosition(clientID, joint_handle, degtorad(theta(i)), vrep.simx_opmode_oneshot);  
        pause(1);
    end

end
