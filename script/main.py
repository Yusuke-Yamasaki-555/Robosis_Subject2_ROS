#!/usr/bin/env python3
# Subscriber

import rospy
from std_msgs.msg import Int32
from mypkg.srv import SetInt

n = -3

def main():
    global n

    rospy.init_node('main')

    cup = rospy.Subscriber('count_up', Int32, cb_cup)
    rospy.loginfo("Start Subscriber 'count_up'")

    check = rospy.ServiceProxy('check', SetInt)
    rospy.loginfo("Waiting check-server")
    rospy.wait_for_service('check')
    rospy.loginfo("Start che-server")

    rate = rospy.Rate(10)

    print("Number | Least common multiple")

    while not rospy.is_shutdown():
        check_b = int(n)
        check_res = check(check_b)

        print("   "+str(n)+"  | "+check_res.result)
        rate.sleep()


def cb_cup(message):
    global n
    
    n = int(message.data)


if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()

    except rospy.ROSInterruptException:
        pass

