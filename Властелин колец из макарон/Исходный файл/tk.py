import tkinter as tk
import main_v2
root = tk.Tk()

root.geometry("1280x720")
#1
lab_i = tk.Label(root, text=main_v2.info_1(1)).grid(row=0, column=0)
s = 1
for i in range(26):
    lab_alf = tk.Label(root, text=main_v2.macarone(i)).grid(row=s,column=0)
    s += 1
lab_sum_macarone = tk.Label(root, text=main_v2.sum_mac(1)).grid(row=s+1, column=0)
#2
lab_i = tk.Label(root, text=main_v2.info_1(1)).grid(row=0, column=1)
s = 1
for i in range(26):
    lab_alf = tk.Label(root, text=main_v2.vlastelin(i)).grid(row=s,column=1)
    s += 1
lab_sum_book = tk.Label(root, text=main_v2.sum_book(1)).grid(row=s+1, column=1)
#3
lab_sum_pack_macaron = tk.Label(root, text=main_v2.sum_pack_macaron(1)).grid(row=0, column=2)
lab_sum_price_pack = tk.Label(root, text=main_v2.sum_price_pack(1)).grid(row=1, column=2)
lab_surplus = tk.Label(root, text=main_v2.surplus(1)).grid(row=2, column=2)
lab_mass_pack = tk.Label(root, text=main_v2.mass_pack(1)).grid(row=3, column=2)
root.mainloop()