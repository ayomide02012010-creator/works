package piscine

func RepeatAlpha(s string) string {
	var result []rune
	for _, c := range s {
		repeat := 1
		if c >= 'a' && c <= 'z' {
			repeat = int(c-'a') + 1
		} else if c >= 'A' && c <= 'Z' {
			repeat = int(c-'A') + 1
		}
		for i := 0; i < repeat; i++ {
			result = append(result, c)
		}
	}
	return string(result)
}
