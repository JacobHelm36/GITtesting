import random
import re
import string

class Dice:
    def __init__(self, size, numb):
        self.size_of_dice = size
        self.number_dice = numb

    def roll(self):
        results = []
        for i in range(self.number_dice):
            results.append(random.randint(1, self.size_of_dice))
        print(results)
        return results
    def get_all(self):
        results = []
        for i in range(self.number_dice):
            results.append(random.randint(1, self.size_of_dice))
        print(sum(results))
        return sum(results)


# magic 8ball
answerNumber = random.randint(1,8)
newnumber = random.randint(1,8)
def getAnswer(any):
    if any == 1:
        return 'It is certain'
    elif any == 2:
        return 'It is decidedly so'
    elif any == 3:
        return 'Yes'
    elif any == 4:
        return 'Reply hazy try again'
    elif any == 5:
        return 'Ask again later'
    elif any == 6:
        return 'Concentrate and ask again'
    elif any == 7:
        return 'My reply is no'
    elif any == 8:
        return 'Outlook not so good'
    elif any == 9:
        return 'Very doubtful'


def rannumber():
    secretnumber = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20')
    for guesses in range(1, 7):
        print('take a guess: ')
        guess = int(input())
        if guess > secretnumber:
            print('too high')
        elif guess < secretnumber:
            print('too low')
        else:
            break
    if guess == secretnumber:
        print('good job you guessed my number in ' + str(guesses) + ' guesses')
        return 'correct guess'
    #can you return both guess and secret number?
    else:
        print('nope the number i have is', str(secretnumber))
        return 'lost'


list = ['Rock', 'Paper', 'Scissor']
def ROCKS():
    Player_win = 0
    Computer_win = 0
    while True:
        #how to set game to end after two wins?
        move = input("choose Rock, Paper, Scissor > ")
        computer = list[random.randint(0, 2)]
        if move == computer:
            print('TIE!!!')
        elif Player_win == 1:
            print("great work you win")
            return 'winner'
            break
        elif Computer_win == 1:
            print("Try again, computer wins")
            return 'loser'
            break
        elif move == 'Rock':
            if computer == 'Scissor':
                print(f'player wins {move} beats {computer}')
                Player_win += 1
            else:
                print(f'computer wins {computer} beats {move}')
                Computer_win += 1
        elif move == 'Paper':
            if computer == 'Rock':
                print(f'player wins {move} beats {computer}')
                Player_win += 1
            else:
                print(f'computer wins {computer} beats {move}')
                Computer_win += 1
        elif move == 'Scissor':
            if computer == 'Paper':
                print(f'player wins {move} beats {computer}')
                Player_win += 1
            else:
                print(f'computer wins {computer} beats {move}')
                Computer_win += 1
        else:
            print('thats not a valid move')


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)


def work():
    command = input("what's your name > ")
    print(f"hello traveller, {command}")


journey = ["You have a journey to attend to",
           "First go to the (mountains)",
           "Then go to the (cave)",
           "Then come back (home)",
           "Don't be afraid to ask for (help)"]


turn = True
def first_program():
    OnlyOneChance = 0
    mountaintoken = 0
    cave_token = 0
    work()
    for x in journey:
        print(x)
    while True:
        print('where next?')
        command2 = input('> ').lower()
        if command2 == 'help':
            print("""
   First go to the 'mountains'"
   "Then go to the 'caves'"
   "Then return 'home'""")
        elif mountaintoken == 1:
            print("you've already been to the mountains go elsewhere")
        elif command2 == 'mountains':
            mountaintoken = 1
            print('you have arrived in the mountains')
            print("You must roll some dice to proceed and be higher than the average sum.")
            pf = input("How many dice do you want? > ")
            dice = Dice(6, int(pf))
            yup = True
            while yup:
                print("'roll' the dice")
                command3 = input().lower()
                if command3 == 'roll':
                    DieAverage = int(3 * pf)
                    PlayersSum = int((dice.get_all()))
                    if PlayersSum >= DieAverage:
                        #Find out how to compare "PlayersSum" to "DieAverage"
                        print('move ahead')
                        yup = False
                    elif OnlyOneChance == 0:
                        #need this to run only once
                        OnlyOneChance = 1
                        if PlayersSum < DieAverage:
                            rannumber()
                            print('Now roll the dice again')
                        else:
                            print("you must not be good with numbers")
                    else:
                        print("Don't gamble with dice ever")
        elif cave_token == 1:
            print("you've already gone to the cave, you can only go once")
        elif command2 == 'cave':
            cave_token = 1
            i = getAnswer(newnumber)
            print("Here's a magic 8ball just to see if you should enter the cave")
            print(i, " ,doesn't matter, still enter no matter the answer")
            print('type play to play Rock, Paper, Scissor and get out of here')
            while True:
                print("you must win in Rock, Paper, Scissors to move on")
                command5 = input('> ')
                if ROCKS() == 'winner':
                    print("well done")
                    break
                elif ROCKS() == 'loser':
                    print("you are not good at this")
                elif command5 == 'play':
                    ROCKS()
                else:
                    print('play the game peasant')
        elif command2 == 'home':
            print('Take this box back home with you as a reward')
            boxsymbol = input("what symbol would you like it to be lined with? > ")
            boxPrint(boxsymbol, 5, 5)
            print('you made it home safely, excellent work')
            break
        else:
            print("don't understand")