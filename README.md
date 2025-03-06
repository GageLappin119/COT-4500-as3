# COT-4500-as3

Contains implementations of numerical algorithms from Chapter 5.

## Directory Structure

- **src/main/**: Contains the main implementation code.
- **src/test/**: Contains test cases for the algorithms.

## How to Use

### Install Dependencies

1. Ensure you have Python installed (3.6 or higher).
2. Install required dependencies by running the following command inside the root folder:
      pip3 install -r requirements.txt
 
   *(Use **`pip`** instead of **`pip3`** if the command does not work.)*

### Running Tests

To execute the test cases, navigate to the `test` folder and run:

   python3 test_assignment_3.py

(Default values are provided in the test cases.)

## Implemented Algorithms

### 1. Euler's Method

- Uses **Euler’s method** to approximate the solution of a first-order ordinary differential equation (ODE) of the form:  
  dy/dt = f(t, y)
- Given an initial value y₀ at t₀, it approximates the solution at discrete time steps using the formula:  
  yₙ₊₁ = yₙ + h * f(tₙ, yₙ)
- **Test Case:** Approximates the solution of dy/dt = t - y² from t = 0 to t = 2 with an initial condition y(0) = 1 using 10 iterations.

### 2. Runge-Kutta Method (Fourth-Order)

- Uses the **fourth-order Runge-Kutta (RK4) method** to approximate the solution of an ODE.
- RK4 provides a more accurate numerical approximation compared to Euler’s method, using the following intermediate steps:

  k₁ = h * f(tₙ, yₙ)  
  k₂ = h * f(tₙ + h/2, yₙ + k₁/2)  
  k₃ = h * f(tₙ + h/2, yₙ + k₂/2)  
  k₄ = h * f(tₙ + h, yₙ + k₃)  

  yₙ₊₁ = yₙ + (1/6) * (k₁ + 2k₂ + 2k₃ + k₄)

- **Test Case:** Approximates the solution of dy/dt = t - y² from t = 0 to t = 2 with y(0) = 1 using 10 iterations.

### Notes:
- Both methods are setup with initial values.
- Ensure dependencies are installed before running the tests.

