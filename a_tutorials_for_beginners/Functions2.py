def countdown(i):
  print(i)
  # base case
  if i <= 0:
    return
  # recursive case
  else:
    countdown(i-1)
#countdown(5)



def age_foo(age):
  new_age = float(age) + 50
  return new_age

age = input("Enter your Age:")
print(age_foo(age))



# Example, demeli listdeki datani vururam for a, sonra for daxilinde functionu cagirirram and returnuu aliram
temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
for t in temperatures:
    print(c_to_f(t))