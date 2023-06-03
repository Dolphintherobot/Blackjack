
import pygame
import os

import cards as C








# pygame.draw.rect(screen,
#                  color,
#                  [(margin + width) * column + margin,
#                   (margin + height) * row + margin,
#                   width,
#                   height])       






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



#check  deck and card classes 

a_deck = C.Deck()
a_deck.load_deck()
test = "deck and card"

reason = "make sure that everything is representing  "

is_print= False

n = 0

while n != 52:
    n+=1
    the_card = a_deck.deal()
    if is_print:
        print(the_card.card,the_card.value)
    


main()