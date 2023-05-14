import csv
import random
 
def dice(dicesim):
    w = open("dice.csv", 'at', newline='', encoding='ANSI')
    wr = csv.writer(w)
 
    for row in dicesim:
        wr.writerow(row)
 
    w.close()
 
 
if __name__ == "__main__":
    data100 = ["100회",0,0,0,0,0,0]
    for i in range(0,100):
        num = random.randrange(1,7)
        data100[num] += 1

    data1000 = ["1000회",0,0,0,0,0,0]
    for i in range(0,1000):
        num = random.randrange(1,7)
        data1000[num] += 1

    data10000 = ["10000회",0,0,0,0,0,0]
    for i in range(0,10000):
        num = random.randrange(1,7)
        data10000[num] += 1

    data100000 = ["100000회",0,0,0,0,0,0]
    for i in range(0,100000):
        num = random.randrange(1,7)
        data100000[num] += 1

    dicesim = [
        data100,
        data1000,
        data10000,
        data100000]
    
    dice(dicesim)
