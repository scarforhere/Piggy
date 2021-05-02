# Programmed by Scar

import pandas as pd


def merge(file_position='node', file_bool='pl', file_merge='merge'):
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
        point_data = []

        # add x,y to Merge[]
        with open(file_position, 'r') as file_p:
            data = file_p.readlines()
            for Data_Point in data:
                merge_line = Data_Point.split()
                point_data.append(merge_line)

        # add bool to Merge[]
        with open(file_bool, 'r') as file_b:
            i = 0
            data = file_b.readlines()
            for result in data:
                point_data[i].append(result.split()[0])
                i += 1

        # get element number of Merge[]
        point_num = len(point_data)

        # crate dict{} for DataFrame
        excel_dict = {'x': [], 'y': [], 'bool': []}
        for i in range(0, point_num):
            excel_dict['x'].append(point_data[i][0])
            excel_dict['y'].append(point_data[i][1])
            excel_dict['bool'].append(point_data[i][2])

        # create Dataframe
        df = pd.DataFrame(excel_dict)

        # write DataFrame back to xlsx
        df.to_excel(file_merge, index=False)

        print("Merge Seccessed!")

    except BaseException as e:
        print('Merge Failed!')
        print("Info:\n", e)


# Test
def main():
    file_position = r'E:\Python_Code\Piggy\DataSource\node'
    file_bool = r'E:\Python_Code\Piggy\DataSource\pl'
    file_merge = r'E:\Python_Code\Piggy\DataSource\merge'
    merge(file_position, file_bool, file_merge)


if __name__ == '__main__':
    main()
