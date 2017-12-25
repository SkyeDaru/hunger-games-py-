### Interactive game


description = "You. Are. ALONE...There is one rule and one rule only to this game: stay alive. May the odds be ever in your favor."
print(description)
answer = input("Do you accept the challenge?")

if answer == "yes":
    print("Very well, then")

else:
    print("Boring")
    
######
    
print("The following weapons are available:")
weapons = [ "sledgehammer",
            "spear",
            "bow and arrow",
            "stick"
            ]

for i in weapons:
    print(i)

choice1 = input("What weapon will you choose?")
print("You have chosen:", choice1, "." "Nice choice!")

#######

print("You get one resource. Choose wisely:")
resources = [ "apple",
              "bandaid",
              "bottled water",
              "blanket"
              ]

for p in resources:
    print(p)

choice2 = input("You choose?")
print("Great!")

#######

path1 = '"through the forest"'
path2 = '"up the mountain"'
print("You have two paths:", path1, "or", path2) 
choice3 = input("Where to?")


#### forest

if choice3 == path1 or path2:
    print("You are approached by several enemies!!!")

ally = input("Do you want to create an ally?")
if ally == "yes":
    print("You are now in an alliance. Camp the night and continue through the forest in the morning.")
    print()
    
elif ally == "no":
    print('Bad choice! You must either "fight" or "run"!!!')
decision = input("What will you choose?")

if decision == "run":
    print("Wow, didn't know you could run so fast. You're safe!")
    print()

elif decision == "fight":
    print("Your poor choice of weaponry did not stand against their heavy metal, machinery. You're injured, but still alive.")
    print()





######



print("Days pass...Only 2 more people remain alive. One of them happens to be you!")
decision2 = input("Do you wish to confront the enemy? Yes or no?")

if decision2 == "yes":
    print("OUCH! Your lack of skill and coordination did not benefit you. You. Are. Dead.")

elif decision2 == "no":
    print("Congrats! Your tactic of hiding behind a bush caused the enemy to become tired, resulting in a bear mauling them during a nap! Oh, man")
    print("YOU SURVIVED AND WON THE GAME!")








          
          




    








