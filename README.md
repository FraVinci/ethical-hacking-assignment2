# Evasion Techniques with Scapy - Bypassing Snort IDS
Assignment 2 of the course "Ethical Hacking"  in the academic year 2024/2025 at the University of Stavanger.

## Project Goal
The main goal of this assignment is to simulate various evasion techniques using Scapy library while trying not to be detected by an Intrusion Detection System (IDS). In this project are performed:  ICMP flooding, slow port scan, obfuscating attack payloads and ICMP tunneling for covert communication.

## Install Libraries
`Scapy` is the library mainly used to implement the required simulations. It can be installed directly in python using this command:
```
pip install scapy
```

## Run Test
To perform tests on individual components, execute the following commands on the machine running Kali as operative system:

```
sudo python3 imcpFlood.py
sudo python3 slowPortScan.py
sudo python3 payloadAttack.py
sudo python3 senderICMP.py
```

The only script to be executed on the victim machine that uses Ubuntu as its operating system is `snifferICMP.py`. Below is the command to run it:

```
sudo python3 snifferICMP.py
```
This file must be executed at the same time as `senderICMP.py` started on Kali.

## Additional information
Snort must be installed as an IDS on the victim machine. For further information on the project and the configuration of Snort, please refer to the full report.

