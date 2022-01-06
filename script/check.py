#!/usr/bin/env python3

'''License
 SPDX-License-Identifier:MIT
 Copyright (C) 2022 Yusuke Yamasaki. All Rights Reserved.
'''

import rospy
from mypkg.srv import SetInt, SetIntResponse

def main():
    rospy.init_node('check')

    che = rospy.Service('check', SetInt, check)

    rospy.loginfo("check-server Ready")
    rospy.spin()


def check(data):
    resp = SetIntResponse()

    resp.result.append(True) if data.data != 0 and data.data%2 == 0 else resp.result.append(False)  # [0]
    resp.result.append(True) if data.data != 0 and data.data%3 == 0 else resp.result.append(False)  # [1]
    resp.result.append(True) if data.data != 0 and data.data%5 == 0 else resp.result.append(False)  # [2]
    resp.result.append(True) if data.data != 0 and data.data%7 == 0 else resp.result.append(False)  # [3]
    resp.result.append(True) if data.data != 0 and data.data%11 == 0 else resp.result.append(False) # [4]
    resp.result.append(True) if data.data != 0 and data.data%13 == 0 else resp.result.append(False) # [5]
    resp.result.append(True) if data.data != 0 and data.data%17 == 0 else resp.result.append(False) # [6]
    resp.result.append(True) if data.data != 0 and data.data%19 == 0 else resp.result.append(False) # [7]
    resp.result.append(True) if data.data != 0 and data.data%23 == 0 else resp.result.append(False) # [8]
    resp.result.append(True) if data.data != 0 and data.data%29 == 0 else resp.result.append(False) # [9]

    return resp


if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()

    except rospy.ROSInterruptException:
        pass


