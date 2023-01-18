# adv. game


name = input("What's Your Name? ")
print("Welcom",name,"To This Adventure!")
answer = input("You are on a muddy road in your car, and you have two roads on the right, a pond and mud that no one knows how deep it is, and on the left is a rickety bridge, which one will you take?").lower()
if answer == 'left' :
    print('You lose! The bridge has broken off')
    quit()
elif answer == 'right' :
    answer = input("Great! You passed the mud pool, but the car broke down. Will you stay to ask for help, or will you go to look for the nearest station?").lower()
    if answer == 'stay' :
        print("you lose! don't be lazy bro")
        quit()
    elif answer == 'go' :
        print("Nice you are now heading to the nearst satuation,......")
        print("..")
        print("...")
        print("....")
        answer = input("oh you saw a An elderly man is being robbed by armed people, will you help him? yes or no").lower()
        if answer == "yes" :
            print("Great! you got it You helped him and he gave you the closest route to the station")
        elif answer == "no" :
            print("This is sad, are you afraid? I lost")


