#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
import numpy as np

class driver():

    def init(self):
        self.pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.targetX = 0;
        self.targetY = 0;
        print("init")

    def run(self):
        try:
            self.init()
            r = rospy.Rate(10)
            while not rospy.is_shutdown():

                self.twist = Twist()
                self.twist.linear.x = 1
                self.twist.angular.z = 0.25
                self.pub_twist.publish(self.twist)
		        print("published")
                r.sleep()
        except rospy.exceptions.ROSInterruptException:
            pass

    def listenForTarget(self):
        self.target_subscriber = rospy.Subscriber('/target', Pose, updateTarget)


    def updateTarget(msg):
        self.targetX = msg.pose.position.x;
        self.targetY = msg.pose.position.y;
        print("updated position to    X: ", self.targetX,"    Y: ", self.targetY)

if __name__ == '__main__':
    rospy.init_node('drive')
    d = driver()
    d.run()
    d.listenForTarget()
