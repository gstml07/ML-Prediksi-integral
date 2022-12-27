def Trapezoid(a,b,f):
    n = 100
    def trapezoid(f,a,b,n=100):
        h=(b-a)/n
        sum = 0.0
        for i in range (1,n):
            x = a+i*h
            sum = sum +f(x)
        integral = (h/2)*(f(a)+2*sum+f(b))
        return integral
    integral = trapezoid(f,a,b,n)
    print(a,",",b,",",round(integral,2))


for i in range(0,5):
    Trapezoid(i,i+1,lambda x: x**2)

for i in range(0,5):
    Trapezoid(i-1,i+1,lambda x: x**2)

for i in range(0,5):
    Trapezoid(i,i+np.pi,lambda x: np.sin(x))

for i in range(0,5):
    Trapezoid(i,i+1,lambda x: np.exp(x))

for i in range(0,5):
    Trapezoid(i,i+2,lambda x: x**2*3)

for i in range(0,5):
    Trapezoid(i-1,i+1,lambda x: x**4)

for i in range(0,5):
    Trapezoid(i,i+np.pi,lambda x: np.cos(x))

for i in range(5,10):
    Trapezoid(i+1,i+2,lambda x: np.ln(x))

for i in range(0,5):
    Trapezoid(i,i+1,lambda x: np.sqrt(x))

for i in range(0,5):
    Trapezoid(i,i+1,lambda x: (x**3)+(2*x**2)+(3*x)+4)
