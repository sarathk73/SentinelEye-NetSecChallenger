# SentinelEye: Automated Wireless Security Toolkit

## Description
"NetSecChallenger" provides a suite of automated tools designed for security professionals and network administrators to test and assess the security of wireless networks. With an intuitive command-line interface, users can streamline the process of monitoring, analyzing, and testing network protocols.

## Table of Contents
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Installation Instructions](#installation-instructions)
- [Usage Guide](#usage-guide)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [Authors and Acknowledgments](#authors-and-acknowledgments)
- [License](#license)


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

## Configuration

 - Ensure Python 3 is installed
 - Update the system paths if necessary in the wifi.py script

## Troubleshooting
  
  For common issues and troubleshooting help, see TROUBLESHOOTING.md in this repository.
  


## Contributing

We welcome contributions from the community! If you would like to contribute to SentinelEye, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes with meaningful commit messages.
- Push your changes to the branch.
- Submit a pull request against the `main` branch.

Please ensure your code adheres to the project's coding standards and include any relevant tests.

## Disclaimer
"NetSecChallenger" is intended for educational purposes and authorized security audits only. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Authors and Acknowledgments

This toolkit is the product of collaborative efforts by AKASH, ASWIN, SUDEV, and SARATH. Special thanks to the cybersecurity and open-source communities for their wisdom and tools.
For inquiries or feedback, contact via amssarath@gmail.com.
