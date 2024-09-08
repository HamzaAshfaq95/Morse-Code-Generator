from morse import Morse

Morse = Morse()
print("Hello! Welcome to Morse Code Generator")
run = True
while run == True:
    code_input = int(input("Do you want to code or decode?\nWrite 1 for 'Code'\nWrite 2 for 'Decode'\nWrite 3 to close 'Morse Code Generator'\nInput: "))
    if code_input == 3:
        run = False
    Morse.morse_coder(code_input)