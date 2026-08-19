#Newton's method

    
def first_derivative(f, x, h=0.001):
    x_first = (f(x+h) - f(x))/ h
    return x_first

def second_derivative(f,x, h=0.001):
    x_second = (f(x+h) - 2*f(x) + f(x-h)) / h**2
    # or： x_second = (first_derivative(f,x+h)- first_derivative(f,x)) / h
    return x_second
    
def Newtons(f, x, diff = 0.001, max_iteration = 1000):
    iteration = 1
    while iteration < max_iteration:
        x_first = first_derivative(f, x)
        x_second = second_derivative(f,x)
        
        x_new = x - x_first/x_second
    
        if abs(x_new - x) < diff:
            return(x_new)
        else: 
            iteration += 1
            x = x_new
    return x_new, "fail to converge"