import sys
import os
from markov import MarkovMatrix
from MarkovAgent import MarkovAgent
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

def pogen(lines, genre, time, seed):
    # Initialize MarkovAgent and Poem
    # STUB

    print("\n*****************************************************************************\n")
    print("This is a " + time + " " + genre + " poem with " + str(lines) + " lines that starts with " + seed + ".\n")
    print("*****************************************************************************\n")

def main():
    # Get user import and create poem with user specified parameters
    print(TITLE)
    print("Please tell us what kind of poem you want to see.\n(You may type 0 at any point to exit)")

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

        # Genre
        genre = 'stub'
        while True:
            if genre == 'l' or genre == 'love':
                break
            elif genre == 'n' or genre == 'nature':
                break
            elif genre == 'm' or genre == 'mythology':
                break
            elif genre == '0':
                return
            else:
                genre = str(input("\nWhat genre is your poem?\n[(L)ove or (N)ature or (M)ythology]: "))
                genre = genre.lower()

        # Time Period
        time = 'stub'
        while True:
            if time == 'm' or time == 'modern':
                break
            elif time == 'r' or time == 'renaissance':
                break
            elif time == '0':
                return
            else:
                time = str(input("\nWhat time period is your poem?\n[(M)odern or (R)enaissance)]: "))
                time = time.lower()

        # Seed
        seed = str(input("\nWhat word does your poem start with?\n[A word of your choice]: "))
        if seed == '0':
            return

        # Poetry Generation
        pogen(lines, genre, time, seed)

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
    main()
    print("\nThank you for using PoGen!\n")
    print("You can check out the project at https://github.com/benguler/Pogen-Poetry-Genration-using-Markov-Chains")
