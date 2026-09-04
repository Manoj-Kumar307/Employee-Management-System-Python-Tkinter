# Employee Management System

A desktop GUI application built with **Python (Tkinter)** for capturing and managing employee records, featuring a styled login screen and a data-entry form.

## Features
- Styled login/landing screen with a custom background image
- Data-entry form for employee **Name, ID, Age, Salary, and Department**
- Add Employee button that validates and logs entries, then resets the form
- Clean, labeled layout built with Tkinter's `place()` geometry manager

## Tech Stack
- **Python 3**
- **Tkinter** — GUI
- **Pillow (PIL)** — image handling for the login screen background

## Getting Started

```bash
git clone https://github.com/Manoj-Kumar307/Employee-Management-System-Python-Tkinter.git
cd Employee-Management-System-Python-Tkinter
pip install pillow
python Employee_Management_system.py
```

> Note: update the background image path in the script to a local image on your machine before running.

## Planned Improvements
- Persist employee records to a database (SQLite/MySQL) instead of just logging to console
- Add a records table (Treeview) to view, edit, and delete existing employees
- Add login authentication instead of a decorative login screen
- Form validation (numeric checks for age/salary, required fields)

## Author
**Manoj Kumar J** — [GitHub](https://github.com/Manoj-Kumar307) · [LinkedIn](https://linkedin.com/in/manojkumar07060300304)
