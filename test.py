import random
def is_valid_num(s):
    if s.isdigit() and 1 <= int(s) <=10:
        return True
    else:
        return False

def main():
    number = random.randint(1,10)
    guessed_number = False
    guess = input("Seg e Zahl zwüsched 1 und 10!: ")
    while not guessed_number:
        if not is_valid_num(guess):
            guess = input("NEEII!! E Zahl vo 1 bis 10 hani gseit!")
            continue

        if guess = number:
            return("ÄÄÄÄÄÄH UUUUUUF verwütscht!!")
        else guess != number:
            return("scheisse!, Chum, mir probierets nomal")

