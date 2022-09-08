func combine2(slice []int) [][]int {
	var slice_out [][]int

	for index1 := 0; index1 < len(slice)-1; index1++ {
		for index2 := 0; index2 < len(slice)-index1-1; index2++ {
			slice_out = append(slice_out, append(make([]int, 0), slice[index1], slice[index1+index2+1]))
		}
	}

	return slice_out
}
