def flippblipp(n:int): 
    if n % 3 == 0 and n % 5 == 0:
        return "flipp blipp"
    elif n % 3 == 0: 
        return "flipp"
    elif n % 5 == 0: 
        return "blipp"
    else:
        return str(n)
    
n = 1 

print("       ", 1)

while True: 
    n += 1 

    answer = flippblipp(n)
    playerAnswer = input(f" Nästa: ")

    if answer != playerAnswer: 
        print(f" Fel - {answer}")
        print("\n Game over")
        break