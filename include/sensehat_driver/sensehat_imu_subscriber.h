#ifndef SENSEHAT_IMU_SUBSCRIBER_H
#define SENSEHAT_IMU_SUBSCRIBER_H

#include <iostream>
#include <string>

#include "ros/ros.h"
#include "sensor_msgs/Imu.h"

namespace sensehat_imu 
{
class SenseHatIMUSubscriber 
{
public:
	SenseHatIMUSubscriber(const ros::NodeHandle& nh);
	
	void IMUCallback(const sensor_msgs::Imu::ConstPtr& imu_msg);

	~SenseHatIMUSubscriber();

private:
	ros::Subscriber sensehat_imu_subscriber_;
	ros::NodeHandle nh_;
};
}

#endif // SENSEHAT_IMU_SUBSCRIBE_H
