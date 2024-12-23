import tkinter as tk
from tkinter import filedialog, messagebox
from file_handler import read_file, write_file
from crypto import encrypt, decrypt

def run_gui():
    root = tk.Tk()
    root.title("Шифровщик файлов")
    root.geometry('900x500+1200+500')
    tk.Label(root, text="Выбранный файл:").pack(padx=10, pady=5)
    entry_file = tk.Entry(root, width=500)
    entry_file.pack(padx=10, pady=5)
    tk.Button(root, text="Выбрать файл",width=20, height=5, command=lambda: choose_file(entry_file)).pack(padx=80, pady=30)
    tk.Button(root, text="Зашифровать",width=20, height=5, command=lambda: handle_encrypt(entry_file)).pack(padx=80, pady=30)
    tk.Button(root, text="Расшифровать",width=20, height=5, command=lambda: handle_decrypt(entry_file)).pack(padx=80, pady=30)
    root.mainloop()

def choose_file(entry_file):
    file_path = filedialog.askopenfilename(title='Выберите файл')
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)

def handle_encrypt(entry_file):
    file_path = entry_file.get()
    if file_path:
        try:
            data = read_file(file_path)
            encrypted_data = encrypt(data)
            write_file(file_path + '.enc', encrypted_data)
            messagebox.showinfo("Успешно!", f"Файл {file_path} успешно зашифрован в {file_path + '.enc'}!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"В процессе шифрования возникла ошибка: {e}")

def handle_decrypt(entry_file):
    file_path = entry_file.get()
    if file_path:
        if file_path[-4:] != '.enc':
            messagebox.showinfo("Ошибка!", f"Файл {file_path} не является зашифрованным!")
            return
        try:
            data = read_file(file_path)
            decrypted_data = decrypt(data)
            write_file(file_path[:-4], decrypted_data)
            messagebox.showinfo("Успешно!", f"Файл {file_path} успешно расшифрован в {file_path[:-4]}!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"В процессе расшифровывания возникла ошибка: {e}")