import numpy as np

def Eulers_Method(range_start, range_end, iterations, initial_point_y, f, h):
    # Initialize time values and solution array
    t_values = np.linspace(range_start, range_end, iterations + 1)  # Generate time steps
    values = [initial_point_y]  # Store y values dynamically

    # Euler's Method using lambda in loop
    euler = lambda y, t: y + h * f(t, y)  # Lambda function for Euler update

    for i in range(iterations):
        values.append(euler(values[i], t_values[i]))  # Compute and store next y

    return values

def Runge_Kutta(range_start, range_end, iterations, initial_point_y, f, h):
    values = [initial_point_y]  # Store y values dynamically

    for i in range(iterations):
        k_1 = h * f(h * i, values[i])
        k_2 = h * f((h * i) + h/2, values[i] + k_1/2)
        k_3 = h * f((h * i) + h/2, values[i] + k_2/2)
        k_4 = h * f((h * i) + h, values[i] + k_3)
        values.append(values[i] + (1/6) * (k_1 + 2*k_2 + 2 * k_3 + k_4))

    return values
