import string
import re
pass_string = input("Nhap mat khau: ")
# Độ dày tối thiểu 8 ký tự
sokytu = len(pass_string)>=8
#print(sokytu)
# Chứa ít nhất 1 chữ hoa
upper = any(char.isupper() for char in pass_string)
#print(upper)
# Chứa ít nhất 1 chữ số
digit = any(char.isdigit() for char in pass_string)
#print(digit)
# Chứa ít nhất 1 ký tự đặc biệt
special = pass_string.isalnum()
#print(special)
# Không bao gồm 3 số liên tiếp
dayso = r'\d{3}'
timdayso = re.findall(dayso, pass_string)
kqdayso = not any(timdayso)
#print(kqdayso)
# In kết quả
if all([sokytu, upper, digit, kqdayso, not special])  : print("Mat khau thoa man")
else: print("Mat khau khong thoa man")