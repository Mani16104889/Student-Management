from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window=Tk()
window.title("Student registration")
window.geometry("1366x768")

global sno
sno=1
def addRecord():
    if(txtName.get() !="" and txtage.get() !="" and txtdob.get() !="" and gentxt.get() !="" and txtstd.get() !="" and
    txtreg.get() !="" and txtCon.get() !="" and txtMail !="" and txtAdd.get() !=""):

        global sno
        myTree.insert("", index="end", iid=sno, values=(sno, txtName.get(), txtage.get(), txtdob.get(), gentxt.get(),
                                                        txtstd.get(), txtreg.get(), txtCon.get(), txtMail.get(), txtAdd.get()))
        txtName.delete(0, END)
        txtage.delete(0, END)
        txtdob.delete(0, END)
        gentxt.delete(0, END)
        txtstd.delete(0, END)
        txtreg.delete(0, END)
        txtCon.delete(0, END)
        txtMail.delete(0, END)
        txtAdd.delete(0, END)

        sno+=1

    else:
        messagebox.showinfo("Message", "Please Fill All Details")

def selectRecord():
    txtName.delete(0, END)
    txtage.delete(0, END)
    txtdob.delete(0, END)
    gentxt.delete(0, END)
    txtstd.delete(0, END)
    txtreg.delete(0, END)
    txtCon.delete(0, END)
    txtMail.delete(0, END)
    txtAdd.delete(0, END)

    selected=myTree.focus()
    values=myTree.item(selected, "values")
    # messagebox.showinfo("Message", values)

    txtName.insert(0, values[1])
    txtage.insert(0, values[2])
    txtdob.insert(0, values[3])
    gentxt.insert(0, values[4])
    txtstd.insert(0, values[5])
    txtreg.insert(0, values[6])
    txtCon.insert(0, values[7])
    txtMail.insert(0, values[8])
    txtAdd.insert(0, values[9])

def updateRecord():
    if (txtName.get() !="" and txtage.get() !="" and txtdob.get() !="" and gentxt.get() !="" and txtstd.get() !="" and
    txtreg.get() !="" and txtCon.get() !="" and txtMail !="" and txtAdd.get() !=""):

        no=myTree.focus()[0] #column id
        selected=myTree.focus() #Row id
        myTree.item(selected, values=(no, txtName.get(), txtage.get(), txtdob.get(), gentxt.get(), txtstd.get(),
                                      txtreg.get(), txtCon.get(), txtMail.get(), txtAdd.get()))
        txtName.delete(0, END)
        txtage.delete(0, END)
        txtdob.delete(0, END)
        gentxt.delete(0, END)
        txtstd.delete(0, END)
        txtreg.delete(0, END)
        txtCon.delete(0, END)
        txtMail.delete(0, END)
        txtAdd.delete(0, END)

    else:
        messagebox.showinfo("Message", "Please Fill All Details")

def deleteRecord():
    record=myTree.selection()[0]
    # messagebox.showinfo("Message", record)
    myTree.delete(record)
    txtName.delete(0, END)
    txtage.delete(0, END)
    txtdob.delete(0, END)
    gentxt.delete(0, END)
    txtstd.delete(0, END)
    txtreg.delete(0, END)
    txtCon.delete(0, END)
    txtMail.delete(0, END)
    txtAdd.delete(0, END)

def deleteAllRecord():
    record=myTree.get_children()
    for data in record:
        myTree.delete(data)


myframe=Frame(window, bg="#d234eb")
myframe.pack(fill=X)

lbltitle=Label(myframe, text="STUDENT REGISTRATION", font=("times", 20, "bold"), fg="black")
lbltitle.grid(row=0, columnspan=7, pady=20)

