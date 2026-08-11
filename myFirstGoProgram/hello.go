package main
import "fmt"
func main() {
	fmt.Print("Hello,World\n")


	numbers := []int{7, 2, 10, 4, 10}

	// Step 1 & 2
	largest := numbers[0]

	// Step 3–6
	for _, number := range numbers[1:] {
		if number > largest {
			largest = number
		}
	}
	// Step 7
	fmt.Println(largest)
}