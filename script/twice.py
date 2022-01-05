#!/usr/bin/env python3
# Subscriber

import rospy
from std_msgs.msg import Int32
# from std_srvs.srv import SetBool

n = 0

def main():
    rospy.init_node('main')

    cup = rospy.Subscriber('count_up', Int32, cb_cup)
    rospy.loginfo("Start Subscriber 'count_up'")

    # che = rospy.ServiceProxy('check', SetBool)
    rospy.loginfo("Waiting check-server")
    # che.wait_for_server()
    rospy.loginfo("Start che-server")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        #che_res = che(n)
        #print(n)
        #rate.sleep()


def cb_cup(message):
    global n
    
    n = message.data


if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()

    except rospy.ROSInterruptException:
        pass

