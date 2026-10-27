eded = int(input("Bir ədəd daxil edin: "))

if eded % 3 == 0:
  if eded % 5 == 0:
    print("FizzBuzz")
  else:
    print("Fizz")
else:
  if eded % 5 == 0:
    print("Buzz")
  else:
    print(eded)