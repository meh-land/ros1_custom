#!/usr/bin/env python3
import rospy as rp

def main():
    rp.init_node("pub_tst")
    rp.loginfo("hello from pub_tst")
    rp.sleep(1.0)
    rp.loginfo("End of node")


if __name__ == "__main__":
    main()
