""" fauxmo_minimal.py - Fabricate.IO

    This is a demo python file showing what can be done with the debounce_handler.
    The handler prints True when you say "Alexa, device on" and False when you say
    "Alexa, device off".

    If you have two or more Echos, it only handles the one that hears you more clearly.
    You can have an Echo per room and not worry about your handlers triggering for
    those other rooms.

    The IP of the triggering Echo is also passed into the act() function, so you can
    do different things based on which Echo triggered the handler.
"""

import fauxmo
import logging
import time
import serial

from debounce_handler import debounce_handler
from pathlib import Path

import serial
from pathlib import Path

arduino_path_is_good_and_serial_is_connected = False;
arduino_path_is_good = False;

def write_serial_out( int_code ):
  #print "arduino_path_is_good_and_serial_is_connected = " + str(arduino_path_is_good_and_serial_is_connected);
  print "int_code = " + str(int_code);
  serial_out_to_arduino.write(str(int_code));

try:
    serial_out_to_arduino = serial.Serial('/dev/ttyACM0', 9600);
    print 'Connected to /dev/ttyACM0' 
    arduino_path_is_good_and_serial_is_connected = True;
    
except serial.serialutil.SerialException:
    arduino_path_is_good_and_serial_is_connected = False;
    print 'EXCEPTION - Could NOT connect to /dev/ttyACM0'        


logging.basicConfig(level=logging.DEBUG)


class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    TRIGGERS = {"television": 52000, "stereo": 52001}
    
    def act(self, client_address, state, name):
        if name == 'television':
          if state:
            write_serial_out(1);
          else:
            write_serial_out(2);
        elif name == 'stereo':
          if state:
            write_serial_out(3);
          else:
            write_serial_out(4);
        else:
          return False;        
        
        return True

if __name__ == "__main__":
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)

    # Register the device callback as a fauxmo handler
    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)

    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception, e:
            logging.critical("Critical exception: " + str(e))
            break
