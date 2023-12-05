from random import randint
from doubleandadd import multiply, add_points

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def elliptic_curve_factorization(N, bound,p):
    while True:
        # Step 1: Choose random values A, a, and b modulo N
        '''a = 14  TEST VALS
        x = 1512
        y = 3166'''

        a = randint(2,N-1)
        x = randint(2,N-1)
        y = randint(2,N-1)

        # Step 2: Set P = (a, b) and B ≡ b^2 − a^3 − A · a (mod N)
        P = (x,y)
        b = (y**2 - x**3 - a * x) % N

        #check if curve is valid
        if((4*pow(a,3,p) + 27 * pow(b,2,p)) % p == 0):
            continue
        
        # Step 3: Loop from j = 2 up to the specified bound
        for j in range(2, bound):
            #  Compute Q ≡ jP (mod N) and set P = Q
            P = multiply(P,j,a,N) 

            #If computation fails, we found a factor
            if P is None:
                d = gcd(j,N)
                if 1 < d < N:
                    return d,a,b,x,y #curve found
                elif d == N:
                    break  # choose a new curve and point

   

def point_order(P, a, p):
    # Initialize variables
    Q = P
    order = 1  # Starting order
    
    while True:
        # Multiply the point by its order
        Q = add_points(Q, P, a, p)  # Assuming add_points function exists
        order += 1
        
        # If the resulting point is the identity element, return the order
        if Q == (float('inf'), float('inf')):
            return order

'''
N=6887
print(elliptic_curve_factorization(N,100))
'''