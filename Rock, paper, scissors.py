import random

choiceList = ["rock", "paper", "scissors"]

playerScore = 0
cpuScore = 0

play = True

while play:

    playerChoice = str(input("Rock, paper, or scissors: ")).lower()
    cpu = random.choice(choiceList)

    score = "You have ", playerScore, "points and the cpu has ", cpuScore, "points."

    if playerChoice == "rock" and cpu == "rock":
        print("Its a Tie")
        print("cpu chose", cpu)

    elif playerChoice == "rock" and cpu == "scissors":
        print("You Win")
        print("cpu chose", cpu)
        playerScore += 1

    elif playerChoice == "rock" and cpu == "paper":
        print("You Lose")
        print("cpu chose", cpu)
        cpuScore += 1

    elif playerChoice == "scissors" and cpu == "scissors":
        print("Its a Tie")
        print("cpu chose", cpu)

    elif playerChoice == "scissors" and cpu == "paper":
        print("You Win")
        print("cpu chose", cpu)
        playerScore += 1

    elif playerChoice == "scissors" and cpu == "rock":
        print("You Lose")
        print("cpu chose", cpu)
        cpuScore += 1

    elif playerChoice == "paper" and cpu == 'scissors':
        print("You Lose")
        print("cpu chose", cpu)
        cpuScore += 1

    elif playerChoice == "paper" and cpu == "rock":
        print("You Win")
        print("cpu chose", cpu)
        playerScore += 1

    elif playerChoice == "paper" and cpu == "paper":
        print("Its a Tie")
        print("cpu chose", cpu)

    elif playerChoice == "score":
        print(score)