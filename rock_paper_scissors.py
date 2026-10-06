import random


def play():
    user = input("Enter your choice (rock (r), paper (p), scissors (s)): ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return "You win!"
    return "You lose!"

if __name__ == "__main__":
    print(play())