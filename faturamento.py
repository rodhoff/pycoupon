from tkinter import *
from tkinter import Tk, Label, ttk, messagebox
from PIL import Image, ImageTk
from escpos import NetworkConnection
from escpos import SerialConnection
from escpos.impl.epson import GenericESCPOS

import pymysql


window = Tk()
window.geometry("1280x960")
window.title("Faturamentos em Python | padilhajordane@gmail.com")
# window.configure(bg='#093249')
#image_path = "caminho\da\sua\imagem"
#image = Image.open(image_path)
#background_Label = Label(window)
#background_Label.place(x=0, y=0, relwidth=1, relheight=1)
#photo = ImageTk.PhotoImage(image)
#background_Label.configure(image=photo)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

def quantityFieldListener(a, b, c):
    global quantityVar
    global costVar
    global itemRate
    quantity = quantityVar.get()
    if quantity != "":
        try:
            quantity = float(quantity)
            cost = quantity * itemRate
            quantityVar.set("%.2f" % quantity)
            costVar.set("%.2f" % cost)
        except ValueError:
            quantity = quantity[:-1]
            quantityVar.set(quantity)
    else:
        quantity = 0
        quantityVar.set("%.2f" % quantity)


def costFieldListener(a, b, c):
    global quantityVar
    global costVar
    global itemRate
    cost = costVar.get()
    if cost != "":
        try:
            cost = float(cost)
            quantity = cost / itemRate
            quantityVar.set("%.2f" % quantity)
            costVar.set("%.2f" % cost)
        except ValueError:
            cost = cost[:-1]
            costVar.set(cost)
    else:
        cost = 0
        costVar.set(cost)


usernameVar = StringVar()
passwordVar = StringVar()

options = ["Item1", "Item2", "Item3"]
rateDict = {}
itemVariable = StringVar()
itemVariable.set(options[0])

quantityVar = StringVar()
quantityVar.trace('w', quantityFieldListener)
itemRate = 2
rateVar = StringVar()
rateVar.set("%.2f" % itemRate)
costVar = StringVar()
costVar.trace('w', costFieldListener)

billsTV = ttk.Treeview(height=15, columns=('Name','Rate', 'Quantity', 'Cost'))

updateTV = ttk.Treeview(height=15, columns=('name', 'rate', 'type','storetype'))


storeOptions = ['Opção1', 'Opção2']
addItemNameVar = StringVar()
addItemRateVar = StringVar()
addItemTypeVar = StringVar()
addstoredVar = StringVar()
addstoredVar.set(storeOptions[0])

itemLists = list ()
totalCost=0.0
totalCostVar = StringVar()
totalCostVar.set("Total = {}" .format(totalCost))

updateItemId =""

def generate_bill():
    global itemVariable
    global quantityVar
    global itemRate
    global costVar
    global itemLists
    global totalCost
    global totalCostVar

    itemName = itemVariable.get()
    quantity = quantityVar.get()
    cost = costVar.get()
    conn = pymysql.connect(host="localhost", user="root", passwd="@Brasil01", db="billservice")
    cursor = conn.cursor()

    query = "insert into tabela_exemplo (name,quantity,rate,cost) value('{}',10,'{}', 10 )".format(itemName, itemRate)
    cursor.execute(query)
    conn.commit()
    conn.close()

    listDict = {"name":itemName, "rate":itemRate, "quantity":quantity,"cost":10}
    itemLists.append(listDict)
    cost = "10"
    totalCost=float(cost)
    quantityVar.set("0")
    costVar.set("0")

    updateListView()
    totalCostVar.set("Total = {}".format(totalCost))

def onDoubleClick(event):
    global  addItemNameVar
    global addItemRateVar
    global addItemTypeVar
    global addstoredVar
    global updateItemId
    item = updateTV.selection()
    updateItemId = updateTV.item(item,"text")
    item_detail = updateTV.item(item,"values")
    item_index = storeOptions.index(item_detail[3])
    addItemTypeVar.set(item_detail[2])
    addItemRateVar.set(item_detail[1])
    addItemNameVar.set(item_detail[0])
    addstoredVar.set(storeOptions[item_index])


