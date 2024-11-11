	.arch armv8-a
	.file	"main.c"
	.text
	.align	2
	.global	Transform
	.type	Transform, %function
Transform:
.LFB6:
	.cfi_startproc
	stp	x29, x30, [sp, -160]!
	.cfi_def_cfa_offset 160
	.cfi_offset 29, -160
	.cfi_offset 30, -152
	mov	x29, sp
	str	x0, [sp, 40]
	str	w1, [sp, 36]
	str	x2, [sp, 24]
	adrp	x0, :got:__stack_chk_guard
	ldr	x0, [x0]
	ldr	x1, [x0]
	str	x1, [sp, 152]
	mov	x1, 0
	mov	w0, 65
	strb	w0, [sp, 80]
	mov	w0, 66
	strb	w0, [sp, 81]
	mov	w0, 67
	strb	w0, [sp, 82]
	mov	w0, 68
	strb	w0, [sp, 83]
	mov	w0, 69
	strb	w0, [sp, 84]
	mov	w0, 70
	strb	w0, [sp, 85]
	mov	w0, 71
	strb	w0, [sp, 86]
	mov	w0, 72
	strb	w0, [sp, 87]
	mov	w0, 73
	strb	w0, [sp, 88]
	mov	w0, 74
	strb	w0, [sp, 89]
	mov	w0, 75
	strb	w0, [sp, 90]
	mov	w0, 76
	strb	w0, [sp, 91]
	mov	w0, 77
	strb	w0, [sp, 92]
	mov	w0, 78
	strb	w0, [sp, 93]
	mov	w0, 79
	strb	w0, [sp, 94]
	mov	w0, 80
	strb	w0, [sp, 95]
	mov	w0, 81
	strb	w0, [sp, 96]
	mov	w0, 82
	strb	w0, [sp, 97]
	mov	w0, 83
	strb	w0, [sp, 98]
	mov	w0, 84
	strb	w0, [sp, 99]
	mov	w0, 85
	strb	w0, [sp, 100]
	mov	w0, 86
	strb	w0, [sp, 101]
	mov	w0, 87
	strb	w0, [sp, 102]
	mov	w0, 88
	strb	w0, [sp, 103]
	mov	w0, 89
	strb	w0, [sp, 104]
	mov	w0, 90
	strb	w0, [sp, 105]
	mov	w0, 97
	strb	w0, [sp, 106]
	mov	w0, 98
	strb	w0, [sp, 107]
	mov	w0, 99
	strb	w0, [sp, 108]
	mov	w0, 100
	strb	w0, [sp, 109]
	mov	w0, 101
	strb	w0, [sp, 110]
	mov	w0, 102
	strb	w0, [sp, 111]
	mov	w0, 103
	strb	w0, [sp, 112]
	mov	w0, 104
	strb	w0, [sp, 113]
	mov	w0, 105
	strb	w0, [sp, 114]
	mov	w0, 106
	strb	w0, [sp, 115]
	mov	w0, 107
	strb	w0, [sp, 116]
	mov	w0, 108
	strb	w0, [sp, 117]
	mov	w0, 109
	strb	w0, [sp, 118]
	mov	w0, 110
	strb	w0, [sp, 119]
	mov	w0, 111
	strb	w0, [sp, 120]
	mov	w0, 112
	strb	w0, [sp, 121]
	mov	w0, 113
	strb	w0, [sp, 122]
	mov	w0, 114
	strb	w0, [sp, 123]
	mov	w0, 115
	strb	w0, [sp, 124]
	mov	w0, 116
	strb	w0, [sp, 125]
	mov	w0, 117
	strb	w0, [sp, 126]
	mov	w0, 118
	strb	w0, [sp, 127]
	mov	w0, 119
	strb	w0, [sp, 128]
	mov	w0, 120
	strb	w0, [sp, 129]
	mov	w0, 121
	strb	w0, [sp, 130]
	mov	w0, 122
	strb	w0, [sp, 131]
	mov	w0, 48
	strb	w0, [sp, 132]
	mov	w0, 49
	strb	w0, [sp, 133]
	mov	w0, 50
	strb	w0, [sp, 134]
	mov	w0, 51
	strb	w0, [sp, 135]
	mov	w0, 52
	strb	w0, [sp, 136]
	mov	w0, 53
	strb	w0, [sp, 137]
	mov	w0, 54
	strb	w0, [sp, 138]
	mov	w0, 55
	strb	w0, [sp, 139]
	mov	w0, 56
	strb	w0, [sp, 140]
	mov	w0, 57
	strb	w0, [sp, 141]
	mov	w0, 43
	strb	w0, [sp, 142]
	mov	w0, 47
	strb	w0, [sp, 143]
	str	wzr, [sp, 60]
	str	wzr, [sp, 56]
	b	.L2
