package main

import (
	"fmt"
	"os"
	"strings"
)
func GenerateAscii(text, banner string) (string, error){
	if banner == "" {
		banner = "standard"
	}
	if !strings.HasSuffix(banner, ".txt") {
		banner += ".txt"
	}
	data, err := os.ReadFile(banner)
	if err != nil {
		return "", err
	}

	input := strings.Split(strings.ReplaceAll(string(data), "\r\n", "\n"), "\n")
	if len(input) > 0 && input[0] == "" {
		input = input[1:]
	}
	text = strings.ReplaceAll(text, `\n`, "\n")
	if text == "" {
		return "", nil
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
		return strings.Repeat("\n", len(lines)-1), nil
	}
	var out string
	for _, line := range lines {
		if line == "" {
			out += "\n"
			continue
		}
		for r := range 8 {
			for _, char := range line {
				if char < 32 || char > 126 {
					continue
				}
				index := (int(char) - 32) * 9
				out += input[index+r]
			}
			out += "\n"
		}
	}
	return out, nil
}

func main() {
	if len(os.Args) < 2 {
		return
	}
	banner := "standard"
	if len(os.Args) > 2 {
		banner = os.Args[2]
	}
	fmt.Print(GenerateAscii(os.Args[1], banner))
}

// // ---------------------------------------------------------------------------------------------------------------
// package main

// import (
// 	"os"
// 	"fmt"
// )

// func main() {
// 	if len(os.Args) < 2 {
// 		return
// 	}
// 	banner := "standard"
// 	if len(os.Args) > 2 {
// 		banner = os.Args[2]
// 	}
// 	fmt.Print(GenerateAscii(os.Args[1], banner))
// }
// func fixNewlines(s string) string {
// 	out := ""
// 	for i := 0; i < len(s); i++ {
// 		if s[i] == '\\' && i+1 < len(s) && s[i+1] == 'n' {
// 			out += "\n"
// 			i++
// 		} else if s[i] != '\r' {
// 			out += string(s[i])
// 		}
// 	}
// 	return out
// }

// func splitLines(s string) []string {
// 	lines := []string{}
// 	cur := ""
// 	for i := 0; i < len(s); i++ {
// 		if s[i] == '\n' {
// 			lines = append(lines, cur)
// 			cur = ""
// 		} else if s[i] != '\r' {
// 			cur += string(s[i])
// 		}
// 	}
// 	return append(lines, cur)
// }

// func hasTxtSuffix(s string) bool {
// 	if len(s) < 4 {
// 		return false
// 	}
// 	return s[len(s)-4:] == ".txt"
// }

// func GenerateAscii(text, banner string) string {
// 	if banner == "" {
// 		banner = "standard"
// 	}
// 	if len(banner) < 4 || banner[len(banner)-4:] != ".txt" {
// 		banner += ".txt"
// 	}

// 	data, err := os.ReadFile(banner)
// 	if err != nil {
// 		fmt.Fprintln(os.Stderr, "Error reading banner file:", err)
// 		os.Exit(1)
// 	}

// 	glyphs := splitLines(string(data))
// 	if len(glyphs) > 0 && glyphs[0] == "" {
// 		glyphs = glyphs[1:]
// 	}

// 	text = fixNewlines(text)
// 	if text == "" {
// 		return ""
// 	}
// 	lines := splitLines(text)
// 	allEmpty := true
// 	for _, l := range lines {
// 		if l != "" {
// 			allEmpty = false
// 			break
// 		}
// 	}
// 	if allEmpty {
// 		out := ""
// 		for i := 0; i < len(lines)-1; i++ {
// 			out += "\n"
// 		}
// 		return out
// 	}
// 	out := ""
// 	for _, line := range lines {
// 		if line == "" {
// 			out += "\n"
// 			continue
// 		}
// 		for r := 0; r < 8; r++ {
// 			for _, ch := range line {
// 				a := int(ch) - 32
// 				if a < 0 || a > 94 {
// 					continue
// 				}
// 				idx := a*9 + r
// 				if idx >= 0 && idx < len(glyphs) {
// 					out += glyphs[idx]
// 				}
// 			}
// 			out += "\n"
// 		}
// 	}
// 	return out
// }
// package main

// import (
// 	"fmt"
// 	"os"
// 	"strings"
// )

// func main() {
// 	if len(os.Args) < 2 {
// 		return
// 	}

// 	input := os.Args[1]
// 	if input == "" {
// 		return
// 	}

// 	// 1. Handle literal newlines (replace "\n" with actual newline character)
// 	input = strings.ReplaceAll(input, "\\n", "\n")

// 	// 2. Load the banner file (e.g., standard.txt)
// 	bannerLines, err := os.ReadFile("standard.txt")
// 	if err != nil {
// 		fmt.Println("Error reading banner file")
// 		return
// 	}
// 	fontData := strings.Split(string(bannerLines), "\n")

// 	// 3. Use strings.Builder for the final output
// 	var result strings.Builder

// 	// Split input by newlines to handle multiple lines of ASCII art
// 	inputLines := strings.Split(input, "\n")

