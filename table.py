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





def main():
    '''
    Purpose:program that runs the gui
    '''
    pygame.init()
    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    
    done = False
    clock = pygame.time.Clock()


    the_card = C.Card("H7")
    GREEN = (0,255,0)
    # background = pygame.Surface(screen.get_size())
    

    
    

    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    the_card.move_image(screen,(1000,1))

        
        # screen.blit(background,(0,0))
        screen.fill(GREEN)
        the_card.draw_image(screen)
    
        
        

        
        
        pygame.display.flip()
        clock.tick(60)
 

    pygame.quit()