def updateListView():
    records = billsTV.get_children()
    for element in records:
        billsTV.delete(element)

    for row in itemLists:
        billsTV.insert('','end', text=row['name'], values=(row["rate"],row["quantity"],row["cost"]))


def getItemLists():
    records=updateTV.get_children()
    for element in records:
        updateTV.delete(element)
    conn = pymysql.connect(host="localhost", user="root", passwd="@Brasil01", db="billservice")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from tabela_exemplo"
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        updateTV.insert('','end',text=row['name'], values=(row['name'],row['rate'],row['type'],row['storetype']))
    updateTV.bind("<Double-1>", onDoubleClick)
    conn.close()


def print_bill():
    conn = SerialConnection.create('COM2:9600,8,1,N')    
    printer = GenericESCPOS(conn)
    printer.init()
    printer.text('----> Printer Test')
    global itemLists
    global totalCost
    print("======================== Cupom Fiscal ======================")
    print("=========================== Nome_qualquer ==================")
    print("{:<20} {:<10} {:<15} {:<10}".format("Nome","Valor Unit.","Quantidade","Valor Total"))
    print("============================================================")

    for item in itemLists:
        print("{:<20} {:<10} {:<15} {:<10}".format(item["name"], item["rate"], item["quantity"], item["cost"]))

    print("============================================================")
    print("{:<20} {:<10} {:<15} {:<10}".format("Total = ", " ", " ",totalCost))
    itemLists = []
    totalCost=0.0
    updateListView()
    totalCostVar.set("Total = {}".format(totalCost))


def iExit():
    window.destroy()

def moveToUpdate():
    remove_all_widgets()
    updateItemWindow()


def moveToBills():
    remove_all_widgets()
    ViewAllBills()



def readAllData():
    global options
    global rateDict
    global itemVariable
    global itemRate
    global rateVar
    options = []
    rateDict = {}
    conn = pymysql.connect(host="localhost", user="root", passwd="@Brasil01", db="billservice")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = "select * from tabela_exemplo"
    cursor.execute(query)
    data = cursor.fetchall()
    count = 0
    for row in data:
        count += 1
        options.append(row['name'])
        rateDict[row['name']] = row['rate']
        itemVariable.set(options[0])
        itemRate = str(rateDict[options[0]])  # int
    conn.close()
    rateVar.set(itemRate)  # "%.2f"%
    if count == 0:
        remove_all_widgets()
        itemAddWindow()
    else:
        remove_all_widgets()
        mainwindow()

def optionMenuListener(event):
    global  itemVariable
    global rateDict
    global itemRate
    item = itemVariable.get()
    itemRate=float(rateDict[item])
    rateVar.set("%.2f"%itemRate)

def remove_all_widgets():
    global window
    for widget in window.winfo_children():
        widget.grid_remove()

def updateBillsData():
    records = billsTV.get_children()
    for element in records:
        billsTV.delete(element)

    conn = pymysql.connect(host="localhost", user="root", passwd="@Brasil01", db="billservice")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from tabela_exemplo"
    cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
            billsTV.insert('', 'end', text=row['name'], values=(row["rate"], row["quantity"], row["cost"]))

    conn.close()


def adminLogin():
    global usernameVar
    global passwordVar

    username = usernameVar.get()
 
#   password = passwordVar.get()

    conn = pymysql.connect(host="localhost", user="root", passwd="@Brasil01", db="billservice")
    cursor = conn.cursor()
    query = "select * from users where username='{}' ".format(username)
#    and password='{}'
    cursor.execute(query)
    data = cursor.fetchall()
    admin = False
    for row in data:
        admin = True
    conn.close()
    if admin:
        remove_all_widgets()
        itemAddWindow()
    else:
        messagebox.showerror("Usuário ou Senha Inválido","Insira usuário e senha corretamente")


