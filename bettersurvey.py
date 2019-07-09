import json
responses=[]
num=3
list_key=["name", "age", "celeb"]
list_quest=["First of all, what is your name?", "How old are you?", "Who is your celebrity crush?"]

def intro():
    print(" ")
    print("Hey! Welcome to my survey!")
    print(" ")

for each in range(num):
    dict={}
    intro()
    for i in range(len(list_key)):
        answer=input(list_quest[i])
        dict[list_key[i]]=answer
    responses.append(dict)
hey=responses
with open('diction.json', "a+")as outfile:
    json.dump(hey, outfile)
