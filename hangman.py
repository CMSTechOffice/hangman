from turtle import *
from random import randint
import time
import math

s=getscreen()
sw =800
sh = 800
s.bgcolor("#222222")
s.setup(sw,sh)
t1=getturtle()
t1.color("#bbbbbb")
t1.width(5)
t1.shape("arrow")
tØ = Turtle()
tØ.hideturtle()
tı = Turtle()
tı.hideturtle()
fontS =int(sh*0.05)
alpha = "abcdefghijklmnopqrstuvwxyz"
letterswrong = ""
letterscorrect= ""
secret =""
display=""
fails= 6
t1.speed(0)
tØ.speed(0)
tı.speed(0)
tØ.color("white")
tı.color("white")
gameDone = False
boxTitle=""


wordlist = ["inception","pavilion",
"pseudoscience","shawl","pneumatic","capybara","smear","stutter",
"praenomen","betroth","progeny","exorcism","prodigy","granary","sphincter",
"awning","rucksack","vulgar","antithetical",
"capricious","reconnaissance","farce","lyre","castanet","heuristic","swatter",
"hamster","gestation","bidding","panorama","siesta","mirage",
"conjure","goody","devious","scheme","foil","thrush","caricature","tunic",
"vintage","forgery","rouge","mascara","fetch","discrepancy","juke"]

def ˆˆ():
    global secret
    secret = wordlist[randint(0,len(wordlist)-1)]
    print (secret)
    
def Å(newText):
    tØ.clear()
    tØ.penup()
    tØ.goto(-int(sw*0.4),int(sh*0.4))
    tØ.pendown()
    tØ.write(newText, font=("Arial",fontS,"bold"))

def ßπ(newText):
    tı.clear()
    tı.penup()
    tı.goto(-int(sw*0.4), -int(sh*0.4))
    tı.write(newText, font=("Arial",fontS,"bold"))
    
def Ω():
    t1.penup()
    t1.goto(-int(sw/4), -int(sh/4))
    t1.pendown()
    t1.forward(int(sw/2))

def ø():
    t1.penup()
    t1.goto(int(sw/4),t1.ycor())
    t1.pendown()
    t1.left(90)
    t1.fd(int(sh/2))

def µ():
    t1.penup()
    t1.pendown()
    t1.left(90)
    t1.fd(int(sh/2)-200)

def ß():
    t1.penup()
    t1.pendown()
    t1.left(90)
    t1.fd(int(sh/16))

def ç():
    t1.penup()
    t1.goto(-int(sh/16),int(sh/8))
    t1.pendown()
    t1.circle(int(sh/16))

def Ï():
    t1.penup()
    t1.goto(0,int(sh/16))
    t1.pendown()
    t1.down()
    t1.fd(int(sh/8))

def å():
    t1.penup()
    t1.goto(0,0)
    t1.pendown()
    t1.left(90)
    t1.fd(int(sh/16))

def Ô():
    t1.penup()
    t1.goto(0,0)
    t1.pendown()
    t1.right(180)
    t1.fd(int(sh/16))

def Ú():
    t1.penup()
    t1.goto(0,-int(sh/16))
    t1.pendown()
    t1.left(30)
    t1.fd(int(sh/12))

def ƒ():
    t1.penup()
    t1.goto(0,-int(sh/16))
    t1.pendown()
    t1.right(240)
    t1.fd(int(sh/12))

def π():
    alpha="abcdefghijklmnopqrstuvwxyz"
    global display
    for l in secret:
        if l.lower() in alpha:
            display += "_" + " "
        else:
            display += str(l) + " "
    print(display)

def œ(newText):
    tı.clear()
    tı.penup()
    tı.goto(-int(sw*0.40), int(sh* 0.40))
    tı.write(newText, font=("Arial", fontS, "bold"))

def Ωå():
    global display, alpha, fails
    display = ""
    for l in secret:
        if str(l) in alpha:
            if str(l).lower() in letterscorrect.lower():
                display += str(l) + " " 
            else:
                display += "_" + " "
        else:
            display += str(l) + " "

def i():
    global fails, display, gameDone
    while gameDone == False and fails > 0:
        boxtitle="Guess the whole Word!"
        guess = s.textinput(boxTitle, "Enter a guess")
        if guess == secret:
            ßπ("Yes! The secret word is " + secret)
            Å("Great job. Game is over.")
            gameDone = True
            fails == 0
            break
        else:
            ßπ("Sorry: it is not " + guess)
            time.sleep(1)
            Å(display)
            fails -= 1
            µå()
        return guess

def œΩı():
    global fails
    boxTitle="letters used:" + letterswrong
    guess = s.textinput(boxTitle, "Guess Letter. Enter ∑∑ to Guess the word")
    return guess
    if input("∑∑"):
        i()
    else:
        boxTitle = "LetterGuess"
        Ωå()
    
def µå():
    global fails, gameDone
    if fails == 5:
        ç()
    if fails == 4:
        Ï()
    if fails == 3:
        å()
    if fails == 2:
        Ô()
    if fails == 1:
        Ú()
    if fails == 0:
        ƒ()
        gameDone = True
    

def πˆ():
    global gameDone, fails, letterswrong, letterscorrect, alpha
    while gameDone == False and fails > 0:
        Guess= œΩı()
        if Guess == "∑∑":
            i()  
        elif len(Guess) >1 or Guess == "":
            ßπ("Sorry I need a letter, guess again.")
            time.sleep(1)
            ßπ(display)
        elif Guess not in alpha:
            ßπ(Guess + " is not a letter. Guess again.")
            time.sleep(1)
            ßπ(display)
        elif Guess.lower() in secret.lower():
            letterscorrect += Guess.lower()
            Ωå()
            ßπ(display)
        elif fails <= 0:
            gameDone = True
            break
        elif Guess in letterswrong:
            ßπ(Guess + " has been guessed. Guess again.")
        else:
            letterswrong += Guess.lower()
            fails -= 1
            µå()
            Å(fails)
            ßπ(display)
            time.sleep(1)
    if "_" not in display:
         ßπ("Great job! Your word is: " + secret)
         gameDone = True
    if fails <= 0:
         ßπ("Sorry. Game is over. The word is: " + secret)
    if gameDone == True:
        œ()

def œπµ():
    global secret, display, gameDone, fails, letterscorrect, letterswrong
    Å("Guess a Letter")
    ˆˆ()
    t1.clear()
    tØ.clear()
    tı.clear()
    t1. penup()
    t1. goto(0,0)
    t1.reset()
    t1.speed(0)
    t1.color("white")
    Ω()
    ø()
    µ()
    ß()
    π()
    time.sleep(1)
    fails = 6
    œΩı()
    Ωå()
    ßπ(display)
    µå()

def œ():
    global gameDone, fails, letterscorrect, letterwrong
    while gameDone == True:
        boxTitle="Want to play again?"
        guess = s.textinput(boxTitle, "Type Y or Yes to play again!")
        if guess.lower()=="y" or guess.lower() == "yes":
            œπµ()
            fails = 6
            gameDone = False
            πˆ()
        else:
            Å("Alright. See you next time!")

    
#Game
ˆˆ()
Å("Guess a Letter")
Ω()
ø()
µ()
ß()
Ï()
ç()
å()
Ô()
Ú()
ƒ()
π()
Å("Guess a Letter")
t1.reset()
t1.clear()
tØ.clear()
tı.clear()
t1. penup()
t1. goto(0,0)
t1.reset()
t1.speed(0)
t1.color("white")
Ω()
ø()
µ()
ß()
π()
πˆ()
œ()
