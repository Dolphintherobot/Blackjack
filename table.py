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

    return player_coord,dealer_coord


def update_coord(coord,offset):
    """Purpose:to modify coordinates so that the next card can go into its proper place
    :param coord: x,y tuple
    :param:offset,int representing how much you want to subtract x by
    :return new_coords: tuple that modifies x value"""

    x,y = coord
    return (x-offset,y)


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
    offset = 100


    dealer = p.Dealer()
    user = p.Player()
    card_deck = c.Deck()
    image_collection = c.Images()
    has_stayed = False
    
    
    

    
    # start_game(user,dealer,card_deck,image_collection,screen)

    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    a_card = hit(user,card_deck)
                    a_card.move_image(screen,user_coord,image_collection)
                    user_coord = update_coord(user_coord,offset)
                    print("a")
                    
                if event.key == pygame.K_r:
                    print("c")
                    has_stayed = True 
                if event.key == pygame.K_s:
                    print("b")
                    dealer = p.Dealer()
                    user = p.Player()
                    card_deck = c.Deck()
                    image_collection = c.Images()
                    user_coord,dealer_coord= start_game(user,dealer,card_deck,image_collection,screen)

                if event.key == pygame.K_ESCAPE:
                    done = True
        
        if has_stayed and not dealer.is_staying():
            print(dealer.is_staying(),dealer.value)
            print(has_stayed and not dealer.is_staying())
            a_card = hit(dealer,card_deck)
            a_card.move_image(screen,dealer_coord,image_collection)
            dealer_coord = update_coord(dealer_coord,offset)
        
        elif not (has_stayed and not dealer.is_staying()):
            print(user.value,dealer.value)
            

        
        screen.fill(GREEN)
        image_collection.update(screen)
        
    
        
        

        
        
        pygame.display.flip()
        clock.tick(60)
 

    pygame.quit()



main()