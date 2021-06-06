password = 'a123456'
i = 3
i = int(i)
while i >= 0:
	input_password = input('請輸入密碼: ')
	if input_password == password:
		print('登入成功!')
		break
	elif i >0:
		print('密碼錯誤! 你還有', i, '次機會')
		i -= 1
	else:
		print('密碼錯誤! 已鎖定')
		break

