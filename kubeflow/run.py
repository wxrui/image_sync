import os
from pathlib import Path

files = os.listdir("./kustomize")
app_dir = Path("./kfapps")
app_dir.mkdir(parents=True, exist_ok=True)

for fname in files:
    filename = "./kustomize/%s"%(fname)
    cmd = "kubectl kustomize %s"%(filename)
    with os.popen(cmd) as fr:
        with open("./kfapps/%s.yaml"%fname,"w") as fw:
            data = fr.read()
            print("%s.yaml"%fname)
            fw.write(data)
