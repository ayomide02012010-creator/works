package piscine

import "fmt"

func PrintMemory(a [10]byte) {
	s := ""
	for i, b := range a {
		fmt.Printf("%02x", b)
		if i < 9 {
			fmt.Print(" ")
		}
		if i == 3 || i == 7 {
			fmt.Println()
		}
		if b < 32 || b > 126 {
			b = '.'
		}
		s += string(b)
	}
	fmt.Println("\n" + s)
}
