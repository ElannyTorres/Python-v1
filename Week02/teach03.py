import math

print('Lets make some calcs together.')
#Stretch3: conversion cm to m
squareSides = float(input('What is the length of a side of the square (in cm)? '))
squareAreaCm = squareSides ** 2
print(f'The area of the square is: {squareAreaCm / 100} cm^2')
print(f'The area of the square is: {squareAreaCm / 10000} m^2')

rectangleLength = float(input('\nWhat is the length of rectangle (in cm)? '))
rectangleWidth = float(input('What is the width of rectangle (in cm)? '))
rectangleAreaCm = rectangleLength * rectangleWidth
print(f'The area of the rectangle is: {rectangleAreaCm / 100} cm^2')
print(f'The area of the rectangle is: {rectangleAreaCm / 10000} m^2')

#Stretch1: Using the math library
circleRadius = float(input('\nWhat is the radius of the circle (in cm)? '))
#pi = 3.14
circleAreaCm = math.pi * (circleRadius ** 2)
print(f'The area of the circle is: {circleAreaCm / 100} cm^2')
print(f'The area of the circle is: {circleAreaCm / 10000} m^2')

#Stretch2: Different areas from one value
value = float(input("\nWhat is the value to be used? "))
squareArea = value ** 2
circleArea = math.pi * (value ** 2)
cubeVolume = value ** 3
sphereVolume = (4 / 3) * math.pi * (value ** 3)
print(f'Area of a square: {squareArea}')
print(f'Area of a circle: {circleArea}')
print(f'Volume of a cube: {cubeVolume}')
print(f'Volume of a sphere: {sphereVolume}')

