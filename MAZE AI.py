import threading
from tkinter import Menu, IntVar, ttk, scrolledtext, messagebox
import tkinter as tk
from MAZE_s import table_c
import time
import datetime
import os
from MAZE_s import telemessage
from PIL import Image, ImageTk
import webbrowser

color = "#f3e6f5"
# ====================================================================================


def quit_1():
    anw = messagebox.askyesno("Exit warning", "Are you sure you want to exit? \n All progress will be cleared.")
    if anw:
        win.quit()
        win.destroy()
        exit()
# ====================================================================================


def new_win():
    anw = messagebox.askyesno("Exit warning", "Are you sure you want to start a new window? \n "
                                              "All progress will be cleared.")
    if anw:
        win.destroy()
        os.startfile("MAZE AI.exe")
# ====================================================================================


godrat = """

  ****      ***      ***    ***           ***********    *****         ***      ***        ****     ***                 ***     *****
 ******     ***      ***    *********     ***********    *******       ****     ***       ******     ***               ***     *** ***
***  ***    ***      ***    ****  ****    ***            ***  ****     *****    ***      ***  ***     ***             ***     ***   ***
 ***        ***      ***    ***     ***   ***            ***   ****    ******   ***     ***    ***     ***           ***     ***     ***
  ***       ***      ***    ****  ****    ***********    ***  ****     *** ***  ***    ***      ***     ***         ***     ***       ***
   ***      ***      ***    *********     ***********    *******       ***  *** ***    ***      ***      ***       ***     *************** 
    ***     ***      ***    ***           ***            **** ***      ***   ******     ***    ***        ***     ***     *****************
***  ***    ***      ***    ***           ***            ***   ***     ***    *****      ***  ***          ***   ***     ***             ***
 ******       ***  *** *    ***           ***********    ***    ***    ***     ****       ******            *** ***     ***               ***
  ****         ******  *    ***           ***********    ***     ***   ***      ***        ****              *****     ***                 ***
 \n \n \n \n"""

# ====================================================================================


def save():
    global a
    try:
        f = open("maze_locations.txt", "x")
        f.write(godrat)
    except FileExistsError:
        f = open("maze_locations.txt", "a")

    try:
        date = str(datetime.datetime.today())
        f.write(date)
        f.write("\n\n")
        xx = a.print_beautiful_shape()
        for li in xx:
            f.write("".join(li))
            f.write("\n")
        more = messagebox.askyesno("File Saved", "We save this maze in maze_locations.txt for you. \n"
                                                 "Are you want to save more information in file? ")
        if more:
            win3 = tk.Tk()
            win3.title(" More information ")
            win3.resizable(False, False)
            win3.configure(background=color)
            tex = ttk.Label(win3, text="Write your more information here to save in file:")
            tex.grid(column=0, row=0, padx=7, pady=7)
            text_save = scrolledtext.ScrolledText(win3, width=30, height=7, wrap=tk.WORD)
            text_save.grid(column=0, row=1, padx=7)

            def info():
                f.write("More information: \n")
                f.write(text_save.get("1.0", tk.END))
                f.write("\n$====================================*-*====================================$\n")
                win3.destroy()
            click = tk.Button(win3, text="Write", command=info)
            click.grid(column=0, row=2, pady=5)
        else:
            f.write("\n$====================================*-*====================================$\n")
    except NameError:
        messagebox.showerror("so soon", "Please start the game then save it...")
# ====================================================================================


def about():
    messagebox.showinfo(" Info ", " MAZE AI \n \n Made by supernova-313 \n"
                                  " Version: 1.0.2 (system setup) \n Date: 2022-23-3")
# ====================================================================================


