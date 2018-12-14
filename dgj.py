clues = 0
bluesClues = 0

print("You arrive on the scene. It's bad. Real bad. Three victims with pies on their face, and a Splatgun left to the side by the assailant. They left footprints right outside the Speakeasy. Looks like you got a job to do.")

while True:
    inputOne=input("What would you like to investigate? > ").lower()

    if inputOne in ["splatgun", "look splatgun", "look at splatgun", "investigate splatgun" "splat", "gun"]:
        print("Whoever handled this was careless. Fingerprints are clearly visible on the grip, trigger, and barrel of the Splatgun. The assailant left smudges of chocolate on the barrel.")
        clues += 1
        print(clues)

    elif inputOne in ["pies", "victims", "look victims", "look at victims", "investigate victims"]:
        print("Clean headshots on all three of them. The first two victims here are unrecognisable, but the last one you know for sure: Two-Tap Tim. Was one of the hardest gangsters to track for the precinct, guess the assailant did you a favour. You know that one of his closest rivals, Dirty Dan, was at the Speakeasy tonight. Time to ask some questions.")
        clues += 1
        print(clues)

    elif inputOne in ["footprints", "look footprints", "look at footprints", "invesitgate footprints"]:
        print("The footprints look small and flat. The assailant was dressed sharp tonight, guess they thought looks could kill.")

    elif inputOne in ["speakeasy", "go to speakeasy", "investigate speakeasy"]:
        print("You walk up to the Speakeasy. The Bouncer's trying not to answer anything directly, after all, Fat Sam's got a standard to keep to.")
        if clues == 2:
            print("You ask him if he saw anyone with a Splatgun. He shrugs. Then you ask him if he saw Two-Tap Tim come in tonight. He shrugs again. Then you ask him if he's seen Dirty Dan lately. The Bouncer lets a drop of sweat go down his brow. He looks towards the street. That's enough of a clue.")
            bluesClues += 1
        else:
            print("You don't have enough evidence to ask a good question, come back later.")

    elif inputOne in ["street", "look street", "investigate street"]:
        if bluesClues == 1:

            print("Your sight's on finding Dirty Dan, or at least one of his cronies. You look out onto the street and see a shadowy figure. They run.")
            inputTwo=input("What will you do? > ").lower()

            if inputTwo in ["chase", "chase figure", "run", "run to figure", "pursue", "pursue figure"]:
                print("You give chase. The figure runs into a narrow path and you follow. You corner the assailant. He's in a suit and tie, but you can't quite see his face.")
                inputThree=input("Do you want to attempt an arrest? > ").lower()
                if inputThree in ["y", "yes"]:
                    print("You get your badge out, ready to read the man his rights. Bang. The assailant collapses, with splat covering the left side of his head. The trail goes cold...")
                    print("-------")
                    print("THE END")
                    print("-------")
                    break
                elif inputThree in ["n", "no"]:
                    print("The assailant looks at you confused, expecting an arrest. You just stand there. Why did you choose this option?")
                    continue
            else:
                print("Why aren't you running after them?")
                continue

    elif inputOne in ["nothing"]:
        print("Alright wisie...")
    else:
        print("That is not a valid option.")
