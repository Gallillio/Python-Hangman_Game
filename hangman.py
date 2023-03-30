hanged = input("Enter Secret Word: ")
listed_hanged = list(hanged)

dash = "-" * len(hanged)
listed_dash = list(dash)

print(dash)

#the times of loses, to calculate if the player has lost yet or not 
loses = 0

for i in range(100):
    letterInputed = input("Enter letter: ")
    if letterInputed in listed_hanged:
        print(f"Letter {letterInputed} FOUND!!!!")
        #get indexes of letter inputed
        letter_index = []
        for j in range(len(listed_hanged)):
            if listed_hanged[j] == letterInputed:
                letter_index.append(j)
#         print(letter_index)
        for k in range(len(letter_index)):
            dash = dash[:letter_index[k]] + letterInputed + dash[letter_index[k] + 1:]
        
        print(dash)
        if dash == hanged:
            print(f"YOU WINNNN, THE WORLD IS: {hanged}")
            break
    else:
        print(f"WRONNNG LETEER")
        loses = loses +1
        lives_left = 7 - loses
        print(f"{lives_left} lives left")
        
        if loses == 6:
            print("\n YOU LOST YOU LOSERR")
            break