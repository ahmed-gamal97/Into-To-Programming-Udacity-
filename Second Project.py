# The Easy Level and the answers
easy_song = ["Oh, Beyonce,", "__1__", "Oh," ,"__2__", "Shakira (hey) He said I'm worth it, his one" ,"__3__", "I know things about \
that him you wouldn't want to read about He" ,"__4__", "me, his one and only, (yes) beautiful" ,"__5__", "Tell me how \
you tolerate the things you just found out about You'll never know Why are we the ones who suffer? I have to let" \
,"__6__", "He won't be the one to cry"]

easy_Hidden_Words = ['shakira' , 'beyonce' , 'desire' , 'kissed' , 'liar' , 'go']

    
# The Meduim Level and the answers
meduim_song = ["It's been a long day without you, my", "__1__", "And I'll tell you all about it when I see you again \
We've come a long way from where we", "__2__", "Oh I'll tell you all about it when I see you", "__3__", "When I see you\
again", "__4__", "who knew all the", "__5__", "we", "__6__", "Good things we've been through That I'll be standing right here"]

meduim_Hidden_Words = ['friend' , 'began' , 'again', 'damn' , 'planes' , 'flew' ]

# The Hard Level and the answers
Hard_song = ["What would I do without your smart", "__1__", "Drawing me in, and you", "__2__", "me out Got my head" ,"__3__",\
"no kidding, I can’t", "__4__", "you down What’s going on in that beautiful mind I’m on your magical mystery\
ride And I’m so", "__5__", "don’t know what hit me, but I’ll be alright My head’s under water \
But I’m", "__6__", "fine You’re crazy and I’m out of my mind"]

Hard_Hidden_Words = ['mouth', 'kicking', 'spinning', 'pin', 'dizzy',  'breathing']


def load_difficulty():
    """
    Behavior: Asks the user for a difficulty level
    Args: Takes no Input
    Returns:
        list of str: song with hidden words for spefic level
        list of str: Hidden_Words for specific level
    """
    while 1 :
        # Get difficulty level from user
        level = input("Please select a difficulty level (easy, medium, or hard): ")
        if level.lower() == "easy":
            return easy_song, easy_Hidden_Words
        if level.lower() == "medium":
            return meduim_song, meduim_Hidden_Words
        if level.lower() == "hard":
            return Hard_song, Hard_Hidden_Words
        else:
            print ("You selected an invalid difficulty level!")



def isAnswerGuessed(blank_number, song, answers):
    """
    Behavior : Asks the user for a guess. If correct, moves to the next blank and Displays the updated fill-in-the-blank.
    and If the guess is not correct prompts the user to try again
    
    Args:
        blank_number (int): the fisrt blank number.
        song (list of str): the fill-in-the-blank song.
        answers (list of str): the Hidden_Words.
.
    Returns:no value
    """
    for answer in answers:
        blank = "__" + str(blank_number) + "__"
        # Get guess for the specified blank
        guess = input("Please fill in blank #" + str(blank_number) + ": ")
        # if correct, Replace __blank_number__ with the answer
        if guess == answer:
            song[song.index(blank)] = answer
            print(" ".join(song))
            blank_number += 1

        else:
            print ("Incorrect. Please try again.\n")
            return isAnswerGuessed(blank_number, song, answers[answers.index(answer) :])


def play_game():
    """
    Behavior : Plays the game of fill-in-the-blanks.
                Asking the user if (he/she) wants to play again.
    
    Args:No Args.
    Returns:No return.
    """
    flag = 1
    while flag:
        song, answers  = load_difficulty()
        print ("\nHere is the Song with the Hiddern words for you to Fill in:\n")
        print(" ".join(song))
    

        isAnswerGuessed(1,song, answers)
                    
        print ("\nCongratulations, you have successfully filled in all of the blanks\n")
        
        # you can not play the same level two times in just one run 
        choice = int(input("Do you Want to Play Again or to Quit ?\nPress 2 if you want to Quit\nPress any number if you want to Play\n"))
        if choice == 2:
            flag = 0

    
play_game()