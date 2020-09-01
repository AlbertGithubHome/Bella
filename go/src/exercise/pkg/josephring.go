package pkg

/*
JosephRing : print final people index(from 0 to start)
*/
func JosephRing(n int, m int) int {
	if n == 1 {
		return 0
	} 

	return (JosephRing(n - 1, m) + m) % n
}