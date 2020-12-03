## Part 1

def func(step_x, step_y):
    data = open("/content/drive/MyDrive/Datasets/AdventOfCode/trees.txt").read().split("\n")
    trees = []
    for i in data:
        trees.append(i.replace("[',\,]", ''))

    encountered = 0
    pointer_x = 0
    pointer_y = 0


    while pointer_y < len(trees)-step_y:
        pointer_x += step_x
        pointer_y += step_y

        if pointer_x >= len(trees[0]):
            pointer_x = 0 + pointer_x - len(trees[0]) 
        if trees[pointer_y][pointer_x] == '#':
            encountered += 1

    return encountered
    
## Part 2
a = func(3,1)
b = func(1,1)
c = func(5,1)
d = func(7,1)
e = func(1,2)
multiplied = a*b*c*d*e
