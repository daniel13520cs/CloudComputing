#!/bin/bash
sudo ovs-vsctl set Bridge s1 protocols=OpenFlow13
sudo ovs-vsctl set Bridge s2 protocols=OpenFlow13
sudo ovs-vsctl set Bridge s3 protocols=OpenFlow13
sudo ovs-vsctl set Bridge s4 protocols=OpenFlow13
ryu-manager --verbose my_controller.py
#ryu-manager --verbose ExampleSwitch13.py

