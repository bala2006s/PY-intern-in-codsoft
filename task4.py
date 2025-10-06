import random

def play():
    while True:
        user_c = input("Choose your weapon: rock, paper, or scissors? ").lower()
        if user_c in ["rock", "paper", "scissors"]:
            break
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
    computer_c = random.choice(["rock", "paper", "scissors"])
    print("\n")
    print(f"You chose: {user_c}")
    print(f"The computer chose: {computer_c}")
    print("\n")
    if user_c == computer_c:
        return "It's a tie!"
    elif (user_c == "rock" and computer_c == "scissors") or (user_c == "scissors" and computer_c == "paper") or (user_c == "paper" and computer_c == "rock"):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_s = 0
    computer_s = 0
    while True:
        res = play()
        print(res)
        if "You win!" in res:
            user_s += 1
        elif "You lose!" in res:
            computer_s += 1
        print(f"\n--- Current Score ---")
        print(f"You: {user_s}")
        print(f"Computer: {computer_s}")
        print("---------------------\n")
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()