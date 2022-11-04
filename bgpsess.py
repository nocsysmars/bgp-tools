from scapy.all import *
from scapy.utils import *
from scapy.layers import *  # load_layer("http")
from scapy.contrib.bgp import *
from scapy.sessions import TCPSession
import pdb

import resource, sys, os
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

#load_layer("bgp")
#conf.tls_session_enable = True
#print(conf.version)  # 2.4.5rc1.dev55

#class TLS_over_TCP(TLSSession, TCPSession):
#    pass
#

#pdb.set_trace()
cap_fpath = os.environ.get('PCAP')

if cap_fpath:
    cap_fname = os.path.basename(cap_fpath)
    cap_fdir  = os.path.dirname(cap_fpath)
    cap_fext  = os.path.splitext(cap_fname)

    pkts = sniff(offline=cap_fpath,
                 session=TCPSession, session_kwargs={"app":False})

    out_fpath = './'+cap_fext[0]+'-s'+cap_fext[1]
    wrpcap(out_fpath, pkts)

    #pkts.nsummary()

    #pkts[5].show()
    print("write re-assembled output to {}".format(out_fpath))

else:
    print("Use PCAP={path to pcap}, and try again...")

