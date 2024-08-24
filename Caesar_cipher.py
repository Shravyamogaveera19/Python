alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
   'n','o','p','q','r','s','t','u','v','w','x','y','z']

from caesar_logo import logo
print(logo)

def caesar(plain_text,shift_amount,direction):
    end_text=""
    if direction=="decode":
        shift_amount *= (-1)
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=((position + shift_amount)%26)
            end_text += alphabet[new_position]
        else:
            end_text+=char
    print(f"The {direction}d word is:{end_text}")

continue_or_not=True
while continue_or_not: 
    print("Type 'encode' to encript,type 'decode' to decript")
    direction=(input())
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    result=input("Do you want to continue?\nType 'yes' or 'no'").lower()
    if result=="no":
        continue_or_not=False
        print("Thank You")
