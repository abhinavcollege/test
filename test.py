## LED Blink 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

for i in range(10):
	GPIO.output(7,true)
  print("Turn on")
  time.sleep(1)
  
	GPIO.output(7,false)
  print("Turn off")
  time.sleep(1)
  
print("done")
RPIO.cleanup()

##########################/

##Displaying Time over 4-Digit 7-Segment Display using Raspberry Pi

##Update your Raspbian:
$ sudo apt update
$ sudo apt upgrade
##6. Configure the Raspberry:
$ sudo raspi-config
##a. Change User Password
##b. Localization Options -> Change Timezone Select your Local
##Timezone
##c. Tab to Finish
##7. Install the software:
$ cd /home/pi
$ sudo apt update
$ sudo apt install git
$ git clone https:##github.com/timwaizenegger/raspberrypiexamples/tree/master/actor-led-7segment-4numbers
##8. Power down your Pi for setting up the hardware
$ shutdown now
##After the LED goes off unplug the power
5V 2
GND 6
CLK 40
DIO 38

##3. SSH into your Pi again like previously.
$ cd actor-led-7segment-4numbers
$ sudo python tm1637.py
$ python -V (capital “V”)  ##Python 2.7.X
$ sudo shutdown now

##Testing
$ sudo python clock.py
$ sudo python displayIP.py


##########################/

##Setting up Wireless Access Point using Raspberry Pi

##Step 1: Install and update Raspbian
##check for updates and ugrades:
sudo apt-get update
sudo apt-get upgrade
##If you get an upgrade, It’s a good idea to reboot with sudo reboot.

##Step 2: Install hostapd and dnsmasq
##These are the two programs we’re going to use to make your Raspberry Pi into a wireless
##access point. To get them, just type these lines into the terminal:
sudo apt-get install hostapd
sudo apt-get install dnsmasq
##Both times, you’ll have to hit y to continue. hostapd is the package that lets us create a
##wireless hotspot using a Raspberry Pi, and dnsmasq is an easy-to-use DHCP and DNS
##server.
##We’re going to edit the programs’ configuration files in a moment, so let’s turn the
##programs off
##before we start tinkering:
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq

##Step 3: Configure a static IP for the wlan0 interface
sudo nano /etc/dhcpcd.conf
##Now that you’re in the file, add the following lines at the end:
##Code
interface wlan0
static ip_address=192.168.1.10/24
denyinterfaces eth0
denyinterfaces wlan0
##After that, press Ctrl+X, then Y, then Enter to save the file and exit the editor.

##Step 4: Configure the DHCP server (dnsmasq)
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo nano /etc/dnsmasq.conf
##Type these lines into your new configuration file:
interface=wlan0
 dhcp-range=192.168.0.11,192.168.0.30,255.255.255.0,24h
##The lines we added mean that we’re going to provide IP addresses between 192.168.0.11
##and 192.168.0.30 for the wlan0 interface.

##Step 5: Configure the access point host software (hostapd)
sudo nano /etc/hostapd/hostapd.conf
##This should create a brand new file. Type in this:
##code
interface=wlan0
bridge=br0
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
ssid=RpiIoTwiFi
wpa_passphrase=Rpi@wifi123

##We still have to show the system the location of the configuration file:
sudo nano /etc/default/hostapd
##In this file, track down the line that says #DAEMON_CONF=”” – delete that # and put
##the path to our config file in the quotes, so that it looks like this:
DAEMON_CONF="/etc/hostapd/hostapd.conf"
##The # keeps the line from being read as code, so you’re basically bringing this line to life
##here while giving it the right path to our config file.

##Step 6: Enable internet connection
##To build the bridge, let’s install one more package:
sudo apt-get install bridge-utils
##We’re ready to add a new bridge (called br0):
sudo brctl addbr br0
##Next, we’ll connect the eth0 interface to our bridge:
sudo brctl addif br0 eth0
##Finally, let’s edit the interfaces file:
sudo nano /etc/network/interfaces
##…and add the following lines at the end of the file:
##code
auto br0
iface br0 inet manual
bridge_ports eth0 wlan0

##Step 9: Reboot
##Now that we’re ready, let’s reboot with sudo reboot.
