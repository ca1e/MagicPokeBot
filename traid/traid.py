from bot.switchbot import   SwitchButton
from pkm.PK8 import PK8
from pkm.seedSolve import searchPKM
import time
from traid.NumpadInterpreter import getButtons,interpretStringList
from traid.PKM import IsGameConnectedToYComm, WaitSearching

raidOffset = 0x886c1ec8
tradeOffset = 0xaf286078
partyOffset = 0x450c68b0
wildOffset = 0x8fea3648

ek8_size = 0x158
pk8_size = 0x148

def initiateTrade(bot):
    print('open menu')
    bot.click(SwitchButton.Y)
    time.sleep(1)
    bot.click(SwitchButton.A)
    time.sleep(0.5)
    bot.click(SwitchButton.DDOWN)
    for i in range(3):
        bot.click(SwitchButton.A)

def input_code(bot, incode):
    datalist, code = getButtons(incode)
    print('code', code)
    interpretStringList(bot, datalist)

def confirmCode(bot):
    print('confirm code')
    bot.click(SwitchButton.PLUS)
    time.sleep(1.5)
    for i in range(4): # ensure ok
        bot.click(SwitchButton.A)

def wait_util(b, t):
    return WaitSearching(b, t)

def exit_traid(bot):
    bot.click(SwitchButton.Y)
    bot.click(SwitchButton.PLUS)
    bot.click(SwitchButton.A)
    while IsGameConnectedToYComm(bot):
        time.sleep(1)
    bot.click(SwitchButton.B)
    bot.click(SwitchButton.B)

def getPokeSeed(bot):
    ek8 = bot.peek(tradeOffset, 0x158)
    pkm = PK8(list(ek8[: 0x148]))
    speci = pkm.getSpecies()
    if (speci > 0 or speci < 900):
        print('species', speci)

        seed = searchPKM(pkm)
        if seed:
            return seed
        else:
            print('no seed found')
    else:
        print('no pkm found')
    return False