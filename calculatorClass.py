# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 17:58:29 2017

@author: owner
"""

from deckOfCardsClass import deckOfCards,player
suit_value_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
for num in xrange(2, 10):
    suit_value_dict[str(num)] = num

def findWinningPlayer(players):
    playersScores = [playeri.handRank for playeri in players]
    winningPlayer = [i for i, j in enumerate(playersScores) if j == max(playersScores)]
    winPlayer = None
    if len(winningPlayer)==1:
        winPlayer = players[winningPlayer[0]]
    else:
        possibleWinners = [players[i] for i in winningPlayer]
        noWinner = True
        cardNumber = 0        
        while noWinner and cardNumber<5:
            highCards = [suit_value_dict[playeri.bestCards[cardNumber][0]] for playeri in possibleWinners]
            playerNumbers = [playeri.playerNumber for playeri in possibleWinners]
            highCardPlayers = [playerNumbers[i] for i, j in enumerate(highCards) if j == max(highCards)]#finds index of highcards
            if len(highCardPlayers) == 1:
                winPlayer = players[highCardPlayers[0]]
                noWinner = False
            else:
                possibleWinners = [players[i] for i in highCardPlayers]#this will get beginning index
                cardNumber+=1
    return winPlayer

def playAGame(noPlayers,player0Cards = None):
    theDeck = deckOfCards()
    if player0Cards is None:
        players = [player(0,theDeck)]
    else:
        try:
            players = [player(0,theDeck,player0Cards)]
        except:
            players = [player(0,theDeck)]    
    [players.append(player(i+1,theDeck)) for i in range(noPlayers)]
    theBoard = theDeck.takenNRandomCards(5)    
    [playeri.myBestHand(theBoard) for playeri in players]
    winPlayer = findWinningPlayer(players)
    return winPlayer

def playAGameDict(cards,noPlayers):
    theDeck = deckOfCards()
    players = []
    theBoard=[]
    if 'flop' in cards and 'turn' in cards and 'river' in cards:
        theBoard.extend(cards['flop'] + cards['turn'] + cards['river'])
        theDeck.removeCardsFromDeck(theBoard)
    elif 'flop' in cards and 'turn' in cards:
        theBoard.extend(cards['flop'] + cards['turn'])
        theDeck.removeCardsFromDeck(theBoard)
    elif 'flop' in cards:
        theBoard.extend(cards['flop'])
        theDeck.removeCardsFromDeck(theBoard)
    for i in range(noPlayers+1):
        try:
            players.append(player(i,theDeck,cards[i]))
        except:
            players.append(player(i,theDeck))
    theBoard.extend(theDeck.takenNRandomCards(5-len(theBoard)))
    [playeri.myBestHand(theBoard) for playeri in players]
    winPlayer = findWinningPlayer(players)
    return winPlayer

def monteCarloSimulationDict(cards,noPlayers,noGames):
    noWins = 0
    noDraws = 0
    for i in range(noGames):   
        winner = playAGameDict(cards,noPlayers)
        if winner is None:
            noDraws+=1
        elif winner.playerNumber == 0:
            noWins+=1
    winPercentage = float(noWins)/noGames
    drawPercentage = float(noDraws)/noGames
    return winPercentage,drawPercentage

def monteCarloSimulation(noPlayers,player0Cards,n):
    noWins = 0
    noDraws = 0
    noGames = n
    for i in range(noGames):   
        winner = playAGame(noPlayers,player0Cards)
        if winner is None:
            noDraws+=1
        elif winner.playerNumber == 0:
            noWins+=1
    winPercentage = float(noWins)/noGames
    return winPercentage
    
def startMPSimulationMC(args):
    noPlayers,player0Cards,n = args
    noWins = 0
    noDraws = 0
    noGames = n
    for i in range(noGames):   
        winner = playAGame(noPlayers,player0Cards)
        if winner is None:
            noDraws+=1
        elif winner.playerNumber == 0:
            noWins+=1
    return noWins

def multiProcessMC(noPlayers,player0Cards,n):
    import multiprocessing
    noProcesses = multiprocessing.cpu_count()-1
    pool = multiprocessing.Pool(noProcesses)
    part_count=[[noPlayers,player0Cards,n/noProcesses] for i in range(noProcesses)]    
    count=pool.map(startMPSimulationMC,part_count)
    winPercentage = float(sum(count))/n
    return winPercentage    
	#print "You won %d hands with starting cards %s \n Win percentage is %f" %(sum(count),player0Cards,winPercentage)

if __name__=="__main__":
    noPlayers = 1
    cards = {}
    cards[0] = ['Ad','Ks']
    cards[1] = ['Jd','Kh']
    #cards[2] = ['Qh','Qd']
    #cards['flop'] = ['Td','Jc','Qc']
    #cards['turn'] = ['Kh']
    winPer,drawPer =  monteCarloSimulationDict(cards,noPlayers,1000)
    print "With starting cards %s your win percentage is %f and your draw percentage is %f" %(cards[0],winPer,drawPer)

if __name__ == "__main__x":
    import time    
    noPlayers = 4
    player0Cards = ['Tc','9c']
    now = time.clock()
    winPer =  monteCarloSimulation(noPlayers,player0Cards,1000)
    print "With starting cards %s your win percentage is %f" %(player0Cards,winPer)
				#print time.clock()-now
    #multiProcessMC(noPlayers,player0Cards,10000)
    print time.clock()-now