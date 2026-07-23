package main

import (
	"fmt"
	"io/fs"
)

func ValidPath() {
	paths := []string{
		".",
		"x",
		"x/y/z",
		" ",
		". .",
		"/x",
		"x/",
		"x/ /y",
		"x/. /y",
		"x/. ./y",
	}

	for _, path := range paths {
		fmt.Printf("ValidPath(%q) = %t\n", path, fs.ValidPath(path))
	}

}
