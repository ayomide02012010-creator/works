package main

import "fmt"

func mAIN() {
    for n := 0; n <= 6; n++ {
        if n%2 == 0 {
            fmt.Println(n, "is EVEN")
        } else {
            fmt.Println(n, "is ODD")
        }
    }
}