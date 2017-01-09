# Newton's method

def newtons_method(f, f_prime, x_0, e = 1e-5):
  """
  Algorythm to approximate a zero of a
  differentiable function.

  Args:
    f: a differentiable function
    f_prime: the first derivative of f
    x_0: initial value
    e: the level of tolerance in the 
      approximation of the root
  """
  i = 1
  while abs(f(x_0) - 0) > e:
    x_0 = x_0 - f(x_0)/f_prime(x_0)
    i += 1
  print("Root found at: {}".format(x_0))
  print("{} iterations to converge".format(i))
  return x_0


def gradient_descent(f_prime, theta, theta_new, alpha, e = 1e-5):
  """
  Find local optimum of a differentiable
  funtion f using gradient descent.

  Args:
    f_prime: the first derivative of f
    theta: initial value
    theta_new: initial value
    alpha: step size
    e: the level of tolerance in the 
      approximation of the root
  """
  i = 1
  while abs(theta_new - theta) > e:
    theta = theta_new
    theta_new = theta - alpha * f_prime(theta)
    i += 1
  print("Root found at: {}".format(theta_new))
  print("{} iterations to converge".format(i))
  return theta_new




def f(x):
    return 6*x**5-5*x**4-4*x**3+3*x**2
 
def df(x):
    return 30*x**4-20*x**3-12*x**2+6*x

newtons_method(f, df, 5)

gradient_descent(df, 5, 1, .001)



x0s = [0, .5, 1]
for x0 in x0s:
    newtons_method(f, df, x0)

# Root found at: 0
# 1 iterations made
# Root found at: 0.6286680781673306
# 4 iterations made
# Root found at: 1
# 1 iterations made
