# quick mininet demo for SDN dev

Tested on Ubuntu 20.04  

This project is to demonstrate mininet capabilities and to run some tests for SDN development  

Prerequisite: mininet, xterm, OpenFlow 1.3, openvswitch python2
```sh
sudo apt update && sudo apt install mininet xterm python openvswitch-testcontroller
```

## Run simple test
```sh
sudo python mininet-test.py
```
it will automatically open xterm windows for each of the nodes
