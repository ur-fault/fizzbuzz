package main

import (
	"fmt"
)

func main() {
	words := map[int]string {
		3: "Fizz",
		5: "Buzz",
		7: "Bazz",
	}

	for i := 1; i <= 100; i++ {
		output := ""

		for key, value := range words {
			if i % key == 0 {
				output += value
			}
		}

		if output == "" {
			output = fmt.Sprintf("%d", i)
		}

		fmt.Println(output)
	}
}