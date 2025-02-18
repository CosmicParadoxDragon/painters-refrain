# from constants import
from decklist import Decklist
from card import Card

def main():
    # Fetch decklist
    # build card objects
    # create text prompts
    # load image generator model
    # dispatch to image generator
    aus = Card("Austere Command")
    print(aus.get_card())

if __name__ == "__main__":
    main()
