package main

import "fmt"

// ************************
// ********* WIP **********
// ************************

func main() {
	fish := []int{4, 3, 2, 1, 5}
	direction := []int{0, 1, 0, 0, 0}

	res := Solution(fish, direction)
	fmt.Println(res)
}

type stack []int

func (s *stack) push(v int) {
	fmt.Println(s)
	s = append(s, v)
	fmt.Println(s)
}

func (s stack) pop() int {
	fmt.Println(s)
	if len(s) > 0 {
		return s[len(s)-1:][0]
	}
	return 0
}

func Solution(A []int, B []int) int {
	s := stack{}
	s.push(1)
	s.push(2)
	b := s.pop()
	fmt.Println(b)
	return 2
	// ups := []
	// survived = 0

	// for idx, fish in enumerate(A):
	//   direction = B[idx]
	//   if direction == 1:
	//     ups.append(fish)
	//   else:
	//     eaten = False
	//     while len(ups):
	//       upFish = ups.pop()
	//       if upFish > fish:
	//         ups.append(upFish)
	//         eaten = True
	//         break

	//     if not eaten:
	//       survived += 1
	// return survived + len(ups)
}
