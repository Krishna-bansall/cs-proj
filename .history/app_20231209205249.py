# File handler
fh =  open("./data.txt", "w+", encoding='utf-8') 

def load_page():
    fh.seek(0)
    data = fh.read()
    print(data)

def write_file(text):
    fh.write(text)
    
write_file("ghoome")
load_page()