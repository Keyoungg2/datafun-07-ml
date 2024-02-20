# Code for creating, shuffling and dealing the Cards 

#import deck in
from deck import DeckOfCards

#set function for deck to repersent
deck_of_cards = DeckOfCards()

print(deck_of_cards)

#shuffling of cards
deck_of_cards.shuffle()

print(deck_of_cards)

# dealing Cards
deck_of_cards.deal_card()

# Class Card’s Other Features
card = deck_of_cards.deal_card()

str(card)

card.image_name