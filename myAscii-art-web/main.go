package main

import (
	"fmt"

	"html/template"
	"net/http"
	"os"
	"strings"
)

func main() {
	h := http.NewServeMux()
	h.HandleFunc("/", homeHandler)
	h.HandleFunc("/ascii-art", asciiArtHandler)

	fmt.Println("Server running at: http://localhost:8080")

	http.ListenAndServe(":8080", h)
}
func homeHandler(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path != "/" {
        http.Error(w, "404 Not Found", http.StatusNotFound)
        return
    }
    if r.Method != http.MethodGet {
        http.Error(w, "405 Method Not Allowed", http.StatusMethodNotAllowed)
        return
    }
    p, err := template.ParseFiles("template/index.html")
    if err != nil {
        http.Error(w, "500 Internal Server Error", http.StatusInternalServerError)
        return
    }
    p.Execute(w, nil)
}
func asciiArtHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "405 Method Not Allowed", http.StatusMethodNotAllowed)
		return
	}

	str := r.FormValue("text") 
	ba := r.FormValue("banner")

	if str == "" {
		http.Error(w, "400 Bad Request: Enter text", http.StatusBadRequest)
		return
	}

	p, err := template.ParseFiles("template/index.html")
	if err != nil {
		http.Error(w, "500 Internal Server Error", http.StatusInternalServerError)
		return
	}
	
	if ba != "standard" && ba != "shadow" && ba != "thinkertoy" && ba != "" {
		http.Error(w, "400 Bad Request: Invalid banner type", http.StatusBadRequest)
		return
	}

	out, err := GenerateArt(str, ba)
	if err != nil {
		http.Error(w, "500 Internal Server Error", http.StatusInternalServerError)
		return
	}
	p.Execute(w, out)
}
func GenerateArt(text, banner string) (string, error) {
	if banner == "" {
		banner = "standard"
	}
	if !strings.HasSuffix(banner, ".txt") {
		banner += ".txt"
	}
	data, err := os.ReadFile("banners/" + banner)
	if err != nil {
		return "", err
	}
	input := strings.Split(strings.ReplaceAll(string(data), "\r\n", "\n"), "\n")
	if len(input) > 0 && input[0] == "" {
		input = input[1:]
	}
	text = strings.ReplaceAll(text, `\n`, "\n")
	if text == "" {
		return "", nil
	}
	lines := strings.Split(text, "\n")

	allEmpty := true
	for _, l := range lines {
		if l != "" {
			allEmpty = false
			break
		}
	}
	if allEmpty {
		return strings.Repeat("\n", len(lines)-1), nil
	}
	var out string
	for _, line := range lines {
		if line == "" {
			out += "\n"
			continue
		}
		for r := range 8 {
			for _, char := range line {
				if char < 32 || char > 126 {
					continue
				}
				index := (int(char) - 32) * 9
				out += input[index+r]
			}
			out += "\n"
		}
	}
	return out, nil
}
