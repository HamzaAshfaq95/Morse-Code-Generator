from codes import morse_code_dict

class Morse:
    def __init__(self):
        self.morse_coder
    def morse_coder(self, code_input):
        if code_input == 1:
            morse_code = []
            string_input = input("What to code?\n").upper()
            for letter in string_input:
                for item in morse_code_dict:
                    if item == letter:
                        value = morse_code_dict[item]
                        morse_code.append(value)
            print(f"Here is your morse code:\n{morse_code}")
        elif code_input == 2:
            code_string = ""
            code_input = input("What to decode?\n")
            values_to_be_replaced = ["[", "]", "'", ","]
            for value in values_to_be_replaced:
                code_input = code_input.replace(value, "")
            code_to_decode = code_input.split(" ")
            for code in code_to_decode:
                for item in morse_code_dict:
                    if morse_code_dict[item] == code:
                        letter = item
                        code_string = code_string + letter
            print(f"Here is your decoded string:\n{code_string}")
        else:
            if not code_input == 3:
                print("Provide correct input 1, 2 or 3")