def addItemListener():
    remove_all_widgets()
    itemAddWindow()


def goBack():
    remove_all_widgets()
    mainwindow()


def addItem():
    global addItemNameVar
    global addItemRateVar
    global addItemTypeVar
    global addstoredVar
    name = addItemNameVar.get()
    rate = addItemRateVar.get()
    Type = addItemTypeVar.get()
    storetype = addstoredVar.get()
    nameId = name.replace(" ", "_")
    conn = pymysql.connect(host="localhost", user="root", passwd="@Brasil01", db="billservice")
    cursor = conn.cursor()
    query = "insert into tabela_exemplo (name,rate,type,storetype) value('{}','{}','{}','{}')".format(name, rate, Type, storetype)
    cursor.execute(query)
    conn.commit()
    conn.close()
    addItemNameVar.set("")
    addItemRateVar.set("")
    addItemTypeVar.set("")

def updateItem():
    global addItemNameVar
    global addItemRateVar
    global addItemTypeVar
    global addstoredVar
    global updateItemId

    name = addItemNameVar.get()
    rate = addItemRateVar.get()
    Type = addItemTypeVar.get()
    storetype = addstoredVar.get()
    conn = pymysql.connect(host="localhost", user="root", passwd="@Brasil01", db="billservice")
    cursor = conn.cursor()
    query = "UPDATE tabela_exemplo SET name='{}', rate='{}', type='{}', storetype='{}' WHERE nameid={}".format(name, rate, Type, storetype, updateItemId)
    cursor.execute(query)
    conn.commit()
    conn.close()

    addItemNameVar.set("")
    addItemRateVar.set("")
    addItemTypeVar.set("")
    getItemLists()



def loginWindow():

    window.geometry(f"{screen_width}x{screen_height}")
    #window.attributes('-fullscreen', True)


    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30), bg='#093249',fg="white")
    titleLabel.grid(row=0, column=0, columnspan=4, padx=(130, 0), pady=(10, 0))

    loginLabel = Label(window, text="Login", font="Arial 30",bg='#093249', fg="white")
    loginLabel.grid(row=1, column=1, padx= (0,850), columnspan=2, pady=(170,5))

    usernameLabel = Label(window, text="Usuario :", font=("bold", 15), bg='#093249', fg="white")
    usernameLabel.grid(row=2, column=1, padx=(30, 100), pady=5)

    passwordLabel = Label(window, text="Senha :", font=("bold", 15),bg='#093249', fg="white")
    passwordLabel.grid(row=3, column=1, padx=(30, 100), pady=5)

    usernameEntry = Entry(window, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2,padx= (0,900), pady=5)

    passwordEntry = Entry(window, textvariable=passwordVar, show="*")
    passwordEntry.grid(row=3, column=2, padx= (0,900), pady=5)

    loginButton = Button(window, text="Entrar", bg='#093249', fg="white", font=("arial", 17), width=15, height=2,command=lambda: adminLogin())
    loginButton.grid(row=4, column=1, columnspan=2,padx= (0,850))




