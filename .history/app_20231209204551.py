# File handler
fh =  open("./data.txt", "a+", encoding='utf-8') 
fh.seek()

def load_page():
    data = fh.read()
    print(data)

def write_file(text):
    fh.write(text)
    
write_file("New Addition Wow")