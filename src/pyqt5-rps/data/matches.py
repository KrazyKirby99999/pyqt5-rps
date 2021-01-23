matches = {
    "rock":"scissors",
    "scissors":"paper",
    "paper":"rock"
}

def result(choice1, choice2):
    if matches[choice1] == choice2:
        return "p1"
    if matches[choice2] == choice1:
        return "p2"
    return "draw"