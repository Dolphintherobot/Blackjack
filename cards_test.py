
import pygame









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
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    
    done = False
    clock = pygame.time.Clock()

    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        

        
        GREEN = (0,255,0)
        screen.fill(GREEN)
        pygame.display.flip()
        pygame.time.wait(500)
        clock.tick(60)
 

    pygame.quit()




main()