import random, re
from collections import defaultdict
import time

# Stolen code

class LString:
    def __init__(self):
        self._total = 0
        self._successors = defaultdict(int)

    def put(self, word):
        self._successors[word] += 1
        self._total += 1

    def get_random(self):
        ran = random.randint(0, self._total - 1)
        for key, value in self._successors.items():
            if ran < value:
                return key
            else:
                ran -= value

couple_words = defaultdict(LString)

def load(phrases):
    with open(phrases, 'r') as f:
        f.readline()
        for line in f:
            listline = list(line.split(" "))
            if "" in listline:
                listline.remove("")
            if len(listline) > 3:
                add_message(line)

def add_message(message):
    message = re.sub(r'[^\w\s\']', '', message)
    words = message.split()
    for i in range(2, len(words)):
        couple_words[(words[i - 2], words[i - 1])].put(words[i])
    couple_words[(words[-2], words[-1])].put("")

def generate():
    result = []
    while len(result) < 10 or len(result) > 20:
        result = []
        s = random.choice(list(couple_words.keys()))
        result.extend(s)
        while result[-1]:
            w = couple_words[(result[-2], result[-1])].get_random()
            result.append(w)

    return " ".join(result)

while True:
    output = open("dict","w")
    load("comments")
    for i in range(10000):
        print(i)
        output.write(str(generate()+";++;++;++;"))
    output.close()
    time.sleep(7200)
