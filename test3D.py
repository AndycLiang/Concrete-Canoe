import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (20,20))
ax = plt.axes(projection='3d')
#plt.rcParams["figure.autolayout"] = True


def slopeOrth(coefficient, power, zval):
    slope = ((-1*coefficient * power * ((zval/coefficient)**((1/power)*(power-1)))) - 0.001 )**-1
    return slope

def slopey(slope):
    slopey = 0.75*(1/12)*(slope/( (((slope ** 2) + 1) ** 0.5)))
    return slopey

def slopex(slope):
    slopex = 0.75*(1/12)*(1/( (((slope ** 2) + 1) ** 0.5)))
    return slopex


index = list(range(0,23)) 

coefficient = [13.9499, 5.3016, 4.304, 4.3201, 3.5602, 2.5695, 1.6929,
               1.02845, 0.59123, 0.38154, 0.3199, 0.27767, 0.24909, 0.22546,
               0.20897, 0.19381, 0.1812, 0.1708, 0.1622, 0.15406, 0.1475,
               0.14118, 0.1362, 0.1342]
constant = [0.4019, 0.0313, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
power = [2/3, 2/3, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/9, 1/9, 1/9, 1/9,
         1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
"""
coefficient = [12/pow(13.999, 9), 12/pow(13.981, 9), 12/pow(13.962, 9), 12/pow(13.941, 9),
               12/pow(13.919, 9), 12/pow(13.895, 9), 12/pow(13.869, 9), 12/pow(13.841, 9),
               12/pow(13.809, 9), 12/pow(13.774, 9), 12/pow(13.735, 9), 12/pow(13.689, 9),
               12/pow(13.635, 9), 12/pow(13.570, 9), 12/pow(13.486, 9), 12/pow(13.369, 9),
               12/pow(13.117, 9), 12/pow(12.661, 7), 12/pow(11.921, 7), 12/pow(11.098, 5),
               12/pow(10.167, 5), 12/pow(9.1000, 5), 12/pow(7.8470, 4),
               11.998/pow(6.331, 4), 11.625/pow(4.409, 4), 7.177/pow(1.785, 3)]

constant = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0.00200000000000067, 0.375, 4.823]

power = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9,
         1/9, 1/9, 1/7, 1/7, 1/5, 1/5, 1/5, 1/4, 1/4, 1/4, 1/3]
"""

#Inner curves
for i in index:
    z = np.arange(0, 1, 1/50)
    y = (0*z)+0.33*i
    x = pow((z - constant[i])/coefficient[i], power[i])
    ax.plot3D(x, y, z, color = 'darkslateblue' )

for i in index:
    z = np.arange(0, 1, 1/50)
    y = (0*z)+0.33*i
    x = -1*pow((z - constant[i])/coefficient[i], power[i])
    ax.plot3D(x, y, z, color = 'darkslateblue')

for i in index:
    z = np.arange(0, 1, 1/50)
    y = (0*z)+ 7.26 + 0.33*i
    x = pow((z - constant[22-i])/coefficient[22-i], power[22-i])
    ax.plot3D(x, y, z, color = 'darkslateblue')

for i in index:
    z = np.arange(0, 1, 1/50)
    y = (0*z)+ 7.26 + 0.33*i
    x = -1*pow((z - constant[22-i])/coefficient[22-i], power[22-i])
    ax.plot3D(x, y, z, color = 'darkslateblue')


#Outer curves
for i in index:
    z = np.arange(0, 1, 1/50)
    y = (0*z)+0.33*i
    x = pow((z - constant[i])/coefficient[i], power[i])
    ax.plot3D(x + slopex(slopeOrth(coefficient[i], 1/power[i] , z)), y, z + slopey(slopeOrth(coefficient[i], 1/power[i] , z)), color = 'lightcoral')

for i in index:
    z = np.arange(0, 1, 1/50)
    y = (0*z)+0.33*i
    x = -1*pow((z - constant[i])/coefficient[i], power[i])
    ax.plot3D(x - slopex(slopeOrth(coefficient[i], 1/power[i] , z)), y, z + slopey(slopeOrth(coefficient[i], 1/power[i] , z)), color = 'lightcoral')

for i in index:
    z = np.arange(0, 1, 1/50)
    y = (0*z)+ 7.26 + 0.33*i
    x = pow((z - constant[22-i])/coefficient[22-i], power[22-i])
    ax.plot3D(x + slopex(slopeOrth(coefficient[22-i], 1/power[22-i] , z)), y, z + slopey(slopeOrth(coefficient[22-i], 1/power[22-i] , z)), color = 'lightcoral')

for i in index:
    z = np.arange(0, 1, 1/50)
    y = (0*z)+ 7.26 + 0.33*i
    x = -1*pow((z - constant[22-i])/coefficient[22-i], power[22-i])
    ax.plot3D(x - slopex(slopeOrth(coefficient[22-i], 1/power[22-i] , z)), y, z + slopey(slopeOrth(coefficient[22-i], 1/power[22-i] , z)), color = 'lightcoral')

""" Test codes
z_1 = np.arange(0, 1, 1/50)
y_1 = (0*z_1)+1
x_1 = pow((z_1 -0.4019)/13.9499, 2/3)
ax.plot3D(x_1, y_1, z_1)

z_2 = np.arange(0, 1, 1/50)
y_2 = (0*z_2)+2
x_2 = pow((z_2 -0.0313)/5.3016, 2/3)
ax.plot3D(x_2, y_2, z_2)

z_3 = np.arange(0, 1, 1/50)
y_3 = (0*z_3)+3
x_3 = pow((z_3)/4.304, 1/2)
ax.plot3D(x_3, y_3, z_3)

z_4 = np.arange(0, 1, 1/50)
y_4 = (0*z_4)+4
x_4 = pow((z_4)/4.3201, 1/3)
ax.plot3D(x_4, y_4, z_4)
"""

"""
z_5 = np.arange(0, 1, 1/50)
y_5 = (0*z_5)
x_5 = pow((z_5)/3.5602, 1/4)
ax.plot3D(x_5, y_5, z_5)
"""

"""
z_test = np.arange(0, 1, 1/50)
y_test = (0*z_test)
x_test = pow((z_test)/3.5602, 1/4)
ax.plot3D(x_test + slopex(slopeOrth(3.5602, 4, z_test)), y_test, z_test + slopey(slopeOrth(3.5602, 4, z_test)))


z_test = np.arange(0, 1, 1/50)
y_test = (0*z_test)
x_test = pow(((z_test)-constant[4])/coefficient[4], power[4])
ax.plot3D(x_test + slopex(slopeOrth(coefficient[4], 1/power[4], z_test)), y_test, z_test + slopey(slopeOrth(coefficient[4], 1/power[4], z_test)))
ax.set_title('3D Parametric Plot')
"""

ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

ax.axes.set_xlim3d(left=0, right=4) 
ax.axes.set_ylim3d(bottom=0, top=4) 
ax.axes.set_zlim3d(bottom=0, top=4)

plt.show()


