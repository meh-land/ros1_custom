#!/usr/bin/env python3
import rospy as rp
from std_msgs.msg import String
from time import sleep

def main():
    rp.init_node("pub_tst")
    rp.loginfo("hello from pub_tst")

    pub = rp.Publisher("/my_topic", String, queue_size=10)

    while not rp.is_shutdown():
        hello_str = f"hello at time {rp.get_time()}"
        rp.loginfo(hello_str)
        pub.publish(hello_str)
        sleep(0.5)




if __name__ == "__main__":
    main()
