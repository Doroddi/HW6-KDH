if __name__ == "__main__":
    import csv
    import matplotlib.pyplot as plt
    f = open('dice.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')

    data100=next(data)
    data1000=next(data)
    data10000=next(data)
    data100000=next(data)
        
    f.close()

    del data100[0]
    data100 = list(map(int, data100))
    del data1000[0]
    data1000 = list(map(int, data1000))
    del data10000[0]
    data10000 = list(map(int, data10000))
    del data100000[0]
    data100000 = list(map(int, data100000))

    x = [1,2,3,4,5,6]
    
    plt.subplot(221)
    plt.title('Dice simulator (number of trials : 100)')
    plt.bar(x,data100,width=1.0)
    plt.xlabel('dice number')
    plt.ylabel('number of trials')
    
    plt.subplot(222)
    plt.title('Dice simulator (number of trials : 1000)')
    plt.bar(x,data1000,width=1.0)
    plt.xlabel('dice number')
    plt.ylabel('number of trials')
    
    plt.subplot(223)
    plt.title('Dice simulator (number of trials : 10000)')
    plt.bar(x,data10000,width=1.0)
    plt.xlabel('dice number')
    plt.ylabel('number of trials')

    plt.subplot(224)
    plt.title('Dice simulator (number of trials : 100000)')
    plt.bar(x,data100000,width=1.0)
    plt.xlabel('dice number')
    plt.ylabel('number of trials')
    
    plt.show()
