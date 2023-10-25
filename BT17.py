def demtu(str):
    num_char = 0
    num_digit = 0
    for char in str:
        if char.isdigit():
            num_digit += 1
        if char.isalpha():
            num_char += 1
    return ('kí tự có:',num_char,'số có:',num_digit)     
print(demtu("Hello world! 123"))       