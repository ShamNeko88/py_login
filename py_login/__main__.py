import tkinter as tk
from tkinter import ttk


"""
エントリーポイント
アプリの起動
"""
def main():
    # 親インスタンス設定
    root = tk.Tk() # 一番上のインスタンス作成
    root.title("ログインテスト")
    root.geometry("300x200")
    # 親インスタンスに対して子インスタンス設定
    app = App(master=root) # rootインスタンスを親としたインスタンス生成
    app.mainloop() # 画面表示



"""
アプリクラス
"""
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="gray")
        self.master = master # 親インスタンス
        self.pack()
        self.widgets(self) # ウィジェット配置
        self.home = Home(master=self) # ホームインスタンス生成

    def widgets(self, master):
        self.txt = ttk.Label(master, text="アプリフレーム")
        self.txt.pack()
        self.del_button = ttk.Button(master, text="アプリフレーム削除", command=self.del_process)
        self.del_button.pack()
    
    def del_process(self):
        self.destroy()
"""
ホーム画面クラス
"""
class Home(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="skyblue")
        self.master = master # 親インスタンス
        self.pack()
        self.widgets(master) # ウィジェット配置

    def widgets(self, master):
        self.txt = ttk.Label(master, text="ホーム画面フレーム")
        self.txt.pack()
        self.del_button = ttk.Button(master, text="ホームフレーム削除", command=self.del_process)
        self.del_button.pack()
        
    def del_process(self):
        self.destroy()

if __name__ == "__main__":
    main()
    