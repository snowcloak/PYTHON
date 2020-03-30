import json as js
from difflib import get_close_matches

#loading data
dictionary = js.load(open("files/data.json"))

def define(w):
    #case sensitivity enforcer
    w = w.lower()
    #checks if the word exists in the dictionary(list)
    if w in dictionary:
        #return word defintion
        return dictionary[w]
    #checks for the alternative, proper noun
    elif w.title() in dictionary:
        return dictionary[w.title()]
    elif w.upper() in dictionary:
        return dictionary[w.upper()]
    elif len(get_close_matches(w, dictionary.keys(), cutoff=.8)) > 0:
        #generate the guessword
        guessword = get_close_matches(w, dictionary.keys(), cutoff=.8)[0]
        yn = input(f"did you mean {guessword}? Enter Y if yes, N if no: ")
        if yn == "Y":
            return dictionary[guessword]
        elif yn == "N":
            return "The word does not exist. Please check your spelling."
        else:
            return "We didn't understand your query"
    else:
        return "The word does not exist. Please check your spelling."

word = input("Enter a word: ")

output = define(word)
if type(output) == list:
    for item in output:
        print(item)
else: print(output)
