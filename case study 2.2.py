"""Consider a situation where two cars are moving from a point P and another car from point Q in the same
direction and meet each other after 1 hour. If they move in the opposite direction, they will meet after 1 hour.
 Find out the velocity of both cars.
 """

distance = float(input("Enter distance between the two cars: "))

time = 1

v1 = float(input("Enter velocity of car 1: "))
v2 = float(input("Enter velocity of car 2: "))

print("Velocity of car 1 =", v1)
print("Velocity of car 2 =", v2)

print("Total distance covered =", (v1 + v2) * time)