import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import sys

root = tk.Tk()
root.title("Hotel Billing System")
root.geometry("1360x400")
root.resizable(True, True)

frame = tk.Frame(root, bg='#8D8D8D')
frame.pack(fill='both', expand=True)

header = tk.Frame(frame, bg='#3c3f41', relief='raised', bd=10)
header.pack(side='top', fill='x')
header_label = tk.Label(header, text="HOTEL GREEN LEAF BILLING SYSTEM", fg='yellow', bg='#3c3f41', font=("Times New Roman", 20, 'bold'))
header_label.pack(pady=10)

content = tk.Frame(frame, bg='#8D8D8D')
content.pack(side='top', fill='both', expand=True)

# Customer Details frame start
customer_frame = tk.LabelFrame(content, text="Customer Details", font=("Georgia", 14, 'bold'),
                               bg='#8D8D8D', fg='yellow', padx=40, pady=1,bd=5, relief='sunken')
customer_frame.pack(pady=10, padx=20, fill='x')

# Input fields frame
input_frame = tk.Frame(customer_frame, bg='#8D8D8D')
input_frame.pack(pady=5)

# Name textbox
name_label = tk.Label(input_frame, text="Name:", font=("Times New Roman", 16), bg='#8D8D8D')
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame, font=("Times New Roman", 12), width=20,bd=3, relief="sunken")
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Mobile No textbox
mobile_label = tk.Label(input_frame, text="Mobile No:", font=("Times New Roman", 16), bg='#8D8D8D')
mobile_label.grid(row=0, column=2, padx=5, pady=5)
mobile_entry = tk.Entry(input_frame, font=("Times New Roman", 12), width=20,bd=3, relief="sunken")
mobile_entry.grid(row=0, column=3, padx=5, pady=5)

# Biller selection (Combobox)
Biller_label = tk.Label(input_frame, text="Biller :", font=("Times New Roman", 16), bg='#8D8D8D')
Biller_label.grid(row=0, column=4, padx=5, pady=5)
Biller_combobox = ttk.Combobox(input_frame, font=("Times New Roman", 12), width=10  )
Biller_combobox['values'] = ("Select","Admin@17", "Admin@18", "Admin@19","Admin@20")
Biller_combobox.current(0)
Biller_combobox.grid(row=0, column=5, padx=5, pady=5)

# Table no textbox
bill_label = tk.Label(input_frame, text="Table no:", font=("Times New Roman", 16), bg='#8D8D8D')
bill_label.grid(row=0, column=6, padx=5, pady=5)
bill_entry = tk.Entry(input_frame, font=("Times New Roman", 12), width=15,bd=3, relief="sunken")
bill_entry.grid(row=0, column=7, padx=5, pady=5)

# Email ID textbox
email_label = tk.Label(input_frame, text="Email ID:", font=("Times New Roman", 16), bg='#8D8D8D')
email_label.grid(row=0, column=8    , padx=5, pady=5)
email_entry = tk.Entry(input_frame, font=("Times New Roman", 12), width=25,bd=3, relief="sunken")
email_entry.grid(row=0, column=9, padx=5, pady=5)
# Customer Details frame end

# Define a Price Dictionary start
prices = {
    "Tea": 10, "Black tea": 12, "Green tea": 15, "Coffee": 20, "Masala milk": 25, "Milk shake": 30,
    "Papadi chaat": 40, "Dahi vada": 45,"Samosa":15,"Dahi puri": 35, "Sev puri": 30,
    "Onion pakoda": 30, "Mirchi vada": 35, "Burger": 50, "Biscuit": 10, "Paneer Pakoda": 45,
    "Garlic Bread": 40, "Cream roll": 25,
    "Upma": 35, "Poha": 30, "Aloo Gobhi": 60, "Poori": 25, "Rava Idli": 40, "Dhokla": 40,
    "Aloo Paratha": 45, "Besan Chilla": 35, "Masala Dosa": 50, "Chole Bhature": 60,"Vada Pav": 15,
    "Misal": 40, "Puri Bhaji": 35, "Oats Porridge": 30, "Uttapam": 40, "Spring Rolls": 45,
    "Misal Pav": 60, "Pav Bhaji": 70,
    "Lunch Thali": 120, "Dal Tadka": 50, "Dum Aloo": 40, "Rajma Chawal": 60, "Mix Veg": 80,
    "Sambar Rice": 70, "Bhindi Masala": 45, "Dal Rice": 40, "Mutter Paneer": 80,
    "Jeera Rice": 120, "Veg Biryani": 110, "Curd Rice": 60, "Roti": 10, "Lemon Rice": 40,
    "Veg Pulao": 50, "Naan": 20, "Paratha": 25,
    "Paneer Bhurji": 140, "Shahi Paneer": 160, "Kadhai Paneer": 150, "Palak Paneer": 110,
    "Malai Kofta": 140,"Veg Thali": 140, "Dal Makhani": 130, "Dal Fry": 120,"Chole": 90,
    "Rajma": 110,"Dal Tadka":140,"Chapati":15
}
# Define a Price Dictionary end

