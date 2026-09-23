package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {	
	if len(os.Args) != 3 {
		fmt.Println("Can't Work with this!!!")
		return
	}
	inputtext := os.Args[1]
	outputtext := os.Args[2]

	data, err := os.ReadFile(inputtext)
	if err != nil {
		fmt.Println("unable to read file", err)
		return
	}

	sentence := string(data)
	words := strings.Fields(sentence)

	words = handleHex(words)
	words = handleBin(words)
	words = HandleUpLowCap(words)
	words = Articles(words)

	result := strings.Join(words, " ")
	
	result = Punctuation(result)
	result = formatQuotes(result)
	
	err = os.WriteFile(outputtext, []byte(result), 0o644)
	if err != nil {
		fmt.Println("unable to write file", err)
		return 
	}
	fmt.Println("Processed Successfully!") 
}
  
func handleHex(words []string) []string {
	for i := 0; i < len(words); i++ {
		if words[i] == "(hex)" && i > 0 {
			read, err := strconv.ParseInt(words[i-1], 16, 64)
			if err == nil {
				words[i-1] = strconv.FormatInt(read, 10)
			}
			words = append(words[:i], words[i+1:]...)
			i--
		}
	}
	return words
}
func handleBin(words []string) []string {
	for i := 0; i < len(words); i++ {
		if words[i] == "(bin)" && i > 0 {
			read, err := strconv.ParseInt(words[i-1], 2, 64)
			if err == nil {
				words[i-1] = strconv.FormatInt(read, 10)
			}
			words = append(words[:i], words[i+1:]...)
			i--
		}
	}
	return words
}
func HandleUpLowCap(words []string) []string {
	var clean []string
	for i := 0; i < len(words); i++ {
		w := words[i]
		
		switch w {
			case "(up)":
				if len(clean) > 0 {
					clean[len(clean)-1] = strings.ToUpper(clean[len(clean)-1])
		        }
			case "(low)":
				if len(clean) > 0 {
					clean[len(clean)-1] = strings.ToLower(clean[len(clean)-1])
		        }
			case "(cap)":
				if len(clean) > 0 {
					clean[len(clean)-1] = capitalize(clean[len(clean)-1])
		        }
            
			case "(up,", "(low,", "(cap,":
				if i+1 < len(words) && strings.HasSuffix(words[i+1], ")") {
					numStr := strings.TrimSuffix(words[i+1], ")")
					num, err := strconv.Atoi(numStr)
			        if err == nil && num > 0 {
						start := len(clean) - num
						if start < 0 {
							start = 0
				        }
	                for j := start; j < len(clean); j++ {
						switch w {
							case "(up,":
								clean[j] = strings.ToUpper(clean[j])
							case "(low,":
								clean[j] = strings.ToLower(clean[j])
					        case "(cap,":
								clean[j] = capitalize(clean[j])
					    }
				    }
			    }
			    i++ 
		    }
		default:
			clean = append(clean, w)
	    }
    }
    return clean
}
func capitalize(s string) string {
	if s == "" {
		return s
	}
	return strings.ToUpper(s[:1]) + strings.ToLower(s[1:])
}
func Punctuation(words string) string {
	runes := []rune(words)
	var result []rune
	puncts := ".,!?:;"
	
	for i := 0; i < len(runes); i++ {
		r := runes[i]
		if strings.ContainsRune(puncts, r) {
			for len(result) > 0 && result[len(result)-1] == ' ' {
				result = result[:len(result)-1]
		    }
		    result = append(result, r)
			if i+1 < len(runes) {
				next := runes[i+1]
				if !strings.ContainsRune(puncts, next) && next != ' ' {
					result = append(result, ' ')
			    }
		    }
	    } else {
			result = append(result, r)
	    }
    }
    return strings.TrimSpace(string(result))
}
func formatQuotes(words string) string {
	runes := []rune(words)
	var result []rune
	
	openQuote := false 
	
	for i := 0; i < len(runes); i++ {
		char := runes[i]
		if char == '\'' {
			if !openQuote {
				result = append(result, char)
			    openQuote = true
			    for i+1 < len(runes) && runes[i+1] == ' ' {
					i++
			    } 
		    } else {
				for len(result) > 0 && result[len(result)-1] == ' ' {
					result = result[:len(result)-1]
			    }
				
				result = append(result, char)
				openQuote = false
		    }	
	    } else {
			result = append(result, char)
	    }
    }   
    return string(result)
}
func Articles(words []string) []string {
	for i := 0; i < len(words)-1; i++ {
		cWord := words[i]
		if cWord == "a" || cWord == "A" {
			nextWord := words[i+1]
			if len(nextWord) > 0 {
				runes := []rune(nextWord)
				firstChar := strings.ToLower(string(runes[0]))
				if strings.Contains("aeiouh", firstChar) {
					if cWord == "a" {
						words[i] = "an"
					} else {
						words[i] = "An"
					}
				}
			}
		}
	}
	return words
}
// package main

