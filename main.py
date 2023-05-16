from sideeye import Sideeye
from snurt import snurt
from normal import normal
from cuteSmile import cuteSmile
from smile import Smile
from sad import sad
from turtle import *

def circkle(x, y):
    color(y)
    for count in range(x):
        fd(5)
        rt(5)


if __name__ == '__main__':
    inn = textinput("", prompt="How are you: ")
    print(inn)
    if inn.lower() == "glad":
        Smile()
    if inn.lower() == "sad":
        sad()
    if inn.lower() == "sideeye":
        Sideeye()
    if inn.lower() == "snurt":
        snurt()
    if inn.lower() == "normal":
        normal()
    if inn.lower() == "cute":
        cuteSmile()

