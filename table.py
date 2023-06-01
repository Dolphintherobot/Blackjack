import cards
import pygame
import players

def hit(a_player,deck):
    '''Purpose:to deal another card to an instance of Players class
    :param a_player: an instance of Player class
    :param deck: an instance of Deck class
    '''
    card = deck.deal()
    a_player.add_card(card)
    a_player.over_21()

