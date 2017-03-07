
from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()

def find_solution(leftSile,righSlide, variable):
  if righSlide != "0":
    expr = Poly(simplify(Poly(leftSile) - Poly(righSlide)))
  else: 
    expr = Poly(simplify(Poly(leftSile)))
  print ("Simplify your expresstion: ", expr)
  
  degreeOfExpr = degree(expr)
  if degreeOfExpr == 1: 
    print ("This is a linear equation with 2 coefficients")
    a = expr.coeffs()[0]
    if len(expr.coeffs()) == 2:
      b = expr.coeffs()[1]
    else:
      b = 0
    print ("a = ", a)
    print ("b = ", b)
    if a == 0 :
      if b == 0 :
        print ("a = 0 and b = 0, so the equation has unlimited solution")
      if b != 0 :
        print ("a = 0 and b <> 0, so the equation has no solution")
    else:
      print ("The solution of equaiton is "+variable+" = ")
      pprint(-b/a, use_unicode=False)
  elif degreeOfExpr == 2:
    print ("This is a Quadratic Equation with three coefficients")
    a, b, c = expr.coeffs()[0], expr.coeffs()[1], expr.coeffs()[2]
    print ("a = ", a)
    print ("b = ", b)
    print ("c = ", c)
    delta  = b**2 - 4 * a * c
    print ("Caculated Delta = b^2 - 4ac =  "+str(b)+"^2 - 4 * "+str(a)+" * "+str(c)+" = "+str(delta))
    if delta > 0:
      print ("Delta > 0: The equation has two different solutions")
      print (str(variable) + "_1 = (-b + sqrt(detal))/2a)")
      print (str(variable) + "_2 = (-b - sqrt(detal))/2a)")
      print (solve(expr, variable))
    elif delta == 0 :
      print ("Delta = 0: The equation has 1  solution")
      print (str(variable) + " = (-b))/2a)")
      print (solve(expr, variable))
    else:
      print ("Detal < 0 : no solution")
  else:
    print ("Out of program!!!!")
      

left = input("Input the left side of equation (ex: 7*x**2 + 3*x + 5):  ")
right = input("Input the right side of equation (ex: 7*x**2 + 3*x + 5):  ")
var = input("Input the variable of equation:")
find_solution(left, right, var)
