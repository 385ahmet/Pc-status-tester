import psutil
import customtkinter as tk
import time
import socket
import subprocess

def disk_scan():
    try:
        disk = psutil.disk_usage("C:")
        free_gb = disk.free / (1024 ** 3)

        if free_gb < 50:
            info_ekran.configure(text="Disk is too low :( clear you trashbin or useless files")
        else:
            info_ekran.configure(text=f"free space: {free_gb:.2f} GB")

    except Exception as A:
        info_ekran.configure(text=f"Error: {A}")

def cpu():
    try:
        boot = psutil.boot_time()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot))
        info_ekran.configure(text=f"System Boot time: {time_str}")
    except Exception as B:
        info_ekran.configure(text=f"Error: {B}")

def cpu_info():
    try:
        freq = psutil.cpu_freq()
        count = psutil.cpu_count()
        info_ekran.configure(text=f"CPU freq.: {freq.current:.2f} MHz\nCPU cores: {count}")
    except Exception as C:
        info_ekran.configure(text=f"Error: {C}")

def battery():
    try:
        bat = psutil.sensors_battery()

        if bat is None:
            info_ekran.configure(text="Battery sensor not found :(")
            return
        
        percent = bat.percent
        charging = "Yes" if bat.power_plugged else "No"

        info_ekran.configure(text=f"Battery: %{percent}\nOn charge?: {charging}")

    except Exception as D:
        info_ekran.configure(text=f"Error: {D}")

def Wifi():
    try:
        ip = socket.gethostbyname(socket.gethostname())
        ping = subprocess.run(["ping", "-n", "1", "1.1.1.1"], capture_output=True, text=True)

        if "TTL=" in ping.stdout:
            info_ekran.configure(text=f"Wifi: connected\nIP: {ip}")
        else:
            info_ekran.configure(text="Wifi: not connected :(")

    except Exception as E:
        info_ekran.configure(text=f"Error: {E}")


pencere = tk.CTk()
pencere.title("Pc-status-tester")
pencere.geometry("400x300")

tk.CTkButton(pencere, text="Disk Scan", command=disk_scan).pack(pady=5)
tk.CTkButton(pencere, text="System Boot time", command=cpu).pack(pady=5)
tk.CTkButton(pencere, text="Cpu info", command=cpu_info).pack(pady=5)
tk.CTkButton(pencere, text="Battery info", command=battery).pack(pady=5)
tk.CTkButton(pencere, text="Wifi test", command=Wifi).pack(pady=5)

info_ekran = tk.CTkLabel(pencere, text="", font=("Arial", 20),)
info_ekran.pack(pady=20)


pencere.mainloop()

#made by ahmet :3
#u can change everthing
# ************Pc-status-tester************
#A "Pc status tester" it tests wifi disk etc. u can use to check any system fault and tells how to fix it
#To download:
#1. first clone this repo
#after installed
#2. go to command bar type: pip install psuitl customtkinter
#and now you can run this repo
