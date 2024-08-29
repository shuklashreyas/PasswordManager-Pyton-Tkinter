Password Manager
Overview
This Password Manager is a desktop application built with Python, using Tkinter for the graphical user interface (GUI). It allows users to securely store and manage their passwords, generate new strong passwords, and retrieve stored passwords when needed. The application utilizes SQLite for local data storage and supports macOS Touch ID for enhanced security. The application is designed to run on macOS and is packaged using py2app.

Features
User Authentication:
Master Password: Secure login with a master password.
Touch ID Support: Optionally use Touch ID for quick and secure authentication on supported macOS devices.
Password Storage: Store and manage passwords for multiple accounts securely using an SQLite database.
Password Generator: Generate strong, random passwords.
Encryption: All passwords are encrypted before storage to ensure security.
Cross-Platform: Designed to run on macOS.
Installation
Prerequisites
Python 3.12 or later
Homebrew (for macOS)
Tkinter (installed by default with Python on macOS)
SQLite3 (installed by default on macOS)
Step 1: Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/password-manager.git
cd password-manager
Step 2: Set Up the Virtual Environment
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Step 4: Build the Application (macOS)
Build the application using py2app:

bash
Copy code
python setup.py py2app
This will create a macOS .app bundle located in the dist directory.

Usage
Running the Application
You can run the application directly by executing the following command in the terminal:

bash
Copy code
python main.py
Or, if you have built the .app bundle, you can open it from the dist directory.

Touch ID Setup
Open the application.
On first launch, you will be prompted to set up a master password.
After setting up the master password, you can enable Touch ID by going to the "Settings" section and following the prompts.
Storing a Password
Open the application.
Enter your master password or use Touch ID to unlock the vault.
Navigate to the "Add Password" section.
Enter the details of the account (e.g., website, username, password).
Click "Save" to securely store the password in the SQLite database.
Retrieving a Password
Open the application.
Enter your master password or use Touch ID to unlock the vault.
Navigate to the "View Passwords" section.
Select the account for which you want to retrieve the password.
Database Management
The application uses an SQLite database (passwords.db) to store all user data. The database is created automatically in the application's directory.
To back up your data, simply copy the passwords.db file to a secure location.
