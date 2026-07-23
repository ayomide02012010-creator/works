package main

import (
	"fmt"
	"os"
	"strings"
)
var color = map[string][3]int {
	"red" : {255, 0, 0},
	"green" : {0, 128, 0},
	"yellow" : {255, 255, 0},
	"blue" : {0, 0, 255},
	"magenta" : {255, 0, 255},
	"cyan" : {0, 255, 255},
	"white" : {255, 255, 255},
	"black" : {0, 0, 0},
	"orange" : {255, 165, 0},
}
func main() {
	argument := os.Args[1:]
	
	if len(argument) == 1 {
		fmt.Print(GenerateAscii(argument[0], "", "", "", ""))
		return
	} 
	if len(argument) == 2 {
		if !strings.HasPrefix(argument[0], "--color=") {
			PrintUsage()
			return
		}  
		colorName := strings.TrimPrefix(argument[0], "--color=")
		rgb, ok := color[colorName]
		if !ok {
			PrintUsage()
			return
		}
		r := rgb[0]
		g := rgb[1]
		b := rgb[2]

		colorStart := fmt.Sprintf("\x1b[38;2;%d;%d;%dm", r, g, b)
		colorReset := "\x1b[0m"
		fmt.Println(GenerateAscii(argument[1], "", "", colorStart, colorReset))
		return
	}
	if len(argument) == 3 {
		if !strings.HasPrefix(argument[0], "--color=") {
			PrintUsage()
			return
		}  
		colorName := strings.TrimPrefix(argument[0], "--color=")
		rgb, ok := color[colorName]
		if !ok {
			PrintUsage()
			return
		}
		r := rgb[0]
		g := rgb[1]
		b := rgb[2]

		colorStart := fmt.Sprintf("\x1b[38;2;%d;%d;%dm", r, g, b)
		colorReset := "\x1b[0m"
		fmt.Println(GenerateAscii(argument[2], "", argument[1], colorStart, colorReset))
		return
	}
	PrintUsage()
	
}
func PrintUsage() {
	fmt.Println("Usage: go run . [OPTION] [STRING]")
	fmt.Println()
	fmt.Println("EX: go run . --color=<color> <substring to be colored> 'something'")
}
func GenerateAscii(text, banner, substring, colorStart, colorReset string) string {
	if banner == "" {
		banner = "standard"
	}
	if !strings.HasSuffix(banner, ".txt") {
		banner += ".txt"
	}
	data, err := os.ReadFile(banner)
	if err != nil {
		fmt.Fprintln(os.Stderr, "Error reading banner file:", err)
		os.Exit(1)
	}

	input := strings.Split(strings.ReplaceAll(string(data), "\r\n", "\n"), "\n")
	if len(input) > 0 && input[0] == "" {
		input = input[1:]
	}
	text = strings.ReplaceAll(text, `\n`, "\n")
	if text == "" {
		return ""
	}
	lines := strings.Split(text, "\n")

	allEmpty := true
	for _, l := range lines {
		if l != "" {
			allEmpty = false
			break
		}
	}
	if allEmpty {
		return strings.Repeat("\n", len(lines)-1)
	}
	var out string
	for _, line := range lines {
		if line == "" {
			out += "\n"
			continue
		}
		lineRunes := []rune(line)
		subRunes := []rune(substring)
		mask := make([]bool, len(lineRunes))

		if substring == "" {
			for i := 0; i < len(mask); i++ {
				mask[i] = true
			}
		} else {
			for i := 0; i <= len(lineRunes)-len(subRunes); i++ {
				match := true
				for j := 0; j < len(subRunes); j++ {
					if lineRunes[i+j] != subRunes[j] {
						match = false
						break
					}
				}
				if match {
					for j := 0; j < len(subRunes); j++ {
						mask[i+j] = true
					}
				}
			}
		}
		for r := 0; r < 8; r++ {
			for pos := 0; pos < len(lineRunes); pos++{
				ch := lineRunes[pos]
				if ch < 32 || ch > 126 {
					continue
				}
				idx := (int(ch) - 32) * 9
				if mask[pos] {
					out += colorStart + input[idx+r] + colorReset
				} else {
					out += input[idx+r] 
				}
			}
			out += "\n"
		}
	}
	return out
}