import os

def walk(path = os.getcwd()):
    black_listed = ["model","assets"]
    for root,_,files in os.walk(path):
        for file in files:
            _p = os.path.join(root,file)
            if _p.endswith(".py") and not os.path.basename(os.path.dirname(_p)) in ("models","image_src") and not os.path.basename(_p) in ("assets.py","assets_rc.py"):
                yield _p
count = 0
out_fd = open("out.py","wb")
for p in walk():
    with open(p,"rb") as fd:
        for _ in fd.readlines():
            count+=1
        fd.seek(0)
        out_fd.write(fd.read())
    print("File: ", p, " Line: ",count)