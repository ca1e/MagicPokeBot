import socket
import time
from .switchbot import SysBot

class NetBot(SysBot):
    def __init__(self, ip: str, port : int = 6000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        self._s = s
    
    def _send_cmd(self, cmd: str):
        cmd += '\r\n' #important for the parser on the switch side
        self._s.sendall(cmd.encode())

    def _read_resp(self, lens = 8):
        time.sleep(0.5) #give time to answer
        return self._s.recv(lens * 2 + 1) 