def connect():
    global frame1
    win2 = tk.Tk()
    win2.title(" Contact us ")
    win2.resizable(False, False)
    # win2.geometry("300x250")
    win2.configure(background=color)

    about_me = ttk.Label(win2, text=" Telegram ID : @A_R_nasa \n Discord : supernova_1#0689 ", border=1)
    about_me.grid(column=0, row=0)
    about_me.configure(background=color)

    frame1 = tk.Frame(win2, border=3)
    frame1.grid(column=0, row=2, padx=9, pady=2)
    frame1.configure(background=color)

    helping = ttk.Label(frame1, text=" You can also write your feedback anonymous in \n this section so that we can "
                                     "send it now.")
    helping.grid(column=0, row=0)
    helping.configure(background=color)

    texts = scrolledtext.ScrolledText(frame1, width=30, height=7, wrap=tk.WORD)
    texts.grid(column=0, row=1, padx=7)

    def click_s():
        text_r = texts.get("1.0", tk.END)

        if "fuck" in text_r:
            messagebox.showerror(" ara ara ", "Your text contains inappropriate words.\n Please try again.")
            win2.destroy()
        elif text_r == "\n":
            texts.configure(state="disabled")
            messagebox.showinfo(" Tnx ", "Have a great day")
            win2.destroy()
        else:
            try:
                telemessage.send(text_r)
            except:
                pass
            texts.configure(state="disabled")
            messagebox.showinfo(" Tnx ", "Thank you for sending your feedback.\n"
                                         " We save it and send it as soon as possible.")
            win2.destroy()

    send_b = ttk.Button(win2, text="Send", command=click_s)
    send_b.grid(column=0, row=4)

    win2.mainloop()
# ====================================================================================


win = tk.Tk()
win.title(" MAZE AI ")
# win.resizable(False, False)
win.configure(background=color)
menus = Menu(win, background=color)
win.config(menu=menus, background=color)
# ====================================================================================

file_menu = Menu(menus, tearoff=0, background=color)
file_menu.add_command(label="New", command=new_win)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_1)

file_menu2 = Menu(menus, tearoff=0, background=color)

file_menu2.add_command(label="connect us", command=connect)
file_menu2.add_command(label="About", command=about)

menus.add_cascade(label="File", menu=file_menu, background=color)
menus.add_cascade(label="Help", menu=file_menu2, background=color)

tabControl = ttk.Notebook(win)
tab1 = tk.Frame(tabControl, background=color)
tab2 = tk.Frame(tabControl, background=color)
tabControl.add(tab1, text=' game ')
tabControl.add(tab2, text=' pattern ')
tabControl.pack(expand=1, fill="both")
# ====================================================================================

frame1 = tk.Frame(tab1, border=3, relief="groove", highlightthickness=2)
frame1.grid(column=0, columnspan=10, row=0, padx=7, pady=3, sticky=tk.N)
frame1.configure(background=color)

titr1 = ttk.Label(frame1, text="Information : \nDraw a maze with a start point and an end point and then see the result"
                               " by pressing the start button.\n"
                               "Click the step-by-step view to see the steps to resolve the tick.", background=color)
titr1.grid(column=0, columnspan=5, row=0, sticky=tk.W, pady=5, padx=1)


position = IntVar()
wall = tk.Radiobutton(frame1, text='Wall', variable=position, value=1, fg="#5c59ff")
wall.grid(column=0, row=1, padx=4, pady=4)
wall.configure(background=color)
wall_col = tk.Button(frame1, bg="#0f0e0e", font=("Helvetica", 6), height=1, width=1, state="disabled")
wall_col.grid(column=0, row=2, padx=4, pady=4)
Empty = tk.Radiobutton(frame1, text='Empty', variable=position, value=2, fg="#5c59ff")
Empty.grid(column=1, row=1, padx=4, pady=4)
Empty.configure(background=color)
empty_col = tk.Button(frame1, bg="#ffffff", font=("Helvetica", 6), height=1, width=1, state="disabled")
empty_col.grid(column=1, row=2, padx=4, pady=4)
Start = tk.Radiobutton(frame1, text='Start', variable=position, value=3, fg="#5c59ff")
Start.grid(column=2, row=1, padx=4, pady=4)
Start.configure(background=color)
start_col = tk.Button(frame1, bg="#09ff00", font=("Helvetica", 6), height=1, width=1, state="disabled")
start_col.grid(column=2, row=2, padx=4, pady=4)
End = tk.Radiobutton(frame1, text='End', variable=position, value=4, fg="#5c59ff")
End.grid(column=3, row=1, padx=4, pady=4)
End.configure(background=color)
end_col = tk.Button(frame1, bg="#00d0ff", font=("Helvetica", 6), height=1, width=1, state="disabled")
end_col.grid(column=3, row=2, padx=4, pady=4)

