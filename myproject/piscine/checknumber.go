package piscine

func CheckNumber(arg string) bool {
	for _, r := range arg {
		if r >= '0' && r <= '9' {
			return true
		}
	}
	return false
}