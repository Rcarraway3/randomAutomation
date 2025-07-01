# Copy Paste Automations: Build Checklist

**Goal:** Every automation is a single .py file. Drop it in the target directory, double-click, and it handles the task—no config, no setup, no dependencies (unless noted).

---

## Required Pattern: Dependency Self-Healing

Every script must check for required dependencies at runtime. If a dependency is missing, the script will attempt to install it automatically using pip, then retry the import. If installation fails, the script exits with a clear error.

**Copy-paste this snippet at the top of any script that needs external packages:**

```python
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

# Example usage:
# ensure_package('pandas')
# ensure_package('openpyxl')
```

---

## Build Checklist

- [ ] Excel to CSV Batch Exporter
    - Converts all `.xlsx` files in a folder to `.csv`.
    - **Instructions:** Script scans directory, converts each Excel file, saves as `.csv` with same base name.

- [ ] Excel Data Merger
    - Merges all Excel files in a directory into one master sheet.
    - **Instructions:** Script finds all `.xlsx`, appends rows, outputs `merged.xlsx`.

- [ ] Column Extractor
    - Extracts specified columns from all Excel files.
    - **Instructions:** Script prompts for column names, processes each file, outputs new files with only those columns.

- [ ] Duplicate Remover
    - Removes duplicate rows from Excel files.
    - **Instructions:** Script scans for `.xlsx`, removes duplicates, saves cleaned versions.

- [ ] Automated Pivot Table Generator
    - Creates a pivot table from a data sheet.
    - **Instructions:** Script prompts for pivot parameters, generates table, saves as new file.

- [ ] Excel to PDF Converter
    - Converts all Excel sheets to PDFs.
    - **Instructions:** Script finds `.xlsx`, exports each sheet as PDF.

- [ ] Bulk Email Sender
    - Sends personalized emails from Excel/CSV list.
    - **Instructions:** Script reads recipients/messages, sends via SMTP. Prompts for credentials if needed.

- [ ] Attachment Downloader
    - Downloads all attachments from inbox.
    - **Instructions:** Script connects to email, downloads attachments from last X days.

- [ ] Inbox Cleaner
    - Moves/deletes old or pattern-matched emails.
    - **Instructions:** Script connects to inbox, processes emails by date/pattern.

- [ ] Auto-Responder
    - Sends templated reply to unread emails.
    - **Instructions:** Script scans inbox, replies to all unread with a template.

- [ ] File Renamer
    - Batch renames files by pattern or mapping.
    - **Instructions:** Script prompts for pattern or reads mapping from Excel, renames files.

- [ ] PDF Merger/Splitter
    - Merges or splits PDFs in a folder.
    - **Instructions:** Script merges all PDFs or splits each into pages, based on user prompt.

- [ ] Daily Report Generator
    - Aggregates data and emails a summary report.
    - **Instructions:** Script pulls from Excel/CSV, generates summary, sends email.

- [ ] Screenshot Archiver
    - Takes periodic screenshots and saves to folder.
    - **Instructions:** Script runs, takes screenshot every X minutes, saves with timestamp.

- [ ] Calendar Event Exporter
    - Exports events from Outlook/Google Calendar to Excel.
    - **Instructions:** Script connects to calendar, exports upcoming events to `.xlsx`.

- [ ] Slack/Teams Notifier
    - Sends message to channel on file update or task completion.
    - **Instructions:** Script monitors directory or task, sends notification via webhook.

- [ ] Folder Watcher
    - Monitors directory for new files and triggers action.
    - **Instructions:** Script watches folder, on new file, moves/processes/emails as needed.

- [ ] Data Scraper
    - Scrapes website for daily data, logs to Excel.
    - **Instructions:** Script fetches target page, parses data, appends to `.xlsx` log.

---

**How to Use:**
- Pick a task. Build as a single .py file.
- Script must be autonomous: drop in, double-click, done.
- If dependencies are needed, prompt user to install (`pip install ...`).
- No config files, no manual setup. All logic in the script.
- Add debug logs and clear output for every action. 