step = tk.IntVar()
check1 = tk.Checkbutton(frame1, text="step-by-step", variable=step, fg="#e62e2e")
check1.grid(column=4, row=1, padx=6)
check1.configure(background=color)
# ====================================================================================

frame2 = tk.Frame(tab1, border=3, relief="groove", highlightthickness=2)
frame2.grid(column=0, columnspan=10, row=1, padx=7, pady=3, sticky=tk.N)
frame2.configure(background=color)
# ====================================================================================
point_counter = 0


def commands(x, y):
    global point_counter, walls_list, position, st_en_list, start_b
    po = position.get()

    if po == 1:
        globals()['b{}_{}'.format(x, y)].configure(bg="#0f0e0e")
        if (x, y) not in walls_list:
            walls_list.append((x, y))
        if (x, y) == st_en_list[0]:
            st_en_list[0] = 0
            point_counter -= 1
            start_b.configure(state="disabled")
        if (x, y) == st_en_list[1]:
            st_en_list[1] = 0
            point_counter -= 1
            start_b.configure(state="disabled")

    elif po == 2:
        globals()['b{}_{}'.format(x, y)].configure(bg="#ffffff")
        if (x, y) in walls_list:
            walls_list.remove((x, y))
        elif (x, y) == st_en_list[0]:
            st_en_list[0] = 0
            point_counter -= 1
            start_b.configure(state="disabled")
        elif (x, y) == st_en_list[1]:
            st_en_list[1] = 0
            point_counter -= 1
            start_b.configure(state="disabled")

    elif po == 3:
        if st_en_list[0] != 0:
            x1, y1 = st_en_list[0]
            globals()['b{}_{}'.format(x1, y1)].configure(bg="#ffffff")
        else:
            point_counter += 1
        if (x, y) in walls_list:
            walls_list.remove((x, y))
        if (x, y) == st_en_list[1]:
            st_en_list[1] = 0
            point_counter -= 1
        globals()['b{}_{}'.format(x, y)].configure(bg="#09ff00")
        st_en_list[0] = (x, y)
        if point_counter == 2:
            start_b.configure(state="active")
        else:
            start_b.configure(state="disabled")

    elif po == 4:
        if st_en_list[1] != 0:
            x1, y1 = st_en_list[1]
            globals()['b{}_{}'.format(x1, y1)].configure(bg="#ffffff")
        else:
            point_counter += 1
        if (x, y) in walls_list:
            walls_list.remove((x, y))
        if (x, y) == st_en_list[0]:
            st_en_list[0] = 0
            point_counter -= 1
        globals()['b{}_{}'.format(x, y)].configure(bg="#00d0ff")
        st_en_list[1] = (x, y)
        if point_counter == 2:
            start_b.configure(state="active")
        else:
            start_b.configure(state="disabled")


walls_list = []
st_en_list = [0, 0]
list_of_button = []
for j in range(20):
    for i in range(30):
        globals()['b{}_{}'.format(i, j)] = tk.Button(frame2, command=lambda x=i, y=j: commands(x, y),
                                                     font=("Helvetica", 2), height=1, width=1, bg="#ffffff")
        globals()['b{}_{}'.format(i, j)].grid(column=i, row=j, padx=1, pady=1)
        if i in [0, 29] or j in [0, 19]:
            globals()['b{}_{}'.format(i, j)].configure(bg="#0f0e0e")
            walls_list.append((i, j))

        list_of_button.append('b{}_{}'.format(i, j))
