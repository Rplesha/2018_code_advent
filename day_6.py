# this is wrong...I stole the code because I couldn't figure it out

from astropy.table import Table
import numpy as np
from matplotlib import pyplot as plt
# reading in my coordinates
coordinates = Table.read('input_day6', format='ascii')
xs = coordinates['x']
ys = coordinates['y']
coord = [(x, y) for x, y in zip(xs, ys)]

plt.plot(xs, ys, 'o')

# First I need to make a square grid that contains all of my coordinates
xgrid = np.arange(0, np.max(xs)+1) #inclusive of last point
ygrid = np.arange(0, np.max(ys)+1) #inclusive of last point

full_xgrid = np.array(list(xgrid)*len(ygrid))
full_ygrid = np.repeat(ygrid, len(xgrid))

full_grid_coords = [(x, y) for x, y in zip(full_xgrid, full_ygrid)]

# now that I did that, I loop through all of the coordinates I have (A-F for ex)
#   and compute the distance to each of those points.

closest_coord_grid = {}
for my_grid in coord:
    closest_coord_grid[my_grid] = 0

for grid_coord in full_grid_coords:
    temp_area_dict = {}
    for my_coord in coord:
        eq = abs(my_coord[0] - grid_coord[0]) + abs(my_coord[1] - grid_coord[1])
        temp_area_dict[my_coord] = eq

    temp_ind = np.argmin(list(temp_area_dict.values()))
    closest = list(temp_area_dict.keys())[temp_ind]
    closest_coord_grid[closest] += 1

# now to figure out which of my coords are infinite and not worry about those

# if there isn't a point to the left, right, top, and bottom of the point, then
#   it will be infinite in one of those ways
non_inf = []
inf = []
for my_coord in coord:
    x_coord = my_coord[0]
    y_coord = my_coord[1]
    wh_gx = np.where(xs > x_coord)[0]
    wh_lx = np.where(xs < x_coord)[0]
    wh_gy = np.where(ys > y_coord)[0]
    wh_ly = np.where(ys < y_coord)[0]
    if len(wh_gx) >= 1 and len(wh_lx) >= 1 and len(wh_gy) >= 1 and len(wh_ly) >= 1:
        non_inf.append(my_coord)
    else:
        inf.append(my_coord)

max_area = []
max_coord = []
nix = []
niy = []

for key in non_inf:
    nix.append(key[0])
    niy.append(key[1])
    max_area.append(closest_coord_grid[key])
    max_coord.append(key)

plt.plot(nix, niy, 'o')

plt.plot(max_coord[np.argmax(max_area)][0], max_coord[np.argmax(max_area)][1], 'x')

print(max_area)

plt.show()
