# Programmed by Scar

import pandas as pd


def Merge(file_position='node', file_bool='pl', file_merge='merge'):
    """
    Merge two .txt files to .xlsx file

    :param file_position: Name or path of .txt file, which contains info of Column_x,Column_y
    :param file_bool: Name or path of .txt file, which contains info of Column_b
    :param file_merge: Name or path of .xlsx file
    """
    try:
        if file_position.find('.txt') == -1:
            file_position += '.txt'
        if file_bool.find('.txt') == -1:
            file_bool += '.txt'
        if file_merge.find('.xlsx') == -1:
            file_merge += '.xlsx'

        # create empty list Merge[x][y]=bool
        Merge = []

        # add x,y to Merge[]
        with open(file_position, 'r') as file_p:
            Data = file_p.readlines()
            for Data_Point in Data:
                Merge_line = Data_Point.split()
                Merge.append(Merge_line)

        # add bool to Merge[]
        with open(file_bool, 'r') as file_b:
            i = 0
            Data = file_b.readlines()
            for result in Data:
                Merge[i].append(result.split()[0])
                i += 1

        # get element number of Merge[]
        Point_num = len(Merge)

        # crate dict{} for DataFrame
        excel_dict = {'x': [], 'y': [], 'bool': []}
        for i in range(0, Point_num):
            excel_dict['x'].append(Merge[i][0])
            excel_dict['y'].append(Merge[i][1])
            excel_dict['bool'].append(Merge[i][2])

        # create Dataframe
        df = pd.DataFrame(excel_dict)

        # write DataFrame back to xlsx
        df.to_excel(file_merge, index=False)

        print("Merge Seccessed!")

    except BaseException as e:
        print('Merge Failed!')
        print("Info:\n", e)


# Test
if __name__ == '__main__':
    file_position = 'node'
    file_bool = 'pl'
    file_merge = 'merge'
    Merge(file_position, file_bool, file_merge)
