from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.topo import MinimalTopo

setLogLevel('info')

net = Mininet(topo=MinimalTopo(), xterms=True)

net.start()
CLI(net)
net.stop()
