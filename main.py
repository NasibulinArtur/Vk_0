import re
from screeninfo import get_monitors
import winapps
import subprocess

for m in get_monitors():
    if (m.is_primary):
        height = (str(m.height))
        width = (str(m.width))

with open('video.txt','r+') as f:
    file = f.read()

    file = re.sub(r'setting.defaultres"\t\t"\d{3,}"', 'setting.defaultres"\t\t"'+ width +'"', file)
    f.seek(0)

    f.write(file)
    f.truncate()
    file = re.sub(r'setting.defaultresheight"\t\t"\d{3,}"', 'setting.defaultresheight"\t\t"'+ height +'"', file)
    f.seek(0)
    f.write(file)
    f.truncate()

f.close()
for item in winapps.list_installed():
    if item.name == "Steam":
        path = item.uninstall_string
        path = path.replace("uninstall.exe","steam.exe")
        subprocess.call(path)
        break

