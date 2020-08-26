package main

import (
	"fmt"
	"log"
	"math"
)

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
		Atk: 490, //490
		Def: 250, //50
	}
	var B = Player{
		Id:  "B",
		Hp:  1500,
		Atk: 500, //100
		Def: 600, //200
	}

	DMG1 := calDMG(A, B)
	fmt.Println(DMG1)
	fmt.Println()
	log.Println()
	DMG2 := calDMG(B, A)
	fmt.Println(DMG2)

}

func calDMGbySub(attacker Player, sufferer Player) (Dmg int) {
	Dmg = attacker.Atk - sufferer.Def
	if Dmg < 0 {
		Dmg = 0
	}
	log.Println("攻擊減去防禦 Dmg:", Dmg)
	return Dmg
}

func getBothWeighted(attacker Player, sufferer Player) (attackerWeighted int, suffererWeighted int) {
	attackerWeighted = attacker.Atk + attacker.Def
	suffererWeighted = sufferer.Atk + sufferer.Def
	return
}

func calDMGbyDiv(attacker Player, sufferer Player) (Dmg int) {
	var mult float64 = float64(attacker.Atk) / float64(sufferer.Def)
	DmgF := mult * float64(attacker.Atk)
	Dmg = int(math.Round(DmgF))
	log.Println("攻擊除以防禦 Dmg:", Dmg)

	return
}

func calDMG(attacker Player, sufferer Player) (Dmg int) {
	DmgSub := calDMGbySub(attacker, sufferer)
	fmt.Println(DmgSub)
	DmgDiv := calDMGbyDiv(attacker, sufferer)
	fmt.Println(DmgDiv)
	wA, wB := getBothWeighted(attacker, sufferer)
	fmt.Println(wA, wB)

	var DmgF float64
	if DmgSub <= DmgDiv {
		//除法對attacker有優勢
		DmgF = float64(DmgDiv*wA+DmgSub*wB) / float64(wA+wB)
		log.Println("除法對attacker有優勢。 DmgF:", DmgF)
	} else {
		// 減法對attacker有優勢
		DmgF = float64(DmgDiv*wA+DmgSub*wB) / float64(wA+wB)
		log.Println("減法對attacker有優勢。 DmgF:", DmgF)
	}
	Dmg = int(math.Round(DmgF))
	return
}
