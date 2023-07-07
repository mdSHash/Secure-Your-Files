# Secure Your Files

This is a Python script that provides a graphical user interface (GUI) for encrypting and decrypting files using the Advanced Encryption Standard (AES) algorithm. The script uses the `Crypto` package to implement AES encryption and decryption.
in the program files you can found an Secure_Your_files.exe & Secure_Your_Files.py.

## Features

- Encrypts and decrypts files using AES encryption
- Supports encryption and decryption of multiple files at once
- Displays the encryption key used for encryption
- Provides a user-friendly GUI for easy file selection and encryption/decryption
- exe file

## How to Use

### Installation

To use the script, ensure that you have Python 3 installed on your system. You can download Python 3 from the official website.

In addition, you need to install the `Crypto` package. You can do this using pip by running the following command:

```sh
pip install pycrypto
```

### Running the Script

To run the script, simply execute the following command in the directory containing the script:

```sh
python Secure_Your_Files.py
```

The GUI will be displayed, allowing you to select files to encrypt or decrypt.

### Encryption

To encrypt one or more files, click the "Encrypt File" button. A file dialog will appear, allowing you to select one or more files to encrypt. Once you have selected the files, click the "Open" button to begin the encryption process.

The encrypted files will be saved with the extension `.enc` appended to the original filename.

### Decryption

To decrypt one or more files, click the "Decrypt File" button. A file dialog will appear, allowing you to select one or more files to decrypt. Once you have selected the files, click the "Open" button to begin the decryption process.

The decrypted files will be saved with the original filename, without the `.enc` extension.

### Display Key

To display the encryption key, click the "Show Key" button. The key will be displayed in a message box. You can copy the key to a secure location for safekeeping.

## Dependencies

This script requires the following Python packages:

- `Crypto` (for AES encryption and decryption)
- `tkinter` (for GUI components)

## Limitations

The script currently only supports AES encryption with a key size of 128 bits.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
