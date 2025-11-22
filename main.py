import psutil
import tkinter as tk
import time
import socket
import subprocess

def disk_scan():
    try:
        disk = psutil.disk_usage("C:")
        free_gb = disk.free / (1024 ** 3)

        if free_gb < 50:
            info_ekran.config(text="Disk is too low :( clear you trashbin or useless files")
        else:
            info_ekran.config(text=f"free space: {free_gb:.2f} GB")

    except Exception as A:
        info_ekran.config(text=f"Error: {A}")

def cpu():
    try:
        boot = psutil.boot_time()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot))
        info_ekran.config(text=f"System Boot time: {time_str}")
    except Exception as B:
        info_ekran.config(text=f"Error: {B}")

def cpu_info():
    try:
        freq = psutil.cpu_freq()
        count = psutil.cpu_count()
        info_ekran.config(text=f"CPU freq.: {freq.current:.2f} MHz\nCPU cores: {count}")
    except Exception as C:
        info_ekran.config(text=f"Error: {C}")

def battery():
    try:
        bat = psutil.sensors_battery()

        if bat is None:
            info_ekran.config(text="Battery sensor not found :(")
            return
        
        percent = bat.percent
        charging = "Yes" if bat.power_plugged else "No"

        info_ekran.config(text=f"Battary: %{percent}\nOn charge?: {charging}")

    except Exception as D:
        info_ekran.config(text=f"Error: {D}")

def Wifi():
    try:
        ip = socket.gethostbyname(socket.gethostname())
        ping = subprocess.run(["ping", "-n", "1", "1.1.1.1"], capture_output=True, text=True)

        if "TTL=" in ping.stdout:
            info_ekran.config(text=f"Wifi: connected\nIP: {ip}")
        else:
            info_ekran.config(text="Wifi: not connected :(")

    except Exception as E:
        info_ekran.config(text=f"Error: {E}")


pencere = tk.Tk()
pencere.title("Pc-status-tester")
pencere.geometry("600x450")

tk.Button(pencere, text="Disk Scan", command=disk_scan).pack(pady=5)
tk.Button(pencere, text="System Boot time", command=cpu).pack(pady=5)
tk.Button(pencere, text="Cpu info", command=cpu_info).pack(pady=5)
tk.Button(pencere, text="Battary info", command=battery).pack(pady=5)
tk.Button(pencere, text="Wifi test", command=Wifi).pack(pady=5)

info_ekran = tk.Label(pencere, text="", font=("Arial", 12),)
info_ekran.pack(pady=20)


pencere.mainloop()

#made by ahmet :3
#u can change everthing
# ************Pc-status-tester************
#A "Pc status tester" it tests wifi disk etc. u can use to check any system fault and tells how to fix it
#To download:
#1.fırst clone this repo
#after installed
#2.go to command bar type: pip install psuitl
#and now you can run this repo
