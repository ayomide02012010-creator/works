package main

import (
	"fmt"
	"io/fs"
	"log"
	"testing/fstest"
)

func ReadFile() {
	fsys := fstest.MapFS{
		"hello.txt": {
			Data: []byte("Hello, World!\n"),
		},
	}

	data, err := fs.ReadFile(fsys, "hello.txt")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(string(data))

}
