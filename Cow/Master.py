from Card import *
from random import randint
from dick import Player as Nplay
from tom import Player as Eplay
from harry import Player as Wplay
from jrstq4 import Player as Splay
#test game player
## N E S W order always



North = Nplay("North")
East = Eplay("East")
South = Splay("South")
West = Wplay("West")

while True:
    North.StartGame("North")
    East.StartGame("East")
    South.StartGame("South")
    West.StartGame("West")

    TotalWins = {"North": 0, "East": 0, "South": 0, "West": 0}

    numjames = input("NUM JAMES?")
    numjames = int(numjames)

    if numjames < 10:
        printy = True
    else:
        printy = False
        
    for james in range(numjames):
        PastTricks = ()
        PastHands = {"North": 0, "East": 0, "South": 0, "West": 0}

        Which_Deal = 0

        #start game
        while Which_Deal <4:

            PlayLineUp = [North, East, South, West]
            PlayLineUpStr = ["North", "East", "South", "West"]
            #Batting order for each deal changes
            for x in range(Which_Deal):
                for lst in (PlayLineUpStr, PlayLineUp):
                    LastItem = lst.pop(0)
                    lst.append(LastItem)
            Which_Deal += 1
            
            GameDeck = Deck()
            GameDeck.Shuffle()
            
            Hands = {"North":[], "East":[], "South":[], "West":[]}
            for player in Hands.keys():
                for x in range(13):
                    Hands[player].append(GameDeck.DealOne())

            if printy:    
                print("DEAL NUMBER:{}, {} START".format(Which_Deal+ 1, PlayLineUpStr[0]))
                for lis in Hands.keys():
                        Hands[lis] = sorted(Hands[lis], key=lambda x: x.Rank)
            #start HAND
            while len(Hands["North"]) > 0:
                
                ThisTrick = ()
                if printy:
                    for plyr in Hands.keys():
                    
                        print(plyr, "Hand:", Hands[plyr])
                    
                ThisTurnMoves = {"North":[], "East":[], "South":[], "West":[]}
                ###Get int moves
                for player in PlayLineUp:
                    ID = player.GetID()
                    ChoiceInt = player.PlayCard(tuple(Hands[ID]), ThisTrick, PastTricks, PastHands)
                    Card = Hands[ID].pop(ChoiceInt)
                    ThisTurnMoves[ID] = Card
                    ThisTrick = ThisTrick + (Card,)

                if printy:
                    
                    printstr = ""
                    for x in range(4):
                        printstr += PlayLineUpStr[x]
                        printstr += ThisTrick[x].__str__()
                        printstr += ",   "
                    print(printstr)
                #Who wins?
                WinnerCard = ThisTrick[0]
                for card in ThisTrick[1:]:
                    if card.GetSuit() == ThisTrick[0].GetSuit():
                        if card.NumericRank() > WinnerCard.NumericRank():
                            WinnerCard = card

                for plr in ThisTurnMoves.keys():
                    if ThisTurnMoves[plr] == WinnerCard:
                        WinnerStr = plr
                        break

                PastHands[WinnerStr] += 1

                TrickTup = tuple(ThisTrick) + (PlayLineUpStr[0], WinnerStr)

                PastTricks = PastTricks + (TrickTup,)
                #change batting order
                LeadInt = PlayLineUpStr.index(WinnerStr)
                for x in range(0, LeadInt):
                    for lst in (PlayLineUpStr, PlayLineUp):
                        LastItem = lst.pop(0)
                        lst.append(LastItem)
                if printy:
                    print(PastHands)
                    input("")
    ##            print("cardsused", South.used_cards)
    ##            print("cardsleft", South.CardsLeft())
    ##            print("hand", Hands["South"])
    ##            print(South.OneSuit(South.CardsLeft(), "S"))
    ##            input("")
        
            

        maxwin = 0
        winall_str = "4 WAY DRAWR"
        Tie = False
        for player in PastHands.keys():
            if PastHands[player] > maxwin:
                maxwin = PastHands[player]
                winall_str = player
            elif PastHands[player] == maxwin:
                Tie = True
                Tiewinner = player
                
        if not Tie:        
           
            TotalWins[winall_str] += 1
        else:
            #print("TIE!", winall_str, Tiewinner)
             pass
            
    print(TotalWins)
    print("SouthWins: {}%".format((TotalWins["South"]/sum(TotalWins.values()))*100))
    input("")
