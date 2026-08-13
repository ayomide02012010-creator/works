// package main
// import (
// 	"fmt"
// 	"math"
// )

// func main() {

// 	// arr := [5]int{1,2,3,4,5}
// 	// arr3 := [3]string{"mentor","coding","tech"}
// 	// arr4 := [8]rune{'a','d','r','f','w','r','d','y'}

// 	// slice1 := []int{1,2,3}
//     // slice5 := []string{"code","python"}
// 	// slice6 := []rune{'h','j','k','l','i'}
// 	// slice4 := []byte{23,45,87}
// 	// // arr4 := rune('d')
// 	// s := string(arr4[6])

// 	// string "alli"
// 	// rune 'a'

// 	// var name string 
// 	// name = "alli"
//     // var language bool 
//     // var number rune
// 	// number = 'A'

// 	// string(dataType)  
// 	// rune()
// 	// town := "GRA" 
//     // age := 89
// 	// make := byte(65)
// 	// var school byte = (45)'z''z''z''z'
    
	
// 	// var number  = string('z')
//    // c := number(byte)

// 	// fmt.Println(arr[4])
// 	// fmt.Println(arr3)
//     // fmt.Println(len(arr3[1]))
// 	// fmt.Println(s)
// 	// fmt.Println(slice1)
// 	// fmt.Println(slice4)
// 	// fmt.Println(slice5)
//     // fmt.Println(slice6)
// 	//  fmt.Println(number)
// 	//  fmt.Printf("%T\n", town)


// 	// name := "q"
// 	// language := "python"
// 	// fmt.Println(name)
// 	// fmt.Println(len(name)) 
// 	// fmt.Println([]rune(name))

// 	// fmt.Println(language)
// 	// fmt.Println(len(language))
// 	// fmt.Println([]byte(language))


// 	g := "python"
// 	runes := []rune(g)
// 	runes[5] = 't'
// 	g = string(runes)
	
// 	fmt.Println(g)
// // 	func RoundToEven(x float64) float64 {
// // 	// RoundToEven is a faster implementation of:
// // 	//
// // 	// func RoundToEven(x float64) float64 {
// // 	//   t := math.Trunc(x)
// // 	//   odd := math.Remainder(t, 2) != 0
// //   if d := math.Abs(x - t); d > 0.5 || (d == 0.5 && odd) {                       func Abs(x float64) float64 {
// // 	return Float64frombits(Float64bits(x) &^ (1 << 63))
// // }

// // 	//     return t + math.Copysign(1, x)
// // 	//   }
// // 	//   return t
// // 	// }
// // 	bits := Float64bits(x)
// // 	e := uint(bits>>shift) & mask
// // 	if e >= bias {
// // 		// Round abs(x) >= 1.
// // 		// - Large numbers without fractional components, infinity, and NaN are unchanged.
// // 		// - Add 0.499.. or 0.5 before truncating depending on whether the truncated
// // 		//   number is even or odd (respectively).
// // 		const halfMinusULP = (1 << (shift - 1)) - 1
// // 		e -= bias
// // 		bits += (halfMinusULP + (bits>>(shift-e))&1) >> e
// // 		bits &^= fracMask >> e
// // 	} else if e == bias-1 && bits&fracMask != 0 {
// // 		// Round 0.5 < abs(x) < 1.
// // 		bits = bits&signMask | uvone // +-1
// // 	} else {
// // 		// Round abs(x) <= 0.5 including denormals.
// // 		bits &= signMask // +-0
// // 	}
// // 	return Float64frombits(bits)
// // }
// 	u := math.RoundToEven(11.9)
// 	fmt.Printf("%.1f\n", u)

// 	d := math.RoundToEven(-13.6)
// 	fmt.Printf("%.1f\n", d)


// } 
package main

import (
	"fmt"
	"strings"
)

func main() {
	number := 1

	// for number <= 500{
		fmt.Println(strings.Repeat("*", number))
		number++
	}
}