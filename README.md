# Quick steps for bgp-tools

## 0. Download submodules and apply patches
```
git clone https://github.com/SquidRo/bgp-tools
cd bgp-tools
git submodule update --init
```

```
cd scapy
git am ../patch/0001-Add-tcp_reassemble-to-BGPHeader.patch
```
```
cd exabgp/
git am ../0002-Modify-protocol.py-to-replay-bgp-pcap-file.patch
```
## 1. Reassemble bgp pcap file
```
PCAP={path to pcap} PYTHONPATH=${PWD}/scapy python3 bgpsess.py
```

## 2 Generate test.ini
```
sed -E 's,\{#PWD#\}/,'"$PWD/"',g' test-ini.tmp > test.ini
```

### 2.a Modify test.ini to use the correct ip settings
```
vi test.ini
```

## 3. Replay the output pcap file in step 1
```
PCAP={path to pcap} ./exabgp/sbin/exabgp ${PWD}/test.ini
```
NOTE: exabgp needs python 3 (3.7+).

## 4. Check if bgp neighbor can receive messages from us

---
