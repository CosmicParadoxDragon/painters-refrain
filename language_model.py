from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage
from card import Card
import os 
from pathlib import Path

llm = OllamaLLM(model="dolphin3")

character = "little blonde girl, 11 years old"
style_input = "Gothic Lolita"
card_name = "Faerie Mastermind"
test_card = Card(card_name)
type_line = test_card.info_block['type_line']
oracle_text = test_card.info_block['oracle_text']

print(f"Name: {card_name}\nType Line: {type_line}\nOracle Text: {oracle_text}")

"""
first_generation = llm.invoke(f"Create an image generation prompt for an image called {card_name}." +
                              f"The image is for a card that depicts a {type_line}, as a final detail " +
                              f"the card does the following use that to inform the artwork {oracle_text}." +
                              f"The prompt should in the form of a comma seperated list, in a plain text paragraph.")
print(first_generation)


define_response = llm.invoke(f"Define the phrase {card_name} using short statements serperated by commas.")
style_breakdown_character = llm.invoke(f"Generate the quintessential features of {style_input} as it relates to characters.")
style_breakdown_scene = llm.invoke(f"Generate the breakdown of the style {style_input} as it relates to everything except characters.")

second_generation = llm.invoke(f"Transform this image generation prompt {first_generation} by adding, and changing details so" +
                               f"the style is {style_input} style. Making the character become {character} as a {type_line}" +
                               f" combining them together.  The background should be transformed becoming more {style_breakdown_scene}.")
print(second_generation)
"""
messages = [
    SystemMessage(f"Image Generation Prompt Creator"),
    HumanMessage(f"{style_input} {character} as a {card_name}, doing {oracle_text}")
]
prompt = llm.invoke(messages)
print(prompt)
