start = '''
You decide to go on a hike one day alone in the woods.
As night begins to fall, you start to walk back to your car.
However, you quickly become lost as there are no signs to guide you back.
You realize that you've been walking in circles, and when you try to call for help, your phone has no signal.
You start to hear a noise in the distance.
It sounds like wind rustling through the trees, but it seems neverending.
It becomes louder and louder and then
BOOooOOooOoOoOoOoOOoO
There's Basper, the super duper evil troublesome ghost!
Millions of things are going through your head, but you must make a decision.
Is this the time to fight for your life, or run away to safety?
'''

print(start)

print("Type 'fight' to go challenge Basper or 'run' to flee to safety.")
user_input = input()
if user_input == "fight":
    print("Ah, bold choice my friend. May the odds be ever in your favor.")
    print("You think you are strong enough to defend yourself, but that is not the case. You need a weapon if you stand any chance of beating him.")
    print("Type 'bow' to choose a bow with only one arrow. Type 'sword' to choose a rusty sword or type 'nerf' to choose a Nerf gun with one bullet. Choose wisely, because only one weapon can bring you victory over Basper.")
weapon = input()
if weapon == "bow":
    print("You carefully aim the bow at Basper and let the arrow fly. Unfortunately, the arrow goes straight through him! Without any weapon, surely you will die now.")
    print("YOU LOSE. TRY AGAIN")
elif weapon == "sword":
    print("You run straight towards Basper, and stab him with your sword. It works, so you continue until he is ripped to shreds.")
    print("Good job! You have successfully killed Basper, and coincedentally found a path that leads straight to your car.")
elif weapon == "nerf":
    print("You aim the nerf gun right at Basper's head and shoot the one bullet. Unfortunately, Basper absorbs the bullet and only seems to get angrier. You now have an angry ghost and no weapon.")
    print("YOU LOSE. You are now as dead as Basper himself. Try again loser.")

elif user_input == "run":
    print("You choose to flee to safety. Ha, coward. Basper senses your fear, and comes chasing after you. It's dark now, and as you stumble through the forest, you trip over a log. You scrape your knee, but Basper is coming closer.")
    print("You can type 'whine' to call for help, or type 'life' to keep running for your life.")
choice2 = input()
if choice2 == "whine":
    print("Basper knew you would be dead meat, so he invited his friends to enjoy your flesh for a lil hangout. Have fun being eaten alive.")
    print("YOU LOSE. Sucks for you.")
elif choice2 == "life":
    print("Must take a lot of courage to get up and keep running. You see an opening between the trees, and spot your car. You make it out just before Basper catches up to you. Good job, soldier.")
