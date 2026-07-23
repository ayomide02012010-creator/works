package piscine

import "strconv"

func FromTo(f, t int) string {
	if f < 0 || f > 99 || t < 0 || t > 99 {
		return "Invalid\n"
	}
	s := ""
	step := 1
	if f > t {
		step = -1
	}
	for i := f; ; i += step {
		if i < 10 {
			s += "0" + strconv.Itoa(i)
		} else {
			s += strconv.Itoa(i)
		}
		if i == t {
			break
		}
		s += ", "
	}
	return s + "\n"
}
