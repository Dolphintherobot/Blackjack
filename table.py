import cards as c
import pygame
import players as p

def hit(a_player,deck):
    '''Purpose:to deal another card to an instance of Players class
    :param a_player: an instance of Player class
    :param deck: an instance of Deck class
    :return card: class of Card
    '''
    card = deck.deal()
    a_player.add_card(card)
    a_player.over_21()

    return card




def start_game(player:p.Player,dealer:p.Player,deck:c.Deck,image_collection:c.Images,screen):
    '''Purpose: to start the game
    :param player: instance of player class, representing the player
    :param dealer: instance of player class, representing the dealer
    :param deck: instance of deck class, representing card deck
    :param image_collection: instance of image class
    :param screen: surface to be drawn onto
    :return: players and dealers coordinates for next card to be moved to'''
    image_collection.image_list.clear()
    deck.load_deck()
    image_collection.add_list(deck.image,(0,0))
    player_coord = (600,400)
    dealer_coord = (600,200)
    n = 0
    while n != 2:
        n+=1
        dealer_card = deck.deal()
        player_card = deck.deal()

        player_card.move_image(screen,player_coord,image_collection)
        dealer_card.move_image(screen,dealer_coord,image_collection)
        player_coord = (player_coord[0] -125,400)
        dealer_coord = (dealer_coord[0]-125,200)
        player.add_card(player_card)
        dealer.add_card(dealer_card)

    return player_coord,dealer_coord


def update_coord(coord,offset):
    """Purpose:to modify coordinates so that the next card can go into its proper place
    :param coord: x,y tuple
    :param:offset,int representing how much you want to subtract x by
    :return new_coords: tuple that modifies x value"""

    x,y = coord
    return (x-offset,y)


def check_winner(player:p.Player,dealer):
    '''Purpose:to check who is the winner of the game
    :param player: player class representing the player
    :param dealer: dealer class representing the dealer
    :return True if the player has won,False otherwise'''

    if player.value > dealer.value and not player.is_bust:
        return True
    elif player.value < dealer.value and dealer.is_bust and not player.is_bust:
        return True
    else:
        return False
   
def display_winner(player,dealer,image_collection):
    '''Purpose:to check who is the winner of the game
    :param player: player class representing the player
    :param dealer: dealer class representing the dealer
    :param image_collection: image_collection representing image storage'''

    BLACK = (0,0,0)
    font_type = pygame.font.get_default_font()
    font = pygame.font.Font(font_type)
    
    if check_winner(player,dealer):
        font = font.render("Player wins",True,BLACK)
    else:
        font = font.render("Dealer wins",True,BLACK)
    
    pygame.transform.scale(font,(300,200))
    image_collection.add_list(font,(500,25))
    

def main():
    '''
    Purpose:program that runs the gui
    '''
    pygame.init()
    pygame.font.init()
    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    done = False
    clock = pygame.time.Clock()
    GREEN = (0,255,0)
    offset = 125


    dealer = p.Dealer()
    user = p.Player()
    card_deck = c.Deck()
    image_collection = c.Images()
    has_stayed = False



    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                print(x,y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    a_card = hit(user,card_deck)
                    a_card.move_image(screen,user_coord,image_collection)
                    user_coord = update_coord(user_coord,offset)
                    user.over_21()
                    
                if event.key == pygame.K_r:
                    has_stayed = True 

                if event.key == pygame.K_s:
                    dealer = p.Dealer()
                    user = p.Player()
                    card_deck = c.Deck()
                    image_collection = c.Images()
                    has_stayed = False
                    user_coord,dealer_coord= start_game(user,dealer,card_deck,image_collection,screen)

                if event.key == pygame.K_ESCAPE:
                    done = True
        
        if has_stayed and not dealer.is_staying():
            a_card = hit(dealer,card_deck)
            a_card.move_image(screen,dealer_coord,image_collection)
            dealer_coord = update_coord(dealer_coord,offset)
            dealer.over_21()
        
        elif has_stayed and dealer.is_staying():
            display_winner(user,dealer,image_collection)
        
        
            

        
        screen.fill(GREEN)
        image_collection.update(screen)
        
    
        
        

        
        
        pygame.display.flip()
        clock.tick(60)
 

    pygame.quit()



main()