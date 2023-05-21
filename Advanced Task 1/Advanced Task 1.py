from djitellopy import Tello
import time
drone = Tello()

drone.connect()
drone.enable_mission_pads()
drone.takeoff()
drone.move_up(30)

pad = -1
# check that drone detect mission pad that is put in front of first obstacle
while pad == -1:
    pad = drone.get_mission_pad_id()
print(pad)
# go to center of mission pad
drone.go_xyz_speed_mid(0,0,105,30,pad)
# set this to the distance to fly to go over the obstacle 1
drone.move_forward(180)

# check that drone detect mission pad that is put in front of second obstacle
pad=-1
while pad == -1:
    pad = drone.get_mission_pad_id()

print(pad)
drone.go_xyz_speed_mid(0,0,60,30,pad)

drone.move_forward(190)
pad = -1
time.sleep(3)
# check that drone detect mission pad that is put in front of third obstacle

while pad == -1:
    pad = drone.get_mission_pad_id()
print(pad)

drone.go_xyz_speed_mid(0,0,45,30,pad)
drone.move_forward(150)
drone.land()