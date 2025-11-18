import psutil
import tkinter as tk
import time
import socket
import subprocess

def tara():
    try:
        disk = psutil.disk_usage("C:")
        free_gb = disk.free / (1024 ** 3)

        if free_gb < 50:
            info_ekran.config(text="Disk is too low :(")
        else:
            info_ekran.config(text=f"free space: {free_gb:.2f} GB")

    except Exception as A:
        info_ekran.config(text=f"Error: {A}")

def cpu():
    try:
        açılma_zamanı = psutil.boot_time()
        zaman_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(açılma_zamanı))
        info_ekran.config(text=f"System Boot time: {zaman_str}")
    except Exception as B:
        info_ekran.config(text=f"Error: {B}")

def cpu_info():
    try:
        cpu_info_freq = psutil.cpu_freq()
        cpu_info_count = psutil.cpu_count()
        info_ekran.config(
            text=f"CPU freq.: {cpu_info_freq.current:.2f} MHz\nCPU core count: {cpu_info_count}"
        )
    except Exception as C:
        info_ekran.config(text=f"Error: {C}")

def battary():
    try:
        batarya_sensor = psutil.sensors_battery()

        if batarya_sensor is None:
            info_ekran.config(text="Battary sensor cant be find :(")
            return
        
        yüzde = batarya_sensor.percent
        şarjda_mı = "Yes" if batarya_sensor.power_plugged else "No"

        info_ekran.config(text=f"Battary: %{yüzde}\nOn charge?: {şarjda_mı}")

    except Exception as D:
        info_ekran.config(text=f"Error: {D}")
def internet():
    try:
        ip = socket.gethostbyname(socket.gethostname())

        ping = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)

        if "TTL=" in ping.stdout:
            info_ekran.config(text=f"Wifi status: connected\nIP Adrrs: {ip}")
        else:
            info_ekran.config(text="Wifi status: not connected :(")

    except Exception as E:
        info_ekran.config(text=f"Error: {E}")



pencere = tk.Tk()
pencere.title("Pc-status-tester")
pencere.geometry("600x350")

button_disk = tk.Button(pencere, text="Disk Scan", command=tara)
button_disk.pack(pady=10)

button_cpu = tk.Button(pencere, text="System Boot time", command=cpu)
button_cpu.pack(pady=10)

button_cpu_info = tk.Button(pencere, text="Cpu info", command=cpu_info)
button_cpu_info.pack(pady=10)

button_batarya = tk.Button(pencere, text="Battary info", command=battary)
button_batarya.pack(pady=10)

button_internet = tk.Button(pencere, text="Wifi test", command=internet)
button_internet.pack(pady=10)

info_ekran = tk.Label(pencere, text="", font=("Arial", 12))
info_ekran.pack(pady=20)

pencere.mainloop()
#made by ahmet :3
#u can change everthing
# Pc-status-tester
#A "Pc status tester" it tests wifi disk etc. u can use to check ans system fault and tells how to fix it
#To download:
#fırst clone this repo
#after installed
#go to command bar type: pip clone psuitl
#and now you can run this repo
