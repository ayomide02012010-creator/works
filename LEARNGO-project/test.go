// // package main
// // import ("fmt")

// // type Person struct {
// //   name string
// //   age int
// //   job string
// //   salary int
// // }

// // func main() {
// //   var pers1 Person
// //   var pers2 Person

// //   // Pers1 specification
// //   pers1.name = "Hege"
// //   pers1.age = 45
// //   pers1.job = "Teacher"
// //   pers1.salary = 6000

// //   // Pers2 specification
// //   pers2.name = "Cecilie"
// //   pers2.age = 24
// //   pers2.job = "Marketing"
// //   pers2.salary = 4500

// //   // Print Pers1 info by calling a function
// //   printPerson(pers1)

// //   // Print Pers2 info by calling a function
// //   printPerson(pers2)
// // }

// //	func printPerson(pers Person) {
// //	  fmt.Println("Name: ", pers.name)
// //	  fmt.Println("Age: ", pers.age)
// //	  fmt.Println("Job: ", pers.job)
// //	  fmt.Println("Salary: ", pers.salary)
// //	}func main() {
// 	var b strings.Builder
// 	for i := 89; i >= 80; i-- {
// 		fmt.Fprintf(&b, "%d...", i)
// 	}
// 	b.Write([]byte{32,32, 57, 32,32, 99})
// 	fmt.Println(b.String())

 

// } 
// Copyright 2017 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// package main

// import (
	
// 	"unsafe"
	
	
	
// )

// type Builder struct {
// 	addr *Builder 
// 	buf []byte
// }



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

package main

import "fmt"

func printValue(v ...any) {
	fmt.Println(v)
}

func maIIn() {
	printValue(10, "s")
	printValue("Ali", 'p')
	printValue(true, false)

	type Person struct {
		Name string
	}

	printValue(Person{  "John"})

	printValue([9]int{1, 3:30, 8:7})
}