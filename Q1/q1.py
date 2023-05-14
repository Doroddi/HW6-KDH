if __name__ == "__main__":
    import csv
    import matplotlib.pyplot as plt
    f = open('nationwide.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    nw = []
    for row in data:
        nw.insert(0,float(row[3]))
    f.close()

    f = open('jeju.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    jj = []
    for row in data:
        jj.insert(0,float(row[3]))
    f.close()

    f = open('busan.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    bs = []
    for row in data:
        bs.append(float(row[3]))
    f.close()

    f = open('daejeon.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    dj = []
    for row in data:
        dj.append(float(row[3]))
    f.close()

    f = open('seoul.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    su = []
    for row in data:
        su.append(float(row[3]))
    f.close()

    print("각 지역별 전국 평균대비 월평균 기온 차이\n")
    print("제주:")
    for j in range(0,12):
        print("{0}월:{1:.1f} ".format(j+1,jj[j]-nw[j]), end=" ")

    sum = 0
    for j in range(0,12):
        sum += jj[j]-nw[j]
    avg = sum / 12
    print("\n월평균 기온 차이의 평균: {0:.1f}".format(avg))
    
    print("\n부산:")
    for j in range(0,12):
        print("{0}월:{1:.1f} ".format(j+1,bs[j]-nw[j]), end=" ")

    sum = 0
    for j in range(0,12):
        sum += bs[j]-nw[j]
    avg = sum / 12
    print("\n월평균 기온 차이의 평균: {0:.1f}".format(avg))
    
    print("\n대전:")
    for j in range(0,12):
        print("{0}월:{1:.1f} ".format(j+1,dj[j]-nw[j]), end=" ")

    sum = 0
    for j in range(0,12):
        sum += dj[j]-nw[j]
    avg = sum / 12
    print("\n월평균 기온 차이의 평균: {0:.1f}".format(avg))

    print("\n서울:")
    for j in range(0,12):
        print("{0}월:{1:.1f} ".format(j+1,su[j]-nw[j]), end=" ")

    sum = 0
    for j in range(0,12):
        sum += su[j]-nw[j]
    avg = sum / 12
    print("\n월평균 기온 차이의 평균: {0:.1f}".format(avg))

    x=[1,2,3,4,5,6,7,8,9,10,11,12]
    
    plt.title('2022 National monthly average temperature')
    plt.plot(x,nw, color="black", label = "nationwide")
    plt.plot(x,jj, color="red", label = "jeju")
    plt.plot(x,bs, color="blue", label = "busan")
    plt.plot(x,dj, color="orange", label = "daejeon")
    plt.plot(x,su, color="green", label = "seoul")
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Average temperature')
    plt.axis([0,13,-5, 30])
    plt.xticks(x)
    plt.show()
