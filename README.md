# Raspberry Pi Home Web Server Setup Script Set

# WAT?

* A couple of scripts for making a Raspberry Pi into a home web-page server.
* A simple Python app that allows the Pi to accept comm. from an Alex Echo. (works, but hacky)

# HOW?

## To Use:

* Download Raspian Lite [Image](https://www.raspberrypi.org/downloads/raspbian/).
* Download [Win32DiskImage](https://sourceforge.net/projects/win32diskimager/) tool.
* Modify [setup_pi_part_1.bash](https://github.com/EntropyHaos/z_haos_raspberry_pi_home_server_setup_script_set/blob/master/setup_pi_part_1.bash) variables with your new user name and ssh public key.
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

# WHY?

*Because i can?* No, really, because i've done this too many times and wanted to stream line it.

# WEN?

*Spring 2017*

Version : 0.0001 (Use at your own risk!)

