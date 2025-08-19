from customtkinter import *

font = ("Bahnschrift", 16)
root = CTk()
root.geometry("400x450")
root.resizable(width=False, height=False)
root.title("CALCULATOR")
root.iconbitmap("s0urcec0de.ico")

ScreenFrame = CTkFrame(root)
InputLabel = CTkLabel(ScreenFrame, height=50, fg_color="white", text_color="gray45", text="", font=font,
                      anchor=E, corner_radius=10)
ResultLabel = CTkLabel(ScreenFrame, height=70, fg_color="#cfcfcf", text_color="#2FA572", text="",
                        font=("Bahnschrift", 28), anchor=E, corner_radius=10)

# Declaring a few global variables we will use for our operations
N_1 = []
N_2 = []
n_1 = ""
n_2 = ""
opp = ""
key = ""
answer = ""
operations = {}


def calculate():
    """Performs the calculations of the calculator"""
    global answer, N_1
    if N_2 and (N_1 != ["-"] or N_2 != ["-"]):
        update_globals()
        try:
            answer = operations[key]
            if answer != "Error":
                if not str(abs(answer)).isdecimal():
                    parts = str(answer).split(".")
                    if parts[1] == "0":
                        answer = int(answer)
                ResultLabel.configure(text=str(round(answer, 4)))
                answer = str(round(answer, 4))
            else:
                ResultLabel.configure(text=f"{answer}")
        except KeyError:
            pass
        else:
            N_1 = [i for i in str(answer)]
            N_2.clear()


def clear_all():
    """Resets all the global variables and updates the result display and input area"""
    global n_1, n_2, opp, key, answer
    N_1.clear()
    N_2.clear()
    n_1 = ""
    n_2 = ""
    opp = ""
    key = ""
    answer = ""
    update_globals()


def delete():
    """Deletes the last element shown on the input area"""
    global opp
    if N_2:
        N_2.pop()
        update_globals()
    elif opp:
        opp = ""
        update_globals()
    elif N_1:
        N_1.pop()
        update_globals()


def update_globals():
    """Updates the value of the global variables and displays the result on the input area and result display"""
    global opp, key, n_2, n_1, operations, answer
    n_1 = ''.join(N_1)
    n_2 = ''.join(N_2)

    key = f"{n_1} {opp} {n_2}"
    if n_1 == "Error":
        clear_all()
    if "." in n_1:
        parts = n_1.split(".")
        if parts[1] == "0":
            n_1 = int(n_1)
        else:
            n_1 = float(n_1)
    elif not n_1 or n_1 == "-":
        pass
    else:
        n_1 = int(n_1)

    if "." in n_2:
        parts = n_2.split(".")
        if parts[1] == "0":
            n_2 = int(n_2)
        else:
            n_2 = float(n_2)
    elif not n_2 or n_2 == "-":
        pass
    else:
        n_2 = int(n_2)

    try:
        operations = {
            f"{n_1} + {n_2}": n_1 + n_2,
            f"{n_1} - {n_2}": n_1 - n_2,
            f"{n_1} / {n_2}": n_1 / n_2,
            f"{n_1} * {n_2}": n_1 * n_2
        }
    except TypeError:
        pass
    except ZeroDivisionError:
        operations = {
            f"{n_1} + {n_2}": n_1 + n_2,
            f"{n_1} - {n_2}": n_1 - n_2,
            f"{n_1} / {n_2}": "Error",
            f"{n_1} * {n_2}": n_1 * n_2
        }
        InputLabel.configure(text=key)
        ResultLabel.configure(text=answer)

    InputLabel.configure(text=key)
    ResultLabel.configure(text=answer)


class CustomButton(CTkButton):
    def __init__(self, master, kind, **kwargs):
        self.kind = kind
        super().__init__(master, **kwargs)
        self.configure(width=73.5, height=69.5, font=font, border_width=1, border_color="gray13", command=self.btn_func)
        if self.kind == "item" or self.kind == "operation":
            root.bind(f"{self.cget('text')}", lambda event: self.btn_func())

    def btn_func(self):
        func_dict = {"item": self.set_item,
                     "operation": self.set_operation,
                     "delete": delete,
                     "equals_to": calculate,
                     "clear": clear_all}
        func_dict[self.kind]()

    def set_operation(self):
        sym = self.cget("text")
        """Sets the operational symbol"""
        global opp
        calculate()
        if N_1:
            opp = sym
        calculate()
        update_globals()

    def set_item(self):
        item = self.cget("text").removeprefix("(").removesuffix(")")
        if not opp:
            if not N_1:
                if item == "-":
                    N_1.append(item)
                elif item.isnumeric():
                    N_1.append(item)
            else:
                if item != "-":
                    N_1.append(item)
        else:
            if not N_2:
                if item == "-":
                    N_2.append(item)
                elif item.isnumeric():
                    N_2.append(item)
            else:
                if item != "-":
                    N_2.append(item)
        update_globals()
