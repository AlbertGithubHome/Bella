package main

import (
	"fmt"
	"exercise/pkg"
)

func main() {
	fmt.Println("go exercise.")
	pkg.Fibonacci(10)
	fmt.Println("joseph ring:")
	fmt.Println(pkg.JosephRing(14, 3))
	fmt.Println(pkg.JosephRing(8, 3))
}