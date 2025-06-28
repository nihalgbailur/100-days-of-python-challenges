# scope ;-> Python
# variable scope
#  LEGB->(Local, Enclosing, Global, Built-in) 



x = 'global x'         # ↪ this is defined in the GLOBAL scope

def test():
    y = 'local y'      # ↪ this is defined in the LOCAL scope of test()
    # print(y)         # ↪ if you uncommented this, it would print "local y"
    print(x)           # ↪ x isn’t found locally, so Python falls back to the GLOBAL x

test()                  # ↪ calls test(), so prints "global x"
# print(y)                # ↪ y was only defined inside test(), so here it isn’t defined at all


"""What happens when you run it:

test() executes, assigns y = 'local y' (in the function’s local frame), 
then print(x) looks for x locally, 
doesn’t find it, so walks up to the global frame and prints

global x

After test() returns, the next line print(y)
runs in the global frame—but y is not a global variable, 
it only ever existed locally inside test(), so you get:


NameError: name 'y' is not defined

"""