import random
import string

RED = "\033[91m"
RESET = "\033[0m"

def generate_random_uppercase():
    return random.choice(string.ascii_uppercase)

def main():
    LOVE = []
    while True:
        char = generate_random_uppercase()
        print(char, end=" ")
        LOVE.append(char)
        
        if len(LOVE) > 4:
            LOVE.pop(0)
        
        if ''.join(LOVE[-4:]) == "LOVE":
            print("\b"*8 + RED + "L O V E" + RESET)
            break

if __name__ == "__main__":
    main()