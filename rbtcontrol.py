#!/usr/bin/env python3
# license removed for brevity
import rospy
import time as t
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties
from std_msgs.msg import Header
from std_msgs.msg import String

a = ""

def setRun(pub,val):
    buff = ApplyJointEffort()
    buff.effort = val*80

    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)

    buff.joint_name = "cc_robot::left_wheel_hinge"
    pub(buff.joint_name,  buff.effort, start_time, end_time)
    buff.joint_name = "cc_robot::right_wheel_hinge"
    pub(buff.joint_name,  buff.effort, start_time, end_time)
    buff.joint_name = "cc_robot::left_b_wheel_hinge"
    pub(buff.joint_name,  buff.effort, start_time, end_time)
    buff.joint_name = "cc_robot::right_b_wheel_hinge"
    pub(buff.joint_name,  buff.effort, start_time, end_time)

def setRot(pub, val):
    buff = ApplyJointEffort()
    buff.effort = val*150
    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)

    buff.joint_name = "cc_robot::left_wheel_hinge"
    pub(buff.joint_name,  buff.effort, start_time, end_time)
    buff.joint_name = "cc_robot::right_wheel_hinge"
    pub(buff.joint_name, -buff.effort, start_time, end_time)
    buff.joint_name = "cc_robot::left_b_wheel_hinge"
    pub(buff.joint_name,  buff.effort, start_time, end_time)
    buff.joint_name = "cc_robot::right_b_wheel_hinge"
    pub(buff.joint_name, -buff.effort, start_time, end_time)


def getPos(pub):
    buff = GetJointProperties()
    buff.joint_name = 'cc_robot::left_wheel_hinge'
    val = pub(buff.joint_name)
    leftw = val.rate[0]

    buff.joint_name = 'cc_robot::left_b_wheel_hinge'
    val = pub(buff.joint_name)
    leftbw = val.rate[0]

    buff.joint_name = 'cc_robot::right_wheel_hinge'
    val = pub(buff.joint_name)
    rightw = val.rate[0]

    buff.joint_name = 'cc_robot::right_b_wheel_hinge'
    val = pub(buff.joint_name)
    rightbw = val.rate[0]
    v = (leftw, rightw, leftbw, rightbw)
    return v


def talkercw():#turn the robot left
#    pub = rospy.Publisher('/gazebo/apply_joint_effort', ApplyJointEffort, queue_size=10)
    rospy.init_node('cc_ctrl', anonymous=True)
    pub    = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    pubget = rospy.ServiceProxy('/gazebo/get_joint_properties',GetJointProperties)
    rate = rospy.Rate(10) # 10hz
    i = 0
    val = 1.0
    #while not rospy.is_shutdown():
    for k in range(0,3):
        print str(k)
        if i > 30:
            if val > 0:
                i = 0
            else:
                i = -30
            val = -val
        i = i + 1
        setRot(pub, val)
        v = getPos(pubget)
        k = k + 1
        
        if(k >= 3):
            val = 0
            setRot(pub,val)
            v = getPos(pubget)
            k = 0

        rate.sleep()


def talkerfw():
#    pub = rospy.Publisher('/gazebo/apply_joint_effort', ApplyJointEffort, queue_size=10)
    rospy.init_node('cc_ctrl', anonymous=True)
    pub    = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    pubget = rospy.ServiceProxy('/gazebo/get_joint_properties',GetJointProperties)
    rate = rospy.Rate(10) # 10hz
    i = 0
    k = 0
    val = 1.0
    #while not rospy.is_shutdown():
    for k in range(0,3):
        print str(k)
        if i > 30:
            if val > 0:
                i = 0
            else:
                i = -30
            val = -val
        i = i + 1
        setRun(pub, val)
        v = getPos(pubget)
        k = k + 1
        
        if(k >= 3):
            val = 0
            setRun(pub,val)
            v = getPos(pubget)
            k = 0

        rate.sleep()


def talkerbw():#move robot back
#    pub = rospy.Publisher('/gazebo/apply_joint_effort', ApplyJointEffort, queue_size=10)
    rospy.init_node('cc_ctrl', anonymous=True)
    pub    = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    pubget = rospy.ServiceProxy('/gazebo/get_joint_properties',GetJointProperties)
    rate = rospy.Rate(10) # 10hz
    i = 0
    val = 1.0
    k = 0
    #while not rospy.is_shutdown():
    for k in range(0,3):
        print str(k)
        if i > 30:
            if val > 0:
                i = 0
            else:
                i = -30
            val = -val
        i = i + 1
        setRun(pub, -val)
        v = getPos(pubget)
        k = k + 1
        
        if(k >= 3):
            val = 0
            setRun(pub,val)
            v = getPos(pubget)
            k = 0

        rate.sleep()

def talkerccw():#turn robot to the right
#    pub = rospy.Publisher('/gazebo/apply_joint_effort', ApplyJointEffort, queue_size=10)
    rospy.init_node('cc_ctrl', anonymous=True)
    pub    = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    pubget = rospy.ServiceProxy('/gazebo/get_joint_properties',GetJointProperties)
    rate = rospy.Rate(10) # 10hz
    i = 0
    val = 1.0
    k = 0 
    #while not rospy.is_shutdown():
    
    for k in range(0,3):
        print str(k)
        if i > 30:
            if val > 0:
                i = 0
            else:
                i = -30
            val = -val
        i = i + 1
        setRot(pub, -val)
        v = getPos(pubget)
        k = k + 1
        
        if(k >= 3):
            val = 0
            setRot(pub,val)
            v = getPos(pubget)
            k = 0

        rate.sleep()


def takeInput():
    a = raw_input("input comand: ")
    
    if(a =="a"):
        print(str(a))
        talkerccw()
        t.sleep(2)
        
    elif(a == "d"):
        print(str(a))
        talkercw()
        t.sleep(2)
        
    elif(a == "w"):
        print(str(a))
        talkerfw()
        t.sleep(2)
        
    elif(a == "s"):
        print(str(a))
        talkerbw()
        t.sleep(2)
        
    else:
        pass

    


if __name__ == '__main__':
    while(True):
        try:
            takeInput()
           
        except rospy.ROSInterruptException:
            pass

