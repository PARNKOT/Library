x = float(input())
y = float(input())
op = str(input()).strip()

if op == "+":     print(x+y)
elif op == "-":   print(x-y)
elif op == "*":   print(x*y)
elif op == "pow": print(x**y)
elif y == 0.0:    print("Деление на 0!") # думаю, здесь проверке на ноль самое место
elif op == "/":   print(x/y)
elif op == "mod": print(x%y)
elif op == "div": print(x//y)
#else print("<"+ op +"> -- неизвестная операция")

#Version 2.0 (ЯП C#)
operations = {
      "+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "/": lambda x, y: x / y,
      "*": lambda x, y: x * y,
      "mod": lambda x, y: x % y,
      "pow": lambda x, y: x ** y,
      "div": lambda x, y: x // y
}

x, y = float(input()), float(input())
operation = input()

if operation in ["mod", "div", "/"] and y == 0:
    print("Деление на 0!")
else:
    print(operations[operation](x, y))