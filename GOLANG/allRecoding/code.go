// ==========================================================GO-RELOADED-RECODING test================================================
// package main

// import (
// 	"fmt"
// 	"regexp"
// 	"strconv"
// 	"strings"
// )

// // Q5 - isPunctuation
// func isPunctuation(s string) bool {
// 	punctuations := []string{".", ",", "!", "?", ":", ";"}
// 	for _, p := range punctuations {
// 		if s == p {
// 			return true
// 		}
// 	}
// 	return false
// }

// // Q1 - joinWithPunctuation
// // Requirement: use 'result' for the output string and loop with 'i, token'
// func joinWithPunctuation(tokens []string) string {
// 	result := ""
// 	for i, token := range tokens {
// 		if isPunctuation(token) {
// 			// remove trailing space before punctuation
// 			if len(result) > 0 && result[len(result)-1] == ' ' {
// 				result = result[:len(result)-1]
// 			}
// 			result += token
// 			// add a space after punctuation if next token exists and isn't punctuation
// 			if i+1 < len(tokens) && !isPunctuation(tokens[i+1]) {
// 				result += " "
// 			}
// 		} else {
// 			result += token
// 			// add a space between words unless next token is punctuation
// 			if i+1 < len(tokens) && !isPunctuation(tokens[i+1]) {
// 				result += " "
// 			}
// 		}
// 	}
// 	return result
// }

// // Q2 - binToDecimal
// // Requirement: use variable names 'result' and 'err'
// func binToDecimal(binStr string) (int64, error) {
// 	result, err := strconv.ParseInt(binStr, 2, 64)
// 	if err != nil {
// 		return 0, err
// 	}
// 	return result, nil
// }

// // Q3 - hexToDecimal
// // Requirement: use variable names 'result' and 'err'
// // We'll use strconv.ParseInt(hexStr, 16, 64) and explain base/bitSize below.
// func hexToDecimal(hexStr string) (int64, error) {
// 	result, err := strconv.ParseInt(hexStr, 16, 64)
// 	if err != nil {
// 		return 0, err
// 	}
// 	return result, nil
// }

// // Q6 - fixSingleQuotes
// // Requirement: declare variables 'result', 'match', and 'inner'
// func fixSingleQuotes(text string) string {
// 	result := text
// 	re := regexp.MustCompile(`'([^']*)'`)
// 	for _, match := range re.FindAllStringSubmatch(result, -1) {
// 		inner := match[1]
// 		inner = strings.TrimSpace(inner)
// 		result = strings.Replace(result, match[0], "'"+inner+"'", 1)
// 	}
// 	return result
// }

// // Q7 - uppercaseLastN
// // Requirement: use variable 'start' for starting index
// func uppercaseLastN(words []string, n int) []string {
// 	if n <= 0 {
// 		return words
// 	}
// 	if n > len(words) {
// 		n = len(words)
// 	}
// 	start := len(words) - n
// 	for i := start; i < len(words); i++ {
// 		words[i] = strings.ToUpper(words[i])
// 	}
// 	return words
// }

// // Q8 - aOrAn
// // Requirement: use variables 'firstLetter', 'vowelsAndH' and loop using 'v'
// func aOrAn(nextWord string) string {
// 	if nextWord == "" {
// 		return "a"
// 	}
// 	runes := []rune(nextWord)
// 	firstLetter := strings.ToLower(string(runes[0]))
// 	vowelsAndH := "aeiouh"
// 	for _, v := range vowelsAndH {
// 		if string(v) == firstLetter {
// 			return "an"
// 		}
// 	}
// 	return "a"
// }

// func <--main-->() {
// 	// Q1
// 	tokens := []string{"hello", ",", "world", "!"}
// 	fmt.Printf("joinWithPunctuation(%q) -> %q\n", tokens, joinWithPunctuation(tokens))

// 	// Q2
// 	res, err := binToDecimal("10")
// 	fmt.Printf("binToDecimal(\"10\") -> %v, %v\n", res, err)
// 	res, err = binToDecimal("11111111")
// 	fmt.Printf("binToDecimal(\"11111111\") -> %v, %v\n", res, err)

