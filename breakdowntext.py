def generate_mtg_image_prompt_from_scryfall(card_data, style="fantasy"):
    """
    Generate an image prompt based on a Scryfall API card data response and desired art style.
    
    Parameters:
    card_data (dict): The JSON response from Scryfall API for a card
    style (str): Desired art style for the image
    
    Returns:
    str: Formatted image generation prompt
    """
    # Extract relevant information from the Scryfall data
    card_name = card_data.get("name", "")
    card_type = card_data.get("type_line", "")
    
    # Extract oracle text and keywords for effect description
    oracle_text = card_data.get("oracle_text", "")
    keywords = card_data.get("keywords", [])
    
    # Convert color identity to color name
    colors = card_data.get("colors", [])
    color_identity = card_data.get("color_identity", [])
    
    # Map color codes to names and determine overall color identity
    color_map = {
        "W": "White",
        "U": "Blue",
        "B": "Black",
        "R": "Red",
        "G": "Green"
    }
    
    if not colors and not color_identity:
        mana_color = "Colorless"
    elif len(colors) > 1 or len(color_identity) > 1:
        mana_color = "Multicolor"
    else:
        color_code = colors[0] if colors else color_identity[0]
        mana_color = color_map.get(color_code, "Colorless")
    
    # Generate effect description from oracle text and card characteristics
    effect_description = generate_effect_description(card_data)
    
    # Call the base function with extracted data
    return generate_mtg_image_prompt(card_name, card_type, effect_description, mana_color, style)


def generate_effect_description(card_data):
    """
    Generate a natural language description of the card's effects.
    
    Parameters:
    card_data (dict): The JSON response from Scryfall API for a card
    
    Returns:
    str: Natural language description of the card's effects
    """
    oracle_text = card_data.get("oracle_text", "")
    power = card_data.get("power", "")
    toughness = card_data.get("toughness", "")
    card_type = card_data.get("type_line", "")
    
    description = ""
    
    # Handle different card types
    if "Creature" in card_type:
        if power and toughness:
            description += f"a {power}/{toughness} creature that "
    
    # Process oracle text into natural language
    if oracle_text:
        # Remove reminder text (text in parentheses)
        import re
        clean_text = re.sub(r'\([^)]*\)', '', oracle_text)
        
        # Split into lines for multi-ability cards
        abilities = [line.strip() for line in clean_text.split('\n') if line.strip()]
        
        # Process each ability
        ability_descriptions = []
        for ability in abilities:
            # Handle common keywords
            if ability.startswith("This creature can't block"):
                ability_descriptions.append("is unable to block attackers")
            elif "Channel" in ability:
                ability_descriptions.append("can be discarded to manifest its power")
            elif "Flying" in ability:
                ability_descriptions.append("soars through the air")
            elif "Deathtouch" in ability:
                ability_descriptions.append("kills with a single touch")
            elif "Lifelink" in ability:
                ability_descriptions.append("drains life energy from its victims")
            else:
                # For other abilities, just use them directly but clean up a bit
                cleaned = ability.replace("{", "").replace("}", "")
                ability_descriptions.append(cleaned.lower())
        
        description += " and ".join(ability_descriptions)
    
    # Fallback for cards with no clear effect description
    if not description:
        if "Creature" in card_type:
            description = "embodies the essence of dark power"
        elif "Instant" in card_type:
            description = "unleashes a quick, powerful spell"
        elif "Sorcery" in card_type:
            description = "performs a complex magical ritual"
        elif "Enchantment" in card_type:
            description = "creates a persistent magical effect"
        elif "Artifact" in card_type:
            description = "harnesses mysterious powers"
        elif "Land" in card_type:
            description = "provides magical energy to fuel spells"
        elif "Planeswalker" in card_type:
            description = "commands powerful magic across the multiverse"
        else:
            description = "manifests magical energy in mysterious ways"
    
    return description


