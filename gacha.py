import random

bachelor_choice = ["hiroshi","leo", "keiran", "soren", "mako"]

def randomizeBachelor():
    pick = random.choice(bachelor_choice)
    print("Picked character: " + pick)
    bachelor_choice.remove(pick)
    print("Remaining characters: " + str(bachelor_choice))

    return pick

def returnBachelorLength():
    print(len(bachelor_choice))
    
    return len(bachelor_choice)