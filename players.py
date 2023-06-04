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

        value += card.value
        self.cards.append(card.card[1:])
    
    def over_21(self):
        '''Purpose:to check to see if Player has bust
        Post-conditions: will change the value of self.is_bust to True if over 21
        '''
        if value > 21 and "A" in self.cards:
            value -=10
        elif value > 21:
            self.is_bust = True
    

class Dealer(Player):
    pass

class User(Player):
    pass




    

