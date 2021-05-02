# Programmed by Scar


def backup(file, suffix="down"):
    """
    Copy origin file(file.xlsx) as new file(file_suffix.xlsx)\n
    And return new filename

    :param file: Name or Path of origin file (Origin or Origin.docx)
    :param suffix: Suffix string of the name of new file (0rigin_suffix.docx)
    :return: Name or Path of new file
    """
    try:
        lst = file.rsplit(sep='.', maxsplit=1)
        lst_new = [lst[0], "_", suffix, ".", lst[1]]
    except:
        lst_new = [file, suffix]

    file_down = ''.join(lst_new)

    with open(file, 'rb') as src_file:
        with open(file_down, 'wb') as target_file:
            target_file.write(src_file.read())
    return file_down


# Test
def main():
    file = 'node.xlsx'
    print(backup(file))
    print(backup(file, "down"))


if __name__ == '__main__':
    main()
