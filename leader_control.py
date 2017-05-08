from uwb import uwb
from serversocket import serversocket
import threading

host = "192.168.1.106"
port = 5454

print "Initializing UWB radio."
radio = uwb(a=2000, port='/dev/ttyACM0')  # UWB init
server = serversocket(host, port)
radiothread = threading.Thread(target=radio.range,
                               args=(True, server))
print "Calculating position..."
radiothread.start()
