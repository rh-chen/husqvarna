#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
import numpy as np

class driver():

    def init(self):
        self.pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.target_subscriber = rospy.Subscriber('/target', Pose, self.updateTarget)
        self.odom_subcriber = rospy.Subscriber('/odom', Odometry, self.callback)

        self.mowerX = 0
        self.mowerZ_ang = 0
        self.targetX = 0
        self.targetY = 0
        self.posX = 0
        self.posY = 0
        self.posZ_ang = 0

        print("init")

    def run(self):
        try:
            self.init()
            r = rospy.Rate(10)
            while not rospy.is_shutdown():
                self.twist = Twist()
                self.twist.linear.x = self.speed()
                self.twist.angular.z = self.angular_vel()
                self.pub_twist.publish(self.twist)
                r.sleep()
        except rospy.exceptions.ROSInterruptException:
            pass


    def callback(self,odom):
        self.posX = odom.pose.pose.position.x
        self.posY = odom.pose.pose.position.y
        (roll, pitch, self.posZ_ang) = tf.transformations.euler_from_quaternion([odom.pose.pose.orientation.x, odom.pose.pose.orientation.y, odom.pose.pose.orientation.z ,odom.pose.pose.orientation.w])
        print("posX = ", self.posX)
        print("posZ_ang = ", self.posZ_ang)

    def updateTarget(self, msg):
        self.targetX = msg.position.x;
        self.targetY = msg.position.y;
        print("updated position to    X: ", self.targetX,"    Y: ", self.targetY)

    def distance(self):
        return sqrt(pow(self.targetY - self.posY, 2) + pow(self.targetX - self.posX, 2))

    def steering_angle(self):
        return atan2(self.targetY - self.posY, self.targetX - self.posX)

    def angular_vel(self,const = 3):
        return const*(self.steering_angle() - self.posZ_ang)

    def speed(self, const = 0.1):
        if self.distance() < 0.1:
            return 0
        else:
            return const*self.distance()


if __name__ == '__main__':
    rospy.init_node('drive')
    d = driver()
    d.run()
