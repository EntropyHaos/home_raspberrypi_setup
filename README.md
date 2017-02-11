# Raspberry Pi Home Web Server Setup Script Setup

# To Use:

* Download Raspian Lite [Image](https://www.raspberrypi.org/downloads/raspbian/).
* Download [Win32DiskImage](https://sourceforge.net/projects/win32diskimager/) tool.
* Modify setup_pi_part_1.bash variables with your new user name and ssh public key.
* Write Image to SD card.
* Copy blank file with name 'ssh' to SD card.
* Boot pi.
* SSH into pi using 
    * login id : 'pi'
    * password : 'raspberry'
* Add modified setup_pi_part_1.bash script to pi user directory.
* Run script with 'sudo bash etup_pi_part_1.bash'
* Exit login with 'exit' command.
* Login with username modified above using ssh key.
* Run bash script to delete pi user.
* Add setup_pi_part_2.bash script to user directory.
* Run script.
* Served pages root is at : '/var/www/html/'