# install packages
import string

#define encode(input_text, shift)
def encode(input_text: str, shift:int):
    
    input_characters = [*input_text]
    all_eng_cha = [*string.ascii_lowercase]
    encoded = []

    for letter in input_characters:
      encoded.append(all_eng_cha[(all_eng_cha.index(letter) + shift)%26])
      
    
    return (
        (all_eng_cha, encoded)
    )

#define decode(input_text, shift)

def decode(input_text: str, shift:int):
        
    input_characters = [*input_text]
    all_eng_cha = [*string.ascii_lowercase]
    decoded = []

    for letter in input_characters:
       decoded.append(all_eng_cha[(all_eng_cha.index(letter) - shift)%26])

    return (decoded)
