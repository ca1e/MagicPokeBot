import random
from bot.switchbot import   SwitchButton
import time

numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
btncmdseq = list()

def findLocation(n):
	i = 0
	j = 0

	while i < 3:
		while j < 3:
			if n == numpad[i][j]:
				return i, j
			j+=1
		j = 0
		i+=1

def findDifference(i, j, desiredLocation):
	di, dj = findLocation(desiredLocation)

	i = di - i
	j = dj - j

	return i, j

def constructString(i, j, desiredLocation):
	global btncmdseq
	Signi = False
	Signj = False

	i, j = findDifference(i,j, desiredLocation)

	if i < 0:
		i = 0 - i
		Signi = True

	if j < 0:
		j = 0 - j
		Signj = True

	if Signi == True:
		x = 0
		while x < i:
			btncmdseq.append('DUP')
			x+=1
	elif Signi == False:
		x = 0
		while x < i:
			btncmdseq.append('DDOWN')
			x+=1

	if Signj == True:
		x = 0
		while x < j:
			btncmdseq.append('DLEFT')
			x+=1
	elif Signj == False:
		x = 0
		while x < j:
			btncmdseq.append('DRIGHT')
			x+=1
	btncmdseq.append('A')
	return findLocation(desiredLocation)

def interpretStringList(bot, arr):
    length = len(arr)
    i = 0
    while i < length:
        if(arr[i] == 'DUP'):
            bot.click(SwitchButton.DUP)
        elif(arr[i] == 'DDOWN'):
            bot.click(SwitchButton.DDOWN)
        elif(arr[i] == 'DLEFT'):
            bot.click(SwitchButton.DLEFT)
        elif(arr[i] == 'DRIGHT'):
            bot.click(SwitchButton.DRIGHT)
        elif(arr[i] == 'A'):
            bot.click(SwitchButton.A)
        time.sleep(0.5)
        i+=1
    ###
    bot.click(SwitchButton.DDOWN)
    bot.click(SwitchButton.DDOWN)
    bot.click(SwitchButton.DDOWN)
    for i in range(4):
        bot.click(SwitchButton.A)

def getButtons(incode):
	global btncmdseq
	btncmdseq.clear()

	if incode == None:
		incode = random.randint(1, 9999)

	thousands = int(incode / 1000)
	hundreds = int((incode / 100) % 10)
	tens = int((incode / 10) % 10)
	ones = incode % 10

	if thousands == 0:
		thousands = random.randint(1,9)

	if hundreds == 0:
		hundreds = random.randint(1,9)

	if tens == 0:
		tens = random.randint(1,9)

	if ones == 0:
		ones = random.randint(1,9)

	i, j = constructString(0, 0, thousands)
	i, j = constructString(i, j, hundreds)
	i, j = constructString(i, j, tens)
	i, j = constructString(i, j, ones)

	value = str(thousands) + str(hundreds) + str(tens) + str(ones)
	return btncmdseq, value