import pyautogui as pag
import random
import time
import json
import pyperclip
def write(text):
    pyperclip.copy(text)
    pag.hotkey('ctrl', 'v')
    pag.press('enter')
def create_words(file):
	words = []
	with open(file, "r") as f:
		for line in f:
			words.append(line.replace("\n", ""))
	return words

def create_flood(list_, cycle):
	word = ""
	for i in range(cycle):
		word += random.choice(list_)
	return word
	

SETTINGS_FILE = "settings.json"
data = {}
with open("settings.json", "r") as f:
	data = json.load(f)
	words = create_words(data["word_list"])
	sleep = data["time_sleep"]
	cycle = data["cycle"]
	speed = data["speed"]
	message_pattern = data["pattern"]
	
def flood():
	word_amt = int(input("Введите количество сообщений>"))
	time.sleep(sleep)
	for i in range(word_amt):
		write(f'{message_pattern} {create_flood(words, cycle)}')
		time.sleep(speed)
if __name__ == "__main__":
	print("flooder by EvilParty")
	while True:
		flood()
