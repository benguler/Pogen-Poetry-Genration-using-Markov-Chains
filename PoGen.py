import sys
import os
from markov import MarkovMatrix
from MarkovAgent import MarkovAgent
from PoemUtility import PoemUtility
from Poem import Poem

TITLE = "\n\
**********************************************************\n\
* $$$$$$$\    $$$$$$\    $$$$$$\   $$$$$$$$\  $$\   $$\\  *\n\
* $$  __$$\  $$  __$$\  $$  __$$\  $$  _____| $$$\  $$ | *\n\
* $$ |  $$ | $$ /  $$ | $$ /  \__| $$ |       $$$$\ $$ | *\n\
* $$$$$$$  | $$ |  $$ | $$ |$$$$\  $$$$$\     $$ $$\$$ | *\n\
* $$  ____/  $$ |  $$ | $$ |\_$$ | $$  __|    $$ \$$$$ | *\n\
* $$ |       $$ |  $$ | $$ |  $$ | $$ |       $$ |\$$$ | *\n\
* $$ |        $$$$$$  | \$$$$$$  | $$$$$$$$\  $$ | \$$ | *\n\
* \__|        \______/   \______/  \________| \__|  \__| *\n\
**********************************************************\n\
*          Poetry Generation using Markov Chains         *\n\
*           by: Alex Castro, Alex Li, Ben Guler          *\n\
**********************************************************\n"

def pogen(syl, time, genre, sBool):
    # Initialize Poem class and generate the poem
    category = time + '_' + genre
    corpus = PoemUtility.tokenize(category + '.csv')
    matrix = MarkovMatrix(corpus, 2)

    poeminstance = Poem(matrix, syl, category, sBool)
    print("\nPlease wait a few seconds, PoGen is thinking...")
    poem = poeminstance.generatePoem()

    print("\n***********************************************\n")
    print(poem)
    print("***********************************************\n")

def main():
    # Get user import and create poem with user specified parameters
    print(TITLE)
    print("Please tell us what kind of poem you would like to see.\n(You may type 0 at any point to exit the program)")

    run = 1
    while run != 0:
        # Number of lines
        lines = -1
        while lines < 0 or lines > 50:
            lines = input("\nHow many lines does your poem have?\n[1-50]: ")
            try:
                lines = int(lines)
            except ValueError:
                lines = -1
            if lines == 0:
                return

        # syllables or not
        sOption = 'stub'
        sBool = False
        while True:
            if sOption == 'y' or sOption == 'yes':
                sBool = True
                break
            elif sOption == 'n' or sOption == 'no':
                sBool = False
                break
            elif sOption == '0':
                return
            else:
                sOption = str(input("\nDoes your poem follow a syllable scheme?\n[(Y)es or (N)o]: "))
                sOption = sOption.lower()

        # Syllable scheme
        syl = []
        if sBool:
            while len(syl) != lines:
                try:
                    syl = [int(item) for item in input("\nWhat syllable scheme does your poem have?\n[eg. 3 5 3]:").split()]
                except ValueError:
                    syl = []
                if len(syl) > 0 and syl[0] == 0:
                    return
        else:
            syl = [20] * lines

        # Time Period
        time = 'stub'
        while True:
            if time == 'm' or time == 'modern':
                time = 'modern'
                break
            elif time == 'r' or time == 'renaissance':
                time = 'renaissance'
                break
            elif time == '0':
                return
            else:
                time = str(input("\nWhat time period is your poem?\n[(M)odern or (R)enaissance)]: "))
                time = time.lower()

        # Genre
        genre = 'stub'
        while True:
            if genre == 'l' or genre == 'love':
                genre = 'love'
                break
            elif genre == 'n' or genre == 'nature':
                genre = 'nature'
                break
            elif genre == 'm' or genre == 'mythology':
                genre = 'mythology_folklore'
                break
            elif genre == '0':
                return
            else:
                genre = str(input("\nWhat genre is your poem?\n[(L)ove or (N)ature or (M)ythology]: "))
                genre = genre.lower()

        # Poetry Generation
        pogen(syl, time, genre, sBool)

        # Generate another poem
        repeat = 'stub'
        while True:
            if repeat == 'y' or repeat == 'yes':
                run = 1
                break
            elif repeat == 'n' or repeat == 'no':
                run = 0
                break
            elif repeat == '0':
                return
            else:
                repeat = str(input("\nWould you like to generate another poem?\n[(Y)es or (N)o]: "))
                repeat = repeat.lower()


if __name__ == "__main__":
    PoemUtility.classifyPoems('all_200.csv')
    main()
    print("\nThank you for using PoGen!\n")
    print("You can check out the project at https://github.com/benguler/Pogen-Poetry-Genration-using-Markov-Chains")
