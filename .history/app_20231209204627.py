# File handler
fh =  open("./data.txt", "a+", encoding='utf-8') 
fh.seek(0)

def load_page():
    data = fh.read()
    print(data)

def write_file(text):
    fh.write("\n" +text)
    
write_file("New Addition Wow")