// 	// Q3
// 	res, err = hexToDecimal("1E")
// 	fmt.Printf("hexToDecimal(\"1E\") -> %v, %v\n", res, err)
// 	res, err = hexToDecimal("FF")
// 	fmt.Printf("hexToDecimal(\"FF\") -> %v, %v\n", res, err)

// 	// Q6
// 	fmt.Printf("fixSingleQuotes(\"' awesome '\") -> %q\n", fixSingleQuotes("' awesome '"))
// 	fmt.Printf("fixSingleQuotes(\"' hello world '\") -> %q\n", fixSingleQuotes("' hello world '"))

// 	// Q7
// 	words := []string{"this", "is", "so", "exciting"}
// 	fmt.Printf("uppercaseLastN(%q, 2) -> %q\n", words, uppercaseLastN(words, 2))

// 	// Q8
// 	fmt.Printf("aOrAn(\"apple\") -> %q\n", aOrAn("apple"))
// 	fmt.Printf("aOrAn(\"horse\") -> %q\n", aOrAn("horse"))
// 	fmt.Printf("aOrAn(\"book\") -> %q\n", aOrAn("book"))
// 	fmt.Printf("aOrAn(\"honest\") -> %q\n", aOrAn("honest"))
// }
// =====================================================================ASCII-ART-RECODING test==============================================================
//  Q1 - Read a file and return its content as a string
// package main

// import (
// 	"fmt"
// 	"os"
// )

// func readFile(filename string) string {
// 	data, err := os.ReadFile(filename)
// 	if err != nil {
// 		fmt.Println("Error reading file:", err)
// 		return ""
// 	}
// 	return string(data)
// }

// func main() {
// 	content := readFile("test.txt")
// 	fmt.Printf("readFile(\"test.txt\") -> %q\n", content)
// }
// // Q2 - Split a string by newlines (handle both \n and \r\n)

// package main

// import (
// 	"fmt"
// 	"strings"
// )

// func splitLines(text string) []string {
// 	normalized := strings.ReplaceAll(text, "\r\n", "\n")
// 	return strings.Split(normalized, "\n")
// }

// func main() {
// 	lines := splitLines("line1\nline2\nline3")
// 	fmt.Printf("splitLines(...) -> %q\n", lines)
// }
// // Q3 - Parse FIGlet font header (extract hardblank and height)
// package main

// import (
// 	"fmt"
// 	"strconv"
// 	"strings"
// )

// func parseFontHeader(header string) (hardblank byte, height int) {
// 	tokens := strings.Fields(header)
// 	hardblank = ' '
// 	height = 8
// 	if len(tokens) > 0 {
// 		first := tokens[0]
// 		if len(first) > 0 {
// 			hardblank = first[len(first)-1]
// 		}
// 	}
// 	if len(tokens) > 1 {
// 		h, err := strconv.Atoi(tokens[1])
// 		if err == nil {
// 			height = h
// 		}
// 	}
// 	return hardblank, height
// }

// func main() {
// 	hb, h := parseFontHeader("flf2a$ 8 6 15 -1 2")
// 	fmt.Printf("parseFontHeader(...) -> hardblank='%c', height=%d\n", hb, h)
// }
// // Q4 - Explain what a "glyph" is

// // text

// // A **glyph** is the visual representation of a single character in ASCII art.
// // In a FIGlet font file, each glyph consists of multiple lines (rows) that form
// // the character's shape. We use a map `map[rune][]string` to store glyphs because
// // each character (rune) maps to an array of strings (one string per row of the glyph).

// // Q5 - Extract a single glyph from font file lines

// package main

// import (
// 	"fmt"
// )

// func extractGlyph(lines []string, char rune, height int) []string {
// 	glyph := make([]string, height)
// 	base := int(char-32) * height

// 	for i := 0; i < height; i++ {
// 		index := base + i
// 		if index >= 0 && index < len(lines) {
// 			line := lines[index]
// 			glyph[i] = line
// 		} else {
// 			glyph[i] = ""
// 		}
// 	}

// 	return glyph
// }

// func main() {
// 	lines := []string{"   ", "   ", "   ", " _ ", "| |", "|_|"}
// 	glyph := extractGlyph(lines, '!', 3)
// 	fmt.Printf("extractGlyph(..., '!', 3) -> %q\n", glyph)
// }

