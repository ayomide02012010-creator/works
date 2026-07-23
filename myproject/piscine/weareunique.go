package piscine

func WeAreUnique(str1, str2 string) int {
	if str1 == "" && str2 == "" {
		return -1
	}

	inStr1 := make(map[rune]bool)
	inStr2 := make(map[rune]bool)

	for _, r := range str1 {
		inStr1[r] = true
	}

	for _, r := range str2 {
		inStr2[r] = true
	}

	count := 0
	for r := range inStr1 {
		if !inStr2[r] {
			count++
		}
	}

	for r := range inStr2 {
		if !inStr1[r] {
			count++
		}
	}
	return count
}
