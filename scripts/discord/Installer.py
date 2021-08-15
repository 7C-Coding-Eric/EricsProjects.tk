import os
libraries = ["discord.py", "aiohttp", "random", "Datetime"]
os.system("pip install --upgrade pip")
os.system("pip3 install --upgrade pip")
for i in range(len(libraries)):
    os.system(f"sudo -S pip install {libraries[i]}")
    os.system(f"sudo -S pip3 install {libraries[i]}")
print("Libraries Installed")
