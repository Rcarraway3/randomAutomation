import sys
import subprocess

def ensure_package(pkg):
    try:
        __import__(pkg)
    except ImportError:
        print(f"[INFO] '{pkg}' not found. Attempting to install...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])
        try:
            __import__(pkg)
        except ImportError:
            print(f"[ERROR] Failed to install '{pkg}'. Exiting.")
            sys.exit(1)

ensure_package('pandas')
ensure_package('openpyxl')

import pandas as pd

data = [
    {"Name": "John", "Age": 30, "Email": "john@example.com"},
    {"Name": "Jane", "Age": 25, "Email": "jane@example.com"},
    {"Name": "Bob", "Age": 40, "Email": "bob@example.com"},
]
df = pd.DataFrame(data)
df.to_excel("sample.xlsx", index=False)
print("sample.xlsx created.") 