import numpy as np
from matplotlib import pyplot as plt
# top left cell = (1, 1)      top right = (300, 1)
# bottom left   = (1, -300)   bottom right = (300, -300)

def calculate_fuel(coord, serial_num):
    rack_id = coord[1] + 10 # fuel cell's rack ID = X + 10
    power_level = rack_id * coord[0] # power level of rack ID * Y
    power_level += serial_num # power level += grid serial number (puzzle input)
    power_level *= rack_id # power level *= rack ID
    try:
        power_level = int(str(power_level).split('-')[-1][-3]) # keep only the hundreds value (12345 -> 3, 45 -> 0)
    except IndexError:
        power_level = 0
    power_level -= 5 # power level -= 5

    return power_level

def find_power_grid(serial_num, xsize, ysize):
    xs = np.arange(0, xsize)
    ys = np.arange(0, ysize)
    possible_coords = []
    for x in xs:
        for y in ys:
            possible_coords.append((y, x))

    power_grid = np.zeros([xsize, ysize])
    for coord in possible_coords:
        power_grid[coord] = calculate_fuel(coord, serial_num)

    return power_grid, possible_coords

if __name__ == "__main__":
    serial_num = 9306
    xsize = 300
    ysize = 300
    pg, pc = find_power_grid(serial_num, xsize, ysize)
    print(pg)

    top_left_coord = []
    tot_power = []
    grid_width = []
    for width in np.arange(1, 30):
        for val in pc:
            x, y = val
            new_grid = pg[y:y+width, x:x+width]
            if len(new_grid[0]) < width or len(new_grid) < width:
                continue
            top_left_coord.append((x,y))
            grid_width.append(width)
            p = 0
            for y2 in np.arange(len(new_grid)):
                p += np.sum(new_grid[y2])
            tot_power.append(p)

    print(top_left_coord[np.argmax(tot_power)], grid_width[np.argmax(tot_power)], np.max(tot_power))
