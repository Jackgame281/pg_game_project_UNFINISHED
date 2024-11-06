# Totally cool Game That is PG Rated for everyone
import datetime
import time
def problem(): # Tells the person that there was a problem doing that 
    print("Oops, we're hanging here. Type something else.")
def write(a): # Does text letter by letter
    for i in a:
        print(i, end="")
        time.sleep(0.03)
    print()
    

time.sleep(0.3)
write("Welcome to this totally good game") #its not good plus this was made by a 13 year old
time.sleep(0.7)
write("You wake up and you find yourself in a trash compactor surrounded by bags of trash and nothing crazy.")
time.sleep(0.4)
answer1 = input("What do you do? (Get out or stay still)> ").lower() # what first?
if answer1 == "stay still": #die regardless
    write("You chose to stay inside the compactor for some reason. Your choice ends up with you dying by being squished to death.")
elif answer1 == "get out": #real stories start here bro
    write("You get out of the trash compactor and you stop it.")
    write("You then walk out to a hallway. Your options are:")
    print("Go north, west, east")
    direction1 = input("which way do you go?> ") #which way first go
    if direction1 == "north":
        write("You go north.")
        write("You have some options. Go west or east.")
        direction2 = input("Which way do you go?> ") #second direction
        if direction2 == "east":
            write("CONGRATS. YOU DIED. A TRUCK HIT YOU AND SENT YOU TO ANOTHER CURSED DIMENSION.") #better idea maybe
        elif direction2 == "west":
            write("wohoo. you won. you escaped a criminal building behind some alley.")
    elif direction1 == "west":
        write("You go west.")
        time.sleep(1.5)
        write(f"Sorry, due to technical limitations with rendering this room, we are unable to keep going. Thanks for trying the simulator.") #too damn lazy to keep going
    elif direction1 == "east":
        write("You go east.")
        write("You come across a man sleeping at an old computer.")
        write("You say to yourself, 'Huh, am I back in time or something?' ")
        write("No, you're not. The facility you're in is just too lazy to upgrade, you idiot.")
        while True: # Loop goes here mr. C
            answer2 = input("Do you; Stab him, Go back and leave him alone, or try to move him?> ").lower() #lower makes all input simple 
        if answer2 == "stab him":
            write("Wow, okay. You stab him and push him off the chair.")
            time.sleep(0.3)
            write("You sit in his chair and you start going through the computer.")
            computerChoice1 = input("Do you go into a security 'camera feed', or play 'epik games'?> ")
            if computerChoice1 == "camera feed": #go to camera that are in funny building lol
                write("You go to the camera feed and you find a easy way to get out. Go north, then west.")
                time.sleep(5.0)
                write(f"Sorry, we can't figure out how to make programs loop or go back, as we ended up hiring an idiot for coding.")
            elif computerChoice1 == "epik games" or "epic games": #the game is the sims and you die with it
                write("You play a game of the most boring game ever.")
                time.sleep(5.0)
                write("You lose track of time and end up playing for 50 minutes as you have a great time.")
                write(f"You realize the time and you run off the computer and hide under a table as you hear something rather big.")
                time.sleep(10.2)
                write("After waiting, you get out and the thing hears you and it kills ya...")
            else: problem()
        elif answer2 == "go back":
            write("You go back to the hallway.")
            write(f"Sorry, we can't figure out how to make programs loop or go back, as we ended up hiring an idiot for coding.")
        elif answer2 == "move him": # die
            write("You try to move him, but he wakes up and pulls a gun on you and you die.")
            
    else: 
        problem()
else: 
    problem()
