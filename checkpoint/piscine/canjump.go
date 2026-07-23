package piscine

func CanJump(nums []uint) bool {
	if len(nums) <= 1 {
		return true
	}
	pos := uint(0)
	n := uint(len(nums))
	for pos < n-1 {
		steps := nums[pos]
		if steps == 0 {
			return false
		}
		pos += steps
		if pos >= n {
			return false
		}
	}
	return pos == n-1
}