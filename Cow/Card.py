import random
class Card(object):
    def __init__(self, suit = '', rank = 0):
        self.Suit = suit
        self.Rank = rank # INTEGER
        if self.Suit.upper() in ('H', 'D'):
            self.Color = 'Red'
        else:
            self.Color = 'Black' 
        self.FaceDown = False
        
    def SetSuit(self, NewSuit):
        self.Suit = NewSuit
		
    def GetSuit(self): 
            return self.Suit
            
    def GetRank(self):
            return self.__RankStr()
        
    def NumericRank(self): 
        return self.Rank; 
            
    def __RankStr(self): 
        if self.Rank in range(2, 11):
            RStr = str(self.Rank)
        elif self.Rank == 11:
            RStr = 'J'
        elif self.Rank == 12:
            RStr = 'Q'
        elif self.Rank == 13:
            RStr = 'K'
        elif self.Rank == 14:
            RStr = 'A'
        else: # should be an error, this should never happen
            RStr = ''
        return RStr
    

    def __str__(self): # Note: Table lookup would be faster. 
        RStr = self.__RankStr()
        RStr = RStr + self.Suit
        if self.FaceDown:
            RStr = '**'
        return '{:>4}'.format(RStr)
		
    def __repr__(self): 
        return self.__str__()

    def TurnFaceUp(self):
        self.FaceDown = False
    def TurnFaceDown(self):
        self.FaceDown = True

class Deck(object):
    def __init__(self):
        self.Cards = []
        for rank in range(2, 15):
            for suit in ('S', 'H', 'D', 'C'):
                self.Cards.append(Card(suit, rank))
    
    def Shuffle(self):
        random.shuffle(self.Cards)

    def DealOne(self):
        ACard = self.Cards.pop()
        return ACard

    
if __name__ == '__main__':
    MyDeck= Deck()
    MyDeck.Shuffle()
    for j in range(len(MyDeck.Cards)):
        MyDeck.Cards[j].TurnFaceUp()
    for j in range(5):
        print(MyDeck.DealOne())
        

    
