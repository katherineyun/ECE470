import vrep
import time
import numpy as np

# Close all open connections (just in case)
vrep.simxFinish(-1)

# Connect to V-REP (raise exception on failure)
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID == -1:
    raise Exception('Failed connecting to remote API server')

# Get "handles"
result, j2handle = vrep.simxGetObjectHandle(clientID, 'Sawyer_joint2', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get object handle for second joint')

result, j1handle = vrep.simxGetObjectHandle(clientID, 'Sawyer_joint1', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get object handle for first joint')

result, j3handle = vrep.simxGetObjectHandle(clientID, 'Sawyer_joint3', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get object handle for third joint')

result, j4handle = vrep.simxGetObjectHandle(clientID, 'Sawyer_joint4', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get object handle for fourth joint')

result, j5handle = vrep.simxGetObjectHandle(clientID, 'Sawyer_joint5', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get object handle for fifth joint')

result, j6handle = vrep.simxGetObjectHandle(clientID, 'Sawyer_joint6', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get object handle for sixth joint')

result, j7handle = vrep.simxGetObjectHandle(clientID, 'Sawyer_joint7', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get object handle for seventh joint')


#start simulation
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

time.sleep(2)

result, theta2 = vrep.simxGetJointPosition(clientID, j2handle, vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get second joint variable')

vrep.simxSetJointTargetPosition(clientID, j2handle, theta2 + (np.pi/2), vrep.simx_opmode_oneshot)

time.sleep(2)

result, theta1 = vrep.simxGetJointPosition(clientID, j1handle, vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get first joint variable')

vrep.simxSetJointTargetPosition(clientID, j1handle, theta1 - (np.pi/2), vrep.simx_opmode_oneshot)

time.sleep(2)

result, theta3 = vrep.simxGetJointPosition(clientID, j3handle, vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get thrid joint variable')

vrep.simxSetJointTargetPosition(clientID, j3handle, theta3 - (np.pi/3), vrep.simx_opmode_oneshot)

time.sleep(2)

result, theta4 = vrep.simxGetJointPosition(clientID, j4handle, vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get fourth joint variable')

vrep.simxSetJointTargetPosition(clientID, j4handle, theta4 - (np.pi/6), vrep.simx_opmode_oneshot)

time.sleep(2)

result, theta5 = vrep.simxGetJointPosition(clientID, j5handle, vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get fifth joint variable')

vrep.simxSetJointTargetPosition(clientID, j5handle, theta5 - (np.pi/6), vrep.simx_opmode_oneshot)

time.sleep(2)

result, theta6 = vrep.simxGetJointPosition(clientID, j6handle, vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get sixth joint variable')

vrep.simxSetJointTargetPosition(clientID, j6handle, theta6 - (np.pi/6), vrep.simx_opmode_oneshot)

time.sleep(2)

result, theta7 = vrep.simxGetJointPosition(clientID, j7handle, vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get sixth joint variable')

vrep.simxSetJointTargetPosition(clientID, j7handle, theta7 - (np.pi/6), vrep.simx_opmode_oneshot)

time.sleep(2)

#hit the ball
result, theta1 = vrep.simxGetJointPosition(clientID, j1handle, vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
    raise Exception('could not get first joint variable')

vrep.simxSetJointTargetPosition(clientID, j1handle, theta1 + (np.pi), vrep.simx_opmode_oneshot)

# Stop simulation
vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)

# Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
vrep.simxGetPingTime(clientID)

# Close the connection to V-REP
vrep.simxFinish(clientID)
