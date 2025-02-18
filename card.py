import requests
from constants import SCRYFALL_URL

class Card():
    
    def __init__(self, name):
        self.info_block = {}
        self.name = name
        self.fetch_infomation()

    def fetch_infomation(self):
        name = self.name
        split_name = "+".join(map(lambda x: x, name.split()))
        self.info_block = requests.get(SCRYFALL_URL + split_name)

    def get_card(self ):
        return self.info_block.json()['name']

