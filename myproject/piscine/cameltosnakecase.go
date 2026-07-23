package piscine

func CamelToSnakeCase(s string) string {
	if s == "" {
		return ""
	}
	if s[len(s)-1] >= 'A' && s[len(s)-1] <= 'Z' {
		return s
	}
	for i := 0; i < len(s)-1; i++ {
		if s[i] >= 'A' && s[i] <= 'Z' && s[i+1] >= 'A' && s[i+1] <= 'Z' {
			return s
		}
	}
	for _, c := range s {
		if !((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')){
			return s
		}
	}
	var result string
	for i, c := range s{
		if c >= 'A' && c <= 'Z'  && i > 0 {
			result += "_"
		}
		result += string(c)
	}
	return  result
}
