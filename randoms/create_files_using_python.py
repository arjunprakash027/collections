import os
import subprocess

code = """
print("hello world")
"""

with open("created_file.py","w") as f:
    f.write(code)

if os.path.exists("created_file.py"):
    print("file created, now running")
    subprocess.run(["python","created_file.py"])


