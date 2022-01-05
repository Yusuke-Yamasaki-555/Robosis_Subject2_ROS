#!/usr/bin/env python3

import rospy
from mypkg.srv import SetInt, SetIntResponse

def main():
    rospy.init_node('check')

    che = rospy.Service('check', SetInt, check)

    rospy.loginfo("check-server Ready")
    rospy.spin()


def check(data):
    resp = SetIntResponse()

    if data.data != 0 and data.data%2 == 0:
        resp.result = str(2)
    else:
        resp.result = str(None)

    return resp


if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()

    except rospy.ROSInterruptException:
        pass


