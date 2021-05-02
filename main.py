# Programmed by Scar
from Excel import Calculate_z
from Excel import Calculate_judge
from Excel import Calculate_sort
from Excel import Calculate_Cylinder
from Merge import Merge
from Image import Plot
import math

file1='node.xlsx'
Calculate_z(file1,5,6,'z','node')
Calculate_judge(file1,5,6,'judge','node')

file2='node_z.xlsx'
Calculate_sort(file2,'z',False,'sort','Sheet1')

# Merge()
file_position = 'node'
file_bool = 'pl'
file_merge = 'merge'
Merge(file_position,file_bool,file_merge)

# Plot()
file_position = 'node'
file_bool = 'pl'
file_merge = 'merge'
Plot(file='Merge', sheet='Sheet1', num_x=51, num_y=101,interpolation_str='None',cmap_str='Reds')

# 3 Dimension Point in Cylinder
file1='node.xlsx'
colume_x_1=3
colume_x_3=4
colume_u_3=5
x_s=0.007
k_1=5
u_s=123
a=0.035
b=16
c=50 / 180 * math.pi
d=0.25
E=22000
Calculate_Cylinder(file1, colume_x_1, colume_x_3, colume_u_3, x_s, k_1, u_s, a, b, c, d, E, suffix="Cylinder", sheet="Sheet1")

print('\n')
print('------------------------------')
print('Finished!'.center(30))
print('------------------------------')

