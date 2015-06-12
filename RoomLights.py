__author__ = 'Daniel'
# ------------------Daniel Coffaro_______________


import paramiko
from tkinter import *

class SshConnection:
    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # self.ssh.connect('74.65.106.45', username='pi', password='qwezxc', port=23)
        self.ssh.connect(host, username=username, password=password, port=port)

    def command(self,command):
        print(command)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.readlines()

    def close(self):
        self.ssh.close()
        print('Connection to '+self.host+' closed')

root = Tk()

# create 'ThePi' object
ThePi = SshConnection('74.65.106.45', 'pi', 'qwezxc', 23)
# ---------------Creates buttons---------------
# Main
MainOn = Button(root, text="Main On", command=lambda: ThePi.command('echo "rf a1 on" |nc localhost 1099'))
MainOn.pack()
MainOff = Button(root, text="Main Off", command=lambda: ThePi.command('echo "rf a1 off" |nc localhost 1099'))
MainOff.pack()
# Red
RedOn = Button(root, text="Red On", command=lambda: ThePi.command('echo "rf a2 on" |nc localhost 1099'))
RedOn.pack()
RedOff = Button(root, text="Red Off", command=lambda: ThePi.command('echo "rf a2 off" |nc localhost 1099'))
RedOff.pack()
# Fans
FanOn = Button(root, text="Fan On", command=lambda: ThePi.command('echo "rf a3 on" |nc localhost 1099'))
FanOn.pack()
FanOff = Button(root, text="Fan Off", command=lambda: ThePi.command('echo "rf a3 off" |nc localhost 1099'))
FanOff.pack()
# command=lambda: action was used instead of command=action because it allowed for the passing of parameters.

root.mainloop()
ThePi.close()
