extern printf
section .data
fmt:    db "%d", 10, 0
section .text
global main
main:
jmp __2
__1:
push rbp
mov rbp, rsp
push rax
push rcx
mov rdi,fmt
mov rsi, [rbp + 16]
xor rax, rax
call printf
pop rcx
pop rax
pop rbp
ret
__2:
push rbp
mov rbp, rsp
add rsp, -32
mov rax, rbp
add rax, -8
push rax
mov rax, 1071
push rax
pop rcx
pop rax
mov [rax], rcx
mov rax, rbp
add rax, -16
push rax
mov rax, 462
push rax
pop rcx
pop rax
mov [rax], rcx
jmp __4
__3:
push rbp
mov rbp, rsp
add rsp, -8
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, 24
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov rdx, 1
cmp rax, rcx
jg __7
mov rdx, 0
__7:
push rdx
pop rax
mov rcx, 1
cmp rax, rcx
jne __6
add rsp, -8
mov rax, rbp
add rax, -8
push rax
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov [rax], rcx
mov rax, rbp
add rax, 16
push rax
mov rax, rbp
add rax, 24
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov [rax], rcx
mov rax, rbp
add rax, 24
push rax
mov rax, rbp
add rax, -8
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov [rax], rcx
jmp __5
__6:
__5:
mov rax, rbp
add rax, 24
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov rdx, 0
div rcx
push rdx
mov rax, 0
push rax
pop rcx
pop rax
mov rdx, 1
cmp rax, rcx
je __11
mov rdx, 0
__11:
push rdx
pop rax
mov rcx, 1
cmp rax, rcx
jne __10
add rsp, 0
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
pop rax
mov rsp, rbp
pop rbp
ret
jmp __9
__10:
mov rax, 1
push rax
pop rax
mov rcx, 1
cmp rax, rcx
jne __12
add rsp, 0
xor rax, rax
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, 24
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov rdx, 0
div rcx
push rdx
call __3
pop rcx
pop rcx
push rax
pop rax
mov rsp, rbp
pop rbp
ret
jmp __9
__12:
__9:
mov rsp, rbp
pop rbp
mov rax, 0
ret
__4:
mov rax, rbp
add rax, -32
push rax
xor rax, rax
mov rax, rbp
add rax, -16
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, -8
push rax
pop rcx
mov rax, [rcx]
push rax
call __3
pop rcx
pop rcx
push rax
pop rcx
pop rax
mov [rax], rcx
xor rax, rax
mov rax, rbp
add rax, -32
push rax
pop rcx
mov rax, [rcx]
push rax
call __1
pop rcx
push rax
mov rsp, rbp
pop rbp
ret
