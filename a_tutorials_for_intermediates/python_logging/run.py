from python_logging  import FirstClass, SecondClass

number = FirstClass()
number.increment_number()
number.increment_number()
print("Current number: %s" % str(number.current_number))
number.clear_number()
print("Current number: %s" % str(number.current_number))


system = SecondClass()
system.enable_system()
system.disable_system()
print("Current system configuration: %s" % str(system.enabled))
