import cards as c
import pygame
import players as p

def hit(a_player,deck):
    '''Purpose:to deal another card to an instance of Players class
    :param a_player: an instance of Player class
    :param deck: an instance of Deck class
    '''
    card = deck.deal()
    a_player.add_card(card)
    a_player.over_21()


def start_game(player:p.Player,dealer:p.Player,deck:c.Deck,image_collection:c.Images,screen):
    '''Purpose: to start the game
    :param player: instance of player class, representing the player
    :param dealer: instance of player class, representing the dealer
    :param deck: instance of deck class, representing card deck
    :param image_collection: instance of image class
    :param screen: surface to be drawn onto'''
    deck.load_deck()

    player_coord = (600,800)
    dealer_coord = (600,400)
    n = 0
    while n != 2:
        n+=1
        dealer_card = deck.deal()
        player_card = deck.deal()

        player_card.move_image(screen,player_coord,image_collection)
        dealer_card.move_image(screen,dealer_coord,image_collection)
        player_coord = (player_coord[0] -100,800)
        dealer_coord = (dealer_coord[0]-100,400)
        player.add_card(player_card)
        dealer.add_card(dealer_card)





def main():
    '''
    Purpose:program that runs the gui
    '''
    pygame.init()
    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    done = False
    clock = pygame.time.Clock()
    GREEN = (0,255,0)


    dealer = p.Player()
    user = p.Player()
    card_deck = c.Deck()
    image_collection = c.Images()
    
    
    

    
    # start_game(user,dealer,card_deck,image_collection,screen)

    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #hit
                    pass
                if event.key == pygame.K_LSHIFT or pygame.K_RSHIFT:
                    #stay
                    pass
                if event.key == pygame.K_LCTRL or pygame.K_RCTRL:
                    start_game(user,dealer,card_deck,image_collection,screen)
                    
                if event.key == pygame.K_ESCAPE:
                    done = True
        
        
        screen.fill(GREEN)
        image_collection.update(screen)
        
    
        
        

        
        
        pygame.display.flip()
        clock.tick(60)
 

    pygame.quit()



main()