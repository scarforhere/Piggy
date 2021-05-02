# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Del
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-02 05:22 PM
-------------------------------------------------
Description : 

    Delete by program created files
        mode = False        -->     record
        mode = True         -->     delete

    Important: Need to recorde() before del_data()

"""
import os
import shutil
import json

# TODO Set Execute Mode!!!
"""
mode = False        -->     record
mode = True         -->     delete
"""
mode = True


def record_data():
    """
    Record source files
    """
    # 遍历文件夹及子文件夹
    file_datasource_path = os.getcwd()

    name_txt = 'Record.txt'
    path_full = ''.join([file_datasource_path, '\\', name_txt])

    with open(path_full, 'w'):
        pass

    files_walk_list = os.walk(file_datasource_path)

    # 将所有文件件及文件夹做成列表
    files_list = []

    for dirpath, dirname, filename in files_walk_list:
        for item in filename:
            file_origin_path = ''.join([dirpath, '\\', item])
            files_list.append(file_origin_path)
        for item in dirname:
            dir_origin_path = ''.join([dirpath, '\\', item])
            files_list.append(dir_origin_path)

    # 将列表内所有内容使用json写入record.json
    json_write(path_full, files_list)

    print('\n')
    print('------------------------------')
    print("Record Successed!".center(30))
    print('------------------------------')


def delete_data():
    """
    Delete by program created files
    """
    file_datasource_path = os.getcwd()

    name_txt = 'Record.txt'
    path_full = ''.join([file_datasource_path, '\\', name_txt])

    # 从Record.txt中读取json格式数据并转化为SET
    file_origin_set = json_read(path_full)

    # 遍历文件夹及子文件夹
    files_walk_list = os.walk(file_datasource_path)
    files_list = []

    # 将所有文件件及文件夹做成列表
    for dirpath, dirname, filename in files_walk_list:
        for item in filename:
            file_origin_path = ''.join([dirpath, '\\', item])
            files_list.append(file_origin_path)
        for item in dirname:
            dir_origin_path = ''.join([dirpath, '\\', item])
            files_list.append(dir_origin_path)

    file_now_set = set(files_list)

    # 获取新建文件及文件夹
    file_new_set = file_now_set.difference(file_origin_set)

    for item in file_new_set:
        try:
            if os.path.isdir(item):
                shutil.rmtree(item)
            else:
                os.remove(item)
            print(fr'Delete Seccessed: {item}')
        except FileNotFoundError:
            continue

    print('\n')
    print('------------------------------')
    print("Delete Seccessed!".center(30))
    print('------------------------------')


def json_write(path, data):
    """
    Write list data in to txt with json format

    :param path: Full path of txt
    :param data: Data in List type
    :return: True --> WriteIn Seccessed!
    """
    with open(path, 'w') as f:

        if isinstance(data, list):
            _data = json.dumps(data)
            f.write(_data)

            print("WriteIn Seccessed!")
        else:
            print("WriteIn Failed!")
            raise TypeError("Data should be list")

    return True


def json_read(path):
    """
    Read a txt with json format

    :param path: Full path of txt
    :return: Data from txt in origin type
    """
    with open(path, "r") as f:
        data = f.read()
    return json.loads(data)


def execute():
    """
    Execute under mode\n
    mode = False        -->     record\n
    mode = True         -->     delete
    """
    if mode:
        delete_data()
    elif not mode:
        record_data()
    else:
        print("")


def main():
    execute()


if __name__ == '__main__':
    main()
