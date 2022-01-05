#!/usr/bin/env python3
# The Publisher

import rospy
from std_msgs.msg import Int32

def main():
    rospy.init_node('count')

    pub = rospy.Publisher('count_up', Int32, queue_size=1)
    rospy.loginfo("Start publisher 'count_up'")

    rate = rospy.Rate(10)

    n = -3

    while not rospy.is_shutdown():
        n += 1
        pub.publish(n)
        # print(n)
        rate.sleep()


if __name__ == "__main__":
    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