// // Q6 - Remove end-marker character from FIGlet font lines

// package main

// import (
// 	"fmt"
// )

// func removeEndMarker(line string) string {
// 	var cleaned string
// 	if len(line) > 0 {
// 		cleaned = line[:len(line)-1]
// 	} else {
// 		cleaned = ""
// 	}
// 	return cleaned
// }

// func main() {
// 	fmt.Printf("removeEndMarker(\"  ##  @\") -> %q\n", removeEndMarker("  ##  @"))
// 	fmt.Printf("removeEndMarker(\"\") -> %q\n", removeEndMarker(""))
// }

// // Q7 - Replace hardblank character with space

// package main

// import (
// 	"fmt"
// 	"strings"
// )

// func replaceHardblank(line string, hardblank byte) string {
// 	result := strings.ReplaceAll(line, string(hardblank), " ")
// 	return result
// }

// func main() {
// 	fmt.Printf("replaceHardblank(\"##$##\", '$') -> %q\n", replaceHardblank("##$##", '$'))
// }

// // Q8 - Render a single row of text using glyph map

// package main

// import (
// 	"fmt"
// )

// func renderRow(glyphs map[rune][]string, word string, row int) string {
// 	result := ""
// 	for _, ch := range word {
// 		glyph, ok := glyphs[ch]
// 		if !ok {
// 			// fallback to space glyph
// 			glyph = glyphs[' ']
// 		}
// 		if row >= 0 && row < len(glyph) {
// 			result += glyph[row]
// 		}
// 	}
// 	return result
// }
// func main() {
// 	glyphs := map[rune][]string{
// 		'H': {" _ ", "| |", "|_|"},
// 		'i': {" ", "|", "|"},
// 		' ': {"   ", "   ", "   "},
// 	}
// 	fmt.Printf("renderRow(..., \"Hi\", 0) -> %q\n", renderRow(glyphs, "Hi", 0))
// 	fmt.Printf("renderRow(..., \"Hi\", 1) -> %q\n", renderRow(glyphs, "Hi", 1))
// 	fmt.Printf("renderRow(..., \"Hi\", 2) -> %q\n", renderRow(glyphs, "Hi", 2))
// }
// package main

// import (
// 	"fmt"
// 	"os"
// 	"strings"
// )

// // Example 1 - Input: "test.txt" (contains "hello") -> Expected Output: "hello"
// // Example 2 - Input: "missing.txt" (doesn't exist) -> Expected Output: ""
// func readFile(filename string) string {
// 	// your code here
// }

// // Example 1 - Input: "line1\nline2\nline3" -> Expected Output: ["line1", "line2", "line3"]
// // Example 2 - Input: "a\r\nb\r\nc" -> Expected Output: ["a", "b", "c"]
// func splitLines(text string) []string {
// 	// your code here
// }

// // Example - Input: "flf2a$ 8 6 15 -1 2" 
// // Expected Output: hardblank='$', height=8
// func parseFontHeader(header string) (hardblank byte, height int) {
// 	// your code here
// }



// Example - Given height=3 and font lines for space(32) then '!'(33):
// lines = ["   ", "   ", "   ", " _ ", "| |", "|_|"]
// extractGlyph(lines, '!', 3) should return [" _ ", "| |", "|_|"]
// func extractGlyph(lines []string, char rune, height int) []string {
// 		// your code here
// }


// // Example 1 - Input: "  ##  @" -> Expected Output: "  ##  "
// // Example 2 - Input: "#####@" -> Expected Output: "#####"
// // Example 3 - Input: "" -> Expected Output: ""
// func removeEndMarker(line string) string {
// 	// your code here
// }

// // Example 1 - Input: line="##$##", hardblank='$' -> Expected Output: "## ##"
// // Example 2 - Input: line="test", hardblank='$' -> Expected Output: "test"
// func replaceHardblank(line string, hardblank byte) string {
// 	// your code here
// }

