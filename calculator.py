# Importing necessary modules
import customtkinter
from functions import *

customtkinter.set_default_color_theme("green")

# Creating and styling the result display

ScreenFrame.pack(side="top", fill=X, padx=15, pady=15)
ResultLabel.pack(side=TOP, fill=X)
InputLabel.pack(side=TOP, fill=X)

btn_frame = CTkFrame(root)


for i in range(4):
    btn_frame.rowconfigure(i, minsize=0)
    btn_frame.columnconfigure(i, minsize=0)

one_btn = CustomButton(btn_frame, kind="item", text="1")
one_btn.grid(row=0, column=0)

two_btn = CustomButton(btn_frame, kind="item", text="2")
two_btn.grid(row=0, column=1)

three_btn = CustomButton(btn_frame, kind="item", text="3")
three_btn.grid(row=0, column=2)

four_btn = CustomButton(btn_frame, kind="item", text="4")
four_btn.grid(row=1, column=0)

five_btn = CustomButton(btn_frame, kind="item", text="5")
five_btn.grid(row=1, column=1)

six_btn = CustomButton(btn_frame, kind="item", text="6")
six_btn.grid(row=1, column=2)

seven_btn = CustomButton(btn_frame, kind="item", text="7")
seven_btn.grid(row=2, column=0)

eight_btn = CustomButton(btn_frame, kind="item", text="8")
eight_btn.grid(row=2, column=1)

nine_btn = CustomButton(btn_frame, kind="item", text="9")
nine_btn.grid(row=2, column=2)

zero_btn = CustomButton(btn_frame, kind="item", text="0")
zero_btn.grid(row=3, column=1)

point_btn = CustomButton(btn_frame, kind="item", text=".")
point_btn.grid(row=3, column=0)

negate_btn = CustomButton(btn_frame, kind="item", text="(-)")
negate_btn.grid(row=3, column=2)

clear_btn = CustomButton(btn_frame, kind="clear", text="A/C")
clear_btn.grid(row=0, column=3)

delete_btn = CustomButton(btn_frame, kind="delete", text="\u2190")
delete_btn.grid(row=0, column=4)

plus_btn = CustomButton(btn_frame, kind="operation", text="+")
plus_btn.grid(row=1, column=3)

minus_btn = CustomButton(btn_frame, kind="operation", text="-")
minus_btn.grid(row=2, column=3)


multiply_btn = CustomButton(btn_frame, kind="operation", text="*")
multiply_btn.grid(row=1, column=4)

divide_btn = CustomButton(btn_frame, kind="operation", text="/")
divide_btn.grid(row=2, column=4)

equals_btn = CustomButton(btn_frame, kind="equals_to", text="=")
equals_btn.grid(row=3, column=3, columnspan=2, sticky="NSEW")

btn_frame.pack(side=TOP, fill=BOTH, expand=1, padx=15, pady=10)

root.bind("<Return>", lambda event: calculate())
root.bind("<BackSpace>", lambda event: delete())
root.bind("<Delete>", lambda event: clear_all())

root.mainloop()
