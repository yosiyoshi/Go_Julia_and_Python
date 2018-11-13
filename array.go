//author: yosiyoshi
package main
import "fmt"
import "go.matrix-go1/go.matrix-go1"

func main() {
	dmat := matrix.Zeros(3,3)
	dmat.Set(0,0,1)
	dmat.Set(1,1,3)
	dmat.Set(2,2,5)
	fmt.Println(dmat)
}