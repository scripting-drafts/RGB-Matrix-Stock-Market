Get Stock Market values and their trend and print them on a 16x32 RGB panel run through its Adafruit Hat. Depending on the trend they're printed in green or red. 

Requirements:
 - Raspberry Pi 3
 - Raspbian Stretch*
 - Geckodriver v0.17.0**
 - Firefox-ESR 52.9.0
 - Selenium 3.141.0
 
 
*https://downloads.raspberrypi.org/raspbian/images/raspbian-2017-08-17/2017-08-16-raspbian-stretch.zip  
*\*https://github.com/d0ku/GeckoDriver_ARMv6/releases/download/v.0.17.0/geckodriver


Notes:  
To install Firefox-ESR 52.9.0 comment the source for non-free packages at /etc/apt/sources.list  
In order to be able to use the geckodriver give it execution permissions with "chmod +x"
