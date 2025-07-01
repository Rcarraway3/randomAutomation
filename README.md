# Copy Paste Automations

This repo is a library of single-file Python automations. Drop any script into a directory, double-click, and let it handle a simple, focused task. No bloat. No setup. Just results.

---

## Automations

### 1. `resize_png.py`

**Purpose:**
Uniformly resizes all PNG images in the script's directory to a specified width and height, maintaining aspect ratio and centering on a transparent canvas. Useful for batch-prepping icons, assets, or thumbnails.

**How it works:**
- Scans the current directory for `.png` files.
- Prompts for target width and height.
- Resizes each image to fit within the target size, preserving aspect ratio.
- Centers the image on a transparent background of the specified size.
- Saves output as `<originalname>_scaled.png`.

**Usage:**
1. Place `resize_png.py` in a folder with your PNG files.
2. Double-click or run: `python resize_png.py`
3. Enter desired width and height when prompted.
4. Find scaled images in the same folder.

**Requirements:**
- Python 3.x
- Pillow (`pip install pillow`)

---

### 2. `move_jt.py`

**Purpose:**
Recursively finds all `.jt` files in subdirectories and moves them to the script's root directory. Useful for consolidating scattered files after exports or batch jobs.

**How it works:**
- Walks all subdirectories (excluding the root itself).
- Moves every `.jt` file found to the root directory (where the script is located).
- Prints each move operation.

**Usage:**
1. Place `move_jt.py` in the root of your target directory tree.
2. Double-click or run: `python move_jt.py`
3. All `.jt` files from subfolders will be moved up to the root.

**Requirements:**
- Python 3.x (no external dependencies)

---

## Philosophy
- Each script is atomic: no config, no dependencies (unless noted), no state.
- Designed for tactical, repeatable use. Copy, run, done.
- Add your own automations. Keep them single-file, self-contained, and bluntly effective. 