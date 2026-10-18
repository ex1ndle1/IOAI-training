from numpy import average


x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y = [92, 75, 88, 60, 55, 42, 48, 30, 15, 22]

def corr(x :list, y :list) -> None: 
    n = len(x) +1
    x_ = float(average(x))
    y_ = float(average(y))
    k = 0
    m =0 
    z =0
    i=0
    for _ in range(1, n):
        m+= (x[i] - x_) * (y[i] - y_)
        i +=1
    i =0
    for _ in range(1, n):
        k+= (x[i] - x_)**2
        i+=1
    i =0 
    for _ in range(1, n):
        z+= (y[i] - y_)**2
        i+=1
    res = m/((k*z)**(0.5))

    return res
    


print(corr(x,y))
