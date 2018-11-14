country = input('請問你是哪國人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以開車喔!! ')
	else:
		print('小屁孩, 旁邊玩沙去吧!!' )
elif country == '美國':
	if age >= 16:
		print('你可以開車喔!! ')
	else:
		print('小屁孩, 旁邊玩沙去吧!!' )
else:
	print('我們只負責台灣跟美國啦!!')
