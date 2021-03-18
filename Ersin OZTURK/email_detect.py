"""
Developer: Ersin ÖZTÜRK
Program Name: EMAIL DETECTION
Date: 17.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program takes the input and detect the email adress first part
"""
import re

def file_operation(text_raw):
    with open("email_detect.txt", "a", encoding="utf-8") as file:
        file.write(text_raw+"\n")

def find_email():
    with open("email_detect.txt", "r", encoding="utf-8") as file:
        sentence=file.read()
        patern=r"[\w]+[\W][\w]+.com"
        text_found=re.findall(patern,sentence)
        if text_found:
            for i in text_found:
                lst=list(i)
                index=lst.index("@")
                a=i[0:index]
                file_operation(a)
            return text_found
        else:
            return print('There is no special text')

input_data = input("Please insert the input data: ")
file_operation(input_data)
find_email()

