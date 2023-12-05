from random import randint
from doubleandadd import multiply
from generateCurve import elliptic_curve_factorization
from primeGenerator import generate_prime
from secrets import randbits

##START VALUES#


#p = 17389  # A prime number
p = generate_prime(128)
print("PRIME FOUND: ", p)
#get a and b on an elliptic curve
compositeN = randbits(100)
if compositeN %2 ==0:
    compositeN +=1

factor, a,b,x,y = elliptic_curve_factorization(compositeN,1000,p)
print(f"Elliptic Curve: y^2 = a^3 + {a}x + {b}")

P = (x, y)  # Example base point on the curve
print(f"Point P: {P}")
#Key Creation
n = randint(1,p-1)
Q = multiply(P,n,a,p)
print(f"\nPublic Key Q: {Q}")




##Menezes Vanstone

message1 = b"Aggie Honor Code"
m1 = int.from_bytes(message1, "big") 
message2 = b"edoC ronoH eiggA"
m2 = int.from_bytes(message2, "big") 


k = randint(1,p-1)
R = multiply(P,k,a,p)
S = multiply(Q,k,a,p)
xs, ys = S[0], S[1]
c1 = xs*m1 % p
c2 = ys*m2 % p
print(f"Cipher text (R,C1,C2): ({R},{c1},{c2})")

T = multiply(R,n,a,p)
xt, yt = T[0], T[1]
m1prime = pow(xt,-1,p) * c1 % p
m2prime = pow(yt,-1,p) * c2 % p
decrypted1 = m1prime.to_bytes((m1prime.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
decrypted2 = m2prime.to_bytes((m2prime.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

print(f"\nORIGINAL MESSAGE 1: {message1.decode('utf-8')}")
print(f"DECRYPTED MESSAGE 1: {decrypted1}")
print(f"ORIGINAL MESSAGE 2: {message2.decode('utf-8')}")
print(f"DECRYPTED MESSAGE 2: {decrypted2}")

valid = message1.decode('utf-8') == decrypted1 and message2.decode('utf-8') == decrypted2
print("\nDo the messages match?", valid)


