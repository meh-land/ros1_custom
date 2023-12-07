#!/usr/bin/env python3
import rospy as rp

def main():
    rp.init_node("pub_tst")
    rp.loginfo("hello from pub_tst")
    while not rp.is_shutdown():
        rp.sleep(1.0)
        rp.loginfo("IT'S ALIVE")
    rp.loginfo("End of node")


if __name__ == "__main__":
    main()
