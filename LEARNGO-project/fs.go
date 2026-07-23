package main

import (
	"fmt"
	"io/fs"
	"log"
	"testing/fstest"
)

func mAiN() {
	fsys := fstest.MapFS{
		"file.txt":        {},
		"file.go":         {},
		"dir/file.txt":    {},
		"dir/file.go":     {},
		"dir/subdir/x.go": {},
		"rid/ridbus/v.go": {},
	}

	patterns := []string{
		"*.txt",
		"*.go",
		"dir/*.go",
		"dir/*/x.go",
		"rid/*/v.go",
	}

	for _, pattern := range patterns {
		matches, err := fs.Glob(fsys, pattern)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%q matches: %v\n", pattern, matches)
	}

}
