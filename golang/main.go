package main

import "fmt"

type Player struct {
	Id  string `json:"id"`
	Hp  int    `json:"hp"`
	Atk int    `json:"atk"`
	Def int    `json:"def"`
}

func main() {
	var A = Player{
		Id:  "A",
		Hp:  1000,
		Atk: 500,
		Def: 50,
	}
	var B = Player{
		Id:  "B",
		Hp:  1500,
		Atk: 100,
		Def: 200,
	}

	Dmg := calDMGbySub(A.Atk, B.Def)
	fmt.Print(Dmg)
}

func calDMGbySub(Atk int, Def int) (Dmg int) {
	Dmg = Atk - Def
	if Dmg < 0 {
		Dmg = 0
	}
	return Dmg
}

func calDMG(Atk int, Def int) (Dmg int) {

	return
}
