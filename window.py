import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import ehentaiz2e
import shutil


class windowsMain(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.pack()
        self.createFrame()

    def createFrame(self):
        # self.lablel = tkinter.Label(self, text='Hello')
        self.entry = tkinter.Entry(self, width=48)

        button1 = tkinter.Button(self, text='打开文件', command=self.button1)

        button2 = tkinter.Button(self, text='转换', command=self.button2)

        button3 = tkinter.Button(self, text='清理缓存', command=self.button3)

        # self.lablel.grid(row=0, column=1)

        self.entry.grid(row=1, column=0)
        button1.grid(row=1, column=1)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=0)

    def button1(self):
        path_ = tkinter.filedialog.askopenfilename(
            title='请选择文件',
        filetypes=[('压缩包', '.zip .ZIP')])

        if path_ == '':
            return
        path_ = path_.replace("/","////")

        self.name = path_.split('////')[-1]

        self.entry.delete(0, "end")
        self.entry.insert(0, path_)

    def button2(self):
        if not os.path.exists('./.cache'):
            os.makedirs('./.cache')
        self.entry.get()

        (filepath, filename) = os.path.split(self.entry.get())

        print(filename)

        try:
            shutil.copy(self.entry.get(), f'./.cache/{self.name}')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)

        ehentaiz2e.z2b(self.name, 'cover.jpg')

        try:
            shutil.copy(f'./.cache/{filename[:-4]}/output.epub', f'{filepath}/{filename[:-4]}.epub')
        except FileExistsError:
            pass
        except Exception as e:
            # print(f'./.cache/{filename[-4]}/output.epub', filename[:-4])
            print(e)
        tkinter.messagebox.showinfo('完成', '转换完成')

    def button3(self):
        shutil.rmtree('./.cache')
        tkinter.messagebox.showinfo('完成', '缓存清理完成')

tk = tkinter.Tk()

tk.geometry("500x200+100+50")
tk.title('zip转epub')

app = windowsMain(tk)

tk.mainloop()