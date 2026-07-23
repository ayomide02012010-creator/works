package main
// import ("fmt")

type Person struct {
  name string
  age int
  job string
  salary int
}

// func mainN() {
//   var pers1 Person
//   var pers2 Person

//   // Pers1 specification
//   pers1.name = "Hege"
//   pers1.age = 45
//   pers1.job = "Teacher"
//   pers1.salary = 6000

//   // Pers2 specification
//   pers2.name = "Cecilie"
//   pers2.age = 24
//   pers2.job = "Marketing"
//   pers2.salary = 4500

//   // Print Pers1 info by calling a function
//   printPerson(pers1)

//   // Print Pers2 info by calling a function
//   printPerson(pers2)
// }

// 	func printPerson(pers Person) {
// 	  fmt.Println("Name: ", pers.name)
// 	  fmt.Println("Age: ", pers.age)
// 	  fmt.Println("Job: ", pers.job)
// 	  fmt.Println("Salary: ", pers.salary)
// 	}
//   func mAAin() {
// 	var b strings.Builder
// 	for i := 89; i >= 80; i-- {
// 		fmt.Fprintf(&b, "%d...", i)
// 	}
// 	b.Write([]byte{32,32, 57, 32,32, 99})
// 	fmt.Println(b.String())

 

// } 

// // import (
// // 	"unsafe"	
// // )

// // type Builder struct {
// // 	addr *Builder 
// // 	buf []byte
// // }



// func (b *Builder) String() string {
// 	return unsafe.String(unsafe.SliceData(b.buf), len(b.buf))
// }

// func (b *Builder) Len() int {
//   return len(b.buf)
// }

// func (b *Builder) Cap() int {
//   return cap(b.buf)
// }

// func (b *Builder) Reset() {
// 	b.addr = nil
// 	b.buf = nil
// }
// func Printf(format string, a ...any)
// // package main

// // import (
// // 	"fmt"
// // )

// func maiN() {

// 		var bill float64
// 		var people float64
// 		var tip float64
// 		fmt.Println("What was the total bill? ")
// 		fmt.Scan(&bill)
// 		fmt.Println("How much tip would you like to give? 10, 12, or 15? ")
// 		fmt.Scan(&tip)
// 		fmt.Println("How many people to split the bill? ")
// 		fmt.Scan(&people)

// 		actualTip := (tip/100) * bill
// 		totalBill := actualTip + bill
// 		eachPays := totalBill/people

// 		fmt.Printf("Each person should pay: %.2f", eachPays)
// }
// func MaIn() {
//     const sample = "\xbd\xb2\x3d\xbc\x20\xe2\x8c\x98"

//     fmt.Println("Println:")
//     fmt.Println(sample)

//     fmt.Println("Byte loop:")
//     for i := 0; i < len(sample); i++ {
//         fmt.Printf("%x ", sample[i])
//     }
//     fmt.Printf("\n")

//     fmt.Printf("Printf with %x:", sample)
//     fmt.Printf("%x\n", sample)

//     fmt.Println("Printf with % x:")
//     fmt.Printf("% x\n", sample)

//     fmt.Printf("Printf with %q:", sample)
//     fmt.Printf("%q\n", sample)

//     fmt.Printf("Printf with %+q:", sample)
//     fmt.Printf("%+q\n", sample)
// }
