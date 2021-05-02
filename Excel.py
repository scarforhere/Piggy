# Programmed by Scar
from Backup import backup
from Cal import PointData
from Cal import PointDataCylinder
import pandas as pd
import math


def calculate_z(file,
                colume_x, colume_y,
                suffix="z",
                sheet="Sheet1"):
    """
    Import file's path , data of x,y \n
    Give back value of z after the last column \n\n

    :param file: Path of target.xlsx
    :param colume_x: Column number of direction x
    :param colume_y: Column number of direction y
    :param suffix: New file's name = target_suffix.xlsx
    :param sheet: Target sheet of target.xlsx
    """
    # copy as new file
    file = backup(file, suffix)

    # create DataFrame from xlsx
    df = pd.read_excel(file, header=0)

    # get max row's and column's number
    n_row = df.shape[0]
    n_column = df.shape[1]

    # insert new empty column after late column
    df.insert(n_column, 'z', None)

    for i in range(0, n_row):
        # get value from DataFrame
        x = df.iloc[i, colume_x]
        y = df.iloc[i, colume_y]
        absolut = ((x ** 2 + y ** 2) ** 0.5)
        point = PointData(absolut)
        # put value back to Dataframe
        df.iloc[i, n_column] = point.z

    # write DataFrame back to xlsx
    df.to_excel(file, index=False)


def calculate_judge(file,
                    colume_x, colume_y,
                    suffix="judge",
                    sheet="Sheet1"):
    """
    Import file's path , data of x,y \n
    if z <= z_0 give judge = 0\n
    if z > z_0 give judge = 1\n
    Give back value of judgementresult after the last column \n\n

    :param file: Path of target.xlsx
    :param colume_x: Column number of direction x
    :param colume_y: Column number of direction y
    :param suffix: New file's name = target_suffix.xlsx
    :param sheet: Target sheet of target.xlsx
    """
    # copy as new file
    file = backup(file, suffix)

    # create DataFrame from xlsx
    df = pd.read_excel(file, sheet_name=sheet, header=0)

    # get max row's and column's number
    n_row = df.shape[0]
    n_column = df.shape[1]

    # insert new empty column after late column
    df.insert(n_column, 'z => z_0', None)

    for i in range(0, n_row):
        # get value from DataFrame
        x = df.iloc[i, colume_x]
        y = df.iloc[i, colume_y]
        absolut = ((x ** 2 + y ** 2) ** 0.5)
        point = PointData(absolut)
        # put value back to Dataframe
        df.iloc[i, n_column] = point.judge

    # write DataFrame back to xlsx
    df.to_excel(file, index=False)


def calculate_sort(file, column='', order=False, suffix="sort", sheet="Sheet1"):
    """
    Sort the data under the order of selected column of keyword

    :param file: Path of target.xlsx
    :param column: Sort keyword of to be selected Column
    :param order: False: ascending    True: descending
    :param suffix: New file's name = target_suffix.xlsx
    :param sheet: Target sheet of target.xlsx
    """
    # copy as new file
    file = backup(file, suffix)

    # create DataFrame from xlsx
    df = pd.read_excel(file, sheet_name=sheet, header=0)

    # get max row's and column's number
    n_column = df.shape[1]

    # get the Info from last column
    head = df.columns.values[n_column - 1]

    if column.isalpha():
        df_new = df.sort_values(by=column, ascending=order)
    elif column.isnumeric():
        # get the Info from last column
        head = df.columns.values[int(column) - 1]
        # sort Dataframe
        df_new = df.sort_values(by=head, ascending=order)
    else:
        # get the Info from last column
        head = df.columns.values[n_column - 1]
        # sort Dataframe
        df_new = df.sort_values(by=head, ascending=order)

    # write DataFrame back to xlsx
    df_new.to_excel(file, index=False)


def calculate_cylinder(file,
                       colume_x_1, colume_x_3, colume_u_3,
                       x_s, k_1, u_s, a, b, c, d, E,
                       suffix="Cylinder",
                       sheet="Sheet1"):
    """
    Import: file's path , colume number of x_1, x_3, u_3 \n
    Set constant: x_s, k_1, u_s, a, b, c, d, E \n
    Give back value of z after the last column \n\n

    :param file: Path of target.xlsx
    :param colume_x_1: Column number of x_1
    :param colume_x_3: Column number of x_3
    :param colume_u_3: Column number of u_3
    :param x_s: Constant x_s
    :param k_1: Constant k_1
    :param u_s: Constant u_s
    :param a: Constant a
    :param b: Constant b
    :param c: Constant c
    :param d: Constant d
    :param E: Constant E
    :param suffix: New file's name = target_suffix.xlsx
    :param sheet: Target sheet of target.xlsx
    """
    # copy as new file
    file = backup(file, suffix)

    # create DataFrame from xlsx
    df = pd.read_excel(file, sheet_name=sheet, header=0)

    # get max row's and column's number
    n_row = df.shape[0]
    n_column = df.shape[1]

    # insert new empty column after late column
    df.insert(n_column, 'z', None)

    for i in range(0, n_row):
        # get value from DataFrame
        x_1 = df.iloc[i, colume_x_1]
        x_3 = df.iloc[i, colume_x_3]
        u_3 = df.iloc[i, colume_u_3]
        point = PointDataCylinder(x_1, x_3, u_3, x_s, k_1, u_s, a, b, c, d, E)
        # put value back to Dataframe
        df.iloc[i, n_column] = point.z

    # write DataFrame back to xlsx
    df.to_excel(file, index=False)


# Test
def main():
    # define patch to xlsx
    # file= r'C:\Users\15152\Desktop\node.xlsx'
    file = 'node.xlsx'
    file1 = 'node_z.xlsx'
    sheet = 'node'
    suffix = 'z'
    tar_x = 5
    tar_y = 6
    calculate_z(file, tar_x, tar_y, 'z', 'node')
    calculate_judge(file, tar_x, tar_y, 'judge', 'node')
    calculate_sort(file1, '', False, "sort", "Sheet1")

    # Point in Cylinder
    file1 = 'node.xlsx'
    colume_x_1 = 3
    colume_x_3 = 4
    colume_u_3 = 5
    x_s = 0.007
    k_1 = 5
    u_s = 123
    a = 0.035
    b = 16
    c = 50 / 180 * math.pi
    d = 0.25
    E = 22000
    calculate_cylinder(file1, colume_x_1, colume_x_3, colume_u_3, x_s, k_1, u_s, a, b, c, d, E,
                       suffix="Cylinder",
                       sheet="Sheet1")


if __name__ == '__main__':
    main()
