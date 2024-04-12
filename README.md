# NetSecChallenger: Automated Wireless Security Toolkit

## Description
"NetSecChallenger" provides a suite of automated tools designed for security professionals and network administrators to test and assess the security of wireless networks. With an intuitive command-line interface, users can streamline the process of monitoring, analyzing, and testing network protocols.

## Key Features
- Interactive CLI menu for easy navigation.
- Simplifies complex wireless security testing procedures.
- Automated monitoring mode, network scanning, handshake sniffing, and more.
- Integrated support for WPS attack vectors, DOS attacks, and other advanced monitoring tools.

## Prerequisites
Before installing and running NetSecChallenger, ensure you have the necessary permissions to test the network. Unauthorized access to networks is illegal and unethical.

## Installation Instructions

Clone the repository:

```bash
git clone https://github.com/sarathk73/SentielEye-NetSecChallenger.git
cd SentinelEye-NetSecChallenger
```

Install the required tools and dependencies:
```bash
chmod +x wifi.py
./wifi.py
```
Or, for a manual installation of requirements:

```bash
sudo apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully wifite bettercap wifipumpkin3
```
## Usage Guide

To launch the toolkit, navigate to the cloned repository and execute:

```bash
python wifi.py
```
You will be greeted by an interface as follows:

- Start/Stop monitor mode
- Scan networks
- Capture handshakes
- Execute WPS network attacks
...
Select an action by entering the corresponding number provided by the menu.

## Disclaimer
"NetSecChallenger" is intended for educational purposes and authorized security audits only. The developers assume no liability and are not responsible for any misuse or damage caused by this program.