# Snacks card section start
Snacks_frame = tk.LabelFrame(content, text="Snacks", font=("Times New Roman", 16, "bold"),
                             fg="yellow", bg="#8D8D8D", bd=4, relief="sunken")
Snacks_frame.place(x=17, y=100, width=220, height=555)

snacks_items = [
    "Tea", "Black tea", "Green tea", "Coffee", "Masala milk", "Milk shake",
    "Papadi chaat", "Dahi vada", "Samosa", "Dahi puri", "Sev puri",
    "Onion pakoda", "Mirchi vada", "Burger", "Biscuit", "Paneer Pakoda", "Garlic Bread",
    "Cream roll"
]

# Dictionary to store counters for snacks
snacks_counters = {}

class Counter:
    def __init__(self, root, row):
        self.value = tk.IntVar(value=0)

        self.btn_decrease = tk.Button(root, text="−", font=("Times New Roman", 7),
                                      command=self.decrease, width=2, height=1,
                                      bg="#D3D3D3", relief="raised")
        self.label = tk.Label(root, textvariable=self.value, font=("Times New Roman", 7, "bold"),
                              width=3, fg="Black", bg="white", borderwidth=2, relief="raised")
        self.btn_increase = tk.Button(root, text="+", font=("Times New Roman", 7),
                                      command=self.increase, width=2, height=1,
                                      bg="#D3D3D3", relief="raised")

        self.btn_decrease.grid(row=row, column=1, padx=2, pady=1)
        self.label.grid(row=row, column=2, padx=2, pady=1)
        self.btn_increase.grid(row=row, column=3, padx=2, pady=1)

    def increase(self):
        self.value.set(self.value.get() + 1)

    def decrease(self):
        if self.value.get() > 0:
            self.value.set(self.value.get() - 1)

for i, item in enumerate(snacks_items):
    tk.Label(Snacks_frame, text=item, font=("Times New Roman", 14), fg="Black",
             bg="#8D8D8D").grid(row=i, column=0, padx=9, pady=1, sticky="w")
    c = Counter(Snacks_frame, row=i)
    snacks_counters[item] = c
# Snacks card section end

# Breakfast card section start
Breakfast_frame = tk.LabelFrame(content, text="Breakfast", font=("Times New Roman", 16, "bold"),
                                fg="yellow", bg="#8D8D8D", bd=4, relief="sunken")
Breakfast_frame.place(x=240, y=100, width=220, height=555)

Breakfast_items = [
    "Upma", "Poha", "Aloo Gobhi", "Poori", "Rava Idli", "Dhokla",
    "Aloo Paratha", "Besan Chilla", "Masala Dosa", "Chole Bhature", "Vada Pav",
    "Misal", "Puri Bhaji", "Oats Porridge", "Uttapam","Spring Rolls","Misal Pav",
    "Pav Bhaji"
]

# Dictionary to store counters for breakfast
breakfast_counters = {}

class Counter:
    def __init__(self, root, row):
        self.value = tk.IntVar(value=0)

        self.btn_decrease = tk.Button(root, text="−", font=("Times New Roman", 7),
                                      command=self.decrease, width=2, height=1,
                                      bg="#D3D3D3", relief="raised")
        self.label = tk.Label(root, textvariable=self.value, font=("Times New Roman", 7, "bold"),
                              width=3, fg="Black", bg="white", borderwidth=2, relief="raised")
        self.btn_increase = tk.Button(root, text="+", font=("Times New Roman", 7),
                                      command=self.increase, width=2, height=1,
                                      bg="#D3D3D3", relief="raised")

        self.btn_decrease.grid(row=row, column=1, padx=2, pady=1)
        self.label.grid(row=row, column=2, padx=2, pady=1)
        self.btn_increase.grid(row=row, column=3, padx=2, pady=1)

    def increase(self):
        self.value.set(self.value.get() + 1)

    def decrease(self):
        if self.value.get() > 0:
            self.value.set(self.value.get() - 1)

