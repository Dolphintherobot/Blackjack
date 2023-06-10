import cards

class Player:
    '''Purpose:create a base class for dealer and the_player to inherit'''
    def __init__(self):
        self.value = 0
        self.cards = []
        self.is_bust = False

    def add_card(self,card):
        '''Purpose:to add a card into Players hand
        :param card: a card object'''


        self.value += card.value
        self.cards.append(card.card[1:])
    
    def over_21(self):
        '''Purpose:to check to see if Player has bust
        Post-conditions: will change the value of self.is_bust to True if over 21
        '''
        if self.value > 21 and "A" in self.cards:
            self.value -=10
        elif self.value > 21:
            self.is_bust = True
    

class Dealer(Player):

    def __init__(self):
        super().__init__()
        
    def is_staying(self):
        """Purpose: to check if dealer is staying or not
        :returns True if staying,False otherwise"""
        return self.value >= 17



    

