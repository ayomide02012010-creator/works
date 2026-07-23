package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Print(NotDecimal("0.1"))             // 1
	fmt.Print(NotDecimal("174.2"))           // 1742
	fmt.Print(NotDecimal("0.1255"))          // 1255
	fmt.Print(NotDecimal("1.20525856"))     // 120525856
	fmt.Print(NotDecimal("-0.0f00d00"))     // -0.0f00d00
	fmt.Print(NotDecimal(""))                // (empty string case)
	fmt.Print(NotDecimal("-19.525856"))     // -19525856
	fmt.Print(NotDecimal("1952"))           // 1952
}

func NotDecimal(dec string) string {
	if dec == "" {
		return "\n"
	}
	_, err := strconv.ParseFloat(dec, 64)
	if err != nil {
		return dec + "\n"
	}
	if strings.Contains(dec, ".") {
		parts := strings.Split(dec, ".")
		integerPart := parts[0]
		decimalPart := parts[1]
		if decimalPart == "0" {
			return dec + "\n"
		}
		return integerPart + decimalPart + "\n"
	}
	return dec + "\n"
}

