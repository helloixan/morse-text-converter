import json
json_file_path = 'morsedict.json'
with open(json_file_path, 'r') as json_data :
    morse_dict = json.load(json_data)['morse']
# print(morse_dict)

def text_to_morse(text):
    morse_units = []
    alphabets = [alpha for alpha in morse_dict['alphabet']]
    numbers = [number for number in morse_dict['number']]
    symbols = [symbol for symbol in morse_dict['symbols']]
    for unit in text :
        if (unit.upper() in alphabets) :
            unit = unit.upper()
            for alpha in alphabets :
                if unit == alpha :
                    morse_units.append(morse_dict['alphabet'][alpha])
        elif (unit in numbers) :
            for num in numbers:
                if unit == num :
                    morse_units.append(morse_dict['number'][num])
        elif (unit in symbols) :
            for symbol in symbols :
                if symbol == unit :
                    morse_units.append(morse_dict['symbols'][symbol])

    morse_code = ' '.join(morse_units)
    return morse_code

input_text = input("Text: ")
morse_code = text_to_morse(input_text)
print(f"Morse: {morse_code}")