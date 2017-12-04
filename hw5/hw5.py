with open("text.txt", "w", encoding="utf-8") as f:
    word=input()
    while word != "":
        if len(word)>5:
            f.write(word+"\n")
        word=input()

        

    
