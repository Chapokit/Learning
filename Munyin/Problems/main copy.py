if os.path.exists(LAB):
    print(f"{LAB} downloaded successfully.")
else:
    print(f"Failed to download {LAB}.")
import urllib.request
import os

LAB = "turtlelab1.py"
url = f"http://elab.cpe.ku.ac.th/turtlelab/%7BLAB%7D"
urllib.request.urlretrieve(url, LAB)
if os.path.exists(LAB):
    print(f"{LAB} downloaded successfully.")
else:
    print(f"Failed to download {LAB}.")