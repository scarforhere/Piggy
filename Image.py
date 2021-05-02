# Programmed by Scar

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# set size of Plot
plt.figure(figsize=(6, 8))


def plot(file='Merge', sheet='Sheet1', num_x=51, num_y=101, pitch=100, interpolation_str='None', cmap_str='Reds'):
    """
    Create Image from .xlsx \n
    Need: Column_x, Column_x, Column_bool \n
    No Header!!!

    :param file: name or path of .xlsx
    :param sheet: Sheet's name of .xlsx
    :param num_x: number of point in x direktion
    :param num_y: number of point in y direktion
    :param pitch: pitch between start and end point
    :param interpolation_str: interpolation reference
                --> See:https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods
    :param cmap_str: colormap reference
                --> See:https://matplotlib.org/stable/gallery/color/colormap_reference
    """
    try:
        if file.find('.xlsx') == -1:
            file += '.xlsx'

        # load DataFrame from .xlsx
        df = pd.read_excel(file, sheet_name=sheet, header=0)
        # get row's number
        n_rou = df.shape[0]

        # create empty list Data[][]
        data = [[i for i in range(0, num_y)] for _ in range(0, num_x)]

        # set Data[x][y]=bool
        for i in range(0, n_rou):
            x = int((df.iloc[i, 0] + 2500) / pitch - 1)
            y = int((df.iloc[i, 1] + 5100) / pitch - 1)
            data[x][y] = df.iloc[i, 2]

        # create List of value of bool
        list_plot = []
        for y in range(0, num_y):
            for x in range(0, num_x):
                list_plot.append(data[x][y])

        # create Plot data
        data_plot = np.array(list_plot).reshape(num_y, num_x)

        # hide axis
        # plt.xticks(())
        # plt.yticks(())

        # set property of Plot
        plt.imshow(data_plot, interpolation=interpolation_str, cmap=cmap_str, origin='lower')
        # interpolation     --> 'None'  'bilinear'  'sinc'
        # cmap              --> 'Reds'  'bwr'  'seismic'

        # show color-value info
        plt.colorbar(shrink=1)

        # get active plt
        ax = plt.gca()
        ax.format_coord = format_coord

        # set axis info
        i_x = 5 * 2
        i_y = 5 * 1
        range_t_x = [int(-(pitch * (num_x - 1) / 2)), int((pitch * (num_x - 1) / 2 + i_x * pitch)), int(i_x * pitch)]
        range_t_y = [int(-(pitch * (num_y - 1) / 2)), int((pitch * (num_y - 1) / 2 + i_y * pitch)), int(i_y * pitch)]
        new_ticks_x = [x for x in range(range_t_x[0], range_t_x[1], range_t_x[2])]
        new_ticks_y = [y for y in range(range_t_y[0], range_t_y[1], range_t_y[2])]
        plt.xticks([x for x in range(0, num_x, i_x)], new_ticks_x)
        plt.yticks([y for y in range(0, num_y, i_y)], new_ticks_y)

        # set label
        plt.xlabel('x')
        plt.ylabel('y')

        # show Plot
        plt.show()

        print("Plot Seccessed!")
    except BaseException as e:
        print("Plot Failed!")
        print("Info:\n", e)


# set mouse cursors display
def format_coord(x, y):
    x_float = math.ceil(float(x)) * 100 - 2500
    y_float = math.ceil(float(y)) * 100 - 5000

    return 'x：%5.0f, y：%5.0f' % (x_float, y_float)


# Test
def main():
    import os
    dir_path = r'E:\Python_Code\Piggy\DataSource\\'
    os.chdir(dir_path)
    file_name = 'Merge'
    file = ''.join([dir_path, file_name])
    plot(file=file,
         sheet='Sheet1',
         num_x=51,
         num_y=101,
         interpolation_str='None',
         cmap_str='Reds')


if __name__ == '__main__':
    main()
