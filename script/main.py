#!/usr/bin/env python3
'''
その数字を割り切ることが出来る素数を判定して、結果を出力していきたい。

素数：2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ・・・

課題：serviceで使用するmessageの型に、リストを使えるのかどうか(数値ならいけることはわかっている。文字でいけるかが問題)（文字でいけなくても数値で判定してまた別の手段で置き換えてやればいい）
'''

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

        print("   "+str(n)+"  | "+check_res.result) # -3だけ出力させないようにしたほうが良さげ
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

