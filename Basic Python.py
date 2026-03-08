name = input("Hello what is your name ")
print(f"Nice to meet you,{name}!")
age = int(input("How old are you "))
bot_age = 4
age_difference = age - bot_age
print (f"You are {age_difference} years older than me. I'm {bot_age} years old!")
colour = input("What is your favorite colour? ")
if colour == "green":
    print(f"thats my favorite colour to")
else: 
    print(f"Oh, {colour} is cool colour")

colours = { #from this point onwards got claud to help me by giving me hints to write the code. I can still explain it though.
    "red": "FF0000",
    "green": "008000",
    "blue": "0000FF",
    "yellow": "FFFF00",
    "orange": "FFA500",
    "purple": "800080",
    "pink": "FFC0CB",
    "white": "FFFFFF",
    "black": "000000",
    "grey": "808080",
    "brown": "A52A2A",
    "cyan": "00FFFF"
}

if colour not in colours:
    print("No, put in a normal colour (case sensitive)")

Hex_Val = colours[colour] 
Hex1 = Hex_Val[0:2]  
Hex2 = Hex_Val[2:4]  
Hex3 = Hex_Val[4:6]  

first = int(Hex1, 16)  # base 16 hex
second = int(Hex2, 16)
third = int(Hex3, 16)

op_first = 255 - first
op_sec = 255 - second
op_third = 255 - third

real_hex1 = hex(op_first)[2:]
real_hex2 = hex(op_sec)[2:]
real_hex3 = hex(op_third)[2:]

print(f"The opposite colour of your colours hex is: {real_hex1 + real_hex2 + real_hex3} you can look up the colour on the internet.")

