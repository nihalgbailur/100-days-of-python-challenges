import math
x = abs(-4)
print(x)



# Basic arithmetic operations
a = 5
b = 2

sum_result = math.sum([a, b])
difference_result = math.diff(a, b)
product_result = math.prod([a, b])
quotient_result = math.quot(a, b)

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")

# Exponential and logarithmic functions
x = 2
power_result = math.pow(x, 3)  # x raised to the power of 3
sqrt_result = math.sqrt(x)     # square root of x
log_result = math.log(x)       # natural logarithm of x

print(f"Power: {power_result}")
print(f"Square Root: {sqrt_result}")
print(f"Natural Logarithm: {log_result}")

# Trigonometric functions
angle_in_radians = math.radians(30)  # Convert degrees to radians
sin_result = math.sin(angle_in_radians)
cos_result = math.cos(angle_in_radians)
tan_result = math.tan(angle_in_radians)

print(f"Sine: {sin_result}")
print(f"Cosine: {cos_result}")
print(f"Tangent: {tan_result}")

