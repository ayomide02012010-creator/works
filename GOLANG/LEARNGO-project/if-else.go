package main 

import (
	"net/http"
	"fmt"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Hello World")
}
func maIn() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}