// import (
// 	// "fmt"     // used for printing to the terminal
// 	// "os"      // used for reading and writing files
// 	"strings" // used for string manipulation
// 	"strconv" // used for converting strings to numbers
// )

// // func main() {

// // 	// Read the content of sample.txt
// // 	data, err := os.ReadFile("sample.txt")
// // 	if err != nil {
// // 		fmt.Println("unable to read file", err)
// // 		return
// // 	}

// // 	// Convert the file data (bytes) into a string
// // 	sentence := string(data)

// // 	// Split the sentence into words using spaces
// // 	words := strings.Fields(sentence)

// // 	// Call different functions to process the words
// // 	words = handleHex(words)      // convert hexadecimal numbers
// // 	words = handleBin(words)      // convert binary numbers
// // 	words = ToUpper(words)        // apply (up) command
// // 	words = ToLower(words)        // apply (low) command
// // 	words = ToCapitalize(words)   // apply (cap) command

// // 	// Join the words back into one sentence
// // 	result := strings.Join(words, " ")

// // 	// Write the final result into result.txt
// // 	err = os.WriteFile("result.txt", []byte(result), 0644)
// // 	if err != nil {
// // 		fmt.Println("unable to write file", err)
// // 		return
// // 	}

// // 	// Print the result in the terminal
// // 	fmt.Println(result)
// // }

// /////////////////////////////////////////////////////////
// // This function handles the (hex) command
// // It converts the previous word from hexadecimal to decimal
// /////////////////////////////////////////////////////////

// func handleHex(words []string) []string {
// 	for i, text := range words {

// 		// Check if the current word is "(hex)"
// 		if text == "(hex)" && i > 0 {

// 			// Convert the previous word from base 16 (hex) to integer
// 			read, err := strconv.ParseInt(words[i-1], 16, 64)

// 			if err == nil {
// 				// Convert the number back to a normal base 10 string
// 				words[i-1] = strconv.FormatInt(read, 10)
// 			}

// 			// Remove "(hex)" by replacing it with an empty string
// 			words[i] = ""
// 		}
// 	}
// 	return words
// }

// /////////////////////////////////////////////////////////
// // This function handles the (bin) command
// // It converts the previous word from binary to decimal
// /////////////////////////////////////////////////////////

// func handleBin(words []string) []string {
// 	for i, text := range words {

// 		// Check if the current word is "(bin)"
// 		if text == "(bin)" && i > 0 {

// 			// Convert the previous word from base 2 (binary)
// 			read, err := strconv.ParseInt(words[i-1], 2, 64)

// 			if err == nil {
// 				// Convert it back to a base 10 string
// 				words[i-1] = strconv.FormatInt(read, 10)
// 			}

// 			// Remove "(bin)"
// 			words[i] = ""
// 		}
// 	}
// 	return words
// }

