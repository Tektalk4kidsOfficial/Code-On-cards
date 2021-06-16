import random
import sys



responses = ["Move forward 2 ", "Move Forward 1", "Move back 1", "Move backward 2", "U-turn", "Turn Right", "Turn Left", "Down and right", "Any direction","Down and left"]
answer = random.choice(responses)
print(answer)
answer = random.choice(responses)
print(answer)
answer = random.choice(responses)
print(answer)

while True:
    question = input("Do You want to generate a random 3 again?")
    if question == "yes":
        responses = ["Move forward 2 ", "Move Forward 1", "Move back 1", "Move backward 2", "U-turn", "Turn Right",
                     "Turn Left", "Down and right", "Any direction", "Down and left"]
        answer = random.choice(responses)
        print(answer)
        answer = random.choice(responses)
        print(answer)
        answer = random.choice(responses)
        print(answer)
    else:
        print("Thanks For Using Me")
        sys.exit()