import tkinter as tk
from login import authenticate
from scanner import scan_ports
from sniffer import start_sniffing, save_pcap
from utils import save_report

def login():
    user = username.get()
    pwd = password.get()
    if authenticate(user, pwd):
        login_frame.pack_forget()
        main_frame.pack()
    else:
        status.config(text="Login Failed")

def run_scan():
    target = target_entry.get()
    ports = scan_ports(target)
    result = f"Open Ports: {ports}"
    output.config(text=result)
    save_report(result)

def sniff_packets():
    start_sniffing()
    save_pcap()
    output.config(text="Packets captured & saved!")

root = tk.Tk()
root.title("Mini Nessus Tool")

login_frame = tk.Frame(root)
tk.Label(login_frame, text="Username").pack()
username = tk.Entry(login_frame)
username.pack()

tk.Label(login_frame, text="Password").pack()
password = tk.Entry(login_frame, show="*")
password.pack()

tk.Button(login_frame, text="Login", command=login).pack()
status = tk.Label(login_frame)
status.pack()
login_frame.pack()

main_frame = tk.Frame(root)
tk.Label(main_frame, text="Target IP").pack()
target_entry = tk.Entry(main_frame)
target_entry.pack()

tk.Button(main_frame, text="Scan Ports", command=run_scan).pack()
tk.Button(main_frame, text="Capture Packets", command=sniff_packets).pack()

output = tk.Label(main_frame)
output.pack()

root.mainloop()