# ====================================================================================


def start():
    global start_b, list_of_button, walls_list, wall, st_en_list, Empty, Start, End, check1, step, a, point_counter
    start_b.configure(state="disabled", text="Restart")
    wall.configure(state="disabled")
    Empty.configure(state="disabled")
    Start.configure(state="disabled")
    End.configure(state="disabled")
    check1.configure(state="disabled")
    for bu in list_of_button:
        globals()[bu].configure(state="disabled")
    steps = step.get()
    a = table_c.Table(x=30, y=20)
    a.add_st_end(start=st_en_list[0], end=st_en_list[1])
    a.add_wall(*walls_list)
    result = a.processing()

    def restart():
        global st_en_list, point_counter
        start_b.configure(state="disabled", command=start, text="START")
        wall.configure(state="normal")
        Empty.configure(state="normal")
        Start.configure(state="normal")
        End.configure(state="normal")
        check1.configure(state="normal")
        st_en_list = [0, 0]
        point_counter = 0
        walls_list.clear()
        for butt in list_of_button:
            globals()[butt].configure(state="normal", bg="#ffffff")
        for s in range(20):
            for d in range(30):
                if d in [0, 29] or s in [0, 19]:
                    globals()['b{}_{}'.format(d, s)].configure(bg="#0f0e0e")
                    walls_list.append((d, s))

    if result:
        if steps == 1:

            def step_gen():
                all_step = a.step_by_step()
                for step_p in all_step:
                    for block_1 in step_p:
                        fe1, se2 = block_1
                        globals()["b{}_{}".format(fe1, se2)].configure(bg="#f2ff00")
                    time.sleep(0.25)

                final_s = a.road()
                for block_s in final_s:
                    fes, ses = block_s
                    globals()["b{}_{}".format(fes, ses)].configure(bg="#ff0000")
                start_b.configure(state="normal", command=restart)

            thread = threading.Thread(target=step_gen)
            thread.start()

        else:
            final = a.road()
            for block in final:
                fe, se = block
                globals()["b{}_{}".format(fe, se)].configure(bg="#ff0000")
            start_b.configure(state="normal", command=restart)

    else:
        messagebox.showerror("Wrong Maze", "There is no way to that point!!\nPleas edit your Maze.")
        start_b.configure(state="normal", text="START")
        wall.configure(state="normal")
        Empty.configure(state="normal")
        Start.configure(state="normal")
        End.configure(state="normal")
        check1.configure(state="normal")
        for but in list_of_button:
            globals()[but].configure(state="normal")


start_b = tk.Button(tab1, command=start, state="disabled", text="START", font=("Helvetica", 13))
start_b.grid(column=0, columnspan=10, row=3, padx=1, pady=1)

# ====================================================================================
tk.Label(tab2, text="First pattern:", bg=color).grid(column=0, row=0)

img = Image.open("MAZE_s/maze2.png")
img = img.resize((450, 280))
tk_image = ImageTk.PhotoImage(img)
fi = tk.Label(tab2, image=tk_image).grid(column=1, columnspan=10, row=0)

tk.Label(tab2, text="Second pattern:", bg=color).grid(column=0, row=1)
img2 = Image.open("MAZE_s/maze3.png")
img2 = img2.resize((300, 300))
tk_image2 = ImageTk.PhotoImage(img2)
si = tk.Label(tab2, image=tk_image2).grid(column=1, columnspan=10, row=1)


def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


tk.Label(tab2, text="for use more maze pattern see :", bg=color).grid(column=0, columnspan=5, row=2, padx=5, pady=5)

lbl = tk.Label(tab2, text=r"https://en.wikipedia.org/wiki/Maze", fg="blue", cursor="hand2", bg=color)
lbl.grid(column=5, columnspan=10, row=2)
lbl.bind("<Button-1>", callback)

win.mainloop()
