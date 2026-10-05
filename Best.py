print ('عليك تسجيل الدخول اولا ✅')
name= str(input("ادخل اسمك :"))
age = int(input("ادخل عمرك :"))

if age >= 18:
	print ("انت مؤهل🎇")
else:
	print('انت غير مؤهل😔')
	exit()
num1 = int(input("ادخل الرقم الاول  :"))
operation = input("اختر + - * /")
num2 = int(input("ادخل الرقم الثانى  :"))
if operation == "+":
     result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
	result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "لا يمكن القسمة على صفر"
else:
    result = "عملية غير صالحة"

  
print("النتيجة هي:", result)
print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
     
     