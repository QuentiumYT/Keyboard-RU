import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 2
__filename__ = "Keyboard-RU"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:urllib.request.urlretrieve("https://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("https://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("https://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("https://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

majuscule = True
verr_maj_true = "Verr.Maj ► Enabled !"
verr_maj_false = "Verr.Maj ► Disabled !"

keys =[ 
[
    [
        ("Caractères"),
        ({"side":"top","expand":"yes","fill":"both"}),
        [
            ("Ё","ъ","№","£\n$","©\n@","|\n—","&\n%","(","[","]",")","^\n*","+\n=","Back"),
            ("Tab","Й","Ц","У","К","Е","Н","Г","Ш","Щ","З","Х",".\n;","Enter"),
            ("Caps","Ф","Ы","В","А","П","Р","О","Л","Д","Ж","Э","!\n:","Enter"),
            ("Shift",">\n<","Я","Ч","С","М","И","Т","Ь","Б","Ю","?\n,","Shift"),
            ("Ctrl", "©","Alt","Space","Alt","©","▓","Ctrl")
        ]
    ]
]
]

class Keyboard(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        global verr_maj
        verr_maj = StringVar()
        verr_maj.set(verr_maj_true)
        Entry(self, textvariable=verr_maj, width=16, state="disabled", font="impact 15").pack()
        self.create_frames_and_buttons()
    def create_frames_and_buttons(self):
        for key_section in keys:
            store_section = Frame(self)
            store_section.pack(side="left", expand="yes", fill="both", padx=10, pady=10, ipadx=10, ipady=10)
            for layer_name, layer_properties, layer_keys in key_section:
                store_layer = LabelFrame(store_section)
                store_layer.pack(layer_properties)
                for key_bunch in layer_keys:
                    store_key_frame = Frame(store_layer)
                    store_key_frame.pack(side="top",expand="yes",fill="both")
                    for k in key_bunch:
                        if len(k)<=3:
                            store_button = Button(store_key_frame, text=k, width=6, height=2)
                        else:
                            store_button = Button(store_key_frame, text=k.center(5," "), width=6, height=2)
                        def simple_button(background, forground, command):
                            store_button["relief"]="groove"
                            store_button["bg"]=background
                            store_button["fg"]=forground
                            store_button["command"]=command
                            store_button.pack(side="left",fill="both",expand="yes")
                        if k == "Space":
                            store_button["width"]=53
                            simple_button("white", "red", lambda q=k: self.button_command(" "))
                        elif k == "Enter":
                            simple_button("white", "red", lambda q=k: self.button_command("\n"))
                        elif k == "Back":
                            simple_button("white", "red", lambda q=k: self.button_command_del())
                        elif k == "Tab":
                            simple_button("white", "red", lambda q=k: self.button_command("\t"))
                        elif k == "Caps":
                            simple_button("white", "red", lambda q=k: self.button_command_maj())
                        elif k in ["Shift", "Ctrl", "Alt", "©", "▓"]:
                            simple_button("lightgray", "red",  None)
                        else:
                            simple_button("white", "blue", lambda q=k: self.button_command(q))
        return

    def button_command(self, event):
        char = event
        if majuscule == True:
            if len(char) >= 3:
                fir = char[:1]
                txtBox.insert(INSERT, fir)
            else:
                txtBox.insert(INSERT, char)
            return
        else:
            if len(char) >= 3:
                fir = char[-1:]
                txtBox.insert(INSERT, fir.lower())
            else:
                txtBox.insert(INSERT, char.lower())
            return

    def button_command_del(self):
        try:
            var = txtBox.get("1.0", END)
            liste = list(str(var))
            liste.pop()
            liste.pop()
            txtBox.delete("1.0", END)
            var = "".join(liste)
            txtBox.insert(INSERT, var)
            return
        except:
            showwarning("Russian Virtual KeyBoard V" + str(__version__), "There is no character remaining !")

    def button_command_maj(self):
        if majuscule == True:
            def replace_false():
                global majuscule
                majuscule = False
            replace_false()
            verr_maj.set(verr_maj_false)
        else:
            def replace_true():
                global majuscule
                majuscule = True
            replace_true()
            verr_maj.set(verr_maj_true)

keyboard = Tk()
width = 775
height = 575
keyboard.update_idletasks()
x = (keyboard.winfo_screenwidth() - width) // 2
y = (keyboard.winfo_screenheight() - height) // 2
keyboard.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
keyboard.title("Russian Virtual KeyBoard V" + str(__version__))
if os.path.exists(__iconpath__):
    keyboard.iconbitmap(__iconpath__)
canvas = Canvas(keyboard, width=150, height=120, background="white")
canvas.pack()
txtBox = Text(canvas, width = 70, height = 12, wrap = WORD, font="impact 15")
txtBox.grid(row = 0, column = 0, sticky = W)
txtBox.pack()
Keyboard(keyboard).pack()
keyboard.mainloop()
