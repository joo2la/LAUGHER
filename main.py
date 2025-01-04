import pyautogui as pag
import random
import time
import json
import pyperclip

def write(text):
    pyperclip.copy(text)
    pag.hotkey('ctrl', 'v')
    pag.press('enter')
    pyperclip.copy("")
def create_words(file):
    words = []
    with open(file, "r") as f:
        for line in f:
            words.append(line.replace("\n", ""))
    return words

def create_flood_NoLin(list_, cycle):
    word = ""
    for i in range(cycle):
        word += random.choice(list_)

def create_flood_Lin(words):
    for item in words:
            write(f'{message_pattern}{item}')
            time.sleep(speed)
                
def no_linear_flood():
    word_amt = int(input("Введите количество сообщений>"))
    time.sleep(sleep)
    for i in range(word_amt):
        write(f'{message_pattern}{create_flood_NoLin(words, cycle)}')
        time.sleep(speed)
def linear_flood():
    word_amt = int(input("Введите количество операций>"))
    time.sleep(sleep)
    create_flood_Lin(words)

data = {}
with open("settings.json", "r") as f:
    data = json.load(f)
    words = create_words(data["word_list"])
    sleep = data["time_sleep"]
    cycle = data["cycle"]
    speed = data["speed"]
    message_pattern = data["pattern"]
    lin_flood = data["linear_flood"]

if __name__ == "__main__":
    print("LAUGHER v2.1")
    while True:
        with open("settings.json", "r") as f:
            data = json.load(f)
            words = create_words(data["word_list"])
            sleep = data["time_sleep"]
            cycle = data["cycle"]
            speed = data["speed"]
            message_pattern = data["pattern"]
            lin_flood = data["linear_flood"]
        if lin_flood:
            linear_flood()
        else:
            no_linear_flood()
