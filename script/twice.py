#!/usr/bin/env python3
# Subscriber

import rospy
from std_msgs.msg import Int32

n = 0

def main():
    rospy.init_node('twice')

    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.loginfo("Start Subscriber 'count_up'")
    
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rospy.loginfo("Start Publisher 'twice'")

    rate = rospy.Rate(10)

    while True:
        pub.publish(n)
        rate.sleep()


def cb(message):
    global n
    
    n = message.data*2


if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass

