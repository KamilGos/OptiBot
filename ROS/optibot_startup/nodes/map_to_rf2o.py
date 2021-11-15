#!/usr/bin/env python  
import roslib
roslib.load_manifest('optibot_startup')

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('map_to_rf2o')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    print("ready")
    while not rospy.is_shutdown():
        br.sendTransform((0.0, 0.0, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "/rf2o_link",
                         "/map")
        rate.sleep()
