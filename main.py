# Programmed by Scar
from Excel import calculate_z
from Excel import calculate_judge
from Excel import calculate_sort
from Excel import calculate_cylinder
from Merge import merge
from Image import plot
import math
import os

dir_path = r'E:\Python_Code\Piggy\DataSource\\'
os.chdir(dir_path)

file_name = 'node.xlsx'
file = ''.join([dir_path, file_name])
print(file)
calculate_z(file, 5, 6, 'z', )
calculate_judge(file, 5, 6, 'judge', 'node')

file_name = 'node_z.xlsx'
file = ''.join([dir_path, file_name])
calculate_sort(file, 'z', False, 'sort', 'Sheet1')

# Merge()
file_position_name = 'node'
file_bool_name = 'pl'
file_merge_name = 'merge'
file_position = ''.join([dir_path, file_position_name])
file_bool = ''.join([dir_path, file_bool_name])
file_merge = ''.join([dir_path, file_merge_name])
merge(file_position, file_bool, file_merge)

# Plot()
file_merge_name = 'merge'
file_merge = ''.join([dir_path, file_merge_name])
plot(file=file_merge,
     sheet='Sheet1',
     num_x=51,
     num_y=101,
     interpolation_str='None',
     cmap_str='Reds')

# 3 Dimension Point in Cylinder
file_name = 'node.xlsx'
file = ''.join([dir_path, file_name])

calculate_cylinder(file,
                   column_x_1=3,
                   column_x_3=4,
                   column_u_3=5,
                   x_s=0.007,
                   k_1=5,
                   u_s=123,
                   a=0.035,
                   b=16,
                   c=50 / 180 * math.pi,
                   d=0.25,
                   E=22000,
                   suffix="Cylinder")

print('\n')
print('------------------------------')
print('Finished!'.center(30))
print('------------------------------')
