
assume cs:code, ds:data
data segment
	sircitit db 10, ?, 10 dup (?)	;declarare sir de caractere citit de la tastatura pana la ENTER
	len equ $-sircitit-2		;lungimea sirului citit
	rez db len dup(?)		;declarare sir rezultat
	newline db 10, 13, '$'		;linie noua

data ends

code segment
start:
mov ax,data
mov ds,ax
mov di,offset rez
citire:
	mov ah, 08h;
	int 21h;
	mov bl,al;
	CMP bl,'$';
	JE afis; daca e elemntul cautat terminam rularea
	sub bl,'0';
	CMP bl,0; verificam daca elementul citit este cifra
	JAE ok1; nu depaseste partea de jos
	JBE continuare; daca nu at continuam
	ok1:
		CMP bl,9
		JBE ok2;nu depaseste partea de sus
		JAE continuare; daca nu at continuam
	ok2:
		add bl,'0'; refac codul ascii
		mov dl,bl; mut in dl
		mov ah,02h; afisez
		int 21h; afisez
		JMP citire;
		
	continuare:
		add bl,'0'; refac codul ascii
		mov rez[di],bl;il pun in sir
		inc di;
		JMP citire;


afis:
	mov rez[di],bl;
	mov ah,09h
	mov dx,offset rez;
	int 21h;


sf:

	mov ax, 4c00h
	int 21h
code ends
end start