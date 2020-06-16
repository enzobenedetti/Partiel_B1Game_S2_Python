import random

#draw is the hangman drawing
draw = []
f = open("pendu.txt", "r")
i = 0
for x in f:
    draw.append(x)
    i = i + 1
f.close()
#Dict is the word dictionary (here a list)
dict = []
d = open("dict.txt", "r")
i = 0
for x in d:
    dict.append(x)
    i = i + 1
d.close()

#Choosing the word
word = random.randrange(0, len(dict))
wordlen = len(dict[word]) - 1
word = dict[word]
hideword = ["_ "] * wordlen
print(hideword)

step = 0
fail = 0
win = False
lettre = "00"
#Game loop
while fail < 8 and win == False:
    #choose letter
    while lettre.isalpha() == False or len(lettre) > 1 :
        lettre = input("Choose a letter : ")
        if len(lettre) > 1 :
            print("One letter at the time please")
        if lettre.isalpha() == False :
            print("Sorry, I take only letter")
    lettre = lettre.upper()
    #Check if letter is in the word
    if lettre in word :
        for x in range(len(word)):
            if word[x] == lettre:
                hideword[x] = lettre
    else :
        while ";" not in draw[step] and step + 1 < len(draw):
            print(draw[step])
            step = step + 1
        step = step +1
        fail = fail +1
    print(hideword)
    #check if you win
    if "_ " in hideword:
        win = False
    else :
        win = True
    lettre = "00"

if win == True:
    print("Congratulations, you win")
else :
    print("Too bad, you lose")
