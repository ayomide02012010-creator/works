package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		return
	}
	for _, arg := range os.Args[1:] {
		words := strings.Fields(arg)
		for i, word := range words {
			word = strings.ToLower(word)
			if len(word) > 0 {
				word = word[:len(word)-1] + strings.ToUpper(string(word[len(word)-1]))
			}
			if i > 0 {
				fmt.Print(" ")
			}
			fmt.Print(word)
		}
		fmt.Println()
	}
}
