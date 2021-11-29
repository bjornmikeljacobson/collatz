def collatz(n1):
    if n1 == 1:
        return
    if n1 % 2 == 0:
        n2 = int(n1/2)
        print("n = " + str(n2))
        collatz(n2)
    else:
        n2 = int((3*n1+1)/2)
        print("n = " + str(n2))
        collatz(n2)


def previous_odd(z1):   # not sure this is correct
    try:
        if z1 % 3 == 0:
            print("No previous odd numbers")
            return
    finally:
        for x in itertools.count(1,):
            if ((2**x * z1)-1) % 3 == 0:
                z2 = int(((2**x * z1)-1) / 3)
                print("z = " + str(z2))
                previous_odd(z2)