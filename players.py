import cards

class Player:
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
        if value > 21 and :
