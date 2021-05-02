# Programmed by Scar
"""
    z = Cal(x, a, b, c,)
    Result == False
        --> Problem

    Possible Problem:
        1. ?/0
"""

import math

e = math.exp(1)
pi = math.pi


def Calculate(x, a=150.0, b=150.0 / 2200.0, c=2200.0):
    try:
        d = 2 * b
        f = ln(a) - ln(c * e * b)
        x_0 = -(d / (2 * f))

        if x <= x_0:
            y = c * x
        else:
            y = c * x * math.pow(e, d / (2 * x) + f)

        z = x * y
        return z

    except:
        return False


def Judge(x, a=150.0, b=150.0 / 2200.0, c=2200.0):
    d = 2 * b
    f = ln(a) - ln(c * e * b)
    x_0 = -(d / (2 * f))
    y_0 = c * x_0 * math.pow(e, d / (2 * x) + f)
    z_0 = x_0 * y_0

    z = Calculate(x, a, b, c)
    if z <= z_0:
        return 0
    else:
        return 1


class PointData:
    def __init__(self, x, a=150.0, b=150.0 / 2200.0, c=2200.0):
        # Init input const. ---> x , a , b , c
        self.x = x
        self.a = a
        self.b = b
        self.c = c

        d = 2 * b
        f = ln(a) - ln(c * e * b)
        x_0 = -(d / (2 * f))
        self.d = d
        self.f = f
        self.x_0 = x_0

        if x <= x_0:
            y = c * x
        else:
            y = c * x * math.pow(e, d / (2 * x) + f)
        z = x * y
        self.y = y
        self.z = z

        # Judge
        # z <= z_0  ---> 0
        # z > z_0   ---> 1
        y_0 = c * x_0 * math.pow(e, d / (2 * x) + f)
        z_0 = x_0 * y_0
        self.y_0 = y_0
        self.z_0 = z_0
        if z <= z_0:
            self.judge = 0
        else:
            self.judge = 1


class PointDataCylinder:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, x_1, x_3, u_3, x_s=0.007, k_1=5, u_s=123, a=0.035, b=16, c=50 / 180 * math.pi, d=0.25, E=22000):
        # set variable
        self.x_1 = x_1
        self.x_3 = x_3
        self.u_3 = u_3

        # set constant
        self.x_s = x_s
        self.k_1 = k_1
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.E = E
        self.K = E / (3 * (1 - 2 * d))
        self.G = E / (2 * (1 + d))

        # get intermediate constant m, n ,x_0
        self.m = k_1 * x_s
        self.n = ln(u_s) - ln(E * e * x_s)
        self.x_0 = -self.m / (2 * self.n)

        # get intermediate constant A_1, A_2, B_1, B_2
        self.A_1 = pow((1 - math.sin(c)), 2) / (2 * self.G * math.cos(5 / 18 * math.pi)) + a / (9 * self.K)
        self.A_2 = -1 / (2 * self.G) + 2 * a / (9 * self.G)
        self.B_1 = 1 / (2 * self.G) - 2 * a / (9 * self.G)
        self.B_2 = -pow((1 + math.sin(c)), 2) / (pow(2 * self.G * math.cos(5 / 18 * math.pi), 2)) - 4 * a / (9 * self.G)

        # get y from compare x_0, x_1
        if x_1 < self.x_0:
            self.y = E * x_1 + (2 * d - 1) * u_3
        else:
            self.y = (E * x_1 * math.exp(((self.m * (self.A_2 * self.B_1 - self.A_1 * self.B_2) * u_3 * x_1) /
                                          (self.A_2 * self.x_1 - 2 * self.A_1 * self.x_3)) + self.n)
                      + (2 * d - 1) * u_3)

        self.z = x_1 * self.y

        # y_1: (0.85 * x_0) instead of x_1
        self.y_1 = (E * (0.85 * self.x_0) * math.exp(
            ((self.m * (self.A_2 * self.B_1 - self.A_1 * self.B_2) * u_3 * (0.85 * self.x_0)) /
             (self.A_2 * (0.85 * self.x_0) - 2 * self.A_1 * self.x_3)) + self.n)
                    + (2 * d - 1) * u_3)
        # y_2: x_0 instead of x_1
        self.y_2 = (E * self.x_0 * math.exp(((self.m * (self.A_2 * self.B_1 - self.A_1 * self.B_2) * u_3 * self.x_0) /
                                             (self.A_2 * self.x_0 - 2 * self.A_1 * self.x_3)) + self.n)
                    + (2 * d - 1) * u_3)
        # z_1: [(0.85 * x_0), y_1] instead of [x_1, y]
        self.z_1 = 0.85 * self.x_0 * self.y_1
        # z_1: [x_0, y_2] instead of [x_1, y]
        self.z_2 = self.x_0 * self.y_2

        # get value of L from compare z, z_1, z_2
        if self.z <= self.z_1:
            self.L = 0
        elif self.z_1 < self.z <= self.z_2:
            self.L = 0.85
        else:
            self.L = 1


