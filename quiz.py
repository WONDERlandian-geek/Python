#The Objective of this program is to quiz the user on basic high school
#trivia.
#By Wonder Pries

score = 0


print("What is the powerhouse of the cell?")
a = input("A) mitochondria B) nucleus C)ribosome")


if(a.upper()==A):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A.")

#Ask the user question two. And store the users answer.

print("How many states comprise the United States?")
b = input("A) 13 B) 45 C) 50")


if(b.upper()==C):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C.")


print("In y - mx + b, what does m stand for?")
c = input("A) slope B) output C) I don't understand math")


if(c.upper()==A):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A.")


print("In English, a person, place or thing is called:")
d = input("A) verb B) adjective C) noun")


if(d.upper()==C):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C.")


g = score/4
p = g*100


print("You got a [score]/4. Or a [p]%.")
