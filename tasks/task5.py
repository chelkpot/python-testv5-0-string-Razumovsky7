# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    str1, str2, str3 = input("Введите три символа, разделённых пробелами").split()

    for i in range(3):
     print(f"Код символа {str1} равен {ord(str1)}")
     print(f"Код символа {str2} равен {ord(str2)}")
     print(f"Код символа {str3} равен {ord(str3)}")
      
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()