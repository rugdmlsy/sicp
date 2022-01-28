def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return (a % 2 == 1) and (b %2 ==1) # You can replace this line!


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    a=n
    while n!=1:
       a=a*(n-1) 
       n-=1
    return a


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    if (a<=0) or (b<=0) or (c<=0):
        return False
    if (a+b>c) and (a+c>b) and (b+c>a):
        return True
    else:
        return False


def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    """
    a=10
    b=1
    while n>a:
        b+=1
        a*=10
    d=0
    while n>0:
        c=n//(10**b)
        if c==6:
            d+=1
        n=n-c*10**b
        b-=1
    return d
    
 

def max_digit(n):
    """Return the max digit of x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    a=10
    b=1
    while n>a:
        b+=1
        a*=10
    d=0
    while n>0:
        c=n//(10**b)
        if c>=d:
            d=c
        n=n-c*10**b
        b-=1
    return d
