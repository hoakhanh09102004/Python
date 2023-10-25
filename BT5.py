def songuyento(n):
    dem=0
    for i in range(2,n+1,1):
        if n % i == 0:
            dem+=1
            if dem > 2:
                break
    if dem > 1:
        return ("không phải là số nguyên tố")
    else:
        return ("là số nguyên tố")
print(songuyento(8))