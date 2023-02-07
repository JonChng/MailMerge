#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open("Input/Names/invited_names.txt", "r") as file:
    data = file.readlines()
    for i in data:
        j = i.strip("\n")
        names.append(j)


for name in names:

    letters = open(f"Output/ReadyToSend/{name}.txt", "w")
    template = open("Input/Letters/starting_letter.txt", "r")
    data = template.readlines()
    data[0] = data[0].replace("[name]", name)

    for i in data:
        letters.write(i)









