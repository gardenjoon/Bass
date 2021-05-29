// !!본 코드는 아두이노에 업로드하는 코드임!!
// String값만 받을수 있는 listener라는 토픽을 생성하여 
// message()함수안에서 처리함
// rostopic echo /listener 명령어를 통해 listener토픽에 들어오는 값을 알 수 있음

#include <Arduino.h>
#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle nh;

void message( const std_msgs::String& msg ){
#받은데이터를 함수안에서 처리하여 보내주기만 하면됨
}
ros::Subscriber<std_msgs::String> sub("listener", &message); 

void setup() {
  nh.initNode(); 
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
}