#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import time
import rospy

def go_home(req):
    rospy.loginfo("“going to home”")
    time.sleep (2)
    rospy.loginfo("“arrived”")
    return EmptyResponse()

def go_to_kitchen(req):
    rospy.loginfo("“going to kitchen”")
    time.sleep (2)
    rospy.loginfo("“arrived”")
    return EmptyResponse()
    
def stop(req):
    rospy.loginfo("“stop”")
    return EmptyResponse()
        
    
def trigger_server():
    rospy.init_node('trigger_server')
    home_ = rospy.Service('/go_home', Empty, go_home)
    print("Ready to do something.")

    kitchen_ = rospy.Service('/go_to_kitchen', Empty, go_to_kitchen)
    print("Ready to do something.")

    stop_ = rospy.Service('/stop', Empty, stop)
    print("Ready to do something.")
    rospy.spin()    
    
if __name__ == "__main__":
    trigger_server()
    
