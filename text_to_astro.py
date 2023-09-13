# Define the planet symbols
planet_symbols = ['☉', '♁', '♀', '⨁', '♂', '♃', '♄', '♅', '♆', '♇', '☾', '☊', '☋', '☌', '☍', '☽', '⚳', '⚴', '⚵', '⚶', '⚷', '⚸', '⚹', '⚺', '⚻', '⚼']

# Define a custom encoding mapping of letters to combinations of planet symbols
encoding_mapping = {
    'A': '☉⚸',
    'B': '♁♀',
    'C': '♅♆',
    'D': '☽⨁',
    'E': '♇☋',
    'F': '⨁♇',
    'G': '☋♇',
    'H': '♇♀',
    'I': '♀☉',
    'J': '♀⨁',
    'K': '⚳⨁',
    'L': '⚸♀',
    'M': '⚶☋',
    'N': '⚸☽',
    'O': '☽☊',
    'P': '⚶♀',
    'Q': '⚸⚳',
    'R': '♃⨁',
    'S': '⨁♀',
    'T': '⚳⚶',
    'U': '⨁⚸',
    'V': '♀⚳',
    'W': '⚴⨁',
    'X': '♀☊',
    'Y': '⨁☊',
    'Z': '☊☋',
    '0': '☉☽',
    '1': '⚳☽',
    '2': '⨁⚴',
    '3': '⚴☊',
    '4': '♀⚴',
    '5': '⚳⚷',
    '6': '⚶⚷',
    '7': '⚴⚹',
    '8': '⚸⚹',
    '9': '☉⚸',
    ' ': ' ',
}

def encode_text(input_text):
    encoded_text = ""
    previous_encoding = ""
    
    for char in input_text.upper():
        if char in encoding_mapping:
            current_encoding = encoding_mapping[char]
            
            # Use the previous encoding if the current letter is the same as the previous one
            if current_encoding != previous_encoding:
                encoded_text += current_encoding
                previous_encoding = current_encoding
        else:
            # If the character is not in the mapping, keep it as it is
            encoded_text += char
            previous_encoding = ""
    
    return encoded_text

def decode_text(encoded_text):
    decoded_text = ""
    current_encoding = ""
    
    for char in encoded_text:
        current_encoding += char
        if current_encoding in encoding_mapping.values():
            for letter, encoding in encoding_mapping.items():
                if encoding == current_encoding:
                    decoded_text += letter
                    current_encoding = ""
                    break
        else:
            # If the current encoding doesn't match any mapping, keep it as is
            decoded_text += current_encoding
            current_encoding = ""
    
    return decoded_text

# Prompt for user choice (encode or decode)
choice = input("Choose 'encode' or 'decode': ").strip().lower()

if choice == 'encode':
    # Input text to be encoded
    input_text = input("Enter the text to encode: ")

    # Encode the input text
    encoded_text = encode_text(input_text)

    # Write the encoded text to a file in UTF-8 encoding
    with open("encoded.txt", "w", encoding="utf-8") as encoded_file:
        encoded_file.write(encoded_text)

    print("Encoded text has been written to 'encoded.txt'.")

elif choice == 'decode':
    # Input text to be decoded (paste the encoded text here)
    input_text = input("Paste the encoded text to decode: ")

    # Decode the input text
    decoded_text = decode_text(input_text)

    print("Decoded Text:", decoded_text)

else:
    print("Invalid choice. Please choose 'encode' or 'decode'.")
