#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import numpy as np

class driver():

    def init(self):
        self.pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.lin = np.array([1,0,0])
        self.ang = np.array([0,0,0.25])
        print("init")

    def run(self):
        try:
            self.init()
            r = rospy.Rate(10)
            while not rospy.is_shutdown():
		print("entering while..")
                self.twist = Twist()
                self.twist.linear.x = 1
                self.twist.angular.z = 0.25
                self.pub_twist.publish(self.twist)
		print("published")
                r.sleep()
        except rospy.exceptions.ROSInterruptException:
            pass


if __name__ == '__main__':
    rospy.init_node('drive')
    d = driver()
    d.run()
