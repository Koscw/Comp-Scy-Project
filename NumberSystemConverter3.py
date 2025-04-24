import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
#Create an instance of tkinter frame or window

#function for converting Decimal to Binary
def DecimalToBinary(n):
    ngt = 0
    if n < 0: ngt = 1 #negative value checker
    n = abs(n)
    int_n = int(n)
    frac_n = n - int_n
    res = '' # binary result

    while int_n > 0: #converting integer to binary
        res = str(int_n % 2) + res
        int_n //= 2

    # Convert fractional part to binary
    frac_res = ''
    count = 0
    while frac_n > 0 and count < 10:  # limit precision to 10 binary digits
        frac_n *= 2
        bit = int(frac_n)
        frac_res += str(bit)
        frac_n -= bit
        count += 1
    if frac_n > 0: res = res + '.' + frac_res
    if ngt == 1: #for negative numbers
        res = '-' + res
    res_t.set(f"Binary: {res}") #showing result

def DecimalToOctal(n):
    res = [0] * 100 # array to store octal result
    i = 0 # counter for octal
    ngt = 0 # variable for negative numbers
    lst=[]

    if n < 0: # checking for negative numbers
        ngt = 1
        n = n * -1

    int_n = int(n)
    frac_n = n - int_n

    while int_n > 0: #converting decimal to octal
        res[i] = int_n % 8
        int_n = int(int_n / 8)
        i += 1

    # printing octal number
    for j in range(i - 1, -1, -1):
        lst.append(str(res[j]))

    if frac_n > 0: # Convert fractional part to octal
        lst.append('.')  # decimal point
        count = 0
        while frac_n != 0 and count < 10: # limiting to 10 decimals
            frac_n *= 8
            digit = int(frac_n)
            lst.append(str(digit))
            frac_n -= digit
            count += 1

    res_t.set(f"Octal: {''.join(lst)}") # show result

    if ngt == 1: # negative number result
        res_t.set(f"Octal: -{''.join(lst)}")

def DecimalToHexadecimal(n): # function which converts decimal value to hexadecimal value
    res = ''
    ngt = 0
    if n < 0:
        ngt = 1 # variable for negative numbers
        n = n * -1
    int_n = int(n)
    frac_n = n - int_n
    # Conversion table of remainders to hexadecimal equivalent
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                        13: 'D', 14: 'E', 15: 'F'}
    while (int_n > 0): #coverting integer to hexa
        remainder = int_n % 16
        res = conversion_table[remainder] + res
        int_n = int_n // 16
    if frac_n > 0:  # Convert fractional part
        res = res + '.'
        count = 0
        while frac_n != 0 and count < 10: # limiting to 10 decimals
            frac_n *= 16
            digit = int(frac_n)
            res += conversion_table[digit]
            frac_n -= digit
            count += 1
    if ngt == 1: #for negative numbers
        res = '-' + res
    res_t.set(f"Hexadecimal: {res}") #show result
#Number System Converter interface
win = Tk()
win.title("Number System Converter")
# Set the geometry of tkinter frame
win.geometry("400x200")
win.resizable(True, True)


# Create an Entry Widget
entry_lable = ttk.Label(win, text="Enter your number:").pack()
entry = (ttk.Entry(win, font=('Century 12'), width=40))
entry.pack()

# Create an Dropdown Widget for number system selection
systems = ['Binary', 'Octal', 'Hexadecimal']
NS_dd_Label = ttk.Label(win, text="Select System").pack()
NS_dropdown = ttk.Combobox(win, values=systems, font=('Century 12'), width=40)
NS_dropdown.pack()
def systempicker():
    try:
        system = NS_dropdown.get()
        n = eval(entry.get())  # n = decimal number
        if system == 'Binary':
            DecimalToBinary(n)
        elif system == 'Octal':
            DecimalToOctal(n)
        elif system == 'Hexadecimal':
            DecimalToHexadecimal(n)
        if n == 0:
            res_t.set("0")
    except Exception as e:
        messagebox.showerror("Input Is Invalid", "Input Is Invalid.")
        res_t.set("")


# Create a button to display the text of entry widget
button = ttk.Button(win, text="Convert", command=systempicker).pack(pady=10)

#text displaying the result
res_t = tk.StringVar()
res_l = tk.Label(win, textvariable=res_t, font=("Century 12", 18))
res_l.pack(pady=10)

win.mainloop()