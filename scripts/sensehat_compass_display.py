#!/usr/bin/env python

import rospy
from sensehat_driver.msg import IMUOrientation
from sense_hat import SenseHat
from sensor_msgs.msg import Imu

def heading_correction_handler(req):
    print("Returning %s" % req.a)
    
def compass_callback(data):
    #rospy.loginfo("yaw: %f" % data.yaw)
    
    if (45 <= data.yaw < 135):
        sense.show_letter("E")
    elif (135 <= data.yaw < 225):
        sense.show_letter("S")
    elif (225 <= data.yaw < 315):
        sense.show_letter("W")
    else:
        sense.show_letter("N")

def sub_imu_data():
    rospy.Subscriber("imu_euler", IMUOrientation, compass_callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node("sensehat_compass_display", anonymous=True) 
    sense = SenseHat()
    sense.clear()
    sub_imu_data()

    
