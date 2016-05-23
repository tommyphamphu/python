# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "PPT"
__date__ = "$May 20, 2016 11:32:09 AM$"

import socket, time


if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    #host = ''
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.
    x= True
    while x== True:
        try:
            c, addr = s.accept()     # Establish connection with client.
            print 'Got connection from', str(addr)
            print s.getsockname()
            x= False
        except:
            print "Cho"
    while True:
        try:
            message = raw_input()
            c.send(str(message))
            data = c.recv(10240)
            print data
        except:
            print "Loi gui"
            pass
    c.close
    time.sleep(100)
    
