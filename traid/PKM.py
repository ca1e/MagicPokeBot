import time

TrainerDataOffset = 0x45068F18
SoftBanUnixTimespanOffset = 0x450C89E8
IsConnectedOffset = 0x30c7cca8
TextSpeedOffset = 0x450690A0
ItemTreasureAddress = 0x45068970

LinkTradePartnerPokemonOffset = 0xAF286078
LinkTradePartnerNameOffset = 0xAF28384C
LinkTradeSearchingOffset = 0x2F76C3C8

#EnsureConnectedToYComm

def IsGameConnectedToYComm(bot):
    conn = bot.peek(IsConnectedOffset, 1)
    # print(conn)
    return conn[0] != 0

def WaitSearching(bot, timeout):
    t = 0
    oldEC = bot.peek(LinkTradePartnerPokemonOffset, 4)
    while True:
        if(t > timeout):
            return
        data = bot.peek(LinkTradePartnerPokemonOffset, 4)
        if(data != oldEC):
            return
        t += 1
        time.sleep(1)