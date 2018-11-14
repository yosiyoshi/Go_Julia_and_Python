//author: yosiyoshi
package main
import "fmt"

type Event struct {
	Name string
	Year int
}

func main() {
	var ev *Event

	ev = &Event{
		Name: "Fall of Byzantine",
		Year: 1453,
	}
	fmt.Printf("Event input: %ev", ev)
}