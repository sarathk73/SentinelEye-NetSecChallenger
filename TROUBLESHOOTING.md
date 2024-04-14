# Troubleshooting

This document aims to help users resolve common issues they may encounter while using SentinelEye. Before seeking further assistance, please go through the common troubleshooting steps provided below.

## Common Issues and Solutions

### Issue: Missing Dependencies
**Symptom:**
The program doesn't start or crashes during startup.

**Solution:**
Ensure that all required dependencies are installed. Refer to the `Installation Instructions` section of the [README.md](README.md) for details on how to install necessary dependencies.

```bash
sudo apt-get update
sudo apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully wifite bettercap wifipumpkin3
```
### Issue: Permissions Error

**Symptom:**
Error messages referring to lack of permissions, like 'Permission Denied'.

**Solution:**
Make sure you’re running SentinelEye with sufficient permissions. This usually requires running the software as the root user.

```bash
sudo python wifi.py
```
### Issue: Monitor Mode Not Starting
**Symptom:**
The interface does not go into monitor mode when using the start option.

**Solution:**
  - Check that your wireless card supports monitor mode.
  - Make sure the proper driver is installed and loaded.
  - Check that no other processes are interfering with the wireless card. You can attempt to stop other processes with:
```bash
sudo airmon-ng check kill
```

### Issue: Unable to Capture Handshakes
**Symptom:**
The program isn’t capturing handshakes even when there is network traffic.

**Solution:**
  - Ensure that you are within range of the wireless access point.
  - Check to see there is ongoing traffic between the AP and its clients.
  - Try targeting a network with a stronger signal.

