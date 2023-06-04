import players as p
import cards as c


#check is bust 

a_player = p.Player()

test = "is_bust and over21 and add_card methods"

reason = "check if over_21 works "  

is_print= True

n = 0
a_deck = c.Deck()

while n != 52:
    n+=1
    the_card = a_deck.deal()
    a_player.add_card(the_card)
    a_player.over_21()


if not a_player.is_bust:
    print(f"error with {test} reason is {reason} ")



