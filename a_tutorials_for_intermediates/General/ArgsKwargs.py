def test_var_args(f_arg, *argv):
    print("Fisrt Argument:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)
test_var_args("salam", "test")
test_var_args("salam", "test","dunya","necesen")


#Usage of **kwargs
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print("%s == %s" %(key, value))

greet_me(name="yasoob", dunya="agac")