def mainwindow():
    window.geometry(f"{screen_width}x{screen_height}")

    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30),  bg='#093249', fg="white")
    titleLabel.grid(row=0, column=1, columnspan=4, pady=(10, 0))

    addNewItem = Button(window, text="Add Produto", font=("bold", 10), width=15, bg='#093249', fg="white", height=2, command=lambda: addItemListener())
    addNewItem.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))
    updateItem = Button(window, text="Atualizar", bg='#093249', font=("bold", 10), fg="white", width=15, height=2, command=lambda: moveToUpdate())
    updateItem.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))

    showallEntry = Button(window, text="Historico", width=15, height=2, font=("bold", 10), bg='#093249', fg="white", command=lambda: moveToBills())
    showallEntry.grid(row=1, column=2, padx=(10, 0), pady=(10, 0))


    itemLabel = Label(window, text="Selecionar Produto", bg='#093249',fg="white")
    itemLabel.grid(row=2, column=0, padx=(5, 0), pady=(10, 0))

    itemDropDown=OptionMenu(window,itemVariable,*options, command=optionMenuListener)
    itemDropDown.grid(row=2, column=1,padx=(10,0), pady=(10,0))

    rateLabel = Label(window, text="Preço",bg='#093249', fg="white")
    rateLabel.grid(row=2, column=2, padx=(10, 0), pady=(10, 0))

    rateValue = Label(window, bg="white", textvariable=rateVar)
    rateValue.grid(row=2, column=3, padx=(10, 0), pady=(10, 0))
    rateValue.config(width=10, height=1)

    quantityLabel = Label(window, bg='#093249', fg="white",text="Quantidade")
    quantityLabel.grid(row=3, column=0, padx=(5, 0), pady=(10, 0))

    quantityEntry = Entry(window, textvariable=quantityVar)
    quantityEntry.grid(row=3, column=1, padx=(5, 0), pady=(10, 0))

    costLabel = Label(window, bg='#093249', fg="white",text="Valor Total do Produto")
    costLabel.grid(row=3, column=2, padx=(10, 0), pady=(10, 0))

    costEntry = Entry(window, textvariable=costVar)
    costEntry.grid(row=3, column=3, padx=(10, 0), pady=(10, 0))

    buttonBill = Button(window, text="Adicionar a lista", font=("bold", 10), width=15, bg='#093249', fg="white",command=lambda: generate_bill())
    buttonBill.grid(row=4, column=4, padx=(2, 0), pady=(20, 0))

    billLabel = Label(window, text="Lista De Produtos", font="bold 25", bg='#093249', fg="white")
    billLabel.grid(row=4, column=2)

    billsTV.grid(row=5, column=0, columnspan=5, padx=(5))

    scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=5, column=3, padx=(300,0),sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading('#0', text="Prod Nome")
    billsTV.heading('#1', text="Taxa")
    billsTV.heading('#2', text="Quantidade")
    billsTV.heading('#3', text="Custo")

    generateBill = Button(window, text="Gerar Cupom Fiscal",font=("bold", 10), width=15, bg='#093249',fg="white", command=lambda:print_bill())
    generateBill.grid(row=1, column=4)

    totalCostLabel = Label(window, textvariable=totalCostVar,bg='#093249',fg="white")
    totalCostLabel.grid(row=6, column=1)
    totalCostLabel.config(width=8, height=1)

    logoutBtn = Button(window, text="Sair", width=15, height=2, font=("bold", 10), bg='#093249', fg="white", command=lambda: iExit())
    logoutBtn.grid(row=6, column=4, pady=(10, 0))

    updateListView()

def itemAddWindow():
    window.geometry(f"{screen_width}x{screen_height}")

    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30), bg='#093249',fg="white")
    titleLabel.grid(row=0, column=2, columnspan=3, pady=(10, 0))

    itemNameLabel = Label(window, text="Nome", bg='#093249',fg="white")
    itemNameLabel.grid(row=1, column=1, pady=(10, 0))

    itemNameEntry = Entry(window, textvariable=addItemNameVar)
    itemNameEntry.grid(row=1, column=2, pady=(10, 0))

    itemRateLabel = Label(window, text="Preço", bg='#093249',fg="white")
    itemRateLabel.grid(row=1, column=3, pady=(10, 0))

    itemRateEntry = Entry(window, textvariable=addItemRateVar)
    itemRateEntry.grid(row=1, column=4, pady=(10, 0))

    itemtypeLabel = Label(window, text="Descrição do Produto",bg='#093249',fg="white")
    itemtypeLabel.grid(row=2, column=1, pady=(10, 0))

    itemTypeEntry = Entry(window, textvariable=addItemTypeVar)
    itemTypeEntry.grid(row=2, column=2, pady=(10, 0))

    storeTypeLabel = Label(window, text="Classificação por tipagem", bg='#093249',fg="white")
    storeTypeLabel.grid(row=2, column=3, pady=(10, 0))
    storeEntry = OptionMenu(window, addstoredVar, *storeOptions)
    storeEntry.grid(row=2, column=4, pady=(10, 0))

    AddItemButton = Button(window, text="Add Prod", bg='#093249',fg="white", width=20, height=2,command=lambda: addItem())
    AddItemButton.grid(row=3, column=3, pady=(10, 0))

    backButton = Button(window, text="Voltar",bg='#093249',fg="white", command=lambda: readAllData())
    backButton.grid(row=6, column=5)



