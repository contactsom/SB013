def outer():
    print("I am outer")
    def inner():
        print("I am inner")

    inner() # I am inside the outer() but outside the inner() function


outer()
#inner()