// // package main

// // import (
// // 	"fmt"

// // )

// // func main() {
// // 	// string
// // 	var nameOne  string = "mario"
// // 	var nameTwo = "yusuf"
// // 	var nameTHree string

// // 	fmt.Println(nameOne, nameTwo, nameTHree)
// // 	nameOne = "peach"
// // 	nameTHree = "ali"

// // 	fmt.Println(nameOne, nameTwo, nameTHree)

// // 	nameFour :=  "yoshi"

// // 	fmt.Println(nameFour)

// // 	// int

// // 	var ageOne int = 20
// // 	var ageTwo = 400
// // 	ageThree := 70

// // 	fmt.Println(ageOne, ageTwo, ageThree)

// // 	// bit & memory
// // 	var numOne int8 = 123

// // 	fmt.Println(numOne)

// // }
// package main

// import "fmt"

// func main() {
// 	x := 10;

// 	changeValue(&x)
// 	fmt.Println(x)

// }

// func changeValue(x *int) {
// 	*x = 7;

// }
package main

import (
	"os"
	"fmt"
	"net/http"
)

// func hello(w http.ResponseWriter, r *http.Request) {
// 	fmt.Fprint(w, "Hello from Go!")
// }

// func main() {
// 	EvenNum := [5]int{0,2,4,6,8}
// 	for i, value := range EvenNum {
// 		fmt.Println(value, i)
// 	}

// 	numSlice := []int{5,4,3,2,1}

// 	sliced := numSlice[2:3]
// 	fmt.Println(sliced)

// 	slice2 := make([]int, 5, 10)
// 	fmt.Println(slice2)

// 	copy(numSlice, slice2)

// 	fmt.Println(numSlice)
// 	// Serve index.html
// 	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
// 		http.ServeFile(w, r, "index.html")
// 	})

// 	// Serve sandbox.js
// 	http.HandleFunc("/sandbox.js", func(w http.ResponseWriter, r *http.Request) {
// 		http.ServeFile(w, r, "sandbox.js")
// 	})

// 	// API endpoint
// 	http.HandleFunc("/api/hello", hello)

// 	fmt.Println("Server running at http://localhost:8080")
// 	http.ListenAndServe(":8080", nil)

// }

//	func main () {
//		http.HandleFunc("/hello", helloHandleFunc)
//		http.ListenAndServe(":8080", nil)
//	}
//
//	func helloHandleFunc(w http.ResponseWriter, r *http.Request) {
//		fmt.Fprint(w, "Hello, world")
//	}
func main() {
	startServer()
}
func startServer() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	http.HandleFunc("/", handleHome)
	http.HandleFunc("/ascii-art", handleASCIIArt)
	http.HandleFunc("/ascii-art-web", handleASCIIArtWeb)

	
	fmt.Printf("🚀 ASCII Command Station running on http://localhost:%s\n", port)
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		fmt.Printf("Error starting server: %v\n", err)
		os.Exit(1)
	}
// 	conn, err := net.Dial("tcp", "golang.org:80")
// if err != nil {
// 	// handle error
// 	fmt.Println("Error connecting:", err)
// 	return
// 	}
	
// 	fmt.Fprintf(conn, "GET / HTTP/1.0\r\n\r\n")
// 	status, err := bufio.NewReader(conn).ReadString('\n')
// 	if err != nil {
// 		fmt.Println("Error reading response:", err)
// 		return
// 	}
	
	// fmt.Println("Response sTatus:", status)
}
func handleHome(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Home Handler called", r.URL.Path, r.Method)
	fmt.Fprintln(w, "Welcome to my Go web server!")
}

func handleASCIIArt(w http.ResponseWriter, r *http.Request) {
	fmt.Println("ASCII handler called", r.URL.Path, r.Method)
	fmt.Fprintln(w, "ASCII Art Endpoint")
}

func handleASCIIArtWeb(w http.ResponseWriter, r *http.Request) {
	fmt.Println("ASCII Web handler called", r.URL.Path, r.Method)
	fmt.Fprintln(w, "ASCII Art Web Endpoint")
}
