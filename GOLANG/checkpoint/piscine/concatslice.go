package piscine

func ConcatSlice(slice1, slice2 []int) []int {
	result := make([]int, 0, len(slice1)+len(slice2))
	result = append(result, slice1...)
	result = append(result, slice2...)
	return result
}