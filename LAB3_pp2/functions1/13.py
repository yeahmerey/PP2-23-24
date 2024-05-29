print("Hello! What is your name?")
p=input()
print("Well,",p,", I am thinking of a number between 1 and 20.")
print("Take a guess.")
u=12
t=0
r=int(input())
for i in  range(10000):
 if r!=u:
    print("Your guess is too low.")
    print("Take a guess.")
    t+=1
    r=int(input())
 else:
    print("Good job,",p+"!","You guessed my number ",t, "guesses!")
    break