.L13:
	ldr	w1, [sp, 56]
	ldr	w0, [sp, 36]
	cmp	w1, w0
	bge	.L3
	ldrsw	x0, [sp, 56]
	ldr	x1, [sp, 40]
	add	x0, x1, x0
	ldrb	w0, [x0]
	b	.L4
.L3:
	mov	w0, 0
.L4:
	str	w0, [sp, 64]
	ldr	w0, [sp, 56]
	add	w0, w0, 1
	ldr	w1, [sp, 36]
	cmp	w1, w0
	ble	.L5
	ldrsw	x0, [sp, 56]
	add	x0, x0, 1
	ldr	x1, [sp, 40]
	add	x0, x1, x0
	ldrb	w0, [x0]
	b	.L6
.L5:
	mov	w0, 0
.L6:
	str	w0, [sp, 68]
	ldr	w0, [sp, 56]
	add	w0, w0, 2
	ldr	w1, [sp, 36]
	cmp	w1, w0
	ble	.L7
	ldrsw	x0, [sp, 56]
	add	x0, x0, 2
	ldr	x1, [sp, 40]
	add	x0, x1, x0
	ldrb	w0, [x0]
	b	.L8
.L7:
	mov	w0, 0
.L8:
	str	w0, [sp, 72]
	ldr	w0, [sp, 64]
	lsl	w1, w0, 16
	ldr	w0, [sp, 68]
	lsl	w0, w0, 8
	add	w0, w1, w0
	ldr	w1, [sp, 72]
	add	w0, w1, w0
	str	w0, [sp, 76]
	ldr	w0, [sp, 76]
	asr	w0, w0, 18
	and	w2, w0, 63
	ldr	w0, [sp, 60]
	add	w1, w0, 1
	str	w1, [sp, 60]
	sxtw	x0, w0
	ldr	x1, [sp, 24]
	add	x0, x1, x0
	sxtw	x1, w2
	add	x2, sp, 80
	ldrb	w1, [x2, x1]
	strb	w1, [x0]
	ldr	w0, [sp, 76]
	asr	w0, w0, 12
	and	w2, w0, 63
	ldr	w0, [sp, 60]
	add	w1, w0, 1
	str	w1, [sp, 60]
	sxtw	x0, w0
	ldr	x1, [sp, 24]
	add	x0, x1, x0
	sxtw	x1, w2
	add	x2, sp, 80
	ldrb	w1, [x2, x1]
	strb	w1, [x0]
	ldr	w0, [sp, 56]
	add	w0, w0, 1
	ldr	w1, [sp, 36]
	cmp	w1, w0
	ble	.L9
	ldr	w0, [sp, 76]
	asr	w0, w0, 6
	and	w0, w0, 63
	sxtw	x0, w0
	add	x1, sp, 80
	ldrb	w0, [x1, x0]
	b	.L10
.L9:
	mov	w0, 61
