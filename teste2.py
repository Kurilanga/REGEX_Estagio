import os
import shutil
import re


src_path =
dest_path =

files = os.listdir(os.path.dirname(src_path))

regex = r'(.*crt$)'

for f in files:
    if (re.search(regex, f)):
        print(f)
        f = os.path.join(src_path, f)
        shutil.move(f, dest_path)

#Queria saber tambem se esta maneira tambem seria válida,
# tentei fazer assim mas da erro no path, falando que nao consegue achar, mas acho que isso é facil de resolver.