import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from py_login import config as con

def main():
    home = Home() # ホーム画面クラスインスタンス生成
    home.display() # 画面起動

"""
HOME画面クラス
"""
class Home():
    def display(self):
        # HOME画面作成と配置
        self.home = tk.Tk()
        self.home.geometry("300x100")
        self.home.title("HOME")
        # ログイン画面へ移動ボタン作成と配置
        self.login_btn = ttk.Button(self.home, text="ログイン画面へ", command=self.to_login_page)
        self.login_btn.pack(pady=25)
        # ログイン画面クラス生成
        self.login = Login()


        # ループで画面表示
        self.home.mainloop()
        
    def to_login_page(self):
        self.home.destroy()
        self.login.display()
        
"""
ログイン画面クラス
"""
class Login():
    def display(self):
        self.login = tk.Tk()
        self.login.geometry("300x100")
        self.login.title("Login")
        # ユーザー名入力欄作成と配置
        self.user_nm = ttk.Label(self.login, text="ユーザー名")
        self.user_nm.grid(row=0, column=0, padx=30, pady=5)
        self.user_nm_entry = ttk.Entry(self.login)
        self.user_nm_entry.grid(row=0, column=1, pady=5)
        # パスワード入力欄作成と配置
        self.password = ttk.Label(self.login, text="パスワード")
        self.password.grid(row=1, column=0, padx=30, pady=5)
        self.password_entry = ttk.Entry(self.login, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        # ログインボタン作成と配置
        self.login_btn = ttk.Button(self.login, text="ログイン", command=self.login_process)
        self.login_btn.grid(row=2, column=1, padx=30, pady=5)
        # 画面クラス生成
        self.app = Application()

    # ログイン処理
    def login_process(self):
        try:
          self.password_entry.get() == con.user_info[f"{self.user_nm_entry.get()}"]
          self.app.display(self.user_nm_entry.get())
        except KeyError:
            mb.showerror("エラー", "ログインできませんでした。")
"""
ログイン後の画面クラス
"""
class Application():
    def display(self, user_name):
        self.app = tk.Tk()
        self.app.geometry("400x300")
        self.app.title("アプリ画面")
        # テキスト
        self.app_text = ttk.Label(self.app, text=f"{user_name}でログインしました。")
        self.app_text.pack()

if __name__ == "__main__":
    main()