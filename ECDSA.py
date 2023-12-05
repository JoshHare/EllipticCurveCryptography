from random import randint
from doubleandadd import multiply,add_points
from generateCurve import elliptic_curve_factorization, point_order
from primeGenerator import generate_prime
from secrets import randbits

##START VALUES#


#p = 17389  # A prime number
p = generate_prime(128)
#get a and b on an elliptic curve
compositeN = randbits(100)
if compositeN %2 ==0:
    compositeN +=1

factor, a,b,x,y = elliptic_curve_factorization(compositeN,1000,p)

G = (x, y)  # Example base point on the curve
q = point_order(G,a,p)


exit()


###CREATE KEY###
#Choose secret signing key 1 <  s < q-1
s = randint(2,q-1)
#Compute V = sG
V = multiply(G,s,a,p)
#Publish V

##SIGN###
#Choose doc d mod q
#message = b"Aggie Honor Code"
#d = int.from_bytes(message, "big") % q
d = 644
#Choose random element e mod q
e = 847
#Compute eG
eG = multiply(G,e,a,p)
#s1 = x(eG)
s1 = eG[0] % q
#s2 = (d+s*s1)*e^-1 mod q
eInverse = pow(e,-1,q)
s2 = (d + s * s1) * eInverse % q
#Publish s1,s2

###VERIFY###
#Compute v1 = d * s2 inverse modq
s2Inverse = pow(s2,-1,q)
v1 = d * s2Inverse % q
#Compute v2 = s1 * s2 inverse modq
v2 = s1 * s2Inverse % q
#Compute verifier = v1 * G + v2*V
v1G = multiply(G,v1,a,p)
v2V = multiply(V,v2,a,p)
xVerifier = add_points(v1G,v2V,a,p)[0]
#Check that x(verifier) mod q == s1
verified = xVerifier % q == s1
print("VERIFIED: ",verified)








