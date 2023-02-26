package main

import "fmt"

func main() {
	var n1, n2 int
	fmt.Scan(&n1, &n2)
	if n1 < n2 {
		fmt.Println("<")
	} else if n1 == n2 {
		fmt.Println("==")
	} else {
		fmt.Println(">")
	}
}
