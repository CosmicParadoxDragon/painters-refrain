from constants import TEST_DECK_PATH
from decklist import Decklist
from card import Card

def main():
    # Fetch decklist
    deck = Decklist(TEST_DECK_PATH)
    print(deck.get_decklist()[0]["name"])

    # create text prompts
    # load image generator model
    # dispatch to image generator
    
    

if __name__ == "__main__":
    main()
