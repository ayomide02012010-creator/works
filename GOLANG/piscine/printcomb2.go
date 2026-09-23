package main

import "fmt"

func Printnbr()  {
	var n1 int
	var n2 int 

	for n1 = 0; n1 <= 99; n1++ {
		for n2 = n1 + 1; n2 <= 99; n2++ {
			fmt.Printf("%02d %02d", n1,n2)
			if n1 != 98 || n2 != 99 {
				fmt.Print(", ")
			}
		}
	}
	fmt.Println()
}