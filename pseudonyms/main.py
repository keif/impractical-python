"""Generate funny names by randomly combining names from 2 separate lists."""

import random

# Load a list of surnames
first = (
    "Baby Oil",
    "Bad News",
    "Big Burps",
    "Bill 'Beenie-Weenie'",
    "Bob 'Stinkbug'",
    "Bowel Noises",
    "Boxelder",
    "Bud 'Lite'",
    "Butterbean",
    "Buttermilk",
    "Buttocks",
    "Chad",
    "Chesterfield",
    "Chewy",
    "Chigger",
    "Cinnabuns",
    "Cleet",
    "Cornbread",
    "Crab Meat",
    "Crapps",
    "Dark Skies",
    "Dennis Clawhammer",
    "Dicman",
    "Elphonso",
    "Fancypants",
    "Figgs",
    "Foncy",
    "Gootsy",
    "Greasy Jim",
    "Huckleberry",
    "Huggy",
    "Ignatious",
    "Jimbo",
    "Joe 'Pottin Soil'",
    "Johnny",
    "Lemongrass",
    "Lil Debil",
    "Longbranch",
    '"Lunch Money"',
    "Mergatroid",
    '"Mr Peabody"',
    "Oil-Can",
    "Oinks",
    "Old Scratch",
    "Ovaltine",
    "Pennywhistle",
    "Pitchfork Ben",
    "Potato Bug",
    "Pushmeet",
    "Rock Candy",
    "Schlomo",
    "Scratchensniff",
    "Scut",
    "Sid 'The Squirts'",
    "Skidmark",
    "Slaps",
    "Snakes",
    "Snoobs",
    "Snorki",
    "Soupcan Sam",
    "Spitzitout",
    "Squids",
    "Stinky",
    "Storyboard",
    "Sweet Tea",
    "TeeTee",
    "Wheezy Joe",
    "Winston 'Jazz Hands'",
    "Worms",
)

nicknames = (
    "Bumblefluff",
    "Whiskerbean",
    "Picklewink",
    "Tootles",
    "Fizzlehop",
    "Wobblejog",
    "Snickerdoodle",
    "Puddingcup",
    "Muffinwhistle",
    "Gigglepants",
    "Bippy-Bop",
    "Skittlewig",
    "Fluffernoodle",
    "Sparky-Spork",
    "Wigglenut",
    "Bumblewhisk",
    "Troublemaker",
    "Chaos Unit",
    "Mayhem Deluxe",
    "Dumpster Phoenix",
    "Trouble Sandwich",
    "Gremlin Mode",
    "Maximum Nonsense",
    "Agent of Mild Inconvenience",
    "Wreaks Havoc Professionally",
    "Certified Menace",
    "Chaos Sprinkle",
    "Ankle-Biter Supreme",
    "Grease-Fire Dreams",
    "Accidental Threat",
    "Biscuits-N-Gravy",
    "Tater Tot",
    "Cornbread",
    "Butterbean",
    "Porkchop",
    "Gravyboat",
    "Snack Attack",
    "Noodle Boy",
    "Noodle Girl",
    "Peanut Brittle",
    "Cinnamon Toast",
    "BBQ Deluxe",
    "Hotdish",
    "Sriracha Whisper",
    "Thunderpunch",
    "Apocalypse Kitten",
    "Storm Biscuit",
    "Doom Whisper",
    "Legendary Side-Quest",
    "Grand Chaos Wizard",
    "The Unprepared",
    "Duke of Shenanigans",
    "Captain Off-Brand",
    "Battle-Ready™",
    "Lord of Leftovers",
    "Spicy Gremlin",
    "Vibe Goblin",
    "Certified Goofball",
    "Beef Supreme",
    "Loot Goblin",
    "Waffle Bandit",
    "Memelord",
    "Bargain Bin Dracula",
    "Oopsie™",
    "The Problem",
)

last = (
    "Appleyard",
    "Bigmeat",
    "Bloominshine",
    "Boogerbottom",
    "Breedslovetrout",
    "Butterbaugh",
    "Clovenhoof",
    "Clutterbuck",
    "Cocktoasten",
    "Endicott",
    "Fewhairs",
    "Gooberdapple",
    "Goodensmith",
    "Goodpasture",
    "Guster",
    "Henderson",
    "Hooperbag",
    "Hoosenater",
    "Hootkins",
    "Jefferson",
    "Jenkins",
    "Jingley-Schmidt",
    "Johnson",
    "Kingfish",
    "Listenbee",
    "M'Bembo",
    "McFadden",
    "Moonshine",
    "Nettles",
    "Noseworthy",
    "Olivetti",
    "Outerbridge",
    "Overpeck",
    "Overturf",
    "Oxhandler",
    "Pealike",
    "Pennywhistle",
    "Peterson",
    "Pieplow",
    "Pinkerton",
    "Porkins",
    "Putney",
    "Quakenbush",
    "Rainwater",
    "Rosenthal",
    "Rubbins",
    "Sackrider",
    "Snuggleshine",
    "Splern",
    "Stevens",
    "Stroganoff",
    "Sugar-Gold",
    "Swackhamer",
    "Tippins",
    "Turnipseed",
    "Vinaigrette",
    "Walkingstick",
    "Wallbanger",
    "Weewax",
    "Weiners",
    "Whipkey",
    "Wigglesworth",
    "Wimplesnatch",
    "Winterkorn",
    "Woolysocks",
)


def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psych 'Sidekick Name Generator.'\n")
    print("A name just like Sean would pick for Gus:'\n")

    while True:
        # Choose a first name at random
        # Assign the first name to a variable
        first_name = random.choice(first)

        # Choose a surname at random
        # Assign the surname to a variable
        last_name = random.choice(last)

        # Print the names to the screen in order and in red font
        print("\n\n")
        print(f"\n{first_name} {last_name}\n")

        # Ask the user to quit or play again
        # If user quits:
        #   End program
        # If user plays again:
        #   Repeat from step 2
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


def build_name(first_name: str, last_name: str) -> str:
    """Build a name from first and last, with a random check to add a nickname."""
    include_nickname = random.random() < (1 / 3)

    if include_nickname:
        middle = random.choice(nicknames)
        return f"{first_name} {middle} {last_name}"

    return f"{first_name} {last_name}"


if __name__ == "__main__":
    main()
