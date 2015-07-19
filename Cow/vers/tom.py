from Card import *
from random import randint
class Player(object):
    def __init__(self, ID : str):
        self.ID = ID

        self.used_cards = []
        self.cardchoice = "wrong" #here for testing
        self.TurnCount = 0
        
    def GetID(self):
        return self.ID

    def UpdateUsedCards(self, ThisTrick, PastTricks):
        self.used_cards.extend(ThisTrick)
        if self.TurnCount > 0:
            try:
                for x in range(4):
                    self.used_cards.append(PastTricks[-1][x])
            except (ValueError , IndexError):
                print("noe")
            
        self.used_cards = list(set(self.used_cards))
        
    def StartGame(self, Pos : str):
        self.position = Pos
        self.TurnCount = 0
        compass = ("North", "East", "South", "West")

        x = compass.index(Pos)
        self.Lpos = compass[(x+1)%4]
        self.Mpos = compass[(x+2)%4]
        self.Rpos = compass[(x+3)%4]

    def GetPosition(self):
        return self.position
    
    def PlayCard(self, Hand, ThisTrick, PastTricks, PastHands):

        #reset cardcount per hand
        if self.TurnCount == 13:
            self.used_cards = []
            self.TurnCount = 0
            
        
        self.UpdateUsedCards(ThisTrick, PastTricks)

        self.TurnCount += 1
        
        # only one card in hand
        if len(Hand) == 1:
            return 0

        #check if you're leading
        if len(ThisTrick) == 0:
            self.cardchoice = self.PickLeadCard(Hand, ThisTrick, PastTricks, PastHands)
            return self.cardchoice
        
        # if only one card to follow suit
        if self.CanFollowSuit(Hand, ThisTrick):
            self.follow_suit_hand = self.OneSuit(Hand, ThisTrick[0].GetSuit())
            if len(self.follow_suit_hand) == 1:
                return Hand.index(self.follow_suit_hand[0])

        if len(ThisTrick) == 1:
            self.cardchoice = self.PickSecondCard(Hand, ThisTrick, PastTricks, PastHands)
        elif len(ThisTrick) == 2:
            self.cardchoice = self.PickThirdCard(Hand, ThisTrick, PastTricks, PastHands)
        else:
            self.cardchoice = self.PickLastCard(Hand, ThisTrick, PastTricks, PastHands)

        return self.cardchoice
    
    def PickLeadCard(self, Hand, ThisTrick, PastTricks, PastHands):
        return randint(0, len(Hand)-1)

    def PickSecondCard(self, Hand, ThisTrick, PastTricks, PastHands):
        #follow_suit_hand = self.OneSuit(Hand, ThisTrick[0].GetSuit())
        if self.CanFollowSuit(Hand, ThisTrick) == True:
            return Hand.index(self.follow_suit_hand[0])
        else:
            return randint(0, len(Hand)-1)
        
    def PickThirdCard(self, Hand, ThisTrick, PastTricks, PastHands):
        if self.CanFollowSuit(Hand, ThisTrick) == True:
            return Hand.index(self.follow_suit_hand[0])
        else:
            return randint(0, len(Hand)-1)
        
    def PickLastCard(self, Hand, ThisTrick, PastTricks, PastHands):
        if self.CanFollowSuit(Hand, ThisTrick) == True:
            return Hand.index(self.follow_suit_hand[0])
        else:
            return randint(0, len(Hand)-1)

    def OneSuit(self, Hand, suit):
        one_suit = ()
        for card in Hand:
            if card.GetSuit() == suit:
                one_suit = one_suit + (card,)
        return one_suit
    
    def CanFollowSuit(self, Hand, ThisTrick)-> bool:
        trick_suit = ThisTrick[0].GetSuit()
        for card in Hand:
            if card.GetSuit() == trick_suit:
                return True
        #no matches
        return False

    

