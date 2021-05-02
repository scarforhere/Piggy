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


def calculate(x, a=150.0, b=150.0 / 2200.0, c=2200.0):
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

    except Exception as exception_info:
        return exception_info


def judge(x, a=150.0, b=150.0 / 2200.0, c=2200.0):
    d = 2 * b
    f = ln(a) - ln(c * e * b)
    x_0 = -(d / (2 * f))
    y_0 = c * x_0 * math.pow(e, d / (2 * x) + f)
    z_0 = x_0 * y_0

    z = calculate(x, a, b, c)
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
def main():
    result = calculate(10, a=150, b=150 / 2200, c=2200)
    print(result)
    result = calculate(10)
    print(result)
    result = calculate(0.03, 0.4323, 0.1212, 0.23432)
    print(result)

    print('---------------------------------------')
    result = judge(10, a=150, b=150 / 2200, c=2200)
    print(result)
    result = judge(10)
    print(result)
    result = judge(0.03, 0.4323, 0.1212, 0.23432)
    print(result)
    print()

    print('---------------------------------------')
    print("2 Dimensions Point")
    print('---------------------------------------')
    # Point = PointData(10)
    # Point = PointData(10, 150, 150 / 2200, 2200)
    point = PointData(10, a=150, b=150 / 2200, c=2200)
    print(f"Point.x:\t{point.x:16.8f}")
    print(f"Point.a: \t{point.a:16.8f}")
    print(f"Point.b: \t{point.b:16.8f}")
    print(f"Point.c: \t{point.c:16.8f}")
    print(f"Point.d: \t{point.d:16.8f}")
    print(f"Point.f: \t{point.f:16.8f}")
    print(f"Point.x_0: \t{point.x_0:16.8f}")
    print(f"Point.y: \t{point.y:16.8f}")
    print(f"Point.y_0: \t{point.y_0:16.8f}")
    print(f"Point.z_0: \t{point.z_0:16.8f}")
    print(f"Point.judge: \t{point.judge}")
    print()

    print('---------------------------------------')
    print("3 Dimensions Point in Cylinder")
    print('---------------------------------------')
    # Point = PointDataCylinder(0.005, 0.00001, 15)
    point = PointDataCylinder(0.005, 0.00001, 15,
                              x_s=0.007,
                              k_1=5,
                              u_s=123,
                              a=0.035,
                              b=16,
                              c=50 / 180 * math.pi,
                              d=0.25,
                              E=22000)
    print(f"Point.x_1:\t{point.x_1:16.8f}")
    print(f"Point.x_3:\t{point.x_3:16.8f}")
    print(f"Point.u_3:\t{point.u_3:16.8f}")
    print(f"Point.x_s:\t{point.x_s:16.8f}")
    print(f"Point.k_1:\t{point.k_1:16.8f}")
    print(f"Point.a:\t{point.a:16.8f}")
    print(f"Point.b:\t{point.b:16.8f}")
    print(f"Point.c:\t{point.c:16.8f}")
    print(f"Point.d:\t{point.d:16.8f}")
    print(f"Point.E:\t{point.E:16.8f}")
    print(f"Point.K:\t{point.K:16.8f}")
    print(f"Point.G:\t{point.G:16.8f}")
    print(f"Point.m:\t{point.m:16.8f}")
    print(f"Point.n:\t{point.n:16.8f}")
    print(f"Point.x_0:\t{point.x_0:16.8f}")
    print(f"Point.A_1:\t{point.A_1:16.8f}")
    print(f"Point.A_2:\t{point.A_2:16.8f}")
    print(f"Point.B_1:\t{point.B_1:16.8f}")
    print(f"Point.B_2:\t{point.B_2:16.8f}")
    print(f"Point.y:\t{point.y:16.8f}")
    print(f"Point.z:\t{point.z:16.8f}")
    print(f"Point.y_1:\t{point.y_1:16.8f}")
    print(f"Point.y_2:\t{point.y_2:16.8f}")
    print(f"Point.z_1:\t{point.z_1:16.8f}")
    print(f"Point.z_2:\t{point.z_2:16.8f}")
    print(f"Point.L:\t{point.L:16.8f}")


if __name__ == '__main__':
    main()
