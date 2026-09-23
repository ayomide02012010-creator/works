// package main
// import (
// 	"fmt"
// 	"myproject/piscine"
// )

// func main() {
// 	fmt.Println(piscine.CamelToSnakeCase("HelloWorld"))
// 	fmt.Println(piscine.CamelToSnakeCase("helloWorld"))
// 	fmt.Println(piscine.CamelToSnakeCase("camelCase"))
// 	fmt.Println(piscine.CamelToSnakeCase("CAMELtoSnackCASE"))
// 	fmt.Println(piscine.CamelToSnakeCase("camelToSnakeCase"))
// 	fmt.Println(piscine.CamelToSnakeCase("camelCase"))
// 	fmt.Println(piscine.CamelToSnakeCase("hey2"))
// }
// func prime() {
	
// }
// func FindPrevPrime(nb int) int {
// 	if nb <= 1 {
// 		return  0
// 	}

// 	if nb == 2 {
// 		return 0
// 	}

// }
// package main

// import "fmt"

// type User struct {
//     Name   string
//     Email  string
//     Active bool
// }

// func NewUser(name, email string) User {
//     return User{Name: name, Email: email, Active: true}
// }

// func (u *User) Deactivate() {
//     u.Active = false
// }

// func (u User) Display() string {
//     status := "inactive"
//     if u.Active {
//         status = "active"
//     }
//     return fmt.Sprintf("%s <%s> (%s)", u.Name, u.Email, status)
// }

// func main() {
//     u := NewUser("Ada", "ada@example.com")
//     fmt.Println(u.Display())
// }
