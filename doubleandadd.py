def multiply(P, n, a, p):
    # Double and add algorithm for scalar multiplication on an elliptic curve
    
    Q = P
    R = (float('inf'), float('inf'))  # Point at infinity
    
    while n > 0:
        if n % 2 == 1:
            R = add_points(R, Q, a, p)
            if R == None:
                return None
        if Q==None:
            return None
        Q = double_point(Q, a, p)
        if Q == None or R == None:
            return None
        n //= 2
    
    return R

def double_point(point, a, p):
    # Double the point on the elliptic curve
    
    if point[1] == float('inf'):
        # Point at infinity, return infinity
        return point
    
    try:
        inv = pow(2 * point[1], -1, p)
    except ValueError:
        return None
    
    # Calculate the slope of the tangent line
    slope = ((3 * point[0] ** 2) + a) * inv % p
    
    
    
    # Calculate the x-coordinate of the result
    x = (slope ** 2 - 2 * point[0]) % p
    
    # Calculate the y-coordinate of the result
    y = (slope * (point[0] - x) - point[1]) % p
    
    return (x, y)


def add_points(point1, point2, a, p):
    # Add two points on the elliptic curve
    
    # If one point is at infinity, return the other point
    if point1[1] == float('inf'):
        return point2
    elif point2[1] == float('inf'):
        return point1
    
    # If the points are the same, call double_point function
    if point1 == point2:
        return double_point(point1, a, p)
    
    # Calculate the slope of the line
    num = (point2[1] - point1[1]) % p
    den = (point2[0] - point1[0]) % p
    
    try:
        inv = pow(den, -1, p)
    except ValueError:
        return None
    
    slope = (num * inv) % p
    
    # Calculate the x-coordinate of the result
    x = (slope ** 2 - point1[0] - point2[0]) % p
    
    # Calculate the y-coordinate of the result
    y = (slope * (point1[0] - x) - point1[1]) % p
    
    return (x, y)
# Example usage:
# Define parameters for the elliptic curve y^2 = x^3 + ax + b (mod p)'''
'''
a = 4
p = 26167  # A prime number
base_point = (7881, 16198)  # Example base point on the curve
two = (4533,6092)
four = (20165,3476)
three = (11761, 23455)

# Scalar to multiply the base point, n
scalar = 4

result = multiply(base_point, scalar, a, p)
print(f"The result of scalar multiplication ({scalar} times the base point {base_point}) is: {result}")
print()'''
