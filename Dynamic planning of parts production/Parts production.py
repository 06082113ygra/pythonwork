# 动态规划——零件生产
t = [(1,0.5),(1.2,1.7),(1.9,0.8)] #每种零件在两台机器加工所需的时间，其中数据替换为试卷中的数据

def produce(t):
    m1=[]
    m2=[]
    for i,(t1,t2) in enumerate(t):
        if t1 >t2:
            m2.append(i+1)
        elif t1 == t2:
            if len(m1)>len(m2):
                m2.append(i+1)
            else:
                m1.append(i+1)
        else:
            m1.append(i+1)
    return m1,m2
print(produce(t))