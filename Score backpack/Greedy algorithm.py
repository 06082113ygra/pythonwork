import iotool

def beibao(s,m,b):
    bb = 0  # 现在的背包容量
    beibaoA = [] #放入背包的东西


    #循环的i的范围不能超过传过来的数量，并且背包的容量也不能超过预定的数量（例如：50，则只能小于等于50）
    i = 0
    while i < len(s) and bb<=b:
        #判断是否已经放入背包了
        if len(beibaoA)  != 0:
            #背包里现在没装，并且数量也不够
            if beibaoA.__contains__(s[i]) == False  and bb<b and (bb + s[i]) <= b:
                beibaoA.append(s[i])  # 暂存
                bb = bb + s[i]
            elif beibaoA.__contains__(s[i]) == False  and bb<b and (bb + s[i]) >= b:
                num = b - bb
                bb = bb + num
                beibaoA.append(num)
        else:
            beibaoA.append(s[i])  # 暂存
            bb = bb + s[i]
        i += 1
    return beibaoA,bb


if __name__ == '__main__':
    # 价值 / 重量    价值比从高低排序，，没超过往里装，超过了就不装了。  分数背包
    s = [ 10, 20, 30]  # 重量
    m = [60, 100, 120]  # 价值
    b = 50  # 背包总容量
    k = 0
    beibao  = beibao(s,m,b)
    print("背包中存入的:", beibao[0])
    print("背包的容量:", beibao[1])

    for i in range(len(s)):
        print("从：商品",i,"取：",beibao[0][i])

    iotool.write(beibao, "output2.txt")
