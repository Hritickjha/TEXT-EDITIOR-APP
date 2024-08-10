import tkinter as tk
from tkinter import filedialog, scrolledtext

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill="both")
        
        self.create_menu()
        
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all_text)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        self.root.config(menu=menu_bar)
        
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("Text Editor")
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, content)
            self.root.title(f"Text Editor - {file_path}")
        
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.root.title(f"Text Editor - {file_path}")
                
    def save_as_file(self):
        self.save_file()
        
    def exit_app(self):
        self.root.quit()
        
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")       
            
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
        
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")
        
    def select_all_text(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        return "break"

def main():
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()   

if __name__ == "__main__":
    main()

            
            