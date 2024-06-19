import os

messages = []

name = input("Name: ")

while True:
    
    #clear terminal output
    os.system('cls')
    
    if len(messages) > 0:
        for m in messages:
            print(m['name'], "-", m['message'])
            
            
    print("_____________________")
    
    #get the text message
    text = input("Text: ")
    if text == "end":
        break
    
    #add the message to the list
    messages.append({
        'name': name,
        'message': text
    })