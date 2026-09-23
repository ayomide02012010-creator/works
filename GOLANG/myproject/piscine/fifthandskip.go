package piscine

import "strings"

func FifthAndSkip(str string) string {
	if str == "" || len(str) < 5 {
		return "Invalid Input\n"
	}
	s := strings.ReplaceAll(str, " ", "")
	var b strings.Builder
	for i, char := range s {
		if i%5 == 0 && i != 0 {
			b.WriteRune(' ')
		}
		b.WriteRune(char)
	}
	b.WriteRune('\n')
	return b.String()
}
