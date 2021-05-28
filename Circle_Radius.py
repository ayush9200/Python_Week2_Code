# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.

def calculate_area():
    # Calculating area of circle by multiplying radius with 3.14(pie value)
    radius = float(input("Please enter radius of circle : "))
    area = 2 * (3.14 * radius)
    print(f'Circle area is : {area} and radius is : {radius}')
