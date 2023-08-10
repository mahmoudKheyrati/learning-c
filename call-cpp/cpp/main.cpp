#include <iostream>

extern "C" {
    void hello() {
        std::cout << "Hello from C++!" << std::endl;
    }

    int count = 0 ;
    int increment() {
        count ++;
        return count;
    }
    int getCounterValue(){
        return count;
    }
    int add(int a , int b ){
        return a+b ;
    }

    typedef struct {
        int x;
        int y;
    } Point;

    Point get_point() {
        Point p;
        p.x = 10;
        p.y = 20;
        return p;
    }

    Point* get_points(int* size) {
        int n = 5; // Number of points
        *size = n;

        Point* points = (Point*)malloc(n * sizeof(Point));
        for(int i = 0; i < n; i++) {
            points[i].x = 10 * i;
            points[i].y = 20 * i;
        }

        return points;
    }

}
