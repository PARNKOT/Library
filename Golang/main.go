package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Task struct {
	ID       interface{}
	Number   interface{}
	Year     interface{}
	Students []struct {
		LastName   interface{}
		FirstName  interface{}
		MiddleName interface{}
		Birthday   interface{}
		Address    interface{}
		Phone      interface{}
		Rating     interface{}
	}
}

type Marks struct {
	Students []struct {
		Rating interface{}
	}
}

func main() {
	json_bytes, _ := os.ReadFile("test.txt")
	marks := new(Marks)

	if err := json.Unmarshal(json_bytes, marks); err != nil {
		fmt.Print(err)
		panic("json.Unmarhal error!")
	}

	var average int = 0

	for _, student := range marks.Students {
		if rating, ok := student.Rating.([3]int); ok {
			average += sum(rating[:])
		} else {
			panic("Converting from interface error!")
		}
	}

	fmt.Print(average)

}

func sum(arr []int) int {
	res := 0

	for _, num := range arr {
		res += num
	}

	return res
}
