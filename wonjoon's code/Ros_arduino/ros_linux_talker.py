# !!jetson|ubuntu에서 사용하려면 catkin으로 빌드해야함!!

#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('listener', String, queue_size=10) #listener라는 이름의 토픽에게 전송
    rospy.init_node('talker', anonymous=True) #talker라는 이름의 토픽을 rosmaster로 알림
    rate = rospy.Rate(10)
    while not rospy.is_shutdown(): #rosrun이 꺼질때까지 반복실행
        hello_str = "hello world %s" % rospy.get_time() # hello와 시간값 생성
        rospy.loginfo(hello_str) #터미널에 로그찍기
        pub.publish(hello_str) #listener토픽으로 퍼블리싱
        rate.sleep() 

if __name__ == '__main__':
    try:
        talker() # rosrun으로 talker.py가 실행되면 talker함수를 실행
    except rospy.ROSInterruptException:
        pass