for i, item in enumerate(Breakfast_items):
    tk.Label(Breakfast_frame, text=item, font=("Times New Roman", 14), fg="Black",
             bg="#8D8D8D").grid(row=i, column=0, padx=1, pady=1, sticky="w")
    c = Counter(Breakfast_frame, row=i)
    breakfast_counters[item] = c
# Breakfast card section end


# Lunch card section start
Lunch_frame = tk.LabelFrame(content, text="Lunch", font=("Times New Roman", 16, "bold"),
                            fg="yellow", bg="#8D8D8D", bd=4, relief="sunken")
Lunch_frame.place(x=463, y=100, width=220, height=555)

Lunch_items = [
    "Lunch Thali", "Dal Tadka", "Dum Aloo", "Chole Bhature", "Rajma Chawal",
    "Mix Veg", "Aloo Gobhi", "Bhindi Masala", "Dal Rice", "Mutter Paneer",
    "Jeera Rice", "Veg Biryani", "Curd Rice", "Roti","Lemon Rice","Veg Pulao","Naan",
    "Paratha"
]

# Dictionary to store counters for lunch
lunch_counters = {}

class Counter:
    def __init__(self, root, row):
        self.value = tk.IntVar(value=0)

        self.btn_decrease = tk.Button(root, text="−", font=("Times New Roman", 7),
                                      command=self.decrease, width=2, height=1,
                                      bg="#D3D3D3", relief="raised")
        self.label = tk.Label(root, textvariable=self.value, font=("Times New Roman", 7, "bold"),
                              width=3, fg="Black", bg="white", borderwidth=2, relief="raised")
        self.btn_increase = tk.Button(root, text="+", font=("Times New Roman", 7),
                                      command=self.increase, width=2, height=1,
                                      bg="#D3D3D3", relief="raised")

        self.btn_decrease.grid(row=row, column=1, padx=2, pady=1)
        self.label.grid(row=row, column=2, padx=2, pady=1)
        self.btn_increase.grid(row=row, column=3, padx=2, pady=1)

    def increase(self):
        self.value.set(self.value.get() + 1)

    def decrease(self):
        if self.value.get() > 0:
            self.value.set(self.value.get() - 1)

for i, item in enumerate(Lunch_items):
    tk.Label(Lunch_frame, text=item, font=("Times New Roman", 14), fg="Black",
             bg="#8D8D8D").grid(row=i, column=0, padx=1, pady=1, sticky="w")
    c = Counter(Lunch_frame, row=i)
    lunch_counters[item] = c
# Lunch card section end

# Dinner card section start
Dinner_frame = tk.LabelFrame(content, text="Dinner", font=("Times New Roman", 16, "bold"),
                             fg="yellow", bg="#8D8D8D", bd=4, relief="sunken")
Dinner_frame.place(x=686, y=100, width=220, height=555)

Dinner_items = [
    "Paneer Bhurji", "Shahi Paneer", "Kadhai Paneer", "Palak Paneer", "Malai Kofta",
    "Sambar Rice", "Bhindi Masala", "Mutter Paneer", "Dal Tadka", "Mix Veg",
    "Dal Makhani", "Dal Tadka", "Rajma", "Chole", "Veg Biryani","Chapati","Dal Fry",
    "Veg Thali"
]
# Dictionary to store counters for dinner
dinner_counters = {}

class Counter:
    def __init__(self, root, row):
        self.value = tk.IntVar(value=0)

        self.btn_decrease = tk.Button(root, text="−", font=("Times New Roman", 7),
                                      command=self.decrease, width=2, height=1,
                                      bg="#D3D3D3", relief="raised")
        self.label = tk.Label(root, textvariable=self.value, font=("Times New Roman", 7, "bold"),
                              width=3, fg="Black", bg="white", borderwidth=2, relief="raised")
        self.btn_increase = tk.Button(root, text="+", font=("Times New Roman", 7),
                                      command=self.increase, width=2, height=1,
                                      bg="#D3D3D3", relief="raised")

        self.btn_decrease.grid(row=row, column=1, padx=2, pady=1)
        self.label.grid(row=row, column=2, padx=2, pady=1)
        self.btn_increase.grid(row=row, column=3, padx=2, pady=1)

    def increase(self):
        self.value.set(self.value.get() + 1)

    def decrease(self):
        if self.value.get() > 0:
            self.value.set(self.value.get() - 1)

for i, item in enumerate(Dinner_items):
    tk.Label(Dinner_frame, text=item, font=("Times New Roman", 14), fg="Black",
             bg="#8D8D8D").grid(row=i, column=0, padx=1, pady=1, sticky="w")
    c = Counter(Dinner_frame, row=i)
    dinner_counters[item] = c