def ln(x):
    return math.log(x)


# Test
if __name__ == '__main__':
    Result = Calculate(10, a=150, b=150 / 2200, c=2200)
    print(Result)
    Result = Calculate(10)
    print(Result)
    Result = Calculate(0.03, 0.4323, 0.1212, 0.23432)
    print(Result)

    print('---------------------------------------')
    Result = Judge(10, a=150, b=150 / 2200, c=2200)
    print(Result)
    Result = Judge(10)
    print(Result)
    Result = Judge(0.03, 0.4323, 0.1212, 0.23432)
    print(Result)
    print()

    print('---------------------------------------')
    print("2 Dimensions Point")
    print('---------------------------------------')
    Point = PointData(10)
    Point = PointData(10, 150, 150 / 2200, 2200)
    Point = PointData(10, a=150, b=150 / 2200, c=2200)
    print(f"Point.x:\t{Point.x:16.8f}")
    print(f"Point.a: \t{Point.a:16.8f}")
    print(f"Point.b: \t{Point.b:16.8f}")
    print(f"Point.c: \t{Point.c:16.8f}")
    print(f"Point.d: \t{Point.d:16.8f}")
    print(f"Point.f: \t{Point.f:16.8f}")
    print(f"Point.x_0: \t{Point.x_0:16.8f}")
    print(f"Point.y: \t{Point.y:16.8f}")
    print(f"Point.y_0: \t{Point.y_0:16.8f}")
    print(f"Point.z_0: \t{Point.z_0:16.8f}")
    print(f"Point.judge: \t{Point.judge}")
    print()

    print('---------------------------------------')
    print("3 Dimensions Point in Cylinder")
    print('---------------------------------------')
    Point = PointDataCylinder(0.005, 0.00001, 15)
    Point = PointDataCylinder(0.005, 0.00001, 15, x_s=0.007, k_1=5, u_s=123, a=0.035, b=16, c=50 / 180 * math.pi, d=0.25,
                              E=22000)
    print(f"Point.x_1:\t{Point.x_1:16.8f}")
    print(f"Point.x_3:\t{Point.x_3:16.8f}")
    print(f"Point.u_3:\t{Point.u_3:16.8f}")
    print(f"Point.x_s:\t{Point.x_s:16.8f}")
    print(f"Point.k_1:\t{Point.k_1:16.8f}")
    print(f"Point.a:\t{Point.a:16.8f}")
    print(f"Point.b:\t{Point.b:16.8f}")
    print(f"Point.c:\t{Point.c:16.8f}")
    print(f"Point.d:\t{Point.d:16.8f}")
    print(f"Point.E:\t{Point.E:16.8f}")
    print(f"Point.K:\t{Point.K:16.8f}")
    print(f"Point.G:\t{Point.G:16.8f}")
    print(f"Point.m:\t{Point.m:16.8f}")
    print(f"Point.n:\t{Point.n:16.8f}")
    print(f"Point.x_0:\t{Point.x_0:16.8f}")
    print(f"Point.A_1:\t{Point.A_1:16.8f}")
    print(f"Point.A_2:\t{Point.A_2:16.8f}")
    print(f"Point.B_1:\t{Point.B_1:16.8f}")
    print(f"Point.B_2:\t{Point.B_2:16.8f}")
    print(f"Point.y:\t{Point.y:16.8f}")
    print(f"Point.z:\t{Point.z:16.8f}")
    print(f"Point.y_1:\t{Point.y_1:16.8f}")
    print(f"Point.y_2:\t{Point.y_2:16.8f}")
    print(f"Point.z_1:\t{Point.z_1:16.8f}")
    print(f"Point.z_2:\t{Point.z_2:16.8f}")
    print(f"Point.L:\t{Point.L:16.8f}")
