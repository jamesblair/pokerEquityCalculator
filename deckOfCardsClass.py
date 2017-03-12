# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 21:02:08 2016
deck@author: owner
"""
import random
import itertools
import collections
suit_value_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
for num in xrange(2, 10):
    suit_value_dict[str(num)] = num
suit_value_dict_rev = {10: "T",  11:"J", 12:"Q", 13:"K", 14:"A"}
for num in xrange(2, 10):
    suit_value_dict_rev[num] = str(num)

def lastValueInList(mylist,myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1
    
class deckOfCards(object):    
    def __init__(self):
        self.suits = 'cdhs'
        self.ranks = '23456789TJQKA'
        self.deck = list(''.join(card) for card in itertools.product(self.ranks, self.suits))
    
    def removeCardsFromDeck(self,listOfCardsToRemove):
        if self.checkAreCardsStillInDeck(listOfCardsToRemove):
            [self.deck.remove(x) for x in listOfCardsToRemove]
        #else:
        #    print "Cards %s are not in deck" %[s for s in listOfCardsToRemove]

    def takenNRandomCards(self,n):
        cards = random.sample(self.deck,n)
        self.removeCardsFromDeck(cards)
        return cards
    
    def checkAreCardsStillInDeck(self,listOfCardsToRemove):
        return (set(listOfCardsToRemove)<set(self.deck))
                
class player(object):
    def __init__(self,playerNumber,deckOfCards,listOfCards = None):
        if listOfCards is None:
            self.cards = deckOfCards.takenNRandomCards(2)
        else:
            if deckOfCards.checkAreCardsStillInDeck(listOfCards):
                self.cards = listOfCards
                deckOfCards.removeCardsFromDeck(listOfCards)
            else:
                #print "Cards %s are not in deck" %[s for s in listOfCards]
                self.cards = deckOfCards.takenNRandomCards(2)
        self.handRank = 0
        self.playerNumber = playerNumber        
    def myBestHand(self,theTable):
        topCards=[]
        short_desc="High Card"
        handRank=0
        allCards = self.cards + theTable
        cardsRanks, cardsSuits = zip(*sorted(zip([suit_value_dict[x[0]] for x in allCards], [x[1] for x in allCards])))
        allCardsSorted = [suit_value_dict_rev[cardsRanks[i]]+cardsSuits[i] for i in range(len(allCards))]        
        numeral_dict_list = collections.defaultdict(list)
        numeral_dict_int = collections.defaultdict(int)        
        suit_dict_list = collections.defaultdict(list)
        suit_dict_int = collections.defaultdict(int)
        
        for rank,suit in zip(cardsRanks,cardsSuits):
            numeral_dict_int[rank] +=1
            numeral_dict_list[rank].append(suit)
            suit_dict_list[suit].append(rank)
            suit_dict_int[suit] += 1  
        numeral_dict_int = collections.OrderedDict(sorted(numeral_dict_int.items()))
        numeral_dict_list = collections.OrderedDict(sorted(numeral_dict_list.items()))
        suit_dict_int = collections.OrderedDict(sorted(suit_dict_int.items()))
        suit_dict_list = collections.OrderedDict(sorted(suit_dict_list.items()))        
        len_snk = len(numeral_dict_list)
        topCards = allCardsSorted[-5:]
        topCards.reverse()
        straight_cards = allCardsSorted[:]#makes deep copy
        #check for flush, straight, pairs and trips
        if len_snk >= 5:
            straight, flush = False, False
            #check for flush
            if 5 in suit_dict_int.values():
                flush = True
                flush_values = suit_dict_list[suit_dict_int.keys()[suit_dict_int.values().index(5)]]
                topFlushCards = [x for x in allCardsSorted if x[1] == suit_dict_int.keys()[suit_dict_int.values().index(5)]]
                topFlushCards.reverse()
            elif 6 in suit_dict_int.values():
                flush = True
                flush_values = suit_dict_list[suit_dict_int.keys()[suit_dict_int.values().index(6)]]
                topFlushCards = [x for x in allCardsSorted if x[1] == suit_dict_int.keys()[suit_dict_int.values().index(6)]]
                topFlushCards.reverse()
            elif 7 in suit_dict_int.values():
                flush = True
                flush_values = suit_dict_list[suit_dict_int.keys()[suit_dict_int.values().index(7)]]
                topFlushCards = [x for x in allCardsSorted if x[1] == suit_dict_int.keys()[suit_dict_int.values().index(7)]]
                topFlushCards.reverse()
            #check for straight            
            cardsRankSet = sorted(numeral_dict_list.keys())
            indexToDelete = []            
            for i in range(len(straight_cards)-1):
                if straight_cards[i][0]==straight_cards[i+1][0]:
                    indexToDelete.append(i)
            indexToDelete.reverse()
            for i in indexToDelete:
                del straight_cards[i]
            if len(indexToDelete)<=1:
                for i in range(len(straight_cards)-4):
                    if suit_value_dict[straight_cards[i+4][0]] - suit_value_dict[straight_cards[i][0]] == 4:
                        straight = True
                        topCards = straight_cards[i:i+5]
                        topCards.reverse()
                    #need to get cards
                    #topCards = cardsRankSet[i:i+5]#this needs suits
            #low straight with ace
                if (suit_value_dict[straight_cards[3][0]]-suit_value_dict[straight_cards[0][0]] == 3) & (suit_value_dict[straight_cards[-1][0]] == 14) & (suit_value_dict[straight_cards[0][0]] == 2):
                    straight = True
                    topCards = [straight_cards[-1]]+straight_cards[0:4]
                    topCards.reverse()
                #need to get cards
                #topCards = list(cardsRankSet[-1:]) + list(cardsRankSet[0:4])
            if straight & ~flush:
                short_desc = "Straight"
                handRank = 4
            #check for straight flush
            elif straight & flush:
                #check for straight
                for i in range(len(flush_values)-4):
                    if flush_values[i+4]-flush_values[i] == 4:
                        handRank = 8
                        topFlushCards.reverse()
                        topCards = topFlushCards[i:i+5]
                        topCards.reverse()
                        short_desc = "Straight flush"
                #check for ace low straight
                if flush_values[-2] == 13:
                    handRank = 9
                    short_desc = "Royal flush" 
                elif  (flush_values[3]-flush_values[0] == 3) & (flush_values[-1] == 14) & (flush_values[0] == 2):
                    topFlushCards.reverse()                    
                    topCards = [topFlushCards[-1]]+topFlushCards[0:4]
                    topCards.reverse()                    
                    handRank = 8
                    short_desc = "Straight flush"
                elif handRank!=8:
                    handRank = 5
                    short_desc = "Flush"
                    topCards = topFlushCards[0:5]
            elif flush:
                handRank = 5
                short_desc = "Flush"
                topCards = topFlushCards[0:5]
            else:
                if len_snk == 6:
                    handRank = 1
                    topCards = [x for x in allCardsSorted if x[0] == suit_value_dict_rev[cardsRankSet[numeral_dict_int.values().index(2)]]]
                    allCardsSorted = [x for x in allCardsSorted if x not in topCards]
                    allCardsSorted = allCardsSorted[-3:]
                    allCardsSorted.reverse()
                    topCards+=allCardsSorted
                    short_desc = "One pair."
                # Two pair or 3-of-a-kind
                elif len_snk == 5:
                    if 3 in numeral_dict_int.values():
                        handRank = 3
                        topCards = [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[numeral_dict_int.values().index(3)]]]
                        allCardsSorted = [x for x in allCardsSorted if x not in topCards]
                        allCardsSorted = allCardsSorted[-2:]
                        allCardsSorted.reverse()
                        topCards+=allCardsSorted                   
                        short_desc ="Three-of-a-kind."
                    else:
                        handRank = 2
                        topCards = [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[lastValueInList(numeral_dict_int.values(),2)]]]
                        allCardsSorted = [x for x in allCardsSorted if x not in topCards]
                        topCards += [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[numeral_dict_int.values().index(2)]]]
                        allCardsSorted = [x for x in allCardsSorted if x not in topCards]
                        topCards+=allCardsSorted[-1:]
                        short_desc ="Two pair."
        else:
            #check for four of a kind
            if 4 in numeral_dict_int.values():
                handRank = 7
                topCards = [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[numeral_dict_int.values().index(4)]]]
                allCardsSorted = [x for x in allCardsSorted if x not in topCards]
                topCards+=[allCardsSorted[-1]]                  
                short_desc ="Four-of-a-kind."
            elif 3 in numeral_dict_int.values():
                handRank = 6
                topCards = [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[lastValueInList(numeral_dict_int.values(),3)]]]
                #see is there a second set of trips or a pair
                if topCards != [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[numeral_dict_int.values().index(3)]]]:
                    topCards += [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[numeral_dict_int.values().index(3)]]][0:2]
                else:
                    topCards += [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[lastValueInList(numeral_dict_int.values(),2)]]]
                short_desc ="Full house."
            #else two pair (3 pairs but take best two)
            else:
                handRank = 2
                bottomPair = [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[numeral_dict_int.values().index(2)]]]                 
 
                allCardsSorted = [x for x in allCardsSorted if x not in bottomPair]
                topCards = [x for x in allCardsSorted if x[0] == suit_value_dict_rev[numeral_dict_int.keys()[lastValueInList(numeral_dict_int.values(),2)]]]
                allCardsSorted = [x for x in allCardsSorted if x not in topCards]
                if allCardsSorted[0][0]==allCardsSorted[1][0]:
                    topCards+=allCardsSorted[0:2]
                    kicker = allCardsSorted[-1]
                elif allCardsSorted[1][0]==allCardsSorted[2][0]:
                    topCards+=allCardsSorted[1:]
                    kicker = allCardsSorted[0]
                else:
                    topCards.append(allCardsSorted[0])
                    topCards.append(allCardsSorted[2])
                    kicker = allCardsSorted[1]
                if bottomPair[0][0]>kicker[0]:
                    topCards.append(bottomPair[0])
                else:
                    topCards.append(kicker)                              
                short_desc = "Two pair."
        self.handRank = handRank
        self.bestCards = topCards
        self.handDesc= short_desc

def testHighCard():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['Ac','2h'])
    theFlop = ['4c','5h','Kd','7s','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have High Card (rank 0) with cards ['Ac','Kd','Jc','7s','5h']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)   
    
def testOnePair():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['Ac','2h'])
    theFlop = ['4c','Ah','Kd','7s','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have One Pair (rank 1) with cards ['Ac','Ah','Kd','Jc','7s']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)   
    
def testTwoPair():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['Ac','2h'])
    theFlop = ['4c','Ah','Kd','Ks','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Two Pair (rank 2) with cards ['Ac','Ah','Ks','Kd','Jc']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)   
         
  
def testThreePair():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['Ac','Jh'])
    theFlop = ['4c','Ah','Kd','Ks','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Two Pair (rank 2) with cards ['Ac','Ah','Ks','Kd','Jc']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)   
                  
def testTrips():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['Ac','2h'])
    theFlop = ['4c','Ah','Ad','Ks','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Trips (rank 3) with cards ['Ac','Ah','Ad','Ks','Jc']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)   

def testStraightAce():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['Ac','2h'])
    theFlop = ['4c','3h','5d','Ks','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Straight (rank 4) with cards ['5d,'4c','3h','2h','Ac']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          

def testStraight():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['6c','2h'])
    theFlop = ['4c','3h','5d','Ks','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Straight (rank 4) with cards ['6c','5d','4c','3h',2h']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          

def testFlush():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['6c','2c'])
    theFlop = ['4c','3h','5c','Kc','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Flush (rank 5) with cards ['Kc','Jc','6c','5c','4c']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          
     
def testFullHouseTripsHigh():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['6c','2c'])
    theFlop = ['4c','6h','Kd','Kc','Kh']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Full house (rank 6) with cards ['Kc','Kd','Kh','6c','6h']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          

def testFullHousePairHigh():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['6c','2c'])
    theFlop = ['4c','6h','6d','Kc','Kh']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Full house (rank 6) with cards ['6c','6h','6d','Kc','Kh']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          

def testFullHouseTwoTrips():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['6c','2c'])
    theFlop = ['Kd','6h','6d','Kc','Kh']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Full house (rank 6) with cards ['Kc','Kh','Kd','6h','6d']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          
    
def testFullHouseTwoPairs():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['2h','2c'])
    theFlop = ['Kd','6h','6d','Kc','Kh']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Full house (rank 6) with cards ['Kc','Kh','Kd','6h','6d']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          
        
def testQuads():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['2h','2c'])
    theFlop = ['Kd','Ks','6d','Kc','Kh']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have quads (rank 7) with cards ['Kc','Kh','Kd','Ks','6d']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          
    
def testStraightFlushAce():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['Ac','2c'])
    theFlop = ['4c','3c','5c','Ks','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Straight Flush (rank 8) with cards ['5c,'4c','3c','2c','Ac']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          

def testStraightFlush():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['6c','2c'])
    theFlop = ['4c','3c','5c','Ks','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Straight flush (rank 8) with cards ['6c','5c','4c','3c',2c']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          

def testRoyalFlush():
    theDeck = deckOfCards()
    player0 = player(0,theDeck,['Ac','Kc'])
    theFlop = ['4c','3h','Tc','Qc','Jc']
    theDeck.removeCardsFromDeck(theFlop)
    player0.myBestHand(theFlop)
    print "Player should have Straight (rank 4) with cards ['Ac,'Kc','Qc','Jc','Tc']"    
    print "Player does has %s (rank %d) with cards %s" %(player0.handDesc,player0.handRank,player0.bestCards)          

if __name__=="__main__":
    testHighCard()#ok
    testOnePair()#ok
    testTwoPair()#ok
    testThreePair()#ok
    testTrips()#ok
    testStraightAce()#ok
    testStraight()#ok
    testFlush()#ok
    testFullHouseTripsHigh()#ok
    testFullHousePairHigh()#ok
    testFullHouseTwoTrips()#ok
    testFullHouseTwoTrips()#ok
    testQuads()#ok
    testStraightFlushAce()#ok
    testStraightFlush()#ok
    testRoyalFlush()#ok