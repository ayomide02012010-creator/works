package main

import (
	"fmt"
	"os"
	"strings"
)

const usage = "Usage: go run . [OPTION] [STRING] [BANNER]\n\nExample: go run . --align=right something standard\n"

func main() {
	align, text, banner, ok := parse(os.Args[1:])
	if !ok || text == "" {
		if !ok {
			fmt.Print(usage)
		}
		return
	}

	ascii, err := loadBanner(banner + ".txt")
	if err != nil {
		return
	}
	termW := termWidth()

	parts := strings.Split(strings.ReplaceAll(text, "\\n", "\n"), "\n")
	for i, part := range parts {
		if part == "" {
			if i < len(parts)-1 {
				fmt.Println()
			}
			continue
		}
		if align == "justify" {
			printJustify(part, ascii, termW)
		} else {
			rows, bw := renderBlock(part, ascii)
			printAligned(rows, bw, align, termW)
		}
	}
}

func parse(args []string) (align, text, banner string, ok bool) {
	align, banner = "left", "standard"
	if len(args) < 1 || len(args) > 3 {
		return "", "", "", false
	}
	if strings.HasPrefix(args[0], "--align") {
		if !strings.HasPrefix(args[0], "--align=") {
			return "", "", "", false
		}
		align = strings.TrimPrefix(args[0], "--align=")
		switch align {
		case "left", "right", "center", "justify":
		default:
			return "", "", "", false
		}
		if len(args) < 2 {
			return "", "", "", false
		}
		text = args[1]
		if len(args) == 3 {
			banner = args[2]
		}
	} else {
		text = args[0]
		if len(args) == 2 {
			banner = args[1]
		} else if len(args) == 3 {
			return "", "", "", false
		}
	}
	switch banner {
	case "standard", "shadow", "thinkertoy":
		return align, text, banner, true
	default:
		return "", "", "", false
	}
}

func loadBanner(file string) (map[rune][8]string, error) {
	b, err := os.ReadFile(file)
	if err != nil {
		return nil, err
	}
	lines := strings.Split(strings.ReplaceAll(string(b), "\r\n", "\n"), "\n")
	out := make(map[rune][8]string)
	for ch := rune(32); ch <= 126; ch++ {
		start := 1 + int(ch-32)*9
		if start+7 >= len(lines) {
			break
		}
		var art [8]string
		for i := 0; i < 8; i++ {
			art[i] = lines[start+i]
		}
		out[ch] = art
	}
	return out, nil
}

func renderBlock(s string, ascii map[rune][8]string) (rows []string, w int) {
	rows = make([]string, 8)
	for _, r := range s {
		art := ascii[r]
		for i := 0; i < 8; i++ {
			rows[i] += art[i]
		}
	}
	for i := 0; i < 8; i++ {
		rows[i] = strings.TrimRight(rows[i], " ")
		if len(rows[i]) > w {
			w = len(rows[i])
		}
	}
	for i := 0; i < 8; i++ {
		rows[i] += strings.Repeat(" ", w-len(rows[i]))
	}
	return rows, w
}

func printAligned(rows []string, blockW int, align string, termW int) {
	pad := 0
	if termW > blockW {
		switch align {
		case "right":
			pad = termW - blockW
		case "center":
			pad = (termW - blockW) / 2
		}
	}
	p := strings.Repeat(" ", pad)
	for _, row := range rows {
		fmt.Println(p + row)
	}
}

func printJustify(s string, ascii map[rune][8]string, termW int) {
	words := strings.Fields(s)
	if len(words) <= 1 {
		rows, _ := renderBlock(s, ascii)
		for _, row := range rows {
			fmt.Println(row)
		}
		return
	}

	type wblock struct {
		rows []string
		w    int
	}
	ws := make([]wblock, len(words))
	total := 0
	for i, wd := range words {
		r, w := renderBlock(wd, ascii)
		ws[i] = wblock{r, w}
		total += w
	}

	gaps := len(ws) - 1
	if termW < total+gaps {
		termW = total + gaps
	}
	space := termW - total
	base, extra := space/gaps, space%gaps

	for row := 0; row < 8; row++ {
		var sb strings.Builder
		for i := 0; i < len(ws); i++ {
			sb.WriteString(ws[i].rows[row])
			if i < gaps {
				g := base
				if i < extra {
					g++
				}
				sb.WriteString(strings.Repeat(" ", g))
			}
		}
		fmt.Println(sb.String())
	}
}

func termWidth() int {
	if v := os.Getenv("COLUMNS"); v != "" {
		var w int
		if _, err := fmt.Sscanf(v, "%d", &w); err == nil && w > 0 {
			return w
		}
	}

	for _, pth := range []string{"/bin/stty", "/usr/bin/stty", "stty"} {
		r, w, err := os.Pipe()
		if err != nil {
			continue
		}
		attr := &os.ProcAttr{Files: []*os.File{os.Stdin, w, os.Stderr}}
		p, err := os.StartProcess(pth, []string{"stty", "size"}, attr)
		if err != nil {
			_ = r.Close()
			_ = w.Close()
			continue
		}
		_ = w.Close()
		_, _ = p.Wait()

		buf := make([]byte, 64)
		n, _ := r.Read(buf)
		_ = r.Close()
		var cols int
		if _, err := fmt.Sscanf(strings.TrimSpace(string(buf[:n])), "%*d %d", &cols); err == nil && cols > 0 {
			return cols
		}
	}
	return 80
}

