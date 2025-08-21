name = input("Enter your name: ")
notes = input("Enter some notes about you: ")
with open("Information.txt","w") as i:
    i.write(notes)

with open("Information.txt","r") as i:
    result = i.read()   

print("Your name is", name , ", and your information are" , result,".")