.L10:
	ldr	w1, [sp, 60]
	add	w2, w1, 1
	str	w2, [sp, 60]
	sxtw	x1, w1
	ldr	x2, [sp, 24]
	add	x1, x2, x1
	strb	w0, [x1]
	ldr	w0, [sp, 56]
	add	w0, w0, 2
	ldr	w1, [sp, 36]
	cmp	w1, w0
	ble	.L11
	ldr	w0, [sp, 76]
	and	w0, w0, 63
	sxtw	x0, w0
	add	x1, sp, 80
	ldrb	w0, [x1, x0]
	b	.L12
.L11:
	mov	w0, 61
.L12:
	ldr	w1, [sp, 60]
	add	w2, w1, 1
	str	w2, [sp, 60]
	sxtw	x1, w1
	ldr	x2, [sp, 24]
	add	x1, x2, x1
	strb	w0, [x1]
	ldr	w0, [sp, 56]
	add	w0, w0, 3
	str	w0, [sp, 56]
.L2:
	ldr	w1, [sp, 56]
	ldr	w0, [sp, 36]
	cmp	w1, w0
	blt	.L13
	ldrsw	x0, [sp, 60]
	ldr	x1, [sp, 24]
	add	x0, x1, x0
	strb	wzr, [x0]
	nop
	adrp	x0, :got:__stack_chk_guard
	ldr	x0, [x0]
	ldr	x2, [sp, 152]
	ldr	x1, [x0]
	subs	x2, x2, x1
	mov	x1, 0
	beq	.L14
	bl	__stack_chk_fail
.L14:
	ldp	x29, x30, [sp], 160
	.cfi_restore 30
	.cfi_restore 29
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE6:
	.size	Transform, .-Transform
	.align	2
	.global	encrypt
	.type	encrypt, %function
encrypt:
.LFB7:
	.cfi_startproc
	stp	x29, x30, [sp, -448]!
	.cfi_def_cfa_offset 448
	.cfi_offset 29, -448
	.cfi_offset 30, -440
	mov	x29, sp
	.cfi_def_cfa_register 29
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	stp	x25, x26, [sp, 64]
	str	x27, [sp, 80]
	sub	sp, sp, #16
	.cfi_offset 19, -432
	.cfi_offset 20, -424
	.cfi_offset 21, -416
	.cfi_offset 22, -408
	.cfi_offset 23, -400
	.cfi_offset 24, -392
	.cfi_offset 25, -384
	.cfi_offset 26, -376
	.cfi_offset 27, -368
	str	x0, [x29, 104]
	str	x1, [x29, 96]
	adrp	x0, :got:__stack_chk_guard
	ldr	x0, [x0]
	ldr	x1, [x0]
	str	x1, [x29, 440]
	mov	x1, 0
	mov	x0, sp
	mov	x19, x0
	mov	w0, 73
	strb	w0, [x29, 168]
	mov	w0, 109
	strb	w0, [x29, 169]
	mov	w0, 83
	strb	w0, [x29, 170]
	mov	w0, 104
	strb	w0, [x29, 171]
	mov	w0, 101
	strb	w0, [x29, 172]
	mov	w0, 108
	strb	w0, [x29, 173]
	mov	w0, 108
	strb	w0, [x29, 174]
	mov	w0, 109
	strb	w0, [x29, 175]
	mov	w0, 52
	strb	w0, [x29, 176]
	mov	w0, 97
	strb	w0, [x29, 177]
	mov	w0, 116
	strb	w0, [x29, 178]
	mov	w0, 101
	strb	w0, [x29, 179]
	mov	w0, 77
	strb	w0, [x29, 180]
	mov	w0, 51
	strb	w0, [x29, 181]
	mov	w0, 109
	strb	w0, [x29, 182]
	mov	w0, 98
	strb	w0, [x29, 183]
	mov	w0, 16
	str	w0, [x29, 144]
	ldr	x0, [x29, 104]
	bl	strlen
	str	w0, [x29, 148]
	str	wzr, [x29, 120]
	b	.L16
