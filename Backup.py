# Programmed by Scar
import os


def copy_file(file1, file2):
    """
    Back up single file

    :param file1: Origin file's path
    :param file2: Target file's path
    """
    with open(file1, "rb") as f1:
        with open(file2, "wb") as f2:
            content = f1.readline()
            while len(content) > 0:
                f2.write(content)
                content = f1.readline()



def copy_dir(dir1, dir2):
    """
    Back up folders and files
    :param dir1:
    :param dir2:
    """
    dir_list = os.listdir(dir1)
    os.mkdir(dir2)

    for f in dir_list:

        file1 = os.path.join(dir1, f)
        file2 = os.path.join(dir2, f)

        if os.path.isfile(file1):
            copy_file(file1, file2)

        if os.path.isdir(file1):
            copy_dir(file1, file2)


# Test
def main():
    src = r'E:\Python_Code\Piggy\DataSource'
    target = r'E:\Python_Code\Piggy\AB'
    copy_dir(src, target)  # 当前文件夹中的aa文件夹复制到bb文件夹 没有会自动创建


if __name__ == '__main__':
    main()
