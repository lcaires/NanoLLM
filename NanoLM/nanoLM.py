# Distributed under Creative Commons License
# Luis Caires FP IST 2024-25

from random import choice, random
from time import sleep

model : dict[tuple[str,str],list[str]] = {}

# define the path where to find the traning files
PREFIX = "/Users/luis_caires/FPLEFT/Python/MarkovChainGPT/"

def process_line(w1:str,w2:str,lw:list[str])->tuple[str,str]:
    if w1=="":
        w1,w2 = lw[0],lw[1]
        lw = lw[2:]
    for word in lw:
        if (w1,w2) not in model:
            model[(w1, w2)] = [word]
        else:
            model[(w1, w2)].append(word)
        w1, w2 = w2, word
    return (w1,w2)

ANSWERLEN = 50
SORRYSTR = "Sorry, cannot elaborate on that ..."

def generate_text(prompt:list[str])->None:
    w1, w2 = prompt[0], prompt[1]
    if (w1,w2) in model:
        output = [w1, w2]
        for _ in range(ANSWERLEN):
            if (w1,w2) in model:
                word = choice(model[(w1, w2)])
                output.append(word)
                w1, w2 = w2, word
            else:
                break
    else:
        output = SORRYSTR.split()
    simulate_typing(output)

# average number of words the system type fast before stopping to "think"
CHUNKWL = 10 

def simulate_typing(output:list[str])->None:
    s = int(random()*CHUNKWL)+1
    for w in output:
        sleep(0.1*random())
        print(w,end=" ",flush=True)
        s = s-1
        if s==0:
            sleep(random())
            s = int(random()*CHUNKWL)+1
    print()

def train_model(fname:str)->None: 
    f = open(PREFIX+fname,"r")
    w1 = w2 = ""
    for line in f:
        lw = line.split()
        (w1,w2) = process_line(w1,w2,lw)
    f.close()

def train_all(fnames:list[str])->None:
    for fname in fnames:
        train_model(fname)

def main():
    train_all(["dickens1.txt","dickens2.txt"])
    while True:
        prompt = input("Prompt (two words)> ").split()
        if len(prompt)==2:
            generate_text(prompt)
        else: break

main()
                   