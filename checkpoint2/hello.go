package main

import "github.com/01-edu/z01"

func M() {
	str := "mabegunde"
	for _, char := range str {
		z01.PrintRune(char)
	}
	z01.PrintRune('\n')
}