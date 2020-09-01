package pkg

import "fmt"

/*
Fibonacci : print fibonacci sequence
*/
func Fibonacci(maxCount int) {

    if maxCount <= 0 { return }

    first, second := 0, 1
    for i := 1; i <= maxCount; i++ {
        first, second = second, first + second
        fmt.Printf("%d ", first)
    }
}