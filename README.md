Secure Your Files
Secure Your Files is a Python script that allows you to encrypt and decrypt files using AES encryption. It provides a graphical user interface (GUI) built with tkinter for easy file selection and encryption/decryption operations.

Features
File Encryption: Encrypt a single file or multiple files simultaneously to protect sensitive data.
File Decryption: Decrypt encrypted files back to their original format for easy access and use.
Random Encryption Key: Generates a random encryption key for each session, ensuring strong encryption.
AES Encryption with CBC Mode: Utilizes AES (Advanced Encryption Standard) encryption algorithm with Cipher Block Chaining (CBC) mode for enhanced security.
PKCS7 Padding: Implements padding with PKCS7 standard to ensure compatibility and proper block alignment.
User-Friendly GUI: Provides a graphical user interface with an intuitive design, inspired by the Discord theme, making it easy to select files and perform encryption or decryption operations.
Dependencies
Python 3.x: Make sure you have Python 3.x installed on your machine.
Crypto library: Install the library by running pip install pycryptodome in your terminal.
tkinter library: Usually included in the Python standard library.
Usage
Clone or download the repository to your local machine.
Open a terminal or command prompt and navigate to the project directory.
Ensure that you have Python 3.x installed.
Install the necessary dependencies by running pip install pycryptodome.
Run the script using the command python Secure_Your_Files.py.
The graphical user interface (GUI) will open, allowing you to select files and perform encryption or decryption operations.
Use the "Encrypt File" button to select one or more files and encrypt them using AES encryption.
Use the "Decrypt File" button to select encrypted files and decrypt them back to their original format.
To view the encryption key used for the session, click on the "Show Key" button.
License
This project is licensed under the MIT License - see the LICENSE file for details.
