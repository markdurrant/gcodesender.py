import os
import argparse

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from gcodesender import sendGCode

parser = argparse.ArgumentParser(description='This is a basic gcode sender. http://crcibernetica.com')
parser.add_argument('-p','--port',help='Input USB port',required=True)
parser.add_argument('-f','--file',help='Gcode file name',required=True)
args = parser.parse_args()

port = args.port
directory = os.path.dirname(args.file)
gcode = os.path.basename(args.file) 


print(port, directory, gcode)

class Handler(FileSystemEventHandler):
  def on_modified(self, event):
    if os.path.basename(event.src_path) == gcode:
      sendGCode(args.port, args.file)

if __name__ == "__main__":
  event_handler = Handler()
  observer = Observer()
  observer.schedule(event_handler, path = directory, recursive = True)
  observer.start()
  observer.join()