import random

import mysql.connector
import time
from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk

Item4 = 0

# Establish connection to the MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="11111111",
    database="taxi_booking"
)

# Now you can use the 'db' connection object to execute SQL queries or interact with the database

# For example:
cursor = db.cursor()
cursor.execute("SELECT * FROM Users")
result = cursor.fetchall()

# Don't forget to close the cursor and connection when done
cursor.close()
db.close()

class user:
    def __init__(self, master):
        # Window
        self.master = master
        # Some useful variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection
        with mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="11111111",
                database="taxi_booking"
        ) as db:
            c = db.cursor()

            find_user = 'SELECT * FROM Users WHERE username = %s and password = %s'
            c.execute(find_user, (self.username.get(), self.password.get()))
            result = c.fetchall()
            if result:
                self.logf.pack_forget()
                self.head['text'] = "Welcome, " + self.username.get()
                self.head.configure(fg="green")
            else:
                ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="11111111",
            database="taxi_booking"
        )
        c = db.cursor()

        # Find existing username if any take proper action
        find_user = 'SELECT * FROM Users WHERE username = %s'
        c.execute(find_user, (self.n_username.get(),))
        if c.fetchall():
            ms.showerror('Error!', 'Username Already Taken!')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
            # Create New Account
            insert = 'INSERT INTO Users(username, password) VALUES(%s, %s)'
            c.execute(insert, (self.n_username.get(), self.n_password.get()))
            db.commit()

    # Frame Packing Methods
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2, column=1)


class TaxiBooking:
    pass