// 	for _, line := range inputLines {
// 		if line == "" {
// 			result.WriteString("\n")
// 			continue
// 		}

// 		// Each ASCII character is 8 lines tall
// 		for i := 1; i <= 8; i++ {
// 			for _, char := range line {
// 				// Calculate starting line in fontData
// 				// ASCII ' ' is 32. The font file usually starts at ' '
// 				// Each block is 9 lines (8 lines of art + 1 separator)
// 				start := int(char-32)*9 + i
// 				result.WriteString(fontData[start])
// 			}
// 			result.WriteString("\n")
// 		}
// 	}

// 	fmt.Print(result.String())
// }
// func GenerateAsci(text string) string{
// 	data,err := os.ReadFile("banners/standard.txt")
// 	if err != nil{
// 		fmt.Println("Unable to read files:standard.txt")
// 		return ""
// 	}
// 	input := strings.Split(string(data), "\n")

// 	lines:= strings.Split(text, "\\n")
// 	result := ""

// 	for _,word := range lines{
// 		if word == ""{
// 			continue
// 		}
// 		for i:=1; i<= 8; i++ {
// 			for _, char := range word {
// 				index := (int(char)-32)* 9
// 				result+= input[index+i]
// 			}
// 		  result +="\n"
// 		}
// 	}

// return result
// }
// package main

// import (
// 	"fmt"
// 	"os"
// 	"strings"
// )

// func main() {
// 	if len(os.Args) < 2 {
// 		return
// 	}
// 	s := strings.ReplaceAll(os.Args[1], `\n`, "\n")
// 	b := "standard.txt"
// 	if len(os.Args) > 2 {
// 		b = os.Args[2]
// 		if !strings.HasSuffix(b, ".txt") {
// 			b += ".txt"
// 		}
// 	}
// 	d, _ := os.ReadFile(b)
// 	ls := strings.Split(strings.ReplaceAll(string(d), "\r\n", "\n"), "\n")
// 	if len(ls) > 0 && ls[0] == "" {
// 		ls = ls[1:]
// 	}
// 	ps := strings.Split(s, "\n")
// 	for i, p := range ps {
// 		if p == "" {
// 			fmt.Println()
// 		} else {
// 			for r := 0; r < 8; r++ {
// 				for j := 0; j < len(p); j++ {
// 					fmt.Print(ls[int(p[j]-32)*9+r])
// 				}
// 				fmt.Println()
// 			}
// 		}
// 		if i == len(ps)-1 && p != "" {
// 			break
// 		}
// 	}
// }
// // ---------------------------------------------PART 2 -----------------------------------------------------------
// func GenerateAsci(text string) string{
// 	data, err := os.ReadFile("banners/standard.txt")
// 	if err != nil {
// 		fmt.Println("Unadle to read file: standard,txt")
// 	}

// 	input := strings.Split(string(data), "\n")
// 	lines := strings.Split(text, "\\n")
// 	result := ""

// 	for _, word := range lines {
// 		if word == "" {
// 			result += "\n"
// 			continue
// 		}
// 		for i := 1; i <= 8; i++ {
// 			for _, char := range word {
// 				index := (int(char) - 32) * 9 
// 				result += input[index + i]
// 			}
// 			result += "\n"
// 		}
// 	}
// 	return result
// }
// // ------------------------------PART 3-----------------------------------------
// func GenerateAscii(text string) string {
// 	data, err := os.ReadFile("banners/standard.txt")
// 	if err != nil {
// 		fmt.Println("Unable to read files: standard.txt")
// 		os.Exit(1)
// 	}
// 	input := strings.Split(strings.ReplaceAll(string(data), "\r\n", "\n"), "\n")
// 	if len(input) > 0 && input[0] == "" {
// 		input = input[1:]
// 	}

// 	text = strings.ReplaceAll(text, `\n`, "\n")
// 	lines := strings.Split(text, "\n")
// 	result := ""

// 	for i, word := range lines {
// 		if word == "" {
// 			result += "\n"
// 		} else {
// 			for r := 0; r < 8; r++ {
// 				for _, char := range word {
// 					index := (int(char) - 32) * 9
// 					result += input[index+r]
// 				}
// 				result += "\n"
// 			}
// 		}
// 		if i == len(lines)-1 && word != "" {
// 			break
// 		}
// 	}

// 	return result
// }
// func fixNewlines(s string) string {
// 	out := ""
// 	for i := 0; i < len(s); i++ {
// 		if s[i] == '\\' && i+1 < len(s) && s[i+1] == 'n' {
// 			out += "\n"
// 			i++
// 		} else if s[i] != '\r' {
// 			out += string(s[i])
// 		}
// 	}
// 	return out
// }

// func splitLines(s string) []string {
// 	lines := []string{}
// 	cur := ""

// 	for i := 0; i < len(s); i++ {
// 		if s[i] == '\n' {
// 			lines = append(lines, cur)
// 			cur = ""
// 		} else if s[i] != '\r' {
// 			cur += string(s[i])
// 		}
// 	}
// 	return append(lines, cur)
// }