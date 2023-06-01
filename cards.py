import pygame
import os
import random as rn




main_dir = os.path.split(os.path.abspath(__file__))[0] 
image_dir = os.path.join(main_dir, "images") 


def load_image(name):
    '''Purpose:to load an image 
    :param name: name of the image 
    :note:must be in images directory in order to load
    :return:image a Suface object that represents the image
    :return:image.get_rect() a Rect object that represents image as Rect
    '''
    abs_path = os.path.join(image_dir,name)
    image = pygame.image.load(abs_path)
    return image,image.get_rect()

class Card:
    def __init__(self,card):
        self.card = card
        self.value = self.calc_value(card)

    def calc_value(self,card):
        '''Purpose:to determine a cards value according to blackjack rules
        :param card: string representing a card 
        :return value: int representing the cards value
        :note: aces will default to 11
        
        '''
        card_value = card[1:]
        numbers = [n for n in range(2,11)]
        tens = ["J","Q","K"]
        value = None

        if card_value in tens:
            value = 10
        elif card_value == "A":
            value = 11
        else:
            for num in numbers:
                if int(card_value) == num:
                    value = num
        return value
        

class Deck(object):
    '''Purpose:used for representing a deck of cards'''
    def __init__(self):
        
        self.__deck = []
        self.load_deck()
    
    def load_deck(self):
        '''Purpose:to create a new deck of cards
        Post-conditions:will modify self.__deck contents'''
        numbers = [str(n) for n in range(2,11)]
        numbers.extend(["A","J","Q","K"])
        card_type = ["S","H","D","?"]

        for type in card_type:
            for num in numbers:
                a_card = type + num
                self.__deck.append(a_card)
        
        rn.shuffle(self.__deck)


    def deal(self):
        """Purpose:to deal out a single card
        Post-conditions:will remove an element out the list
        :returns a card object:"""

        a_card = self.__deck[-1]
        self.__deck.pop()
        return Card(a_card)
    

                