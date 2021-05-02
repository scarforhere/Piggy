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
    print(f'\tBackup Succeeded:'
          f'\n\t\tfrom: {file1}'
          f'\n\t\tto    {file2}')


def copy_dir(dir1, dir2):
    """
    Back up folders and files

    :param dir1: Target folder's or file's path
    :param dir2: Origin folder's or file's path
    """
    dir_list = os.listdir(dir1)
    os.mkdir(dir2)

    for f in dir_list:

        file1 = os.path.join(dir1, f)
        file2 = os.path.join(dir2, f)

        if os.path.isfile(file1):
            copy_file(file1, file2)
            print(f'\tBackup Succeeded:'
                  f'\n\t\tfrom: {file1}'
                  f'\n\t\tto    {file2}')

        if os.path.isdir(file1):
            copy_dir(file1, file2)


def backup(origin, target=None, suffix='down'):
    print('Start to Backup:')
    if os.path.isfile(origin):
        if not target:
            lst = origin.rsplit(sep='.', maxsplit=1)
            target_list = [lst[0], "_", suffix, ".", lst[1]]
            target = ''.join(target_list)

        copy_file(origin, target)
        return target

    else:
        if not target:
            target_list = [origin, "_", suffix]
            target = ''.join(target_list)

        copy_dir(origin, target)
        return target


# Test
def main():
    import Delete

    src = r'E:\Python_Code\Piggy\DataSource'
    target = r'E:\Python_Code\Piggy\AB'
    new_dir = backup(origin=src)
    print(new_dir)
    print()
    new_dir = backup(origin=src, suffix='new')
    print(new_dir)
    print()
    backup(origin=src, target=target)
    print(new_dir)
    print()
    new_dir = backup(origin=r'E:\Python_Code\Piggy\DataSource\\node.xlsx')
    print(new_dir)
    print()

    input("Press Enter To Delete")
    Delete.execute(path=os.getcwd())


if __name__ == '__main__':
    main()