lblName=Label(myframe, text="Name", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lblName.grid(row=1, column=0, sticky=W)

txtName=Entry(myframe, font=("times", 15), bg="#eb3495")
txtName.grid(row=1, column=1, padx=10)

lblAdd=Label(myframe, text="Address", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lblAdd.grid(row=2, column=0, sticky=W)

txtAdd=Entry(myframe, font=("times", 15))
txtAdd.grid(row=2, column=1, padx=10)

lblCon=Label(myframe, text="Contract", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lblCon.grid(row=3, column=0, sticky=W)

txtCon=Entry(myframe, font=("times", 15))
txtCon.grid(row=3, column=1, padx=10)

lblage=Label(myframe, text="Age", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lblage.grid(row=1, column=2, sticky=W)

txtage=Entry(myframe, font=("times", 15))
txtage.grid(row=1, column=3, padx=10)

lbldob=Label(myframe, text="Date of Birth", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lbldob.grid(row=1, column=4, sticky=W)

txtdob=Entry(myframe, font=("times", 15))
txtdob.grid(row=1, column=5, padx=10)

lblreg=Label(myframe, text="Reg No", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lblreg.grid(row=2, column=2, sticky=W)

txtreg=Entry(myframe, font=("times", 15))
txtreg.grid(row=2, column=3, padx=10)

lblgen=Label(myframe, text="Gender", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lblgen.grid(row=2, column=4, sticky=W)

gentxt=ttk.Combobox(myframe, state="readonly", font=("times", 14, "bold"), width=18)
gentxt["values"] = ("Male", "Female")
gentxt.grid(row=2, column=5, padx=10)

lblstd=Label(myframe, text="Standard", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lblstd.grid(row=3, column=2)

txtstd = ttk.Combobox(myframe, state="readonly", font=("times",14,"bold"), width=18)
txtstd["values"] = ("6th", "7th", "8th", "9th", "10th", "11th", "12th")
txtstd.grid(row=3, column=3, padx=10)

lblMail=Label(myframe, text="Email", font=("times", 15, "bold"), bg="#d234eb", pady=5)
lblMail.grid(row=3, column=4, sticky=W)

txtMail=Entry(myframe, font=("times", 15))
txtMail.grid(row=3, column=5, padx=10)

btnframe=Frame(window, bg="#34abeb")
btnframe.pack(fill=X)

btnAdd=Button(btnframe, text="Add Record", bg="#1289A7", width=10, padx=5, pady=5, fg="white",
              font=("times", 13, "bold"), command=addRecord)
btnAdd.grid(row=1, column=0, padx=5, pady=10)

btnSelect=Button(btnframe, text="Select Record", bg="#10ac84", width=10, padx=5, pady=5, fg="white",
                 font=("times", 13, "bold"), command=selectRecord)
btnSelect.grid(row=1, column=1, padx=5, pady=10)

btnUpdate=Button(btnframe, text="Update Record", bg="#3c6382", width=10, padx=5, pady=5, fg="white",
                 font=("times", 13, "bold"), command=updateRecord)
btnUpdate.grid(row=1, column=2, padx=5, pady=10)

btnDelete=Button(btnframe, text="Delete Record", bg="#d63031", width=10, padx=5, pady=5, fg="white",
                 font=("times", 13, "bold"), command=deleteRecord)
btnDelete.grid(row=1, column=3, padx=5, pady=10)

btndeleteall=Button(btnframe, text="DeleteAll Record", bg="#d63031", width=15, padx=5, pady=5, fg="white",
                    font=("times", 13, "bold"), command=deleteAllRecord)
btndeleteall.grid(row=1, column=4, padx=5, pady=10)

myTree=ttk.Treeview(window)
myTree["columns"]=("S.No", "Name", "Age", "Date of birth", "Gender", "Standard", "Regno", "Contact", "Email", "Address")

myTree.column("#0", width=0, stretch=NO)
myTree.column("#1", width=10)
myTree.column("#2", width=80)
myTree.column("#3", width=20)
myTree.column("#4", width=80)
myTree.column("#5", width=80)
myTree.column("#6", width=60)
myTree.column("#7", width=80)
myTree.column("#8", width=80)
myTree.column("#9", width=80)
myTree.column("#10", width=80)

myTree.heading("#0", text="")
myTree.heading("#1", text="S.No")
myTree.heading("#2", text="NAME")
myTree.heading("#3", text="AGE")
myTree.heading("#4", text="DATE OF BIRTH")
myTree.heading("#5", text="GENDER")
myTree.heading("#6", text="STANDARD")
myTree.heading("#7", text="REG NO")
myTree.heading("#8", text="CONTRACT")
myTree.heading("#9", text="EMAIL")
myTree.heading("#10", text="ADDRESS")


data=[["Manikandan", "16", "22/04/1999", "Male", "viii", "16104889", "9677311696", "mani@gmail.com", "Puducherry"],
["Ganesh", "12", "27/08/1997", "Male", "vi", "16104887", "9677311691", "ganesh@gmail.com", "Salem"],
["barath", "12", "22/09/1992", "Male", "vi", "16104866", "9677311789", "barath@gmail.com", "Puducherry"],
["jagan", "14", "14/07/1996", "Male", "vii", "16104877", "9677311356", "jagan@gmail.com", "Trichy"],
["sasi", "12", "30/04/2002", "Male", "vi", "16104856", "9677311769", "sasi@gmail.com", "Puducherry"],
]

for datas in data:
    myTree.insert("", index="end", iid=sno, values=(sno, datas[0], datas[1], datas[2], datas[3], datas[4],
                                                    datas[5], datas[6], datas[7], datas[8]))
    sno+=1

# myTree.insert("", index=0, values=(1, "Manikandan", "Puducherry", "9677311696", "mani@gmail.com"))

myTree.pack(fill=X)



window.mainloop()