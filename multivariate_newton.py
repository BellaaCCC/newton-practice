import numpy as np

def multivariate_newton(gradient, hessian, x0, tol=1e-6, max_iter=100):
    x = np.array(x0, dtype=float)

    for _ in range(max_iter):
        grad = gradient(x)
        H = hessian(x)

        x_new = x - np.linalg.solve(H, grad)

        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new

    return x