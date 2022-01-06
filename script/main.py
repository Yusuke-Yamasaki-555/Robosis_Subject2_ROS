#!/usr/bin/env python3


import rospy
from std_msgs.msg import Int32
from mypkg.srv import SetInt

n = -2

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

    print(" 数字 | 2  | 3  | 5  | 7  | 11 | 13 | 17 | 19 | 23 | 29 |")
    print("ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー")

    while not rospy.is_shutdown():
        if int(n) == -2:
            continue

        check_res = check(int(n))

        print("   " + str(n) + "  | " + \
                ("● " if check_res.result[0] else "  ") + " | " + \
                ("● " if check_res.result[1] else "  ") + " | " + \
                ("● " if check_res.result[2] else "  ") + " | " + \
                ("● " if check_res.result[3] else "  ") + " | " + \
                ("● " if check_res.result[4] else "  ") + " | " + \
                ("● " if check_res.result[5] else "  ") + " | " + \
                ("● " if check_res.result[6] else "  ") + " | " + \
                ("● " if check_res.result[7] else "  ") + " | " + \
                ("● " if check_res.result[8] else "  ") + " | " + \
                ("● " if check_res.result[9] else "  ") + " |")
        print("ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー")
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

