"""
Developer: Ersin ÖZTÜRK
Program Name: FIND 8 digid letter
Date: 17.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program takes the input and detect the digid letter
"""
import re

def file_operation(text_raw):
    with open("find_8_letter.txt", "a", encoding="utf-8") as file:
        file.write(text_raw+"\n")

def find_8():
    with open("find_8_letter.txt", "r", encoding="utf-8") as file:
        sentence=file.read()
        patern=r"\s\w{8}\s"
        text_found=re.findall(patern,sentence)
        if text_found:
            for i in text_found:
                file_operation(i)
            return text_found
        else:
            return print('There is no special text')

input_data = input("Please insert the input data: ").upper()
file_operation(input_data)
find_8()
