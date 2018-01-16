#!/usr/bin/python
"""
Simple g-code streaming script
"""
 
import serial
import time
import argparse

def sendGCode(port, gCode):
  ## show values ##
  print ("USB Port: %s" % port)
  print ("Gcode file: %s" % gCode)

  
  # Open serial port
  #s = serial.Serial('/dev/ttyACM0',115200)
  s = serial.Serial(port, 115200)
  print('Opening Serial Port')
  
  # Open g-code file
  #f = open('/media/UNTITLED/shoulder.g','r');
  f = open(gCode, 'r');
  print('Opening gcode file')
  
  # Wake up 
  s.write("\r\n\r\n".encode()) # Hit enter a few times to wake the Printrbot
  time.sleep(2)   # Wait for Printrbot to initialize
  s.flushInput()  # Flush startup text in serial input
  print('Sending gcode')
  
  # Stream g-code
  for line in f:
    l = line.strip() # Strip all EOL characters for streaming
    if  (l.isspace()==False and len(l)>0) :
      print('Sending: ' + l)
      s.write((l + '\n').encode()) # Send g-code block
      grbl_out = s.readline() # Wait for response with carriage return
      print(' : ' + grbl_out.strip().decode("utf-8"))
  
  # Wait here until printing is finished to close serial port and file.
  # input("  Press <Enter> to exit.")
  
  # Close file and serial port
  f.close()
  s.close()