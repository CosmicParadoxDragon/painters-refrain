import os
from pathlib import Path
from card import Card

class Decklist:
    def __init__(self, file_path):
        self.cards = []
        self.deck_file_path = file_path
        self.import_deck()

    def import_deck(self):
        if not os.path.isdir(self.deck_file_path):
            raise ValueError(f"Decks directory does not exist: {self.deck_file_path}")

        if not os.path.exists(self.deck_file_path):
            raise ValueError(f"Deck file does not exist in: {self.deck_file_path}")
        try:
            # Here we are just going to fetch the card names
            with open(self.deck_file_path, "r") as deck_file:
                for line in deck_file:
                    post_split = line.strip().split()
                    set_tag_index = 2
                    for i in range(set_tag_index, len(post_split)):
                        if "(" in post_split[i]:
                            set_tag_index = i

                    name_list = post_split[1:set_tag_index - 1]
                    card_name = " ".join(name_list)
                    self.cards.append(card_name)
        except:

    def get_decklist():
        return self.cards
    
    def get_file_path():
        return self.deck_file_path
