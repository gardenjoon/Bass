#!/usr/bin/env python

import serial
import rospy
from std_msgs.msg import Float64
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout =1)

def ang():
    pub= rospy.Publisher('imu',Float64,queue_size=10)
    rospy.init_node('imu',anonymous =True)
    while not rospy.is_shutdown():
        b=ser.readline()
        print(b)
        pub.publish(b)

if __name__=='__main__':
    try:
        ang()
    except rospy.ROSInterruptException:
        pass
