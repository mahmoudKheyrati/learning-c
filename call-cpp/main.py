import ctypes
from ctypes import cdll, POINTER


# Define the Point structure in Python
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def main():
    lib = cdll.LoadLibrary("./cpp/main.so")
    lib.hello()

    lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
    lib.add.restype = ctypes.c_int
    res = lib.add(1, 45)
    print(f"add result: {res}")



    lib.get_point.restype = Point
    point = lib.get_point()
    print(f"Point coordinates are: ({point.x}, {point.y})")

    # counter example
    for i in range(10):
        lib.increment()
    print(f"the value of the counter is: {lib.getCounterValue()} ")


    #### get points
    # Set the argument and return types of the get_points function
    lib.get_points.argtypes = (POINTER(ctypes.c_int),)
    lib.get_points.restype = POINTER(Point)

    # Call the get_points function
    size = ctypes.c_int()
    points_ptr = lib.get_points(size)

    # Convert the result to a Python list
    points = [points_ptr[i] for i in range(size.value)]
    # Print the points
    for point in points:
        print(f"Point coordinates are: ({point.x}, {point.y})")

main()
