package main

import "fmt"

func Printcomb() {
	for n1 := 0; n1 <= 7; n1++ {
		for n2 := n1 + 1; n2 <= 8; n2++ {
			for n3 := n2 + 1; n3 <= 9; n3++ {
				fmt.Printf("%d%d%d", n1,n2,n3)
				if n1 != 7 || n2 != 8 || n3 != 9 {
					fmt.Print(", ")
				}
			}
		}
	}
	fmt.Println()
}