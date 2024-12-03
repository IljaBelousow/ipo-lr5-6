with open("output.txt", "w", encoding= 'utf-8') as b:
    with open("ipo-lr5-text.txt", "r", encoding= 'utf-8') as a:
        for line in a:
            b.write(line[::-1]) 

