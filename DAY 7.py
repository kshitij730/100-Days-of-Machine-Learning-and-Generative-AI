# Calculus for ML: Derivatives and IntegralsCode: Use SymPy to compute derivatives and integrals for given functions.
import sympy as sp

# Define the variable and the function
x = sp.Symbol('x')
# Example function
f = x**3 + 2*x**2 + 3*x + 5

# Compute the derivative of the function
derivative_f = sp.diff(f, x)
print(f"Function: {f}")
print(f"Derivative: {derivative_f}")

# Compute the integral of the function
integral_f = sp.integrate(f, x)
print(f"Integral: {integral_f}")

# Evaluate the derivative at a specific point (e.g., x=2)
x_val = 2
derivative_value = derivative_f.evalf(subs={x: x_val})
print(f"Derivative at x={x_val}: {derivative_value}")

# Evaluate the definite integral over a specific range (e.g., from 0 to 3)
a, b = 0, 3
definite_integral = sp.integrate(f, (x, a, b))
print(f"Definite integral from {a} to {b}: {definite_integral}")
