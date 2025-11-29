import random

print("Welcome to the Psych 'Sidekick Name Generator.'\n")
print("A name just like Sean would pick for Gus:'\n")

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
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    # If user quits:
    #   End program
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")

# If user plays again:
#   Repeat from step 2
