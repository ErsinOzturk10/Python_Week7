"""
Developer: Ersin ÖZTÜRK
Program Name: ID DETECTION
Date: 17.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program takes the input and detect the spefic pattern ID
"""
import re

def file_operation(text_raw):
    with open("detect_id.txt", "a", encoding="utf-8") as file:
        file.write(text_raw+"\n")

def find_id():
    with open("detect_id.txt", "r", encoding="utf-8") as file:
        sentence=file.read()
        patern=r"\w{2}\d{1}\w{2}\d\d\w\d"
        id_found=re.search(patern,sentence)
        if id_found:
            file_operation(id_found.group())
            return id_found.group()
        else:
            return print('There is no id')

input_data = input("Please insert the input data: ").upper()
file_operation(input_data)
find_id()