class travel:

    def __init__(self, root):
        self.root = root
        self.root.title("Sejong Royal traveling Taxi")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='black')

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        journeyType = IntVar()
        carType = IntVar()

        varl1 = StringVar()
        varl2 = StringVar()
        varl3 = StringVar()
        self.reset_counter = 0

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Mobile = StringVar()
        Telephone = StringVar()
        Email = StringVar()

        TaxiTax = StringVar()
        Km = StringVar()
        Travel_Ins = StringVar()
        Luggage = StringVar()
        Receipt = StringVar()

        Standard = StringVar()
        PrimeSedan = StringVar()
        PremiumSedan = StringVar()

        TaxiTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")

        Standard.set("0")
        PrimeSedan.set("0")
        PremiumSedan.set("0")

        # Define Functions
        def iExit():
            iExit = ms.askyesno("Prompt!", "Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            TaxiTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            PrimeSedan.set("0")
            PremiumSedan.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0", END)
            self.txtReceipt2.delete("1.0", END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtTaxiTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)

            self.txtStandard.configure(state=DISABLED)
            self.txtPrimeSedan.configure(state=DISABLED)
            self.txtPremiumSedan.configure(state=DISABLED)
            self.reset_counter = 1

        def Receiptt():
            if self.reset_counter == 0 and Firstname.get() != "" and Surname.get() != "" and Address.get() != "" and Postcode.get() != "" and Mobile.get() != "" and Telephone.get() != "" and Email.get() != "":
                self.txtReceipt1.delete("1.0", END)
                self.txtReceipt2.delete("1.0", END)
                x = random.randint(10853, 500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END, "Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END, 'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END, 'Taxi No:\n')
                self.txtReceipt2.insert(END, 'TR' + randomRef + "\n")
                self.txtReceipt1.insert(END, 'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END, 'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END, 'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END, 'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END, 'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END, 'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END, 'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END, 'From:\n')
                self.txtReceipt2.insert(END, self.cboPickup.get() + "\n")
                self.txtReceipt1.insert(END, 'To:\n')
                self.txtReceipt2.insert(END, self.cboDrop.get() + "\n")
                self.txtReceipt1.insert(END, 'Pooling:\n')
                self.txtReceipt2.insert(END, self.cboPooling.get() + "\n")

                if var1.get() == 1:
                    self.txtReceipt1.insert(END, 'Standard:\n')
                    self.txtReceipt2.insert(END, Standard.get() + "\n")

                if var2.get() == 1:
                    self.txtReceipt1.insert(END, 'Prime Sedan:\n')
                    self.txtReceipt2.insert(END, PrimeSedan.get() + "\n")

                if var3.get() == 1:
                    self.txtReceipt1.insert(END, 'SUV:\n')
                    self.txtReceipt2.insert(END, PremiumSedan.get() + "\n")

                self.txtReceipt1.insert(END, 'Cost of Journey:\n')
                self.txtReceipt2.insert(END, SubTotal.get() + "\n")
                self.txtReceipt1.insert(END, 'Tax Paid:\n')
                self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                self.txtReceipt1.insert(END, 'SubTotal:\n')
                self.txtReceipt2.insert(END, SubTotal.get() + "\n")
                self.txtReceipt1.insert(END, 'Total Cost:\n')
                self.txtReceipt2.insert(END, TotalCost.get() + "\n")

            else:
                self.txtReceipt1.delete("1.0", END)
                self.txtReceipt2.delete("1.0", END)
                self.reset_counter = 0

        def taxi_cost():
            journeyCost = 0
            if carType.get() == 1:
                journeyCost = float(25.5)
                Km.set("15")
                if var1.get() == 1:
                    Standard.set("0")
                    PrimeSedan.set("0")
                    PremiumSedan.set("0")
                elif var2.get() == 1:
                    journeyCost += 2
                    Standard.set("0")
                    PrimeSedan.set("1")
                    PremiumSedan.set("0")
                elif var3.get() == 1:
                    journeyCost += 5
                    Standard.set("0")
                    PrimeSedan.set("0")
                    PremiumSedan.set("1")

            elif carType.get() == 2:
                journeyCost = float(30)
                Km.set("20")
                if var1.get() == 1:
                    Standard.set("1")
                    PrimeSedan.set("0")
                    PremiumSedan.set("0")
                elif var2.get() == 1:
                    journeyCost += 2
                    Standard.set("0")
                    PrimeSedan.set("1")
                    PremiumSedan.set("0")
                elif var3.get() == 1:
                    journeyCost += 5
                    Standard.set("0")
                    PrimeSedan.set("0")
                    PremiumSedan.set("1")

            elif carType.get() == 3:
                journeyCost = float(35.5)
                Km.set("30")
                if var1.get() == 1:
                    Standard.set("1")
                    PrimeSedan.set("0")
                    PremiumSedan.set("0")
                elif var2.get() == 1:
                    journeyCost += 2
                    Standard.set("0")
                    PrimeSedan.set("1")
                    PremiumSedan.set("0")
                elif var3.get() == 1:
                    journeyCost += 5
                    Standard.set("0")
                    PrimeSedan.set("0")
                    PremiumSedan.set("1")

            Travel_Ins.set("2")
            Luggage.set("1")

            Cost_of_Journey = "₩" + str('%.2f' % (journeyCost))
            Tax = "₩" + str('%.2f' % (journeyCost * 0.09))
            STotal = "₩" + str('%.2f' % (journeyCost + (journeyCost * 0.09)))
            TTotal = "₩" + str('%.2f' % (journeyCost + (journeyCost * 0.09) + 1 + 2))

            SubTotal.set(STotal)
            TotalCost.set(TTotal)
            PaidTax.set(Tax)

            self.txtReceipt1.insert(END, 'Cost of Journey:\n')
            self.txtReceipt2.insert(END, SubTotal.get() + "\n")
            self.txtReceipt1.insert(END, 'Tax Paid:\n')
            self.txtReceipt2.insert(END, PaidTax.get() + "\n")
            self.txtReceipt1.insert(END, 'SubTotal:\n')
            self.txtReceipt2.insert(END, SubTotal.get() + "\n")
            self.txtReceipt1.insert(END, 'Total Cost:\n')
            self.txtReceipt2.insert(END, TotalCost.get() + "\n")

        def Reset_Passenger():
            TaxiTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            PrimeSedan.set("0")
            PremiumSedan.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0", END)
            self.txtReceipt2.delete("1.0", END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtTaxiTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)

            self.txtStandard.configure(state=DISABLED)
            self.txtPrimeSedan.configure(state=DISABLED)
            self.txtPremiumSedan.configure(state=DISABLED)

            self.reset_counter = 0

        def check_button_state():
            if journeyType.get() == 1:
                self.txtTaxiTax.configure(state=NORMAL)
                self.txtKm.configure(state=NORMAL)
                self.txtTravel_Ins.configure(state=NORMAL)
                self.txtLuggage.configure(state=NORMAL)

            elif journeyType.get() == 2:
                self.txtTaxiTax.configure(state=NORMAL)
                self.txtKm.configure(state=NORMAL)
                self.txtTravel_Ins.configure(state=NORMAL)
                self.txtLuggage.configure(state=NORMAL)

            elif journeyType.get() == 3:
                self.txtTaxiTax.configure(state=NORMAL)
                self.txtKm.configure(state=NORMAL)
                self.txtTravel_Ins.configure(state=NORMAL)
                self.txtLuggage.configure(state=NORMAL)

        # Frames
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 60, 'bold'), text="\tSejong Royal Taxi\t", padx=12)
        self.lblTitle.grid()

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=500, padx=26, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=500, padx=26, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=750, height=300, font=('arial', 12, 'bold'), text="Booking Info\n", relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=550, height=300, font=('arial', 12, 'bold'), text="Receipt\n", relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)

        # Widgets
        self.lblFirstname = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Firstname", padx=2, pady=2)
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        self.txtFirstname = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Firstname, width=25)
        self.txtFirstname.grid(row=0, column=1)

        self.lblSurname = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Surname", padx=2, pady=2)
        self.lblSurname.grid(row=1, column=0, sticky=W)
        self.txtSurname = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Surname, width=25)
        self.txtSurname.grid(row=1, column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Address", padx=2, pady=2)
        self.lblAddress.grid(row=2, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Address, width=25)
        self.txtAddress.grid(row=2, column=1)

        self.lblPostcode = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Postal Code", padx=2, pady=2)
        self.lblPostcode.grid(row=3, column=0, sticky=W)
        self.txtPostcode = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Postcode, width=25)
        self.txtPostcode.grid(row=3, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Mobile", padx=2, pady=2)
        self.lblMobile.grid(row=4, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Mobile, width=25)
        self.txtMobile.grid(row=4, column=1)

        self.lblTelephone = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Telephone", padx=2, pady=2)
        self.lblTelephone.grid(row=5, column=0, sticky=W)
        self.txtTelephone = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Telephone, width=25)
        self.txtTelephone.grid(row=5, column=1)

        self.lblEmail = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Email", padx=2, pady=2)
        self.lblEmail.grid(row=6, column=0, sticky=W)
        self.txtEmail = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Email, width=25)
        self.txtEmail.grid(row=6, column=1)

        self.lblPickup = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Pickup", padx=2, pady=2)
        self.lblPickup.grid(row=7, column=0, sticky=W)
        self.cboPickup = ttk.Combobox(DataFrameLEFT, textvariable=varl1, state='readonly', font=('arial', 12, 'bold'), width=23)
        self.cboPickup['value'] = ('', 'Seoul', 'Busan', 'Daegu', 'Incheon', 'Daejeon', 'Gwangju', 'Ulsan')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=7, column=1)

        self.lblDrop = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Drop", padx=2, pady=2)
        self.lblDrop.grid(row=8, column=0, sticky=W)
        self.cboDrop = ttk.Combobox(DataFrameLEFT, textvariable=varl2, state='readonly', font=('arial', 12, 'bold'), width=23)
        self.cboDrop['value'] = ('', 'Seoul', 'Busan', 'Daegu', 'Incheon', 'Daejeon', 'Gwangju', 'Ulsan')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=8, column=1)

        self.lblPooling = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Pooling", padx=2, pady=2)
        self.lblPooling.grid(row=9, column=0, sticky=W)
        self.cboPooling = ttk.Combobox(DataFrameLEFT, textvariable=varl3, state='readonly', font=('arial', 12, 'bold'), width=23)
        self.cboPooling['value'] = ('', 'Yes', 'No')
        self.cboPooling.current(0)
        self.cboPooling.grid(row=9, column=1)

        self.chkStandard = Checkbutton(DataFrameLEFT, text="Standard", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold')).grid(row=10, column=0, sticky=W)
        self.txtStandard = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Standard, width=25, state=DISABLED)
        self.txtStandard.grid(row=10, column=1)

        self.chkPrimeSedan = Checkbutton(DataFrameLEFT, text="Prime Sedan", variable=var2, onvalue=1, offvalue=0, font=('arial', 12, 'bold')).grid(row=11, column=0, sticky=W)
        self.txtPrimeSedan = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PrimeSedan, width=25, state=DISABLED)
        self.txtPrimeSedan.grid(row=11, column=1)

        self.chkPremiumSedan = Checkbutton(DataFrameLEFT, text="Premium Sedan", variable=var3, onvalue=1, offvalue=0, font=('arial', 12, 'bold')).grid(row=12, column=0, sticky=W)
        self.txtPremiumSedan = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PremiumSedan, width=25, state=DISABLED)
        self.txtPremiumSedan.grid(row=12, column=1)

        self.lblTaxiTax = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Taxi Tax", padx=2, pady=2)
        self.lblTaxiTax.grid(row=0, column=2, sticky=W)
        self.txtTaxiTax = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=TaxiTax, width=25, state=DISABLED)
        self.txtTaxiTax.grid(row=0, column=3)

        self.lblKm = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Distance(Km)", padx=2, pady=2)
        self.lblKm.grid(row=1, column=2, sticky=W)
        self.txtKm = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Km, width=25, state=DISABLED)
        self.txtKm.grid(row=1, column=3)

        self.lblTravel_Ins = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Travelling Insurance", padx=2, pady=2)
        self.lblTravel_Ins.grid(row=2, column=2, sticky=W)
        self.txtTravel_Ins = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Travel_Ins, width=25, state=DISABLED)
        self.txtTravel_Ins.grid(row=2, column=3)

        self.lblLuggage = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Extra Luggage", padx=2, pady=2)
        self.lblLuggage.grid(row=3, column=2, sticky=W)
        self.txtLuggage = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Luggage, width=25, state=DISABLED)
        self.txtLuggage.grid(row=3, column=3)

        self.lblMode = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Mode of Payment", padx=2, pady=2)
        self.lblMode.grid(row=4, column=2, sticky=W)
        self.cboMode = ttk.Combobox(DataFrameLEFT, state='readonly', font=('arial', 12, 'bold'), width=23)
        self.cboMode['value'] = ('', 'Cash', 'Debit Card', 'Credit Card', 'Paytm', 'PhonePe', 'Amazon Pay')
        self.cboMode.current(0)
        self.cboMode.grid(row=4, column=3)

        # ===================================Receipt=======================================================
        self.txtReceipt1 = Text(DataFrameRIGHT, height=22, width=70, bd=10, font=('arial', 12, 'bold'))
        self.txtReceipt1.grid(row=0, column=0)
        self.txtReceipt2 = Text(DataFrameRIGHT, height=22, width=70, bd=10, font=('arial', 12, 'bold'))
        self.txtReceipt2.grid(row=0, column=1)

        # ===================================Buttons=======================================================
        self.btnTotal = Button(ButtonFrame, text='Total', padx=2, pady=2, bd=2, font=('arial', 20, 'bold'), width=14, height=1, command=Receipt).grid(row=0, column=0)
        self.btnReceipt = Button(ButtonFrame, text='Receipt', padx=2, pady=2, bd=2, font=('arial', 20, 'bold'), width=14, height=1, command=Receipt).grid(row=0, column=1)
        self.btnReset = Button(ButtonFrame, text='Reset', padx=2, pady=2, bd=2, font=('arial', 20, 'bold'), width=14, height=1, command=Reset_Passenger).grid(row=0, column=2)
        self.btnExit = Button(ButtonFrame, text='Exit', padx=2, pady=2, bd=2, font=('arial', 20, 'bold'), width=14, height=1, command=iExit).grid(row=0, column=3)

        # ===================================Binding Function===============================================
        self.cboPickup.bind("<<ComboboxSelected>>", taxi_cost)
        self.cboDrop.bind("<<ComboboxSelected>>", taxi_cost)
        self.cboPooling.bind("<<ComboboxSelected>>", taxi_cost)
        self.cboMode.bind("<<ComboboxSelected>>", taxi_cost)

        self.chkStandard.bind("<Button-1>", taxi_cost)
        self.chkPrimeSedan.bind("<Button-1>", taxi_cost)
        self.chkPremiumSedan.bind("<Button-1>", taxi_cost)

        self.txtFirstname.bind("<FocusOut>", taxi_cost)
        self.txtSurname.bind("<FocusOut>", taxi_cost)
        self.txtAddress.bind("<FocusOut>", taxi_cost)
        self.txtPostcode.bind("<FocusOut>", taxi_cost)
        self.txtMobile.bind("<FocusOut>", taxi_cost)
        self.txtTelephone.bind("<FocusOut>", taxi_cost)
        self.txtEmail.bind("<FocusOut>", taxi_cost)

        check_button_state()

    # Run the application
    root = Tk()

    root.mainloop()
