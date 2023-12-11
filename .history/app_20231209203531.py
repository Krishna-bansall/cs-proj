# File handler

try:
  with open("data.txt", "a+") as fh:
    data = fh.read()
    print(data)
except FileNotFoundError:
  with open("data.txt", "w+") as fh:
    data = ""
    print(data)
except Exception as e:
  print(f"Error: {e}")
