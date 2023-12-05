import hashlib


# Calculate y^2 = x^3 + ax + b (mod p)
def is_y_square(x,a,b,p):
    return (x ** 3 + a * x + b) % p

# Find the y-coordinate given the x-coordinate (using brute-force)
def find_y(x,a,b,p):
    ysquared = is_y_square(x,a,b,p)
    y = pow(ysquared, (p + 1) // 4, p)  # Calculate y^2 = x^3 + ax + b (mod p) with modulo square root
    return y if pow(y, 2, p) == ysquared else p - y  # Choose y or p - y

def message_to_point(message,a,b,p):
    hashed_message = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')

    # Generate the x-coordinate from the hashed message
    x_encoded = hashed_message % p
    y_encoded = find_y(x_encoded,a,b,p)
    return (x_encoded,y_encoded)



