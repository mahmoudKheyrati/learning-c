package main

/*
#cgo CFLAGS: -I../cpp
#cgo LDFLAGS: /home/mahmoud/Desktop/c-learning/learning-c/call-cpp/cpp/main.so
#include "main.h"
*/
import "C"
import "fmt"
import "unsafe"

func main() {
	C.hello()

	// Call add function
	res := C.add(1, 45)
	fmt.Printf("add result: %d\n", res)

	// Increment counter
	for i := 0; i < 10; i++ {
		C.increment()
	}
	fmt.Printf("the value of the counter is: %d\n", C.getCounterValue())

	// Get point
	point := C.get_point()
	fmt.Printf("Point coordinates are: (%d, %d)\n", point.x, point.y)

	// Get points
	var size C.int
	points := C.get_points(&size)
	goPoints := (*[1 << 30]C.Point)(unsafe.Pointer(points))[:size:size]
	for _, p := range goPoints {
		fmt.Printf("Point coordinates are: (%d, %d)\n", p.x, p.y)
	}
}