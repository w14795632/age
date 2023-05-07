driving = input("請問你有沒有開過車:")

age = input("請問你幾歲?")
age = int(age)
if driving == '有':
	if age >= 18:
		print("很棒，成年之後才去考駕照!!")
	else:
		print("什麼!? 你未滿18怎麼開車的!違法耶!")
elif driving == '沒有':
	if age >= 18:
		print("蛤..該去考駕照了吧，不然怎麼把妹阿")
	else:
		print("沒關係，再過幾年你就可去考了，忍著點")

else:
	print("只能輸入有跟沒有啦!")