import random
import string

RED = "\033[91m"
RESET = "\033[0m"

def generate_random_uppercase():
    return random.choice(string.ascii_uppercase)

def main():
    MIKADO = []
    while True:
        char = generate_random_uppercase()
        print(char, end=" ")
        MIKADO.append(char)
        
        if len(MIKADO) > 6:
            MIKADO.pop(0)
        
        if ''.join(MIKADO[-6:]) == "MIKADO":
            print("\b"*12 + RED + "M I K A D O" + RESET)
            break

if __name__ == "__main__":
    main()