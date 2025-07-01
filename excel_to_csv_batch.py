import os
import sys
import subprocess
import glob

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

# Ensure dependencies
ensure_package('pandas')
ensure_package('openpyxl')

import pandas as pd
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def xlsx_to_csv(xlsx_path):
    try:
        base, _ = os.path.splitext(xlsx_path)
        csv_path = base + '.csv'
        df = pd.read_excel(xlsx_path, engine='openpyxl')
        df.to_csv(csv_path, index=False)
        log(f"Converted: {xlsx_path} -> {csv_path}")
    except Exception as e:
        log(f"[ERROR] Failed to convert {xlsx_path}: {e}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xlsx_files = glob.glob(os.path.join(script_dir, '*.xlsx'))
    if not xlsx_files:
        log("No .xlsx files found in this directory.")
        return
    log(f"Found {len(xlsx_files)} .xlsx file(s). Processing...")
    for xlsx in xlsx_files:
        xlsx_to_csv(xlsx)
    log("All files processed.")

if __name__ == "__main__":
    main() 