.L17:
	ldr	w0, [x29, 120]
	and	w2, w0, 255
	ldrsw	x0, [x29, 120]
	add	x1, x29, 184
	strb	w2, [x1, x0]
	ldr	w0, [x29, 120]
	add	w0, w0, 1
	str	w0, [x29, 120]
.L16:
	ldr	w0, [x29, 120]
	cmp	w0, 255
	ble	.L17
	str	wzr, [x29, 124]
	str	wzr, [x29, 128]
	b	.L18
.L19:
	ldrsw	x0, [x29, 128]
	add	x1, x29, 184
	ldrb	w0, [x1, x0]
	mov	w1, w0
	ldr	w0, [x29, 124]
	add	w1, w1, w0
	ldr	w0, [x29, 128]
	ldr	w2, [x29, 144]
	sdiv	w3, w0, w2
	ldr	w2, [x29, 144]
	mul	w2, w3, w2
	sub	w0, w0, w2
	sxtw	x0, w0
	add	x2, x29, 168
	ldrb	w0, [x2, x0]
	add	w0, w1, w0
	negs	w1, w0
	and	w0, w0, 255
	and	w1, w1, 255
	csneg	w0, w0, w1, mi
	str	w0, [x29, 124]
	ldrsw	x0, [x29, 128]
	add	x1, x29, 184
	ldrb	w0, [x1, x0]
	strb	w0, [x29, 119]
	ldrsw	x0, [x29, 124]
	add	x1, x29, 184
	ldrb	w2, [x1, x0]
	ldrsw	x0, [x29, 128]
	add	x1, x29, 184
	strb	w2, [x1, x0]
	ldrsw	x0, [x29, 124]
	add	x1, x29, 184
	ldrb	w2, [x29, 119]
	strb	w2, [x1, x0]
	ldr	w0, [x29, 128]
	add	w0, w0, 1
	str	w0, [x29, 128]
.L18:
	ldr	w0, [x29, 128]
	cmp	w0, 255
	ble	.L19
	ldr	w0, [x29, 148]
	sxtw	x1, w0
	sub	x1, x1, #1
	str	x1, [x29, 152]
	sxtw	x1, w0
	mov	x26, x1
	mov	x27, 0
	lsr	x1, x26, 61
	lsl	x23, x27, 3
	orr	x23, x1, x23
	lsl	x22, x26, 3
	sxtw	x1, w0
	mov	x24, x1
	mov	x25, 0
	lsr	x1, x24, 61
	lsl	x21, x25, 3
	orr	x21, x1, x21
	lsl	x20, x24, 3
	sxtw	x0, w0
	add	x0, x0, 15
	lsr	x0, x0, 4
	lsl	x0, x0, 4
	and	x1, x0, -65536
	sub	x1, sp, x1
.L20:
	cmp	sp, x1
	beq	.L21
	sub	sp, sp, #65536
	str	xzr, [sp, 1024]
	b	.L20
.L21:
	and	x1, x0, 65535
	sub	sp, sp, x1
	str	xzr, [sp]
	and	x0, x0, 65535
	cmp	x0, 1024
	bcc	.L22
	str	xzr, [sp, 1024]
.L22:
	add	x0, sp, 16
	add	x0, x0, 0
	str	x0, [x29, 160]
	str	wzr, [x29, 132]
	str	wzr, [x29, 136]
	str	wzr, [x29, 140]
	b	.L23
