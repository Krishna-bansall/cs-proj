# File handler

try:
    fh =  open("data.txt", "a+", encoding='utf-8') 
    data = fh.readlines()
    print(data)
except FileNotFoundError:
    fh = open("data.txt", "w+")
    data = ""
    print(data)
except Exception as e:
  print(f"Error: {e}")
