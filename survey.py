import time
import json
i=1
dictionary0={}
dictionary1={}
dictionary2={}
responses=[]

def intro(answer1, answer2, answer3):
    print("Welcome to my survey!")
    print(" ")
    print("These questions are VERY serious. So PLEASE answer with the truth and nothing but the truth.")
    answer1=input("First of all, what is your name?")
    return answer1
    print("Hey ", answer1, "!")
    answer2=input("How old are you?")
    return answer2
    print("COooooooOOol")
    answer3=input("Who is your celebrity crush?")
    return answer3



def firstperson(answer1, answer2, answer3):
    userinput1=answer1
    dictionary1["name"]=userinput1
    userinput2=answer2
    dictionary1["age"]=userinput2
    userinput3=answer3
    dictionary1["celeb"]=userinput3
    responses.append(dictionary1)
    # i+1

def secondperson(answer1, answer2, answer3):
    userinput4=answer1
    dictionary2["name"]=userinput4
    userinput5=answer2
    dictionary2["age"]=userinput5
    userinput6=answer3
    dictionary2["celeb"]=userinput6
    responses.append(dictionary2)
    # i+1

def main():
    print("Welcome to my survey!")
    print(" ")
    print("These questions are VERY serious. So PLEASE answer with the truth and nothing but the truth.")
    answer1=input("First of all, what is your name?")
    print("Hey ", answer1, "!")
    answer2=input("How old are you?")
    print("COooooooOOol")
    answer3=input("Who is your celebrity crush?")
    firstperson(answer1, answer2, answer3)
    time.sleep(1.5)
    intro(answer1, answer2, answer3)
    secondperson(answer1, answer2, answer3)
    i+1

for i in range (5):
    main()
print("Thanks for completing my survey!")
app_json=responses
with open('dictionary.json', "a+")as outfile:
    json.dump(app_json, outfile)
