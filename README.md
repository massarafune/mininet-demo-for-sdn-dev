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

You can run scripts or commands in the xterm window or type commands in mininet terminal  
(e.g. mininet> h1 ping h2)  

## Run simulated DDOS packet injection attack
ddos-randip.py uses Scapy module to spoof its IP address.  
[Scapy](https://github.com/secdev/scapy)  
To run the script you need to install Scapy module locally
```sh
sudo apt install python3-scapy
```
At the time of writing this, scapy version 2.4.3 was tested in the script with Ubuntu 20.04  

### Basic usage of the file
```sh
usage: sudo python3 ddos-randip.py [--random] [--dest <ip>] [--time <duration of ddos attack>] [--help]

optional arguments:
  -h, --help            show this help message and exit
  -r, --random          use random IP for destination
  -d DSTIP, --dest DSTIP
                        use specific IP for destination
  -t TIME, --time TIME  specify duration of ddos attack in seconds
```
It automatically randomises source IP address. By adding -r, --random flag, destination IP address will be randomised.  
--time is a mandatory option which specify the duration of the attack, and either -r or -d is required as well.  

This file is meant to be used within SDN network simulator to cause southbound API flooding.  

By combining mininet, it simply simulates packet injection attacks against a SDN switch.  
[![asciicast](https://asciinema.org/a/fxVkzdb2RsYQdrzKJR4TeF8Jr.svg)](https://asciinema.org/a/fxVkzdb2RsYQdrzKJR4TeF8Jr)  

