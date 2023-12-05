from random import randint
from secrets import randbits


def generate_curve(p):
    while True:
        # Step 1: Choose random values A, a, and b modulo N
        '''a = 14  TEST VALS
        x = 1512
        y = 3166'''

        a = randbits(256)
        x = randbits(256)
        y = randbits(256)

       
        P = (x,y)
        b = (y**2 - x**3 - a * x) % p
      #  print(P)

        #check if curve is valid
        if((4*pow(a,3,p) + 27 * pow(b,2,p)) % p == 0):
            continue

        return a,b,x,y
       

   
