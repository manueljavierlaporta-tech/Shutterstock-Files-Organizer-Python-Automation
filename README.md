# 📂 Shutterstock Files Organizer | Python Automation
<div>
  <p>
    This project contains a <b>Python Automation Script</b> built to organize downloaded some Shutterstock assets (images and videos) automatically into structured folders.
    <br>
    Downloaded creative assets often accumulate in a single directory, making manual sorting repetitive and inefficient. This script detects Shutterstock files based on naming patterns and supported file extensions, then moves them into categorized folders.
    <br>
    The solution is lightweight, portable, and can also be packaged into a standalone executable for distribution.
  </p>
</div>

---

## ⚙️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)
![Automation](https://img.shields.io/badge/Automation-Scripting-green?style=for-the-badge)

---

## ✍🏻 Workflow
<div>
  <p>This script was created to make uploading images and videos purchased from Shutterstock to Google Drive easier and faster. It doesn't automatically upload files to Google Drive (yet), but it allows you to quickly identify images and videos within your "Downloads" folder (or wherever you're saving your Shutterstock downloads), so you can then easily select and upload them all to Google Drive.
  <br>
  It runs interactively using native system dialogs, in which you:
  </p>
  <ol>
    <li>Select the destination folder where the organized structure will be created.</li>
    <li>Select the source folder containing the downloaded files.</li>
    <li>The script scans all files in the source directory.</li>
    <li>Files are processed only if:</li>
    <ul>
      <li>The filename starts with "shutterstock".</li>
      <li>The extension matches a supported format.</li>
    </ul>
    <li>The script automatically creates the following structure (if it does not exist):</li>
    <small>
    <pre>
      Shutterstock/
      ├─ Images/
      └─ Videos/
    </pre>
    </small>
    <li>Files are moved into their corresponding category.</li>
    <li>A completion message indicated whether files were organized.</li>
  </ol>
</div>

---

## 🎯 Project Objective

<div>
  <p>This automation solves common workflow problems:</p>
  <ul>
    <li>Disorganized download directories.</li>
    <li>Manual classification of creative assets.</li>
    <li>Time loss when handling large batches of files.</li>
  </ul>
  <p>The script ensures:</p>
  <ul>
    <li>Automatic folder creation.</li>
    <li>Extension-based classification.</li>
    <li>Safe file movement using native Python modules.</li>
  </ul>
</div>

---

## Supported File Types

### Images
- `.jpg`
- `.jpeg`
- `.png`
- `.svg`

### Videos
- `.mov`
- `.mp4`

The extension system is easily scalable by modifying the dictionary inside the script.

---

## 🧠 Core Logic

Files are filtered using two conditions:

```python
if ext in extensions and name.startswith("shutterstock"):
```
This guarantees that:
- Only supported formats are processed.
- Only Shutterstock assets are moved.

## 🖥️ User Interaction

The script uses Tkinter native dialogs to avoid hardcoded paths and allow execution on any machine:

```python
filedialog.askdirectory()
```

## 📦 Executable Version (Optional)

The script can be converted into a standalone .exe file so it can run without requiring Python to be installed.

Example:
```bash
pyinstaller --onefile --noconsole organizer.py
```

## 📌 Use Case

This tool is useful in workflows where:
- Creative assets are downloaded frequently.
- Files accumulate in a general downloads directory.
- Assets must be organized quickly before indexing or tracking.

## ⚠️ Notes

- Files are moved, not copied.
- Existing folders are reused.
- Only files starting with "shutterstock" are processed.
- The script does not overwrite existing files with the same name.

## 🚀 Possible Improvements

- Automatic detection of the Downloads folder
- Logging system
- Duplicate file handling
- Drag & drop support
- Simple GUI interface
- Batch automation mode (no dialogs)
