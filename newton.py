#Newton's method 
def first_derivative(f, x, h=1e-15):
    """#calculates the value of the first derivative of the function f, at the value x"""
    x_first = (f(x+h) - f(x))/ h
    return x_first


def second_derivative(f,x, h=1e-15):
    """calculates the value of the second derivative of the function f, at the value x"""
    x_second = (f(x+h) - 2*f(x) + f(x-h)) / h**2
    # or： x_second = (first_derivative(f,x+h)- first_derivative(f,x)) / h
    return x_second


def optimize(f, x, diff = 0.001,h=0.001, max_iteration = 1000):
    """Optimaises the function f, starting from value x"""
    iteration = 1
    while iteration < max_iteration:
        x_first = first_derivative(f, x, h)
        x_second = second_derivative(f,x, h)
        
        x_new = x - x_first/x_second
    
        if abs(x_new - x) < diff:
            return(x_new)
        else: 
            iteration += 1
            x = x_new
    return x_new, "fail to converge"