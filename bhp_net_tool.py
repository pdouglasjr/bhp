import sys
import socket
import getopt
import threading
import subprocess

# define some global variables
listen              = False
command             = False
upload              = False
execute             = ""
target              = ""
upload_destination  = ""
port                = 0

def usage():
    print "BHP Net Tool"
    print
    print "Usage: bhpynet.py -t target_host -p port"
    print
    print "-l --listen\t\t\t- list on [host]:[port] for\n\t\t\t\t  incoming messages"
    print "-e --execute=file_to_run\t- execute the given file upon\n\t\t\t\t  receiving a connection"
    print "-c --command\t\t\t- initialize a command shell"
    print "-u --upload=destination\t\t- upon receiving connection, upload a file and write to [destination]"

usage()