def generate_mtg_image_prompt(card_name, card_type, card_effect, mana_color, style):
    """
    Generate an image prompt based on MTG card details and desired art style.
    
    Parameters:
    card_name (str): Name of the MTG card
    card_type (str): Type of the card (Creature, Instant, etc.)
    card_effect (str): Description of what the card does
    mana_color (str): Color identity of the card (White, Blue, Black, Red, Green, Colorless, Multicolor)
    style (str): Desired art style for the image
    
    Returns:
    str: Formatted image generation prompt
    """
    # Base description derived from card mechanics
    base_description = ""
    
    # Handle card type specific imagery
    if "Creature" in card_type:
        base_description = f"A {mana_color} aligned creature, {card_name}, "
    elif "Instant" in card_type:
        base_description = f"A dynamic spell being cast, representing {card_name}, "
    elif "Sorcery" in card_type:
        base_description = f"A powerful magical ritual, {card_name}, "
    elif "Enchantment" in card_type:
        if "Saga" in card_type:
            base_description = f"A mystical storybook page or tapestry depicting the saga {card_name}, showing multiple connected scenes that "
        else:
            base_description = f"A mystical aura or enchantment, {card_name}, "
    elif "Artifact" in card_type:
        base_description = f"A magical artifact, {card_name}, "
    elif "Planeswalker" in card_type:
        base_description = f"A powerful {mana_color} planeswalker, {card_name}, "
    elif "Land" in card_type:
        base_description = f"A magical landscape, {card_name}, "
    elif "Battle" in card_type:
        base_description = f"An epic battlefield scene depicting the conflict {card_name}, showing a dynamic struggle that "
    else:
        base_description = f"A mystical {mana_color} entity, {card_name}, "
    
    # Add effect description
    base_description += f"{card_effect}. "
    
    # Add color-specific elements
    if "White" in mana_color:
        base_description += "Radiating light, order, and protection. "
    elif "Blue" in mana_color:
        base_description += "Emanating arcane knowledge and manipulation. "
    elif "Black" in mana_color:
        base_description += "Surrounded by darkness, decay, and power. "
    elif "Red" in mana_color:
        base_description += "Burning with passion, chaos, and destruction. "
    elif "Green" in mana_color:
        base_description += "Teeming with natural growth and primal force. "
    elif "Colorless" in mana_color:
        base_description += "With an otherworldly, eldritch presence. "
    elif "Multicolor" in mana_color:
        base_description += "Blending multiple magical energies in harmony. "
    
    # Add style-specific formatting
    style_description = ""
    style_lower = style.lower()
    
    if style_lower == "realistic":
        style_description = "Ultra-realistic digital painting, highly detailed textures, dramatic lighting, cinematic composition"
    elif style_lower == "fantasy":
        style_description = "High fantasy illustration, vibrant colors, epic scale, magical atmosphere, intricate details"
    elif style_lower == "minimalist":
        style_description = "Minimalist design, simple shapes, limited color palette, elegant composition, negative space"
    elif style_lower == "dark":
        style_description = "Dark fantasy artwork, ominous atmosphere, muted colors, shadowy details, forbidding environment"
    elif style_lower == "cyber":
        style_description = "Cyberpunk aesthetics, neon accents, tech infused, digital distortion, futuristic elements"
    elif style_lower == "anime":
        style_description = "Anime-inspired illustration, stylized characters, dynamic poses, bold outlines, expressive features"
    elif style_lower == "watercolor":
        style_description = "Elegant watercolor painting, soft color transitions, flowing textures, artistic brushstrokes"
    elif style_lower == "storybook":
        style_description = "Storybook illustration style, detailed narrative scenes, rich symbolism, illustrative quality"
    elif style_lower == "ukiyo-e":
        style_description = "Traditional Japanese ukiyo-e style, woodblock print aesthetics, flat perspective, decorative patterns"
    elif style_lower == "kamigawa":
        style_description = "Japanese-inspired fantasy art, Shinto spiritual elements, flowing forms, ethereal spirits, traditional ink painting style"
    else:
        style_description = "Professional fantasy card illustration, detailed rendering, atmospheric lighting"
    
    # Combine everything into final prompt
    return f"{base_description} {style_description}, 4K, professional quality, perfect for a trading card game illustration."


# Example usage with the provided Scryfall API response
if __name__ == "__main__":
    import json
    
    # Sample Scryfall data (you can replace this with actual API response)
    sample_card_data = {
        "object": "card",
        "name": "Shinen of Fear's Chill",
        "type_line": "Creature — Spirit",
        "oracle_text": "This creature can't block.\nChannel — {1}{B}, Discard this creature: Target creature can't block this turn.",
        "power": "3",
        "toughness": "2",
        "colors": ["B"],
        "color_identity": ["B"],
        "keywords": ["Channel"]
    }
    
    # Generate prompt with different styles
    dark_prompt = generate_mtg_image_prompt_from_scryfall(sample_card_data, "dark")
    kamigawa_prompt = generate_mtg_image_prompt_from_scryfall(sample_card_data, "kamigawa")
    anime_prompt = generate_mtg_image_prompt_from_scryfall(sample_card_data, "anime")
    
    print("DARK STYLE PROMPT:")
    print(dark_prompt)
    print("\nKAMIGAWA STYLE PROMPT:")
    print(kamigawa_prompt)
    print("\nANIME STYLE PROMPT:")
    print(anime_prompt)
    
    # Load and use the full provided JSON data
    try:
        # Parse the full JSON data provided in the document
        with open('paste.txt', 'r') as file:
            full_card_data = json.load(file)
            
        # Generate a prompt from the full data
        full_data_prompt = generate_mtg_image_prompt_from_scryfall(full_card_data, "fantasy")
        print("\nFULL DATA PROMPT:")
        print(full_data_prompt)
    except Exception as e:
        print(f"\nNote: Could not process full_card_data: {e}")
        print("Instead, here's a demonstration with the sample data above.")
