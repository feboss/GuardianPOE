#IfWinActive, ahk_class POEWindowClass

;----------------------------------------------------------------------
; Hotkey
;----------------------------------------------------------------------	

$Space::
	Gosub, ciclo_flask
	return

;$+n::
;	Gosub, SeiLink
;	return
	
$^a::
	suspend
	return

$F1::
	Send, 6
	return

$F2:: 
	Send, 7
	return

;----------------------------------------------------------------------
; Ciclo delle flask
;----------------------------------------------------------------------	

ciclo_flask:
	random, totalDelay, 4000, 4200
	Array := [2,3,4,5]
	Loop, % Array.Length()
		{
		Random, F_Index,  1, % Array.Length()
		Flask := Array.RemoveAt(F_Index)
		Send, % Flask
		random, delay, -66, 129
		sleep, %delay%
		if array.Length() = 0
			break
		}
	SetTimer, first_beep, -4200
	sleep, %totalDelay%	
	
	return

first_beep:
	SoundBeep, 1000, 50
	return

;----------------------------------------------------------------------
; 6 link
;----------------------------------------------------------------------	
	   
SeiLink:
	Loop, 50
	{
		Send +{Click}
		random, delay, -5, 80
		sleep, %delay%
	}
	return
		
;----------------------------------------------------------------------
; Svuota Inventario
;----------------------------------------------------------------------	

Svuota:
	xa := 1295
	yb := 610
	Loop, 5
	{		
		Loop, 13
		{
			Send ^{Click %xa% %yb%} 
			xa := xa+50
			sleep 20
		}
		xa := 1295
		yb := yb + 50
	}
	return



	