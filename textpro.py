def sentece_maker(phrase):
    #create interrogatives
    interrogatives = ("who", "what", "when", "where", "why", "how")
    #capitalization
    capitalized = phrase.capitalize()
    #sentence generator
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#list declaration
results = []
#looping
while True:
    user_input = input("Say Something (to end, please type in end): ")
    if user_input == "end":
        break
    else:
        results.append(sentece_maker(user_input))

#join
print(" ".join(results))