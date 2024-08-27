from setuptools import setup

APP = ['main.py']  # Replace with the name of your main script
DATA_FILES = [
    'background.jpg',
    'azure.tcl',
    'Azure-ttk-theme-main/theme/dark.tcl',
    'Azure-ttk-theme-main/theme/light.tcl'
]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL', 'tkinter'],  # Include packages that need to be bundled
    'plist': {
        'CFBundleName': 'PasswordManager',  # The name of your app
        'CFBundleDisplayName': 'Password Manager',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    },
    'resources': DATA_FILES,  # Include additional resources
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
