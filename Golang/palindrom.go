func IsPalindrom(word string) bool {
	runeArray := []rune(word)
	length := len(runeArray)

	for index := 0; index < length; index++ {
		if runeArray[index] != runeArray[length-index-1] {
			return false
		}
	}
	return true
}
