package piscine

func RevConcatAlternate(slice1, slice2 []int) []int {
	var result []int
	len1 := len(slice1)
	len2 := len(slice2)

	if len1 > len2 {
		for i := len1 - 1; i >= 0; i-- {
			result = append(result, slice1[i])
			if i < len2 {
				result = append(result, slice2[len2-1-i])
			}
		}
	} else if len2 > len1 {
		for i := len2 - 1; i >= 0; i-- {
			result = append(result, slice2[i])
			if i < len1 {
				result = append(result, slice1[len1-1-i])
			}
		}
	} else {
		for i := len1 - 1; i >= 0; i-- {
			result = append(result, slice1[i])
			result = append(result, slice2[i])
		}
	}
	return result
}