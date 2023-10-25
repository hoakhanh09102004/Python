def lamdep(str):
    words = str.split()
    unique_word = ""
    words.sort()
    for word in words:
        if unique_word.find(word) == -1:
            unique_word += word + " "
    return (unique_word)
print(lamdep("hello world and practice makes and hello world again"))