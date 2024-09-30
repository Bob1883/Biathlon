import random
from typing import List

def initTarg(numTarg:int = 5) -> List[str]:
    targs = []
    for _ in range(numTarg):
        targs.append("*")
    return targs

def displayTargs(targs:List[str]) -> None:
    for i in range(len(targs)):
        print(i + 1, end=" ")
    print("")

    for targ in targs:
        print(targ, end=" ")

    print("")

def shoot(targs:List[str], pos:int, hitProb:float) -> str:
    if pos < 1 or pos > len(targs):
        return "Miss"

    if random.random() > hitProb:
        return "Miss"

    targ = targs[pos - 1]
    if targ == "*":
        targs[pos - 1] = "O"
        return "Hit"
    else:
        return "Miss"

def playRound(targs:List[str], totShots:int, initHitProb:float) -> int:
    hits = 0
    displayTargs(targs)

    for shotNum in range(1, totShots + 1):
        hitProb = initHitProb - (shotNum - 1) * 0.1

        if hitProb < 0.1: 
            hitProb = 0.1

        print("")
        pos = int(input(f"Shot nr {shotNum} at: "))
        
        result = shoot(targs, pos, hitProb)
        print(result+"\n\n")
        
        if result == "Hit":
            hits += 1
        
        displayTargs(targs)

    return hits

def play():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon                ")
    print("         a hit or miss game           ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    numPlayers = int(input("Enter number of players: "))
    numRounds = int(input("Enter number of rounds: "))
    totShots = 5
    initHitProb = 0.9 
    
    players = {}
    for i in range(numPlayers):
        name = input(f"Enter name for player {i+1}: ")
        players[name] = {"targs": initTarg(), "score": 0}

    for round in range(1, numRounds + 1):
        print(f"\n--- Round {round} ---")
        
        for player, data in players.items():
            print(f"\n{player}'s turn. You got {totShots} shots\n")
            hits = playRound(data["targs"], totShots, initHitProb)
            data["score"] += hits
            data["targs"] = initTarg() 
            print(f"\n{player} hit {hits} of {totShots} targets")

    print("\n--- Final Scores ---")
    for player, data in players.items():
        print(f"{player}: {data['score']}")

play()