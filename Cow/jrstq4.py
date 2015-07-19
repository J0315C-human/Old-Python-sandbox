from Card import *
from random import randint


class Player(object):
    def __init__(self, ID : str):
        self.ID = ID

        self.used_cards = []
        self.cardchoice = "wrong" #here for testing
        self.TurnCount = 0
        self.SuitLst = ["H", "S", "C", "D"]
        self.unused_cards = []
        self.Imaginary_Deck = Deck()
        
        for j in range(len(self.Imaginary_Deck.Cards)):
            self.Imaginary_Deck.Cards[j].TurnFaceUp()
        
        
    def GetID(self):
        return self.ID
    def GetPosition(self):
        return self.position
    
    def StartGame(self, Pos : str):
        self.position = Pos
        self.used_cards = []
        self.unused_cards = []
        self.TurnCount = 0
        
    def UpdateUsedCards(self, ThisTrick, PastTricks):
        self.used_cards.extend(ThisTrick)
        if (self.TurnCount % 13) > 0:
            try:
                for x in range(4):
                    self.used_cards.append(PastTricks[-1][x])
            except (ValueError , IndexError):
                pass
            
        self.used_cards = list(set(self.used_cards))
        self.used_cards = sorted(self.used_cards, key=lambda x: x.Rank)
        
    def UsedCardsStr(self):
        newlist = []
        for card in self.used_cards:
            newlist.append(card.__str__())

        newlist = set(newlist)
        newlist = list(newlist)
        return newlist
    
    def CardsLeft(self, hand=()):
        handstrs = []
        for card in hand:
            handstrs.append(card.__str__())
        
        used_cards_str = self.UsedCardsStr()
        unused_cards = []
        for card in self.Imaginary_Deck.Cards:
            if card.__str__() in used_cards_str:
                continue
            if card.__str__() in handstrs:
                continue
            unused_cards.append(card)

        return unused_cards
    
    def CardsLeftStr(self, hand=()):
        unused_cards = []
        for card in self.CardsLeft(hand):
            unused_cards.append(card.__str__())

        return unused_cards
    
    def CommonSuit(self, hand=()):
    #most common suit of cards left, available in your hand
        HSCD = [0, 0, 0, 0]
        for card in self.unused_cards:
            cardsuit = card.GetSuit().upper()
            if cardsuit == "H":
                HSCD[0] += 1
            elif cardsuit == "S":
                HSCD[1] += 1
            elif cardsuit == "C":
                HSCD[2] += 1
            elif cardsuit == "D":
                HSCD[3] += 1
            else:
                pass
        MaxIndex = HSCD.index(max(HSCD))
        
        CommonSuit = self.SuitLst[MaxIndex]
        
        if len(hand) > 0:
            increment = 1
            while True:
                for card in hand:
                    if card.GetSuit().upper() == CommonSuit:
                        #print("Comonsuit", CommonSuit)
                        return CommonSuit
                HSCD[MaxIndex] -= increment
                MaxIndex = HSCD.index(max(HSCD))
                CommonSuit = self.SuitLst[MaxIndex]
                #print(HSCD)
                increment += 1
        return CommonSuit

    def RareSuit(self, hand=()):
    #most rare suit left of cards unplayed, in your hand
        HSCD = [0, 0, 0, 0]
        for card in self.unused_cards:
            cardsuit = card.GetSuit().upper()
            if cardsuit == "H":
                HSCD[0] += 1
            elif cardsuit == "S":
                HSCD[1] += 1
            elif cardsuit == "C":
                HSCD[2] += 1
            elif cardsuit == "D":
                HSCD[3] += 1
            else:
                pass
        
        MinIndex = HSCD.index(min(HSCD))

        RareSuit = self.SuitLst[MinIndex]
        #print(hand)
        if len(hand) > 0:
            while True:
                increment = 1
                for card in hand:
                    if card.GetSuit().upper() == RareSuit:
                        #print("raresuit", RareSuit)
                        return RareSuit
                HSCD[MinIndex] += increment
                MinIndex = HSCD.index(min(HSCD))
                #print(HSCD)
                RareSuit = self.SuitLst[MinIndex]
                increment += 1
        return RareSuit
                

    def PlayCard(self, Hand, ThisTrick, PastTricks, PastHands):
        #reset cardcount per hand
        if self.TurnCount % 13 == 0:
            self.used_cards = []
        
        self.UpdateUsedCards(ThisTrick, PastTricks)
        self.unused_cards = self.CardsLeft(Hand)
        self.TurnCount += 1
            
        # only one card in hand
        if len(Hand) == 1:
            return 0

        #check if you're leading
        if len(ThisTrick) == 0:
            self.cardchoice = self.PickLeadCard(Hand, ThisTrick)
            return self.cardchoice

        self.CanFollow = self.CanFollowSuit(Hand, ThisTrick)
        # if only one card to follow suit
        if self.CanFollow == True:
            self.follow_suit_hand = self.OneSuit(Hand, ThisTrick[0].GetSuit())
            self.follow_suit_hand = sorted(self.follow_suit_hand, key=lambda x: x.Rank)
            if len(self.follow_suit_hand) == 1:
                return Hand.index(self.follow_suit_hand[0])
            
        if len(ThisTrick) == 1 or len(ThisTrick) == 2:
            self.cardchoice = self.Pick23Card(Hand, ThisTrick)
        else:
            self.cardchoice = self.PickLastCard(Hand, ThisTrick)

        return self.cardchoice
        
    def CantFollow(self, Hand):
        #play lowest card of most common suit???
        BestSuit = self.RareSuit(Hand)
        SuitCards = self.OneSuit(Hand, BestSuit)
        SuitCards = sorted(SuitCards, key=lambda x: x.Rank)
        return Hand.index(SuitCards[0])
        
    def PickLeadCard(self, Hand, ThisTrick):
        BestSuit = self.RareSuit(Hand)
        SuitCards = self.OneSuit(Hand, BestSuit)
        SuitCards = sorted(SuitCards, key=lambda x: x.Rank)
        return Hand.index(SuitCards[-1])

    def Pick23Card(self, Hand, ThisTrick):
        #follow_suit_hand = self.OneSuit(Hand, ThisTrick[0].GetSuit())
        if self.CanFollow == True:
            HighCard = self.follow_suit_hand[-1]
            LowCard = self.follow_suit_hand[0]
            if HighCard.Rank > ThisTrick[0].Rank:
                #!!test if higher cards are still unplayed
                return Hand.index(HighCard)
            else:
                return Hand.index(LowCard)
            
        else:
            return self.CantFollow(Hand)
        
    def PickLastCard(self, Hand, ThisTrick):
        if self.CanFollow == True:
            HighCard = self.follow_suit_hand[-1]
            LowCard = self.follow_suit_hand[0]
            if HighCard.Rank > ThisTrick[0].Rank:
                return Hand.index(HighCard)
            else:
                return Hand.index(LowCard)
        else:
            return self.CantFollow(Hand)

    def OneSuit(self, Hand, suit)->list:
        one_suit = []
        for card in Hand:
            if card.GetSuit() == suit:
                one_suit.append(card)
        return one_suit
    
    def CanFollowSuit(self, Hand, ThisTrick)-> bool:
        trick_suit = ThisTrick[0].GetSuit()
        for card in Hand:
            if card.GetSuit() == trick_suit:
                return True
        return False
