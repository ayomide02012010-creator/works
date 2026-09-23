package piscine

func Slice(a []string, nbrs ...int) []string {
	n := len(a)
	start := 0
	end := n

	if len(nbrs) >= 1 {
		start = nbrs[0]
	}
	if len(nbrs) >= 2 {
		end = nbrs[1]
	}
	if start < 0 {
		start = n + start
	}
	if end < 0 {
		end = n + end
	}
	if start < 0 {
		start = 0
	}
	if end > n {
		end = n
	}
	if start > end {
		return nil
	}
	return a[start:end]
}