package main

import "fmt"

// CanJump checks if it's possible to jump to the last index
func CanJump(nums []uint) bool {
    if len(nums) == 0 {
        return false
    }

    maxReach := 0
    for i := 0; i < len(nums); i++ {
        // If we can't reach this position, return false
        if i > maxReach {
            return false
        }

        // Update the farthest position we can reach from this point
        maxReach = max(maxReach, i + int(nums[i]))

        // If we can reach the last index, return true
        if maxReach >= len(nums)-1 {
            return true
        }
    }

    return false
}

// Helper function to return the maximum of two numbers
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    // Test cases as described in the prompt
    fmt.Println(CanJump([]uint{2, 3, 1, 1, 4})) // true
    fmt.Println(CanJump([]uint{3, 2, 1, 0, 4})) // false
    fmt.Println(CanJump([]uint{0}))              // true
}