def updateItemWindow():
    window.geometry(f"{screen_width}x{screen_height}")

    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30), bg='#093249',fg="white")
    titleLabel.grid(row=0, column=2, columnspan=4, pady=(10, 0))

    itemNameLabel = Label(window, text="Nome", bg='#093249',fg="white")
    itemNameLabel.grid(row=1, column=1, pady=(10, 0))

    itemNameEntry = Entry(window, textvariable=addItemNameVar)
    itemNameEntry.grid(row=1, column=2, pady=(10, 0))

    itemRateLabel = Label(window, text="Preço", bg='#093249',fg="white")
    itemRateLabel.grid(row=1, column=3, pady=(10, 0))

    itemRateEntry = Entry(window, textvariable=addItemRateVar)
    itemRateEntry.grid(row=1, column=4, pady=(10, 0))

    itemtypeLabel = Label(window, text="Descrição do Produto", bg='#093249',fg="white")
    itemtypeLabel.grid(row=2, column=1, pady=(10, 0))

    itemTypeEntry = Entry(window, textvariable=addItemTypeVar)
    itemTypeEntry.grid(row=2, column=2, pady=(10, 0))

    storeTypeLabel = Label(window, text="Classificação por tipagem", bg='#093249',fg="white")
    storeTypeLabel.grid(row=2, column=3, pady=(10, 0))
    storeEntry = OptionMenu(window, addstoredVar, *storeOptions)
    storeEntry.grid(row=2, column=4, pady=(10, 0))

    AddItemButton = Button(window, text="Atualizar Produto", bg='#093249', fg="white", width=20, height=2, command=lambda: updateItem())
    AddItemButton.grid(row=3, column=3, pady=(10, 0))

    updateTV.grid(row=5, column=0, columnspan=5, padx=(9))

    scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=5, column=4, sticky="NSE")

    updateTV.configure(yscrollcommand=scrollBar.set)

    updateTV.heading('#0', text="Prod ID")
    updateTV.heading('#1', text="Prod Nome")
    updateTV.heading('#2', text="Preço")
    updateTV.heading('#3', text="Tipo")
    updateTV.heading('#4', text="Tipo Estoque")

    backButton = Button(window, text="Voltar", bg='#093249', fg="white", command=lambda: readAllData())
    backButton.grid(row=6, column=5)

    getItemLists()

def ViewAllBills():
    window.geometry(f"{screen_width}x{screen_height}")

    titleLabel = Label(window, text="▀▄▀▄▀▄▀▄▀▄▀▄Outofbox Faturamentos▀▄▀▄▀▄▀▄▀▄▀▄", font=("bold", 30), bg='#093249',fg="white")
    titleLabel.grid(row=1, column=0, columnspan=4,padx=30, pady=(10,10))


    billsTV.grid(row=5, column=0, columnspan=5, padx=(5))

    scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=5, column=3, padx=(300, 0), sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading('#0', text="Prod Nome")
    billsTV.heading('#1', text="Taxa")
    billsTV.heading('#2', text="Quantidade")
    billsTV.heading('#3', text="Custo")

    backButton = Button(window, text="Voltar",bg='#093249',fg="white", command=lambda: readAllData())
    backButton.grid(row=6, column=5)

    updateBillsData()


loginWindow()
window.mainloop()
