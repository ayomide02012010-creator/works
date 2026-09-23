package main

import "fmt"
func ConcatAlternate(slice1, slice2 []int) []int {
    var result []int
    i, j := 0, 0
    len1, len2 := len(slice1), len(slice2)
    for i < len1 || j < len2 {
        if len1 >= len2 {
            if i < len1 {
                result = append(result, slice1[i])
                i++
            }
            if j < len2 {
                result = append(result, slice2[j])
                j++
            }
        } else {
            if j < len2 {
                result = append(result, slice2[j])
                j++
            }
            if i < len1 {
                result = append(result, slice1[i])
                i++
            }
        }
    }
    return result
}

func main() {
    fmt.Println(ConcatAlternate([]int{1, 2, 3}, []int{4, 5, 6}))  // [1 4 2 5 3 6]
    fmt.Println(ConcatAlternate([]int{2, 4, 6, 8, 10}, []int{1, 3, 5, 7, 9, 11}))  // [2 1 4 3 6 5 8 7 10 9 11]
    fmt.Println(ConcatAlternate([]int{1, 2, 3}, []int{4, 5, 6, 7, 8, 9}))  // [4 1 5 2 6 3 7 8 9]
    fmt.Println(ConcatAlternate([]int{1, 2, 3}, []int{}))  // [1 2 3]
}
