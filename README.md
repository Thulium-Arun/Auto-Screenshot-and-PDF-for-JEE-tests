# Glorifire-Screenshot-Bot


---

### Instructions to Set Up and Run the Project

#### 1. **Prerequisites**

Before starting, ensure that you have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

Additionally, you will need to install Playwright to interact with the browser. This can be done by running the following commands:

```bash
pip install playwright
playwright install
pip install reportlab
```

This will install Playwright and the necessary browser binaries required for the automation scripts.

---

#### 2. **File Structure**

Make sure the project folder structure looks like this:

```
/project_directory
    ├── screenshots/           # Folder to store the screenshots, organized by test name
    ├── Used/                  # Folder where processed folders will be moved
    ├── Tests/                 # Folder to store the generated PDFs
    ├── play.py                # Script to log in and navigate through the portal
    ├── playwriter.py          # Script that uses Playwright to automate taking screenshots
    ├── topdflandscape.py      # Script to convert images to PDF
    ├── Data/                  # Directory for Playwright persistent context (stores login session)
    └── state.json (optional)  # File for saving Playwright's storage state (optional)
```

- The `screenshots/` folder will be where the screenshots are stored, organized by test names.
- The `Used/` folder will store processed test folders.
- The `Tests/` folder is where the final PDFs will be saved after the screenshots are processed.

If these directories don't exist, the script will try to create them automatically. 

Delete all the dot.text files, I simply added them to create file structures. They may mess with the working of the code.
---

#### 3. **Login Setup**

You need to log in to the portal at least once to create a valid session and save the login state. 

You must login in manually once every time you open the script (when your session runs out)
You can log in by running the `play.py` script interactively, which will log you into the portal and save the session:
You need to log in with OTP and stuff

```bash
python -i play.py
```

The first time you run this script, it will open the browser, let you log in manually, and store the session in the `Data/` directory. Make sure to enter your credentials correctly. After logging in, the script will store your session, allowing future runs to skip the login step.

---

#### 4. **Running the Scripts**

Once you have logged in and the session is saved, you can run the main automation script. This will take screenshots of the test results and save them into the appropriate folder. 

1. **Run the `playwriter.py` script** to start taking screenshots of your test results:
   
   ```bash
   python playwriter.py
   ```

   This will:
   - Log in using the saved session.
   - Navigate through the test results.
   - Capture screenshots of the test results.
   - Store them in the `screenshots/` directory under the respective test name folder.

2. **Run the `topdflandscape.py` script** to convert the screenshots into a PDF for easy viewing:

   ```bash
   python topdflandscape.py
   ```

   This will:
   - Organize the screenshots into a PDF in landscape mode.
   - Save the PDF in the `Tests/` folder.

   You can open the generated PDFs later to review the tests.

---

#### 5. **Folder Cleanup**

Once you’ve processed the screenshots and converted them into PDFs, the processed test folder will be moved to the `Used/` folder. This keeps your workspace organized.

---

#### 6. **Common Errors and Troubleshooting**

- **Missing Directories**: If any of the necessary directories (`screenshots/`, `Used/`, `Tests/`, `Data/`) are missing, make sure to create them manually or let the script create them. If you're missing these directories, the script may not work correctly.
  
- **Session State Issues**: If the login session (`state.json`) is not found or has expired, you will need to run the `play.py` script again to manually log in and save the session state.

- **Permission Issues**: Ensure you have write permissions for the directories. If you're on Linux/macOS, you might need to run the scripts with `sudo` if permission errors occur.

---

#### 7. **Additional Notes**

- **Playwright Setup**: Playwright requires browser binaries to be installed, which is handled by `playwright install` during setup. If you encounter any errors related to browser installations, re-run the `playwright install` command.
  
- **Running Scripts from Correct Directory**: Always run the scripts from the root of the project directory (where the `screenshots`, `Used`, `Tests`, etc. directories are located). If you run the scripts from another location, you might encounter path issues.

  Example:

  ```bash
  cd /path/to/project_directory
  python playwriter.py
  ```

---

### Summary of Steps to Run the Project:

1. Install dependencies:
   ```bash
   pip install playwright
   playwright install
   ```

2. Run `play.py` interactively to log in and save the session:
   ```bash
   python play.py
   ```

3. Run `playwriter.py` to take screenshots:
   ```bash
   python playwriter.py
   ```

4. Run `topdflandscape.py` to generate a PDF:
   ```bash
   python topdflandscape.py
   ```

---



#Words of caution
I have hard coded which buttons to click during login, but the order on your screen may be different, appropriately change which index button it needs to press during your login session. 
