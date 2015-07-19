import Card 
import pickle 

# change name of module to name of your python file 
from jrstq4 import Player 

def TestHand(Hand, ThisTrick, Tricks, Choice): 
    if not Choice in range(len(Hand)):  # out of range for size of hand 
        return False 
    elif len(ThisTrick) == 0:  # lead card, anything would be OK 
        return True 
    else:
        Suit = ThisTrick[0].GetSuit() 
        Compare = Hand[Choice].GetSuit() 
        if Suit == Compare: # followed suit 
            return True 
        else:
            for c in Hand:  # didn't follow suit, were there any of that suit in hand? 
                if c.GetSuit() == Suit:  # yep, this was a misplay 
                    return False 
            # if we're here, then there was nothing of that suit to play 
            return True 
        
    

if __name__ == '__main__': 
    P = Player('Test')
    P.StartGame('North')
    
    try:
        DataFile = open("HandData.dat", "rb")
    except IOError:
        print("Data file not found, please check target directory and try again.")
    else:
        N = 0
        Fails = 0
        PointDict = {'North':0, 'South':0, 'East':0, 'West':0} 
        ingt = 0
        while True: 
            try: 
                if ingt%500 == 0:
                    print(ingt)
                Hand = pickle.load(DataFile)
                Trick = pickle.load(DataFile)
                N += 1
                for i in range(len(Hand)):  # new code begins here
                   Hand[i].TurnFaceUp()
                for i in range(len(Trick[-1])):
                    Trick[-1][i].TurnFaceUp() 
                if len(Trick[-1]) == 4: 
                    ThisTrick = ()
                else:
                    ThisTrick = tuple(Trick[-1])
                Choice = P.PlayCard(Hand, ThisTrick, (Trick), PointDict)
                if not TestHand(Hand, ThisTrick, Trick, Choice):
                    print("Error in hand", N)
                    print("Hand: ", Hand) 
                    print("Presented with:", ThisTrick)
                    print("Returned:", Choice)
                    print("==================================================\n")
                    Fails += 1
                ingt += 1
                          
            except EOFError: 
                DataFile.close()
                print(N, "hands read.")
                if Fails == 0: 
                    print("Silence is golden.") 
                break
            
                
    