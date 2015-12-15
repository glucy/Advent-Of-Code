'''
Created on 15 Dec 2015

@author: glucy
'''

# Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
# Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
# Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
# Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8


class Ingredient():

    name = ""
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayFifteen", "r") as f:
    lines = f.readlines()
    ingredientsList = list()
    for line in lines:
        line = line[:-1]
        name, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split()
        ingredientsList.append(Ingredient(name[:-1], int(capacity[:-1]), int(durability[:-1]),
                                          int(flavor[:-1]), int(texture[:-1]), int(calories)))

    score = 0
    maxScore = 0
    for i in range(0, 100):
        for j in range(0, 100-i):
            for k in range(0, 100-i-j):
                h = 100-i-j-k
                a = (ingredientsList[0].capacity * i + ingredientsList[1].capacity * j +
                     ingredientsList[2].capacity * k + ingredientsList[3].capacity * h)
                b = (ingredientsList[0].durability * i + ingredientsList[1].durability * j +
                     ingredientsList[2].durability * k + ingredientsList[3].durability * h)
                c = (ingredientsList[0].flavor * i + ingredientsList[1].flavor * j +
                     ingredientsList[2].flavor * k + ingredientsList[3].flavor * h)
                d = (ingredientsList[0].texture * i + ingredientsList[1].texture * j +
                     ingredientsList[2].texture * k + ingredientsList[3].texture * h)
                e = (ingredientsList[0].calories * i + ingredientsList[1].calories * j +
                     ingredientsList[2].calories * k + ingredientsList[3].calories * h)

                # Condition for Part 2.  Uncomment the 2 lines below for Part2.
#                 if(not(e == 500)):
#                     continue

                if a <= 0 or b <= 0 or c <= 0 or d <= 0:
                    score = 0
                    continue
                score = a*b*c*d
                if score > maxScore:
                    maxScore = score

    print "MaxScore: ", maxScore
    # Part 1 MaxScore:  21367368
    # Part 2 MaxScore:  1766400