# Dinner card section end

# Bill card section start
Dinner_frame = tk.LabelFrame(content, text="Bill Receipt", font=("Times New Roman", 16, "bold"),
                             fg="yellow", bg="#8D8D8D", bd=4, relief="sunken",
                             labelanchor="n")  # Centers text at the top
Dinner_frame.place(x=910, y=100, width=430, height=500)

# Text box to display the bill
bill_text = tk.Text(Dinner_frame, font=("Times New Roman", 12), width=50, height=25, bd=3, relief="sunken")
bill_text.pack(padx=5, pady=5)
# Bill card section end

#Bill generation section start
def generate_bill():
    bill_text.delete('1.0', tk.END)  # Clear previous content

    customer_name = name_entry.get() or "Unknown"
    mailid = email_entry.get()
    biller = Biller_combobox.get()
    date_str = "16/1/2007"

    bill_text.insert(tk.END, "-" * 44 + "\n")
    bill_text.insert(tk.END, f"{'HOTEL GREEN LEAF':^40}\n")
    bill_text.insert(tk.END, "-" * 44 + "\n")
    bill_text.insert(tk.END, f" Name of customer : {customer_name}\n")
    bill_text.insert(tk.END, f" Date             : {date_str}\n")
    bill_text.insert(tk.END, f" Mail id          : {mailid}\n")
    bill_text.insert(tk.END, f" Biller id        : {biller}\n")
    bill_text.insert(tk.END, f" Bill no          : 12934643908\n")
    bill_text.insert(tk.END, "-" * 44 + "\n")

    # **Header of the table**
    bill_text.insert(tk.END, f"{'Item':<15}{'Price':>10}{'Qty':>7}{'Amount':>12}\n")
    bill_text.insert(tk.END, "-" * 44 + "\n")

    subtotal = 0

    # Process each order category dictionary
    order_categories = [snacks_counters, breakfast_counters, lunch_counters, dinner_counters]
    for order in order_categories:
        for item, counter_obj in order.items():
            qty = counter_obj.value.get()
            if qty > 0:
                price = prices.get(item.strip(), 0)
                amt = price * qty
                subtotal += amt

                # **Proper spacing for alignment**
                bill_text.insert(tk.END, f"{item:<13}{price:>12}{qty:>7}{amt:>12}\n")

    bill_text.insert(tk.END, "-" * 44 + "\n")
    bill_text.insert(tk.END, f"{'                 Amount without GST :':<5}{subtotal:>7.2f}\n")
    bill_text.insert(tk.END, "-" * 44 + "\n")

    cgst = subtotal * 0.025
    sgst = subtotal * 0.025
    gst_total = cgst + sgst
    total = subtotal + gst_total

    bill_text.insert(tk.END, f"{'                         CGST (2.5%):':<5}{cgst:>5.2f}\n")
    bill_text.insert(tk.END, f"{'                         SGST (2.5%):':<5}{sgst:>5.2f}\n")
    bill_text.insert(tk.END, "-" * 44 + "\n")
    bill_text.insert(tk.END, f"{'               Total payable amount :':<5}{total:>7.2f}\n")
    bill_text.insert(tk.END, "-" * 44 + "\n")
    bill_text.insert(tk.END, "=" * 15 + " VISIT  AGAIN " + "=" * 15)
    bill_text.insert(tk.END, "-" * 44 + "\n")

#Bill font size and name
bill_text.config(font=("Courier", 11))
#Bill generation section end

#print button Popup section start
def printer_not_found():
    messagebox.showerror("Printer Error", "Printer not detected. Please check the connection and try again.")
#print button Popup section end

#Save button Popup section start
def Saved():
    messagebox.showerror("Save Error", "Database connection failed. Please check your internet or database settings!")
#save button Popup section end

#Program restart section start
def restart_program():
    python = sys.executable
    os.execv(python, [python] + sys.argv)
# Program restart section end

# Control buttons section start
btn1 = tk.Button(root, text="Save", bg="#212020", fg="White",command=Saved)
btn1.place(x=910, y=690, width=100, height=40)

btn2 = tk.Button(root, text="Bill", bg="#212020", fg="White", command=generate_bill)
btn2.place(x=1020, y=690, width=100, height=40)

btn3 = tk.Button(root, text="Print", bg="#212020", fg="White",command=printer_not_found)
btn3.place(x=1130, y=690, width=100, height=40)

btn4 = tk.Button(root, text="Cancel", bg="#212020", fg="White",command=restart_program)
btn4.place(x=1240, y=690, width=100, height=40)
# Control buttons section end

root.mainloop()
