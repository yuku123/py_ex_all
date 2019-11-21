
def transform(a,b):
    theta = a+b
    if theta > 3.14:
        return theta - 2*3.14

def pic(t,x,phix):
    x0 = 0.05 * t
    x1 = 0.1 * t
    theta = transform(x0,x1)
    phix[0]=1
    phix[1]=1
    phix[2]=1
    phix[3]=1
    phix[4]=2

a=[0,1,2,3,4]
pic(1,2,a)
print(a)

matrix=[1 for i in range(4)]

print(matrix)