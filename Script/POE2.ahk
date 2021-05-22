#IfWinActive, ahk_class POEWindowClass

;----------------------------------------------------------------------
; Hotkey
;----------------------------------------------------------------------	

$Space::
	Gosub, CicloFlask
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

CicloFlask:		
	;Send, 1	
	;random, delay, -15, 50
	;sleep, %delay%
	Send, 2	
	random, delay, -18, 42
	sleep, %delay%
	Send, 3	
	random, delay, -25, 50
	sleep, %delay%
	Send, 4
	random, delay, -10, 30
	sleep, %delay%
	Send, 5
	random, delay, -5, 5
	sleep, %delay%		
	SetTimer, first_beep, -4000
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

;----------------------------------------------------------------------
; TEST
;----------------------------------------------------------------------	

test:
	random, totalDelay, 1900, 3300
	Array := [1,2,3,4,5]
	Loop
		{
		Random, F_Index,  1, % array.Length()
		Flask := Array.RemoveAt(F_Index)
		Send, % Flask
		random, delay, 48, 278
		sleep, %delay%
		if array.Length() = 0
			break
		}
	sleep, %totalDelay%
	return

	