# Problem: Determine how fast an object will fall.

import math

print('Welcome to the velocity calculator. Please enter the following:')
#mass
m = float(input('Mass (in kg): '))
#gravity
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
#time
t = int(input('Time (in seconds): '))
#density
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
#cross sectional area
A = float(input('Cross sectional area (in m^2): '))
#drag constant
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

#? v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
#* 1. c = (1/2) * p * A * C
c = (1 / 2) * p * A * C
#* 2. Total
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

print('\n--------------------------------------------')
print(f'The inner value of c is: {c:.3f}')
print(f'The velocity after 10.0 seconds is: {v:.3f} m/s')
print('--------------------------------------------')