import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

g = tk.Tk()

g.geometry("400x400+1100+100")
g.resizable(True, True)

Frame = ttk.Frame(g)
t = tk.Text(Frame, width=10, height=5)
t.grid(column=0, row=0)

h = ttk.Scrollbar(Frame, orient='vertical', command=t.yview)
h.grid(column=1, row=0, sticky='NS')

t['yscrollcommand'] = h.set
Frame.pack()
Frame.place(x=10, y=8)


def gh(mn):
    if c.get() == 'Blue':
        t['background'] = '#aac2fe'
        j['background'] = '#aac2fe'
        qr['background'] = '#aac2fe'
    if c.get() == 'Yellow':
        t['background'] = '#fcffa6'
        j['background'] = '#fcffa6'
        qr['background'] = '#fcffa6'
    if c.get() == 'Green':
        t['background'] =  '#9fffa6'
        j['background'] = '#9fffa6'
        qr['background'] = '#9fffa6'


def mg(asd):
    a = (L.curselection())
    g.title(rola[int((list(a))[0])])


qe = ttk.Style()
qe.theme_use('vista')
qe.configure('malakoi.TButton', foreground='yellow', background='green')

b = ttk.Separator(g, orient='vertical')
b.pack(fill=tk.Y)

j = ScrolledText(width=10, height=5)
j.pack()
j.place(x=140, y=8)

jk = tk.StringVar()
c = ttk.Combobox(g, textvariable=jk, state='readonly')
c.set('*****')
c['values'] = ('Blue', 'Yellow', 'Green')

c.bind('<<ComboboxSelected>>', gh)

c.pack()
c.place(x=245, y=8)

rola = ['oi', 'thcua', 'gblo']
listasla = tk.Variable(value=rola)
L = tk.Listbox(g, listvariable=listasla, height=3, selectmode=tk.EXTENDED)
L.bind('<<ListboxSelect>>', mg)
L.pack()
L.place(x=245, y=30)


def hj(sd):
    bv['text'] = '{: .0f}'.format(kl.get())
    qr.pack(padx='{: .0f}'.format(kl.get()))


mn = ttk.Frame(g)
kl = tk.DoubleVar()
slider = ttk.Scale(
    mn,
    from_=0,
    to=100,
    orient='horizontal',
    length=80,
    command=hj,
    variable=kl
)

slider.grid(column=0, row=0)
bv = ttk.Label(mn, text='0')
bv.grid(column=0, row=1, pady=0, padx=10)
mn.pack()
mn.place(x=13, y=100)


def polonia():
    print(spi.get())
    qr.pack(pady=(spi.get()))


spi = tk.StringVar()
sp = ttk.Spinbox(g, from_=0, to=10, textvariable=spi, wrap=True, command=polonia, width=5)


sp.pack()
sp.place(x=160, y=105)

sz = ttk.Sizegrip(g)
sz.pack()
sz.place(x=385, y=385)

lf = ttk.Labelframe(text='ronaldinho')
gkl = ttk.Button(lf, text='wer', style='malakoi.TButton')
gkl.pack()

lf.pack()
lf.place(x=15, y=150)

gj = ttk.Notebook(g)
gj.pack()
gj.place(x=0, y=225)

frames = tk.Canvas(gj, width=400, height=150, background='black')
frames.pack()
frame2 = ttk.Frame(gj, width=100, height=150)
frame2.pack()

ql = tk.Canvas(frame2, width=380, height=130, background='purple')
ql.pack()
ql.place(y=9, x=7)

nom = ttk.Label(frame2, text='asdasd')
nom.pack()

imagem = tk.PhotoImage(file='D s.PNG')
gj.add(frames, text="rolon")
gj.add(frame2, text="alads")


qr = tk.Canvas(frames, width=380, height=130, background='yellow')
qr.pack(padx=6, pady=10)

g.mainloop()
