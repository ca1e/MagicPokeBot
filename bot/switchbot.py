import binascii
from enum import Enum
import time

class MethodType(Enum):
    Heap = 0
    Main = 1
    Absolute = 2

class SwitchButton(Enum):
    A = 'A'
    B = 'B'
    X = 'X'
    Y = 'Y'
    RSTICK = 'RSTICK'
    LSTICK = 'LSTICK'
    L = 'L'
    R = 'R'
    ZL = 'ZL'
    ZR = 'ZR'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    DUP = 'DUP'
    DDOWN = 'DDOWN'
    DLEFT = 'DLEFT'
    DRIGHT = 'DRIGHT'
    HOME = 'HOME'
    CAPTURE = 'CAPTURE'

class SysBot:
    def __init__(self, ip: str, port : int):
        pass
    
    def _send_cmd(self, cmd: str):
        pass

    def _read_resp(self, lens = 8):
        pass
    
    ## info commands
    def get_version(self):
        self._send_cmd(f"getVersion")
        raw = self._read_resp()
        return bytes2str(raw)
    
    def get_main_base(self):
        self._send_cmd(f"getMainNsoBase")
        raw = self._read_resp()
        return int(bytes2str(raw), 16)

    def get_heap_base(self):
        self._send_cmd(f"getHeapBase")
        raw = self._read_resp()
        return int(bytes2str(raw), 16)

    def get_title_id(self):
        self._send_cmd(f"getTitleID")
        raw = self._read_resp()
        return int(bytes2str(raw), 16)

    def get_build_id(self):
        self._send_cmd(f"getBuildID")
        raw = self._read_resp()
        return int(bytes2str(raw), 16)
    
    ## I/O commands
    _peeks = ['peek', 'peekMain', 'peekAbsolute']
    def peek(self, addr: int, lens, ti: MethodType = MethodType.Heap):
        #print(f"{self._peeks[ti.value]} {hex(addr)} {lens}")
        self._send_cmd(f"{self._peeks[ti.value]} {hex(addr)} {lens}")
        hstr = self._read_resp(lens).decode()
        return bytes.fromhex(hstr)

    _pokes = ['poke', 'pokeMain', 'pokeAbsolute']
    def poke(self, addr: int, data, ti: MethodType = MethodType.Heap):
        ed = data.to_bytes(2, byteorder = 'little')
        st = binascii.hexlify(ed).decode()
        #print(f"{self._pokes[ti.value]} {hex(addr)} 0x{st}")
        self._send_cmd(f"{self._pokes[ti.value]} {hex(addr)} 0x{st}")
        pass # no returns
    
    ## extra I/O commands
    def pointer(self, base: int, *offsets):
        # f"pointerAll 0xD9674B8 0x60 0x10"
        self._send_cmd(f"pointer {hex(base)} data")
        hstr = self._read_resp().decode()
        return bytes.fromhex(hstr)
    
    def pointer_all(self, base: int, *offsets):
        self._send_cmd(f"pointerAll {hex(base)} data")
        hstr = self._read_resp().decode()
        return bytes.fromhex(hstr)
    
    def pointer_peek(self):
        pass
    def pointer_poke(self):
        pass
    
    ## button commands
    def click(self, button: SwitchButton):
        self._send_cmd(f"click {button.value}")
        time.sleep(1)

    def hold(self, button: SwitchButton):
        self._send_cmd(f"press {button.value}")
        time.sleep(1)

    def release(self, button: SwitchButton):
        self._send_cmd(f"release {button.value}")
        time.sleep(1)


def bytes2str(b: bytes):
    return b.decode().strip()