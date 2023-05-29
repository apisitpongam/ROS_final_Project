#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy

def go_home():
    rospy.wait_for_service('trigger')
    try:
        trigger = rospy.ServiceProxy('/go_home', Empty)
        print("Please do something.")
        resp1 = trigger()       
        print("done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
def go_to_kitchen():
    rospy.wait_for_service('trigger')
    try:
        trigger = rospy.ServiceProxy('/go_to_kitchen', Empty)
        print("Please do something.")
        resp1 = trigger()       
        print("done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
       
def stop():
    rospy.wait_for_service('trigger')
    try:
        trigger = rospy.ServiceProxy('/stop', Empty)
        print("Please do something.")
        resp1 = trigger()       
        print("done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
                
if __name__ == "__main__":
    go_home()