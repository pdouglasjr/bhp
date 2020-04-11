import socket

target_host = raw_input("Enter target host: ")
target_port = int(raw_input("Enter target port: "))

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
data = raw_input("Enter some data: ")
client.send(data)

# receive some data
response = client.recv(4096)
print "\nData sent: %s" % data
print "Data received: %s" % response
