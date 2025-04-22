from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage
from card import Card
from breakdowntext import generate_mtg_image_prompt_from_scryfall as img_gen_prompt
import os
from pathlib import Path
 
llm = OllamaLLM(model="dolphin3")

character = "little blonde girl"
style_input = "lewd art"
card_name = "Faerie Mastermind"
test_card = Card(card_name)
type_line = test_card.info_block['type_line']
oracle_text = test_card.info_block['oracle_text']

messages = [
    SystemMessage( f"""
        Output should be in the form of a paragraph of short descriptive image tags, incomplete setances; noun or descriptive adjective noun"),
        Be descriptive: Include details about colors, shapes, objects, and composition. Provide additional context,
        Create an image generation prompt for an image based on the phrase {card_name} and on actions {oracle_text}.
        The main focus is a {type_line} {style_input} {character}.
        """ ),
    HumanMessage(  f"Generate tags." )
]

"""
first_generation = llm.invoke( messages )
print(first_generation)
"""

messages = [
    SystemMessage(
        """
        General Guidelines:
            You are a bot build to take in a magic the gathering card name, effect, types
            as well as maybe a character description and a style prompt, and blend elements of 
            all those inputs into a image generation prompt.
        Response Guidelines:
            Structure: The response should be a unordered list of descriptive statements
            Descriptive: Use vivid detailed descriptions
            Complete: The description of the scene should be complete and address all details
            The inputs: phrase: is the name of the card the artwork is for; description: is the oracle text, or abilities and effects of the
            card that the image is for, they should be used to inform that final generation.  

            Example Output:
            sexy young blonde girl, sevelte body, medium breasts, flawless body, blue color palette, {depth of field,blurry foreground, contrast, backlighting}, glowing eyes,
        """),
    SystemMessage(f"Combine the inputs into an image generation prompt based on the phrase {card_name} and the decription: {oracle_text}"),
    HumanMessage( f"{character} {type_line} {style_input}")
]


second_generation = llm.invoke( messages )
print( second_generation )


# print(img_gen_prompt(test_card.info_block))