// /////////////////////////////////////////////////////////
// // This function handles the (up) command
// // It converts the previous word(s) to uppercase
// /////////////////////////////////////////////////////////

// func ToUpper(words []string) []string {
// 	for i, text := range words {

// 		// Check if the word starts with "(up"
// 		if strings.HasPrefix(text, "(up") {

// 			// Default number of words to change is 1
// 			n := 1

// 			// If there is a number like (up, 3)
// 			if strings.Contains(text, ",") {

// 				// Remove "(up," from the text
// 				numStr := strings.TrimPrefix(text, "(up,")

// 				// Remove the closing ")"
// 				numStr = strings.TrimSuffix(numStr, ")")

// 				// Remove extra spaces
// 				numStr = strings.TrimSpace(numStr)

// 				// Convert the number string into an integer
// 				n, _ = strconv.Atoi(numStr)
// 			}

// 			// Make sure there are enough words before the command
// 			if i >= n {

// 				// Convert the previous n words to uppercase
// 				for j := 1; j <= n; j++ {
// 					words[i-j] = strings.ToUpper(words[i-j])
// 				}
// 			}

// 			// Remove the "(up)" command
// 			words[i] = ""
// 		}
// 	}
// 	return words
// }

// /////////////////////////////////////////////////////////
// // This function handles the (low) command
// // It converts the previous word(s) to lowercase
// /////////////////////////////////////////////////////////

// func ToLower(words []string) []string {
// 	for i, text := range words {

// 		// Check if the word starts with "(low"
// 		if strings.HasPrefix(text, "(low") {

// 			// Default is 1 word
// 			n := 1

// 			// Check if there is a number like (low, 2)
// 			if strings.Contains(text, ",") {

// 				numStr := strings.TrimPrefix(text, "(low,")
// 				numStr = strings.TrimSuffix(numStr, ")")
// 				numStr = strings.TrimSpace(numStr)

// 				// Convert to integer
// 				n, _ = strconv.Atoi(numStr)
// 			}

// 			// Make sure enough words exist before the command
// 			if i >= n {

// 				// Convert previous n words to lowercase
// 				for k := 1; k <= n; k++ {
// 					words[i-k] = strings.ToLower(words[i-k])
// 				}
// 			}

// 			// Remove the "(low)" command
// 			words[i] = ""
// 		}
// 	}
// 	return words
// }

// /////////////////////////////////////////////////////////
// // This function handles the (cap) command
// // It capitalizes the first letter of the previous word(s)
// /////////////////////////////////////////////////////////

// func ToCapitalize(words []string) []string {
// 	for p, text := range words {

// 		// Check if the word starts with "(cap"
// 		if strings.HasPrefix(text, "(cap") {

// 			// Default is 1 word
// 			n := 1

// 			// Check if there is a number like (cap, 2)
// 			if strings.Contains(text, ",") {

// 				numStr := strings.TrimPrefix(text, "(cap,")
// 				numStr = strings.TrimSuffix(numStr, ")")
// 				numStr = strings.TrimSpace(numStr)

// 				// Convert string to integer
// 				n, _ = strconv.Atoi(numStr)
// 			}

// 			// Ensure enough words before the command
// 			if p >= n {

// 				// Capitalize the previous n words
// 				for l := 1; l <= n; l++ {
// 					words[p-l] = CapitalizeWord(words[p-l])
// 				}
// 			}

// 			// Remove the "(cap)" command
// 			words[p] = ""
// 		}
// 	}
// 	return words
// }

// /////////////////////////////////////////////////////////
// // Helper function
// // Capitalizes the first letter of a word
// /////////////////////////////////////////////////////////

// func CapitalizeWord(s string) string {

// 	// Convert first letter to uppercase
// 	// Convert the rest of the word to lowercase
// 	return strings.ToUpper(s[:1]) + strings.ToLower(s[1:])
// }