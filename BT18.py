def demhoathuong(str):
    char_hoa = 0
    char_thuong = 0
    for char in str:
        if char.islower():
            char_thuong += 1
        if char.isupper():
            char_hoa += 1
    return ('kí tự thường có:',char_thuong,'kí tự hoa có:',char_hoa)     
print(demhoathuong("Lap Trinh Python"))