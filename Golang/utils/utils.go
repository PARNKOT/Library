package utils

func SumInt(args ...int) (int, int) {
	var sum int = 0

	for _, arg := range args {
		sum += arg
	}

	return len(args), sum
}