.L24:
	ldr	w0, [x29, 132]
	add	w0, w0, 1
	negs	w1, w0
	and	w0, w0, 255
	and	w1, w1, 255
	csneg	w0, w0, w1, mi
	str	w0, [x29, 132]
	ldrsw	x0, [x29, 132]
	add	x1, x29, 184
	ldrb	w0, [x1, x0]
	mov	w1, w0
	ldr	w0, [x29, 136]
	add	w0, w1, w0
	negs	w1, w0
	and	w0, w0, 255
	and	w1, w1, 255
	csneg	w0, w0, w1, mi
	str	w0, [x29, 136]
	ldrsw	x0, [x29, 132]
	add	x1, x29, 184
	ldrb	w0, [x1, x0]
	strb	w0, [x29, 117]
	ldrsw	x0, [x29, 136]
	add	x1, x29, 184
	ldrb	w2, [x1, x0]
	ldrsw	x0, [x29, 132]
	add	x1, x29, 184
	strb	w2, [x1, x0]
	ldrsw	x0, [x29, 136]
	add	x1, x29, 184
	ldrb	w2, [x29, 117]
	strb	w2, [x1, x0]
	ldrsw	x0, [x29, 132]
	add	x1, x29, 184
	ldrb	w1, [x1, x0]
	ldrsw	x0, [x29, 136]
	add	x2, x29, 184
	ldrb	w0, [x2, x0]
	add	w0, w1, w0
	and	w0, w0, 255
	sxtw	x0, w0
	add	x1, x29, 184
	ldrb	w0, [x1, x0]
	strb	w0, [x29, 118]
	ldrsw	x0, [x29, 140]
	ldr	x1, [x29, 104]
	add	x0, x1, x0
	ldrb	w1, [x0]
	ldrb	w0, [x29, 118]
	eor	w0, w1, w0
	and	w2, w0, 255
	ldr	x1, [x29, 160]
	ldrsw	x0, [x29, 140]
	strb	w2, [x1, x0]
	ldr	w0, [x29, 140]
	add	w0, w0, 1
	str	w0, [x29, 140]
.L23:
	ldr	w1, [x29, 140]
	ldr	w0, [x29, 148]
	cmp	w1, w0
	blt	.L24
	ldr	x2, [x29, 96]
	ldr	w1, [x29, 148]
	ldr	x0, [x29, 160]
	bl	Transform
	mov	sp, x19
	nop
	adrp	x0, :got:__stack_chk_guard
	ldr	x0, [x0]
	ldr	x2, [x29, 440]
	ldr	x1, [x0]
	subs	x2, x2, x1
	mov	x1, 0
	beq	.L25
	bl	__stack_chk_fail
.L25:
	mov	sp, x29
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x25, x26, [sp, 64]
	ldr	x27, [sp, 80]
	ldp	x29, x30, [sp], 448
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 27
	.cfi_restore 25
	.cfi_restore 26
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa 31, 0
	ret
	.cfi_endproc
.LFE7:
	.size	encrypt, .-encrypt
	.section	.rodata
	.align	3
.LC0:
	.string	"Ciphertext : %s\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
.LFB8:
	.cfi_startproc
	stp	x29, x30, [sp, -304]!
	.cfi_def_cfa_offset 304
	.cfi_offset 29, -304
	.cfi_offset 30, -296
	mov	x29, sp
	str	w0, [sp, 28]
	str	x1, [sp, 16]
	adrp	x0, :got:__stack_chk_guard
	ldr	x0, [x0]
	ldr	x1, [x0]
	str	x1, [sp, 296]
	mov	x1, 0
	ldr	w0, [sp, 28]
	cmp	w0, 1
	bgt	.L27
	mov	w0, 1
	b	.L29
.L27:
	ldr	x0, [sp, 16]
	ldr	x0, [x0, 8]
	str	x0, [sp, 32]
	add	x0, sp, 40
	mov	x1, x0
	ldr	x0, [sp, 32]
	bl	encrypt
	add	x0, sp, 40
	mov	x1, x0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
.L29:
	mov	w1, w0
	adrp	x0, :got:__stack_chk_guard
	ldr	x0, [x0]
	ldr	x3, [sp, 296]
	ldr	x2, [x0]
	subs	x3, x3, x2
	mov	x2, 0
	beq	.L30
	bl	__stack_chk_fail
.L30:
	mov	w0, w1
	ldp	x29, x30, [sp], 304
	.cfi_restore 30
	.cfi_restore 29
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE8:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
	.section	.note.GNU-stack,"",@progbits
