if __name__ == "__main__":
    import csv
    import matplotlib.pyplot as plt
    f = open('2008.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    rate=[]
    
    data2008 = next(data)
    del data2008[0]
    del data2008[0]
    del data2008[0]
    rate.append(data2008[2])
    del data2008[2]
    data2008 = list(map(int, data2008))
            
    f.close()
    
    f = open('2013.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    data2013 = next(data)
    del data2013[0]
    del data2013[0]
    del data2013[0]
    rate.append(data2013[2])
    del data2013[2]
    data2013 = list(map(int, data2013))
            
    f.close()

    f = open('2017.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    data2017 = next(data)
    del data2017[0]
    del data2017[0]
    del data2017[0]
    rate.append(data2017[2])
    del data2017[2]
    data2017 = list(map(int, data2017))
            
    f.close()

    f = open('2022.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    data2022 = next(data)
    del data2022[0]
    del data2022[0]
    del data2022[0]
    rate.append(data2022[2])
    del data2022[2]
    data2022 = list(map(int, data2022))
            
    f.close()

    rate = list(map(float, rate))
    
    x = ["male","female"]
    
    plt.subplot(231)
    plt.title("Jeju's Population(2008)")
    plt.bar(x,data2008)
    plt.xlabel('gender')
    plt.ylabel('population')
    
    plt.subplot(232)
    plt.title("Jeju's Population(2013)")
    plt.bar(x,data2013)
    plt.xlabel('gender')
    plt.ylabel('population')
    
    plt.subplot(233)
    plt.title("Jeju's Population(2013)")
    plt.bar(x,data2013)
    plt.xlabel('gender')
    plt.ylabel('population')

    plt.subplot(234)
    plt.title("Jeju's Population(2022)")
    plt.bar(x,data2022)
    plt.xlabel('gender')
    plt.ylabel('population')

    x = ['2008', '2013', '2017', '2022']
    
    plt.subplot(235)
    plt.title("Jeju's Population(rate)")
    plt.bar(x,rate)
    plt.xlabel('years')
    plt.ylabel('rate')
    
    plt.show()
