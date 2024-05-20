import random
import string

RED = "\033[91m"
RESET = "\033[0m"

def generate_hiragana():
    start = 0x3040
    end = 0x309F
    hiragana = random.choice(range(start,end))
    return chr(hiragana)

def main():
    MIKADO = []
    while True:
        char = generate_hiragana()
        print(char, end=" ")
        MIKADO.append(char)
        
        if len(MIKADO) > 3:
            MIKADO.pop(0)
        
        if ''.join(MIKADO[-3:]) == "みかど":
            print("\b"*6 + RED + "み か ど" + RESET)
            break

if __name__ == "__main__":
    main()