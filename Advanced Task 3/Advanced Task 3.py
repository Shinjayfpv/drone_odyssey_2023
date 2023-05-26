from djitellopy import Tello
import time
drone = Tello()

drone.connect()
drone.enable_mission_pads()
drone.takeoff()
drone.move_up(30)
takeoffmissionpad = -1
pad = -1

while pad == -1:
    pad = drone.get_mission_pad_id()
print(pad)
takeoffmissionpad = pad
# go to center of mission pad
#drone.go_xyz_speed_mid(0,0,60,30,pad)

time.sleep(3)
drone.move_forward(110)

pad = -1
time.sleep(3)
while pad == -1:
    pad = drone.get_mission_pad_id()

print(pad)
time.sleep(3)
#drone.go_xyz_speed_mid(0,0,60,30,pad)

if takeoffmissionpad != pad:
    drone.go_xyz_speed_mid(0,0,60,30,pad)
    time.sleep(3)
    drone.land()
else:
    drone.move_right(110)
    pad = -1
    
    time.sleep(3)
    
    while pad == -1:
        pad = drone.get_mission_pad_id()
    print(pad)
    

    
    if takeoffmissionpad != pad:
        drone.go_xyz_speed_mid(0,0,60,30,pad)
        time.sleep(3)
        drone.land()
    else:
        drone.move_right(110)
        pad = -1
    
        time.sleep(3)

        while pad == -1:
            pad = drone.get_mission_pad_id()
        print(pad)
       
        
        if takeoffmissionpad != pad:
            drone.go_xyz_speed_mid(0,0,60,30,pad)
            time.sleep(3)
            drone.land()
            pad = -1
            
            time.sleep(3)
            
            while pad == -1:
                pad = drone.get_mission_pad_id()
            print(pad)
            
            if takeoffmissionpad != pad:
                drone.go_xyz_speed_mid(0,0,60,30,pad)
                time.sleep(3)
                drone.land()
            else:
                drone.move_left(110)
                
                time.sleep(3)
                
                while pad == -1:
                    pad = drone.get_mission_pad_id()
                print(pad)
               # drone.go_xyz_speed_mid(0,0,60,30,pad)
                
                if takeoffmissionpad != pad:
                    drone.land()
                else:
                    drone.move_left(110)
                    time.sleep(3)
                    drone.land()
                
                
        
        