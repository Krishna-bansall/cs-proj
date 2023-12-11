# File handler


fh =  open("./data.txt", "a+", encoding='utf-8') 
fh.seek(-1)




data = fh.read()
print(data)
