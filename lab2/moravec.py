from PIL import Image

threshold = 100
file_name = "cats_1g.png"
g = Image.open(file_name)
xy_shifts = [(1, 0), (1, 1), (0, 1), (-1, 1)]

min_E = [[0 for x in range(g.size[0])] for y in range(g.size[1])]
for y in range(1, g.size[1]-1):
    for x in range(1, g.size[0]-1):
        E = 100000
        for shift in xy_shifts:
            diff = g.getpixel((x+shift[0], y+shift[1])) - g.getpixel((x, y))
            diff = diff * diff
            if diff < E:
                E = diff
        min_E[y][x] = E 

gc = g.copy()
for y in range(g.size[1]):
    for x in range(g.size[0]):
        if min_E[y][x] > threshold:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    gc.putpixel((x+dx, y+dy), 255)
gc.save(file_name[:-4] + str(threshold) + ".png")
