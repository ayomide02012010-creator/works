package piscine

func HashCode(dec string) string {
	if len(dec) == 0 {
		return ""
	}
	size := len(dec)
	var result string
	
	for _, r := range dec {
		hashed := (int(r) + size) % 127
		if hashed < 33 {
			hashed += 33
		}
		result += string(rune(hashed))
	}
	return result
}