# A to E and E to A and a to e and e to a using single while loop

i = 1
while (i <= 10):
    if i <=5:
        print(chr(i + 64),"\t",chr(i + 96))
    else:
        print(chr(75 - i),"\t",chr(107 - i))
    i += 1