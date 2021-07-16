from bot.net_back import NetBot
from traid.traid import *

#-#-#
bot = NetBot("192.168.1.26")

v = bot.get_title_id()
b = bot.get_build_id()

sword_tid = 0x0100ABF008968000
shield_tid = 0x01008DB008C2C000
print(f'tid: {v:X}, bids:{b:X}')

m = bot.get_main_base()
h = bot.get_heap_base()
ok = m != 0 and h != 0
if not ok:
    print('not ok')

initiateTrade(bot)
print('init linked traid')
input_code(bot, None)
print('input traid code')
confirmCode(bot)

wait_util(bot, 10)

seed = getPokeSeed(bot)

if seed:
    print(f"seed: {seed:X}")
else:
    print('no pkm found')
    exit_traid(bot)
