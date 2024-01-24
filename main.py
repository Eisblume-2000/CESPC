import json
import tkinter as tk
from tkinter import filedialog
import webbrowser
from datetime import datetime

class Main:
    import python_nbt.nbt as nbt
    #have no clue why but for some reason this needs to be imported in the class
    def __init__(self):
        try:
            self.GUI = tk.Tk()
            self.GUI.geometry("900x800")
            self.GUI.resizable(0, 0)
            self.GUI.title("CESPC")
            self.GUI['background'] = '#202124'

            self.welcomelabel = tk.Label(self.GUI, text="Preis Rechner für Schematics (CESPC)", fg="#c7c6c3", font=("Arial", 20), bg="#202124")
            self.welcomelabel.place(y=50, relx=0.5, anchor="center", width=700)

            self.buttonfileinput = tk.Button(self.GUI, text="Datei Pfad der Schematic", fg="#c7c6c3", font=("Arial", 15), width=20, height=2, bg="#3c3d42", command=self.filegraber)
            self.buttonfileinput.place(y=250, relx=0.5, anchor="center")

            self.prompt2 = tk.Label(self.GUI, text="Ausgewählte Datei: ", fg="#c7c6c3", font=("Arial", 15),bg="#202124")
            self.prompt2.place(y=325, relx=0.5, anchor="center", width=700)

            self.calcbutton = tk.Button(self.GUI, text="Kalkulation starten", fg="#c7c6c3", font=("Arial", 15), width=20, height=2, bg="#3c3d42", command=self.CalcGUI)
            self.calcbutton.place(y=450, relx=0.5, anchor="center")

            self.buttonframe1 = tk.Frame(self.GUI)
            self.buttonframe1.columnconfigure(0, weight=1)
            self.buttonframe1.columnconfigure(1, weight=1)

            self.buttonclose = tk.Button(self.buttonframe1, text="Close", fg="#c7c6c3", font=("Arial", 15), width=20, height=2, bg="#3c3d42", command=self.close)
            self.buttonclose.grid(row=0, column=0)

            # Button for settings menu
            self.buttonsettings = tk.Button(self.buttonframe1, text="Settings", fg="#c7c6c3", font=("Arial", 15), width=20, height=2, bg="#3c3d42", command=self.SettinsGUI)
            self.buttonsettings.grid(row=0, column=1)

            # Button to github page
            self.buttonabout = tk.Button(self.buttonframe1, text="Credits", fg="#c7c6c3", font=("Arial", 15), width=20, height=2, bg="#3c3d42", command=self.about)
            self.buttonabout.grid(row=0, column=2)

            self.buttonframe1.place(y=700, relx=0.5, anchor="center")

            self.GUI.mainloop()

        except Exception as e:
            timeanddate = datetime.now()
            timeanddate = str(timeanddate)
            e = str(e)
            r = open(r"debuglog.txt", "a")
            r.write(timeanddate)
            r.write("\n")
            r.write(str(e))
            r.write("\n")
            r.close()

            ErrorGUI = tk.Tk()
            ErrorGUI.geometry("900x800")
            ErrorGUI.resizable(0, 0)
            ErrorGUI.title("CESPC")
            ErrorGUI['background'] = '#202124'

            errorprompt = tk.Text(ErrorGUI, height=10, borderwidth=0, fg="#c7c6c3", font=("Arial", 15), bg="#202124")
            errorprompt.insert(1.0, e)
            errorprompt.place(y=200, relx=0.5, anchor="center")

            ErrorGUI.mainloop()

    def filegraber(self):
        self.filepath = tk.filedialog.askopenfilename()
        self.prompt2 = tk.Label(self.GUI, text="Ausgewählte Datei: \n" + self.filepath, fg="#c7c6c3", font=("Arial", 15), bg="#202124")
        self.prompt2.place(y=325, relx=0.5, anchor="center", width=700)


    def SettinsGUI(self):

        self.configGUI = tk.Tk()
        self.configGUI.geometry("900x800")
        self.configGUI.resizable(0, 0)
        self.configGUI.title("CESPC-Einstellungen")
        self.configGUI['background'] = '#202124'

    def about(self):
        url = "https://github.com/Eisblume-2000/CESPC"
        webbrowser.open(url)

    def close(self):
        self.GUI.destroy()
        exit()

    def CalcGUI(self):
        try:
            self.blockcounter(self.filepath)
            self.ignored_blocks_count, self.priceless_blocks_count, self.combined_block_price = self.line_slicer()

            self.CalcuGUI = tk.Tk()
            self.CalcuGUI.geometry("700x800")
            self.CalcuGUI.resizable(0, 0)
            self.CalcuGUI.title("CESPC-Ergebnis")
            self.CalcuGUI['background'] = '#202124'

            self.calcwelcomelabeltk = tk.Label(self.CalcuGUI, text="Ergebniss für Schematic: \n" + self.filepath, fg="#c7c6c3", font=("Arial", 15), bg="#202124")
            self.calcwelcomelabeltk.place(y=150, relx=0.5, anchor="center", width=700)


            self.combined_block_price_prompt = tk.Label(self.CalcuGUI, text="Ungefährer Preis aller Resourcen (in Talern): \n" + str(self.combined_block_price), fg="#c7c6c3", font=("Arial", 15), bg="#202124")
            self.combined_block_price_prompt.place(y=250, relx=0.5, anchor="center", width=700)

            self.priceless_blocks_count_prompt = tk.Label(self.CalcuGUI, text="So viele Blöcke sind nicht am Spawn erhältlich oder Craftbar: \n" + str(self.priceless_blocks_count), fg="#c7c6c3", font=("Arial", 15), bg="#202124")
            self.priceless_blocks_count_prompt.place(y=350, relx=0.5, anchor="center", width=700)

            self.ignored_blocks_count_prompt = tk.Label(self.CalcuGUI, text="So viele Blöcke wurden währen der Berechnungen ignoriert: \n" + str(self.ignored_blocks_count), fg="#c7c6c3", font=("Arial", 15), bg="#202124")
            self.ignored_blocks_count_prompt.place(y=450, relx=0.5, anchor="center", width=700)

            self.closeCalcuGUI = tk.Button(self.CalcuGUI, text="Close", fg="#c7c6c3", font=("Arial", 15), width=20, height=2, bg="#3c3d42", command=self.CalcuGUI.destroy)
            self.closeCalcuGUI.place(y=650, relx=0.5, anchor="center")
        except Exception as e:
            timeanddate = datetime.now()
            timeanddate = str(timeanddate)
            e = str(e)
            r = open(r"debuglog.txt", "a")
            r.write(timeanddate)
            r.write("\n")
            r.write(str(e))
            r.write("\n")
            r.close()

            ErrorGUI = tk.Tk()
            ErrorGUI.geometry("900x800")
            ErrorGUI.resizable(0, 0)
            ErrorGUI.title("CESPC")
            ErrorGUI['background'] = '#202124'

            errorprompt = tk.Text(ErrorGUI, height=10, borderwidth=0, fg="#c7c6c3", font=("Arial", 15), bg="#202124")
            errorprompt.insert(1.0, e)
            errorprompt.place(y=200, relx=0.5, anchor="center")

            ErrorGUI.mainloop()

    def line_slicer(self):
        self.ignored_blocks_count  = 0
        self.priceless_blocks_count = 0
        self.combined_block_price = 0
        with open("List.txt") as self.file:
            for self.item in self.file:
                self.block, self.amount = self.item.split(",")
                self.block = self.block.replace("minecraft:", "")
                print(self.block)
                print(self.amount)

                self.result = self.price_calculator(self.block, self.amount)

                if self.result == True:
                    self.ignored_blocks_count = int(self.ignored_blocks_count) + int(self.amount)
                elif self.result == 0:
                    self.priceless_blocks_count = int(self.priceless_blocks_count) + int(self.amount)
                else:
                    self.combined_block_price = float(self.combined_block_price) + float(self.result)

        return self.ignored_blocks_count, self.priceless_blocks_count, self.combined_block_price

    def singleblock_calc(self, amount, block_value):
        self.total_block_type_value = float(self.amount) * float(self.block_value)
        return self.total_block_type_value

    def price_calculator(self, block, amount):
        r = open("ignoreconfig.json","r")
        self.ignoredata = r.read()
        r.close()

        r = open("pricelist.json","r")
        self.pricedata = r.read()
        r.close()

        self.ignoredata = json.loads(self.ignoredata)
        self.ignoredata = self.ignoredata[self.block]

        self.pricedata = json.loads(self.pricedata)
        self.block_value = self.pricedata[block]


        if self.ignoredata == True:
            return True

        self.total_block_type_value = self.singleblock_calc(self.amount, self.block_value)

        return self.total_block_type_value


    def blockcounter(self, filepath):
        self.nbt_file = self.open_file(self.filepath)
        self.block_list = self.count_blocks(self.nbt_file)
        self.output_block_list(self.block_list)


    def open_file(self, filepath):
        return self.nbt.read_from_nbt_file(self.filepath)


    def count_blocks(self, nbt_file):
        self.palette = []
        for self.block_type in self.nbt_file["palette"].value:
            self.palette.append(self.block_type["Name"].value)

        self.block_list = {}
        for block in self.nbt_file["blocks"]:
            self.block_list[self.palette[block["state"].value]] = self.block_list.get(self.palette[block["state"].value], 0) + 1
        return self.block_list


    def output_block_list(self, block_list):
        with open("List" ".txt", "w") as f:
            for k, v in self.block_list.items():
                f.write(k + "," + str(v) + "\n")


Main()


