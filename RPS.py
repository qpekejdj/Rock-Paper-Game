import random
import time
while True:
    inp = ""
    oop = {"rock":1,"r": 1, "paper":2,"p": 2, "scissors":3,"s": 3}
    oopa = {1:'O',2:'⌷',3:'>8'}
    bot = random.randint(1,3)
    print('Scissors Paper Rock')
    while inp.lower() not in oop:
        print("What do you do")
        inp = input()

    time.sleep(0.5)
    print()
    print('Scissors')
    print()
    time.sleep(0.5)

    print('Paper')
    print()
    time.sleep(0.5)

    print('Rock!')
    print()
    time.sleep(0.3)

    print('You:', oopa[oop[inp]])
    print()
    print('Opponent:',oopa[bot])
    if oopa[oop[inp]] == oopa[bot]:
        print('Tie!')
    elif oop[inp] == 1 and bot == 2:
        print('You got Captured')
    elif oop[inp] == 2 and bot == 1:
        print('You captured them')
    elif oop[inp] == 3 and bot == 1:
        print('you got smashed')
    elif oop[inp] == 3 and bot == 2:
        print('you snip them')
    elif oop[inp] == 1 and bot == 3:
        print('you smashed them')
    elif oop[inp] == 2 and bot == 3:
        print('You got snipped')
    for i in 'abc':
        print()
