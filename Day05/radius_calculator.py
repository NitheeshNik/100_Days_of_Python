print("RADIUS CALCULATOR")
radius = float(input("Enter the radius: "))
PI = 3.14159
area = PI * pow(radius, 2)
surface_area = 4 * PI * pow(radius, 2)
volume = 4.0 / 3.0 * PI * pow(radius, 3)
print(f"Area:{area:.2f}\nsurface Area:{surface_area:.2f}\nVolume:{volume:.2f}")