// // Example - 
// // glyphs = map[rune][]string{
// //   'H': {" _ ", "| |", "|_|"},
// //   'i': {" ", "|", "|"},
// // }
// // renderRow(glyphs, "Hi", 0) -> " _  "
// // renderRow(glyphs, "Hi", 1) -> "| ||"
// // renderRow(glyphs, "Hi", 2) -> "|_||"
// func renderRow(glyphs map[rune][]string, word string, row int) string {
// 	// your code here
// }


// ====================================================ASCII-ART-WEB-RECODING================================================

package main

import (
	// "errors"
	"fmt"
	// "html/template"
	"net/http"
	// "strings"
)

// //--------------------------------InPUT TEXT CHARACTER VALIDATOR------------------------------------------------
// func validateinput(input string) bool {
// 	for _, r := range input {
// 		if r < 31 || r > 126 && (r != '\n' || r != '\t' || r != '\r') {
// 			return false
// 		}
// 	}
// 	return true
// }
// func mAin() {
// 	fmt.Println(validateinput("Helllo, world123"))
// }

// //----------------------------FORM INPUT EXTRACTION---------------------------------------
// func extractField(formValue map[string][]string, key string) string {
// 	value, ok := formValue[key]

// 	if ok {
// 		return value[0]
// 	}
// 	return ""
// }

// func MAin() {
// 	vals:= map[string][]string{"text": {"hello"}, "banner":{"standard"}}
// 	fmt.Println(extractField(vals, "text"))
// }

// // ---------------------------------HTTP METHOD CHECK-----------------------------------------------

func checkMethod(method string) (int,string) {
	if method == http.MethodGet {
		return http.StatusOK, "OK"
	} else if method == http.MethodPost {
		return http.StatusMethodNotAllowed, "Method Not Allowed"
	} else {
		return http.StatusBadRequest, "Bad Request"
	}
}

func main() {
	status, msg := checkMethod("PUT")
	fmt.Printf("%d: %s\n", status, msg)
}
// -------------------------HTTP STATUS CODE DETERMINER------------------------------------------------

// func determineStatus(err error, templateOrBnnerMissing bool, pathFound bool) int {

// 	newerror := errors.New("Invalid Input")

// 	if err == newerror {
// 		return 400
// 	} else if templateOrBnnerMissing == true{
// 		return 404
// 	} else if pathFound == false {
// 		return 404
// 	} else {
// 		return 200
// 	}
// }

// func main() {
// 	fmt.Println(determineStatus(nil, false, true))
// }
// // ---------------------------------------------------------------------------------
// func renderResult(w http.ResponseWriter, tmplcontent string, data string) error {
// 	tmpl, err := template.New("Index").Parse(tmplcontent)
// 	if err != nil {
// 		return err
// 	}

// 	err = tmpl.Execute(w, data)
// 	if err != nil {
// 		return err
// 	}
// 	return nil
// }
// // -------------------------------------------------------------------------------

// func routePath(path string, method string) (int, string) {
// 	if path == "/" && method == http.MethodGet {
// 		return http.StatusOK, "Home"
// 	}
// 	if path == "/ascii-art" && method == http.MethodPost {
// 		return http.StatusOK, "Render"
// 	}
// 	if path != "/ascii-art" && method != http.MethodPost {
// 		return http.StatusMethodNotAllowed, "Method Not Allowed"
// 	}
// 	return http.StatusBadRequest, "Not found"
// }

// // --------------------------------------------------------------------------------

// func isValidTemplate(filename string) bool {
// 	lowFileName := strings.ToLower(filename)
// 	return strings.HasSuffix(lowFileName, ".html") || strings.HasSuffix(lowFileName, ".tmpl")
// }

// // --------------------------------------------------------------------------
// func buildArtHTML(artText string, banner string) (string, int) {
// 	if artText == "" {
// 		return "", http.StatusBadRequest
// 	}
// 	htmlString := fmt.Sprintf("<html><body><prev>%s</prev><p>Banner: %s</p></body></html>", artText, banner)
// 	return htmlString, http.StatusOK
// }

// func logRequest(r *http.Request) string {
// 	if r.URL.RawQuery != "" {
// 		return fmt.Sprintf("[%s] %s?%s", r.Method, r.URL.Path, r.URL.RawQuery)
// 	}
// 	return fmt.Sprintf("[%s] %s, r.Method, r.URL.Path")
// }
