#!/usr/bin/env python3

'''License
 SPDX-License-Identifier:MIT
 Copyright (C) 2022 Yusuke Yamasaki & Ryuichi Ueda. All Rights Reserved.
'''

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

    rospy.sleep(0.5)
    rospy.loginfo("Start Program")

    rospy.sleep(0.5)
    print("\n\
  ==================================================================\n\
  ==    素数の倍数を判定するプログラムです。                      ==\n\
  ==    対象の素数は、２～２９の範囲にある１０個となっています。  ==\n\
  ==    左端の数字が素数の倍数になっていれば、　　　　　　　　　　==\n\
  ==  その素数に対応する列に●印が付きます。                      ==\n\
  ==                                                              ==\n\
  ==    このプログラムは無限に続く仕様になっています。            ==\n\
  ==    プログラム終了方法：Ctrl+Cを入力                          ==\n\
  ==================================================================\n")

    rospy.sleep(1.0)
    print(" 数字 | 2  | 3  | 5  | 7  | 11 | 13 | 17 | 19 | 23 | 29 |")
    print("ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    
    rospy.sleep(0.5)
    while not rospy.is_shutdown():
        if int(n) == -2:
            continue

        check_res = check(int(n))

        print("   " + str(n) + "  | " + \
                ("●" if check_res.result[0] else "  ") + " | " + \
                ("●" if check_res.result[1] else "  ") + " | " + \
                ("●" if check_res.result[2] else "  ") + " | " + \
                ("●" if check_res.result[3] else "  ") + " | " + \
                ("●" if check_res.result[4] else "  ") + " | " + \
                ("●" if check_res.result[5] else "  ") + " | " + \
                ("●" if check_res.result[6] else "  ") + " | " + \
                ("●" if check_res.result[7] else "  ") + " | " + \
                ("●" if check_res.result[8] else "  ") + " | " + \
                ("●" if check_res.result[9] else "  ") + " |")
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

