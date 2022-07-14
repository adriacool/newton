from sympy import *
x = Symbol('x') 

#Takes a function and list of values, approximates roots using Newton's method
def newton(f,x_o):
  df = f.diff(x)
  d_o=lambdify(x,df)

  root=0
  for x_m in x_o:
    if d_o(x_m)==0:
      df+=.1
    u=f/df
    u_o=lambdify(x,u)

    n=1
    while n<2000:
      x_n=x_m-u_o(x_m)
      if x_n==x_m:
        break   
      x_m=x_n  
      n+=1
    root+=1
    print(f"{root}) Computed x={x_n} in {n} iterations.")
    
   
newton(4*x**4-4*x**2,[21**(1/2)/7+.05, 21**(1/2)/7-.001, 21**(1/2)/7+.1])    