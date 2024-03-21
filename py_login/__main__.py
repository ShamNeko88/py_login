import tkinter as tk
from tkinter import ttk

def main():
    home = Home()
    home.display()

class Home():
    def display(self):
        self.home = tk.Tk()
        self.home.geometry("300x200")
        self.home.title("HOME")
        self.home.mainloop()




if __name__ == "__main__":
    main()