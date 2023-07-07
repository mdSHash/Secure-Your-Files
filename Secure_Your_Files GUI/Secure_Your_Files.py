import os
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import tkinter as tk
from tkinter import filedialog, messagebox

class FileEncrypterDecrypter:
    def __init__(self):
        self.key_filename = "key.txt"
        self.key = self.get_key()

        self.root = tk.Tk()
        self.root.title("Secure Your Files")
        self.root.geometry("400x500")

        # Set Discord theme-like appearance
        self.root.configure(bg="#36393F")

        self.author_label = tk.Label(
            self.root, text="Script Maker", fg="#FFFFFF", bg="#36393F"
        )
        self.author_label.pack(pady=5)

        self.title_label = tk.Label(
            self.root, text="Secure Your Files", fg="#FFFFFF", bg="#36393F"
        )
        self.title_label.pack(pady=5)

        self.encrypt_button = tk.Button(
            self.root,
            text="Encrypt File",
            command=self.on_encrypt,
            bg="#7289DA",
            fg="#FFFFFF",
            font=("Arial", 12, "bold")
        )
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(
            self.root,
            text="Decrypt File",
            command=self.on_decrypt,
            bg="#7289DA",
            fg="#FFFFFF",
            font=("Arial", 12, "bold")
        )
        self.decrypt_button.pack(pady=10)

        self.show_key_button = tk.Button(
            self.root,
            text="Show Key",
            command=self.show_key,
            bg="#7289DA",
            fg="#FFFFFF",
            font=("Arial", 12, "bold")
        )
        self.show_key_button.pack(pady=10)

        # Center the window on the screen
        self.root.eval('tk::PlaceWindow . center')

        self.root.mainloop()

    def generate_key(self):
        # Generate a random key
        key = secrets.token_bytes(16)
        with open(self.key_filename, "wb") as f:
            f.write(key)
        return key

    def get_key(self):
        if os.path.exists(self.key_filename):
            with open(self.key_filename, "rb") as f:
                key = f.read()
        else:
            key = self.generate_key()
        return key

    def encrypt_file(self, filename):
        # Encrypt a file using AES encryption
        iv = secrets.token_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        with open(filename, "rb") as f:
            plaintext = f.read()
        padded_plaintext = pad(plaintext, AES.block_size)
        ciphertext = iv + cipher.encrypt(padded_plaintext)
        encrypted_filename = filename + ".enc"
        with open(encrypted_filename, "wb") as f:
            f.write(ciphertext)

    def decrypt_file(self, filename):
        # Decrypt a file using AES decryption
        with open(filename, "rb") as f:
            ciphertext = f.read()
        iv = ciphertext[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext[16:])
        plaintext = unpad(padded_plaintext, AES.block_size)
        decrypted_filename = os.path.splitext(filename)[0]
        with open(decrypted_filename, "wb") as f:
            f.write(plaintext)

    def encrypt_files(self, filenames):
        # Encrypt multiple files
        for filename in filenames:
            self.encrypt_file(filename)

    def decrypt_files(self, filenames):
        # Decrypt multiple files
        for filename in filenames:
            self.decrypt_file(filename)

    def on_encrypt(self):
        # Event handler for encrypt button
        filenames = filedialog.askopenfilenames()
        if not filenames:
            messagebox.showerror("File Error", "No files selected")
            return
        try:
            self.encrypt_files(filenames)
            messagebox.showinfo("Encryption Complete", "Encryption complete")
        except Exception as e:
            messagebox.showerror(
                "Encryption Error", f"An error occurred while encrypting the files: {e}"
            )

    def on_decrypt(self):
        # Event handler for decrypt button
        filenames = filedialog.askopenfilenames()
        if not filenames:
            messagebox.showerror("File Error", "No files selected")
            return
        try:
            self.decrypt_files(filenames)
            messagebox.showinfo("Decryption Complete", "Decryption complete")
        except Exception as e:
            messagebox.showerror(
                "Decryption Error", f"An error occurred while decrypting the files: {e}"
            )

    def show_key(self):
        # Display the encryption key
        messagebox.showinfo("Encryption Key", self.key.hex())


if __name__ == "__main__":
    app = FileEncrypterDecrypter()
