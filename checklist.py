import platform
import subprocess
import tkinter as tk

Telas = [
    "Hardware",
    "WiFi",
    "Bluetooth",
    "Lan",
    "HDMI",
    "VGA",
    "Som",
    "Microfone",
    "Webcam",
    "Teclado",
    "Fonte",
    "Resultado Final"
]
pagina = 0

class TelaFrame(tk.Frame):
    def __init__(self, master, titulotext):
        super().__init__(master)
        titulo = tk.Label(self, text=titulotext)
        titulo.pack(side="top")
        rodape = tk.Frame(self)
        rodape.pack(side="bottom", fill="x")
        botProximo = tk.Button(rodape, text="Próximo", command=lambda: mudarPagina(1))
        botProximo.pack(side="right")
        botVoltar = tk.Button(rodape, text="Voltar", command=lambda: mudarPagina(-1))
        botVoltar.pack(side="left")

class TelaHardware(TelaFrame):
    def obterCPU(self):
        obterCPU = subprocess.run("lscpu | grep 'Model name'", capture_output=True, text=True, shell=True)
        return(obterCPU.stdout)
    def obterRAM(self):
        obterRAM = subprocess.run("sudo dmidecode -t memory | grep -i size", capture_output=True, text=True, shell=True)
        somaRAM = 0
        for pente in obterRAM.stdout.splitlines():
            strRAM = pente.split()[1].replace("GB", "")
            strRAM = int(strRAM)
            somaRAM = somaRAM+strRAM
        return(f"Memoria RAM: {somaRAM}GB")
    def obterDisco(self):
        obterDisco = subprocess.run("sudo fdisk -l | grep 'Disk /dev/sd' | grep -v 'Disklabel'", capture_output=True, text=True, shell=True)
        return(obterDisco.stdout)
    def __init__(self, master):
        super().__init__(master, "Hardware")
        mostrarCPU = tk.Label(self, text=self.obterCPU())
        mostrarCPU.pack()
        mostrarRAM = tk.Label(self, text=self.obterRAM())
        mostrarRAM.pack()
        mostrarDisco = tk.Label(self, text=self.obterDisco())
        mostrarDisco.pack()

class TelaWiFi(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "WiFi")

class TelaBluetooth(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "Bluetooth")

class TelaLan(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "Lan")

class TelaHDMI(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "HDMI")

class TelaVGA(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "VGA")

class TelaSom(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "Som")

class TelaMicrofone(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "Microfone")

class TelaWebcam(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "Webcam")

class TelaTeclado(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "Teclado")

class TelaFonte(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "Fonte")

class TelaResultado(TelaFrame):
    def __init__(self, master):
        super().__init__(master, "Resultado Final")


TelasClasses = [
    TelaHardware,
    TelaWiFi,
    TelaBluetooth,
    TelaLan,
    TelaHDMI,
    TelaVGA,
    TelaSom,
    TelaMicrofone,
    TelaWebcam,
    TelaTeclado,
    TelaFonte,
    TelaResultado
]

def mudarPagina(quantPag):
    global pagina
    
    if pagina+quantPag>=0 and pagina+quantPag<len(TelasClasses):
        pagina = pagina + (quantPag)
        
        for i in janela.winfo_children():
            i.destroy()
        
        TelasClasses[pagina](janela).pack(fill="both", expand=True)
    
    else:
        pass


janela = tk.Tk()
janela.geometry("800x600")
mudarPagina(0)
janela.mainloop()