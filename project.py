from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
import cx_Oracle

class login_system:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #######################################################################################################

        self.ID_var=StringVar()
        self.NAME_var=StringVar()
        self.SEX_var=StringVar()
        self.FATHERS_NAME_var=StringVar()
        self.MOBILE_NO_var=StringVar()
        self.FATHERS_MOBILE_NO_var=StringVar()
        self.SECONDARY_var=StringVar()
        self.HIGHER_SECONDARY_var=StringVar()
        self.BRANCH_var=StringVar()
        self.ACADEMIC_YEAR_var=StringVar()
        self.STATE_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.room=StringVar()
        self.First_Sem=StringVar()
        self.Second_Sem=StringVar()
        self.Third_Sem=StringVar()
        self.Fourth_Sem=StringVar()
        self.Fivth_Sem=StringVar()
        self.Sixth_Sem=StringVar()
        self.Seventh_Sem=StringVar()
        self.Eighth_Sem=StringVar()
        self.receipt_no=StringVar()
        self.tuition_fees=StringVar()
        self.hostel_fees=StringVar()
        self.status=StringVar()
        self.uname=StringVar()
        self.pass_=StringVar()
        self.hostel_check=StringVar()
        self.t=0
        self.check=list()
        self.a=0
        self.receipt=0
        self.receipt_max=0
        self.hostel_status=0

        ########################################################################################################################
        ############################################ LOGIN FRAME ###############################################################
        ########################################################################################################################

        self.bg_icon=PhotoImage(file="images.png")
        self.user_icon=PhotoImage(file="usr.png")
        self.pass_icon=PhotoImage(file="pass.png")
        self.logo_icon=PhotoImage(file="icon.png")
        bg_lbl=Label(self.root, image=self.bg_icon).pack()
        title=Label(self.root, text="Login", font=("Algerian", 40), bg="cadetblue", fg='chartreuse', bd=10,
                    relief=RAISED)
        title.place(x=0, y=0, relwidth=1)

        login_frame=Frame(self.root)
        login_frame.place(x=100, y=150)
        logolbl=Label(login_frame, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)
        userlbl=Label(login_frame, text='Username', image=self.user_icon, bd=0, compound=LEFT,
                      font=("times new roman", 20, "bold")).grid(row=1, column=0, padx=20, pady=10)
        txtuser=Entry(login_frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("", 15))
        txtuser.focus_set()
        txtuser=txtuser.grid(row=1, column=1, padx=20)
        passlbl=Label(login_frame, text='Password', image=self.pass_icon, bd=0, compound=LEFT,
                      font=("times new roman", 20, "bold")).grid(row=2, column=0, padx=20, pady=10)
        txtpass=Entry(login_frame, bd=5, textvariable=self.pass_, show='*', relief=GROOVE, font=("", 15)).grid(row=2,
                                                                                                               column=1,
                                                                                                               padx=20)
        btn_log=Button(login_frame, text="Login", width=15, command=self.login, font=("Adobe Gothic Std B", 15, "bold"),
                       bg="light coral", fg="misty rose").grid(row=3, column=1, pady=7)

    def login(self):
        while self.t < 3:
            if (self.uname.get() == "" or self.pass_.get() == ""):
                messagebox.showerror("Error", "All fields are required....!!!")
                break
            elif self.uname.get() == "admin" and self.pass_.get() == "user":
                self.top=Toplevel()
                self.top.focus()
                self.top.title("Login")
                self.top.geometry("200x100+600+360")
                self.success_bg=PhotoImage(file="images.png")
                success_lbl=Label(self.top, image=self.success_bg).pack()
                btn=Button(self.top, text="SUCCESSFUL....!!!", command=self.main, bg='lavender')
                btn.focus_set()
                btn.place(x=50, y=30)
                break
            else:
                self.t=self.t + 1
                if self.t == 3:
                    messagebox.showerror("Error", "Maximum Attempt...!!! Access Denied")
                    break
                messagebox.showerror("Error", "Invalid Username Or Password....!!!")
                break
        if self.t == 3:
            root.destroy()

    ########################################################################################################################
    ############################################ MAIN FRAME ################################################################
    ########################################################################################################################

    def main(self):
        self.uname.set("")
        self.pass_.set("")
        self.top.destroy()
        self.top1=Toplevel()
        self.top1.focus()
        self.top1.title("Main Frame")
        self.top1.geometry("1350x700+0+0")
        self.main_bg=PhotoImage(file="images.png")
        main_lbl=Label(self.top1, image=self.main_bg).pack()

        Main_frame=Frame(self.top1, bg="light blue")
        Main_frame.place(x=950, y=150)
        stu_btn=Button(Main_frame, text="Student Record", command=self.student, width=15,
                       font=("times new roman", 14, "bold"), bg="light coral", fg="white")
        stu_btn.focus_set()
        stu_btn=stu_btn.grid(row=0, column=0, pady=10)
        hostel_btn=Button(Main_frame, text="Hostel Record", command=self.hostel, width=15,
                          font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=1, column=0,
                                                                                                   pady=10)
        result_btn=Button(Main_frame, text="Result Record", command=self.result, width=15,
                          font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=2, column=0,
                                                                                                   pady=10)
        fees_btn=Button(Main_frame, text="Fees Record", command=self.fees, width=15,
                        font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=3, column=0,
                                                                                                 pady=10)
        exit_btn=Button(Main_frame, text="Exit", command=self.top1.destroy, width=15,
                        font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=4, column=0,
                                                                                                 pady=10)

    ########################################################################################################################
    ############################################ STUDENT TABLE #############################################################
    ########################################################################################################################

    def student(self):

        self.top2=Toplevel()
        self.top2.focus()
        self.top2.title("STUDENT Record")
        self.top2.geometry("1350x700+0+0")
        title_stu=Label(self.top2, text='STUDENT RECORD', bd=10, relief=GROOVE, font=("algerian", 40), bg="gold",
                        fg="brown")
        title_stu.pack(side=TOP, fill=X)
        self.stu_bg=PhotoImage(file="images.png")
        insert_stu_lbl=Label(self.top2, image=self.stu_bg).pack()

        btn_frame=Frame(self.top2, bd=4, relief=RIDGE)
        btn_frame.place(x=1000, y=100, width=300, height=270)
        self.btnframe=PhotoImage(file="images.png")
        btnfrm=Label(btn_frame, image=self.btnframe).pack()
        btn1_frame=Frame(btn_frame, bg='sky blue', bd=5, relief=RIDGE)
        btn1_frame.place(x=60, y=18)
        addbtn=Button(btn1_frame, text='ADD RECORD', width=20, command=self.add_student, bg="light coral",
                      fg="white").grid(row=0, column=0, padx=10, pady=10)
        updatebtn=Button(btn1_frame, text='UPDATE RECORD', width=20, command=self.update, bg="light coral",
                         fg="white").grid(row=1, column=0, pady=5)
        deletebtn=Button(btn1_frame, text='DELETE RECORD', width=20, command=self.delete, bg="light coral",
                         fg="white").grid(row=2, column=0, pady=10)
        clearbtn=Button(btn1_frame, text='CLEAR RECORD', width=20, command=self.clear, bg="light coral",
                        fg="white").grid(row=3, column=0, pady=5)
        exitbtn=Button(btn1_frame, text='Exit', command=self.top2.destroy, width=20, bg="light coral", fg="white").grid(
            row=4, column=0, pady=10)

        insert_stu_frame=Frame(self.top2, bd=4, relief=RIDGE, bg='purple')
        insert_stu_frame.place(x=50, y=100, width=915, height=270)
        lbl1=Label(insert_stu_frame, text='Roll No.', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        lbl1.grid(row=0, column=0, padx=5)
        txt1=Entry(insert_stu_frame, textvariable=self.ID_var, font=("times new roman", 15, 'bold'), bd=5,
                   relief=GROOVE)
        txt1.focus_set()
        txt1.grid(row=0, column=1, padx=10)
        lbl2=Label(insert_stu_frame, text='Name', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        lbl2.grid(row=0, column=2, padx=25)
        txt2=Entry(insert_stu_frame, textvariable=self.NAME_var, font=("times new roman", 15, 'bold'), bd=5,
                   relief=GROOVE)
        txt2.grid(row=0, column=3, padx=15)
        lbl3=Label(insert_stu_frame, text='Sex', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        lbl3.grid(row=1, column=0, padx=15, pady=4)
        combo_sex=ttk.Combobox(insert_stu_frame, textvariable=self.SEX_var, font=("times new roman", 14),
                               state='readonly')
        combo_sex['values']=("M", "F")
        combo_sex.grid(row=1, column=1)
        lbl4=Label(insert_stu_frame, text='Father`s Name', font=("times new roman", 20, 'bold'), bg='purple',
                   fg='white')
        lbl4.grid(row=1, column=2, padx=45, pady=4)
        txt4=Entry(insert_stu_frame, textvariable=self.FATHERS_NAME_var, font=("times new roman", 15, 'bold'), bd=5,
                   relief=GROOVE)
        txt4.grid(row=1, column=3, padx=5, pady=4)
        lbl5=Label(insert_stu_frame, text='Mobile_No', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        lbl5.grid(row=2, column=0, padx=5, pady=4)
        txt5=Entry(insert_stu_frame, textvariable=self.MOBILE_NO_var, font=("times new roman", 15, 'bold'), bd=5,
                   relief=GROOVE)
        txt5.grid(row=2, column=1, padx=5, pady=4)
        lbl6=Label(insert_stu_frame, text='Father`Mobile_No', font=("times new roman", 20, 'bold'), bg='purple',
                   fg='white')
        lbl6.grid(row=2, column=2, padx=5, pady=4)
        txt6=Entry(insert_stu_frame, textvariable=self.FATHERS_MOBILE_NO_var, font=("times new roman", 15, 'bold'),
                   bd=5, relief=GROOVE)
        txt6.grid(row=2, column=3, padx=5, pady=4)
        lbl7=Label(insert_stu_frame, text='Secondary', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        lbl7.grid(row=3, column=0, padx=5, pady=4)
        txt7=Entry(insert_stu_frame, textvariable=self.SECONDARY_var, font=("times new roman", 15, 'bold'), bd=5,
                   relief=GROOVE)
        txt7.grid(row=3, column=1, padx=5, pady=4)
        lbl8=Label(insert_stu_frame, text='Higher_Secondary', font=("times new roman", 20, 'bold'), bg='purple',
                   fg='white')
        lbl8.grid(row=3, column=2, padx=5, pady=4)
        txt8=Entry(insert_stu_frame, textvariable=self.HIGHER_SECONDARY_var, font=("times new roman", 15, 'bold'), bd=5,
                   relief=GROOVE)
        txt8.grid(row=3, column=3, padx=5, pady=4)
        lbl9=Label(insert_stu_frame, text='Branch', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        lbl9.grid(row=4, column=0, padx=5, pady=4)
        combo_branch=ttk.Combobox(insert_stu_frame, textvariable=self.BRANCH_var, font=("times new roman", 14),
                                  state='readonly')
        combo_branch['values']=("CSE", "CIVIL", "ME", "ECE")
        combo_branch.grid(row=4, column=1)
        lbl10=Label(insert_stu_frame, text='Academic_Year', font=("times new roman", 20, 'bold'), bg='purple',
                    fg='white')
        lbl10.grid(row=4, column=2, padx=5, pady=4)
        combo_year=ttk.Combobox(insert_stu_frame, textvariable=self.ACADEMIC_YEAR_var, font=("times new roman", 14),
                                state='readonly')
        combo_year['values']=("1")
        combo_year.grid(row=4, column=3)
        lbl11=Label(insert_stu_frame, text='State', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        lbl11.grid(row=5, column=0, padx=5, pady=4)
        txt11=Entry(insert_stu_frame, textvariable=self.STATE_var, font=("times new roman", 15, 'bold'), bd=5,
                    relief=GROOVE)
        txt11.grid(row=5, column=1, padx=5, pady=4)
        lbl12=Label(insert_stu_frame, text='Hostel', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        lbl12.grid(row=5, column=2, padx=5, pady=4)
        combo_hostel=ttk.Combobox(insert_stu_frame, textvariable=self.hostel_check, font=("times new roman", 14),
                                  state='readonly')
        combo_hostel['values']=("Yes", "No")
        combo_hostel.grid(row=5, column=3)

        dis_stu_frame=Frame(self.top2, bd=4, relief=RIDGE, bg='purple')
        dis_stu_frame.place(x=50, y=380, width=1250, height=300)
        searchlbl=Label(dis_stu_frame, text='SEARCH BY', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        searchlbl.grid(row=0, column=0, padx=10, pady=5)
        combo_search=ttk.Combobox(dis_stu_frame, textvariable=self.search_by, font=("times new roman", 14), width=10,
                                  state='readonly')
        combo_search['values']=("ID", "NAME", "BRANCH", "STATE")
        combo_search.grid(row=0, column=1, padx=10, pady=5)
        searchtxt=Entry(dis_stu_frame, textvariable=self.search_txt, font=("times new roman", 10, 'bold'), bd=5,
                        relief=GROOVE)
        searchtxt.grid(row=0, column=3, padx=10, pady=5)
        searchbtn=Button(dis_stu_frame, text='SEARCH', width=20, pady=3, command=self.search, bg="light coral",
                         fg="white").grid(row=0, column=4, padx=10, pady=5)
        showbtn=Button(dis_stu_frame, text='SHOW', width=20, pady=3, command=self.fetch_data, bg="light coral",
                       fg="white").grid(row=0, column=5, padx=10, pady=5)

        tableframe=Frame(dis_stu_frame, bd=4, relief=RIDGE, bg='purple')
        tableframe.place(x=10, y=45, width=1220, height=240)
        scrol_x=Scrollbar(tableframe, orient=HORIZONTAL)
        scrol_y=Scrollbar(tableframe, orient=VERTICAL)
        self.stutable=ttk.Treeview(tableframe, columns=(
        "ID", "NAME", "SEX", "FATHERS_NAME", "MOBILE_NO", "FATHERS_MOBILE_NO", "SECONDARY", "HIGHER SECONDARY",
        "BRANCH", "ACADEMIC_YEAR", "STATE", "HOSTEL"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_x.config(command=self.stutable.xview)
        scrol_y.config(command=self.stutable.yview)
        self.stutable.heading("ID", text="ROLL NO.")
        self.stutable.heading("NAME", text="STUDENT NAME")
        self.stutable.heading("SEX", text="SEX")
        self.stutable.heading("FATHERS_NAME", text="FATHER'S NAME")
        self.stutable.heading("MOBILE_NO", text="MOBILE NO.")
        self.stutable.heading("FATHERS_MOBILE_NO", text="FATHER'S MOBILE NO.")
        self.stutable.heading("SECONDARY", text="SECONDARY")
        self.stutable.heading("HIGHER SECONDARY", text="HIGHER SECONDARY")
        self.stutable.heading("BRANCH", text="BRANCH")
        self.stutable.heading("ACADEMIC_YEAR", text="ACADEMIC YEAR")
        self.stutable.heading("STATE", text="STATE")
        self.stutable.heading("HOSTEL", text="HOSTEL")
        self.stutable['show']='headings'
        self.stutable.column("ID", width=80)
        self.stutable.column("NAME", width=135)
        self.stutable.column("SEX", width=30)
        self.stutable.column("FATHERS_NAME", width=135)
        self.stutable.column("MOBILE_NO", width=120)
        self.stutable.column("FATHERS_MOBILE_NO", width=150)
        self.stutable.column("SECONDARY", width=110)
        self.stutable.column("HIGHER SECONDARY", width=130)
        self.stutable.column("BRANCH", width=80)
        self.stutable.column("ACADEMIC_YEAR", width=120)
        self.stutable.column("STATE", width=100)
        self.stutable.column("HOSTEL", width=30)
        self.stutable.pack(fill=BOTH, expand=1)
        self.stutable.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    ########################################################################################################################

    def add_student(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur1=con.cursor()
        cur2=con.cursor()
        cur3=con.cursor()
        try:
            cur.execute(
                "insert into main(ID,NAME,SEX,FATHERS_NAME,MOBILE_NO,FATHERS_MOBILE_NO,SECONDARY,HIGHER_SECONDARY,BRANCH,ACADEMIC_YEAR,STATE,HOSTEL) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)",
                (self.ID_var.get(),
                 self.NAME_var.get(),
                 self.SEX_var.get(),
                 self.FATHERS_NAME_var.get(),
                 self.MOBILE_NO_var.get(),
                 self.FATHERS_MOBILE_NO_var.get(),
                 self.SECONDARY_var.get(),
                 self.HIGHER_SECONDARY_var.get(),
                 self.BRANCH_var.get(),
                 self.ACADEMIC_YEAR_var.get(),
                 self.STATE_var.get(),
                 self.hostel_check.get()))
            cur1.execute("insert into fees(ID,NAME,BRANCH,ACADEMIC_YEAR) VALUES(:1,:2,:3,:4)",
                         (self.ID_var.get(),
                          self.NAME_var.get(),
                          self.BRANCH_var.get(),
                          self.ACADEMIC_YEAR_var.get()))
            cur2.execute("insert into result(ID,NAME,BRANCH,ACADEMIC_YEAR) VALUES(:1,:2,:3,:4)",
                         (self.ID_var.get(),
                          self.NAME_var.get(),
                          self.BRANCH_var.get(),
                          self.ACADEMIC_YEAR_var.get()))
            if self.hostel_check.get() == "Yes":
                cur3.execute("insert into hostel(ID,NAME,ACADEMIC_YEAR,BRANCH,STATE) VALUES(:1,:2,:3,:4,:5)",
                             (self.ID_var.get(),
                              self.NAME_var.get(),
                              self.ACADEMIC_YEAR_var.get(),
                              self.BRANCH_var.get(),
                              self.STATE_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Added", "Record Successfully Added.....!!!", parent=self.top2)
        except cx_Oracle.IntegrityError as ac:
            error1,=ac.args
            if error1.code == 1:
                messagebox.showinfo("Error", "Roll No. Already Exist...!!!", parent=self.top2)
            if error1.code == 1400:
                messagebox.showinfo("Error", "Field Can't Be Empty...!!!", parent=self.top2)
        except cx_Oracle.DatabaseError as ab:
            error,=ab.args
            if error.code == 1438:
                messagebox.showerror("Error", "Size Exceeds...!!!", parent=self.top2)
            if error.code == 2290:
                messagebox.showerror("Error", "Give Valid Secondary or Higher Secondary Grades...!!!", parent=self.top2)
            if error.code == 1722:
                messagebox.showerror("Error", "Give Valid Format of Data...!!!", parent=self.top2)

    def fetch_data(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute("select * from main")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.stutable.delete(*self.stutable.get_children())
            for row in rows:
                self.stutable.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.ID_var.set("")
        self.NAME_var.set("")
        self.SEX_var.set("")
        self.FATHERS_NAME_var.set("")
        self.MOBILE_NO_var.set("")
        self.FATHERS_MOBILE_NO_var.set("")
        self.SECONDARY_var.set("")
        self.HIGHER_SECONDARY_var.set("")
        self.BRANCH_var.set("")
        self.ACADEMIC_YEAR_var.set("")
        self.STATE_var.set("")
        self.hostel_check.set("")

    def get_cursor(self, ev):
        cursor_row=self.stutable.focus()
        content=self.stutable.item(cursor_row)
        row=content['values']
        self.ID_var.set(row[0])
        self.NAME_var.set(row[1])
        self.SEX_var.set(row[2])
        self.FATHERS_NAME_var.set(row[3])
        self.MOBILE_NO_var.set(row[4])
        self.FATHERS_MOBILE_NO_var.set(row[5])
        self.SECONDARY_var.set(row[6])
        self.HIGHER_SECONDARY_var.set(row[7])
        self.BRANCH_var.set(row[8])
        self.ACADEMIC_YEAR_var.set(row[9])
        self.STATE_var.set(row[10])
        self.hostel_check.set(row[11])

    def update(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        try:
            cur.execute(
                "update main set NAME=:1,SEX=:2,FATHERS_NAME=:3,MOBILE_NO=:4,FATHERS_MOBILE_NO=:5,SECONDARY=:6,HIGHER_SECONDARY=:7,BRANCH=:8,ACADEMIC_YEAR=:9,STATE=:10 where ID=:11",
                (self.NAME_var.get(),
                 self.SEX_var.get(),
                 self.FATHERS_NAME_var.get(),
                 self.MOBILE_NO_var.get(),
                 self.FATHERS_MOBILE_NO_var.get(),
                 self.SECONDARY_var.get(),
                 self.HIGHER_SECONDARY_var.get(),
                 self.BRANCH_var.get(),
                 self.ACADEMIC_YEAR_var.get(),
                 self.STATE_var.get(),
                 self.ID_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record Updated...!!!", parent=self.top2)
        except cx_Oracle.IntegrityError as ac:
            error1,=ac.args
            if error1.code == 1:
                messagebox.showinfo("Error", "Roll No. Already Exist...!!!", parent=self.top2)
            if error1.code == 1400:
                messagebox.showinfo("Error", "Field Can't Be Empty...!!!", parent=self.top2)

        except cx_Oracle.DatabaseError as ab:
            error,=ab.args
            if error.code == 1438:
                messagebox.showerror("Error", "Size Exceeds...!!!", parent=self.top2)
            if error.code == 2290:
                messagebox.showerror("Error", "Give Valid Secondary or Higher Secondary Grades...!!!", parent=self.top2)
            if error.code == 1722:
                messagebox.showerror("Error", "Give Valid Format of Data...!!!", parent=self.top2)

    def delete(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute("delete from main where ID=:1", {'1': self.ID_var.get()})
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success", "Record Deleted...!!!", parent=self.top2)

    def search(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute(
            "select * from main where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.stutable.delete(*self.stutable.get_children())
            for row in rows:
                self.stutable.insert('', END, values=row)
            con.commit()
        con.close()

    ########################################################################################################################
    ################################################### Hostel Table #######################################################
    ########################################################################################################################

    def hostel(self):

        self.top3=Toplevel()
        self.top3.focus()
        self.top3.title("HOSTEL RECORD")
        self.top3.geometry("1350x700+0+0")
        title_hos=Label(self.top3, text='HOSTEL RECORD', bd=10, relief=GROOVE, font=("times new roman", 40, 'bold'),
                        bg='gold', fg='brown')
        title_hos.pack(side=TOP, fill=X)
        self.hostel_bg=PhotoImage(file="images.png")
        hostel_lbl=Label(self.top3, image=self.hostel_bg).pack()
        btn2_frame=Frame(self.top3, bd=4, relief=RIDGE, bg='white')
        btn2_frame.place(x=1000, y=100, width=300, height=270)
        self.btnframe1=PhotoImage(file="images.png")
        btnfrm=Label(btn2_frame, image=self.btnframe1).pack()
        btn3_frame=Frame(btn2_frame, bg='sky blue', bd=5, relief=RIDGE)
        btn3_frame.place(x=60, y=18)
        hos_addbtn=Button(btn3_frame, text='ADD RECORD', width=20, command=self.add_hostel, bg='light coral',
                          fg='white').grid(row=0, column=0, padx=10, pady=10)
        hos_updatebtn=Button(btn3_frame, text='UPDATE RECORD', width=20, command=self.update_hostel, bg='light coral',
                             fg='white').grid(row=1, column=0, pady=5)
        hos_deletebtn=Button(btn3_frame, text='DELETE RECORD', width=20, command=self.delete_hostel, bg='light coral',
                             fg='white').grid(row=2, column=0, pady=10)
        hos_clearbtn=Button(btn3_frame, text='CLEAR RECORD', width=20, command=self.clear_hostel, bg='light coral',
                            fg='white').grid(row=3, column=0, pady=5)
        hos_exitbtn=Button(btn3_frame, text='Exit', command=self.top3.destroy, width=20, bg='light coral',
                           fg='white').grid(row=4, column=0, pady=10)

        hostel_frame=Frame(self.top3, bd=4, relief=RIDGE, bg='purple')
        hostel_frame.place(x=50, y=100, width=915, height=270)
        hos_lbl1=Label(hostel_frame, text='Roll No.', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        hos_lbl1.grid(row=0, column=0, padx=5, pady=20)
        hos_txt1=Entry(hostel_frame, textvariable=self.ID_var, font=("times new roman", 15, 'bold'), bd=5,
                       relief=GROOVE)
        hos_txt1.focus_set()
        hos_txt1.grid(row=0, column=1, padx=10, pady=20)
        hos_lbl2=Label(hostel_frame, text='Name', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        hos_lbl2.grid(row=0, column=2, padx=25, pady=20)
        hos_txt2=Entry(hostel_frame, textvariable=self.NAME_var, font=("times new roman", 15, 'bold'), bd=5,
                       relief=GROOVE)
        hos_txt2.grid(row=0, column=3, padx=15, pady=20)
        hos_lbl4=Label(hostel_frame, text='Room No.', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        hos_lbl4.grid(row=1, column=0, padx=45, pady=14)
        hos_txt4=Entry(hostel_frame, textvariable=self.room, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE)
        hos_txt4.grid(row=1, column=1, padx=5, pady=14)
        hos_lbl9=Label(hostel_frame, text='Branch', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        hos_lbl9.grid(row=1, column=2, padx=5, pady=14)
        hos_combo_branch=ttk.Combobox(hostel_frame, textvariable=self.BRANCH_var, font=("times new roman", 14),
                                      state='readonly')
        hos_combo_branch['values']=("CSE", "CIVIL", "ME", "ECE")
        hos_combo_branch.grid(row=1, column=3)
        hos_lbl10=Label(hostel_frame, text='Academic_Year', font=("times new roman", 20, 'bold'), bg='purple',
                        fg='white')
        hos_lbl10.grid(row=2, column=0, padx=5, pady=14)
        hos_combo_year=ttk.Combobox(hostel_frame, textvariable=self.ACADEMIC_YEAR_var, font=("times new roman", 14),
                                    state='readonly')
        hos_combo_year['values']=("1", "2", "3", "4")
        hos_combo_year.grid(row=2, column=1)
        hos_lbl11=Label(hostel_frame, text='State', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        hos_lbl11.grid(row=2, column=2, padx=5, pady=14)
        hos_txt11=Entry(hostel_frame, textvariable=self.STATE_var, font=("times new roman", 15, 'bold'), bd=5,
                        relief=GROOVE)
        hos_txt11.grid(row=2, column=3, padx=5, pady=14)
        dis_hos_frame=Frame(self.top3, bd=4, relief=RIDGE, bg='purple')
        dis_hos_frame.place(x=50, y=380, width=1250, height=300)
        hos_searchlbl=Label(dis_hos_frame, text='SEARCH BY', font=("times new roman", 20, 'bold'), bg='purple',
                            fg='white')
        hos_searchlbl.grid(row=0, column=0, padx=10, pady=5)
        hos_combo_search=ttk.Combobox(dis_hos_frame, textvariable=self.search_by, font=("times new roman", 14),
                                      width=10, state='readonly')
        hos_combo_search['values']=("ID", "NAME", "BRANCH", "STATE", "ROOM_NO")
        hos_combo_search.grid(row=0, column=1, padx=10, pady=5)
        searchtxt=Entry(dis_hos_frame, textvariable=self.search_txt, font=("times new roman", 10, 'bold'), bd=5,
                        relief=GROOVE)
        searchtxt.grid(row=0, column=3, padx=10, pady=5)
        searchbtn=Button(dis_hos_frame, text='SEARCH', width=20, pady=3, command=self.hos_search).grid(row=0, column=4,
                                                                                                       padx=10, pady=5)
        showbtn=Button(dis_hos_frame, text='SHOW', width=20, pady=3, command=self.hos_fetch_data).grid(row=0, column=5,
                                                                                                       padx=10, pady=5)
        hos_tableframe=Frame(dis_hos_frame, bd=4, relief=RIDGE, bg='purple')
        hos_tableframe.place(x=10, y=45, width=1220, height=240)
        scrol_x=Scrollbar(hos_tableframe, orient=HORIZONTAL)
        scrol_y=Scrollbar(hos_tableframe, orient=VERTICAL)

        self.hostable=ttk.Treeview(hos_tableframe,
                                   columns=("ID", "NAME", "ROOM_NO", "ACADEMIC_YEAR", "BRANCH", "STATE"),
                                   xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_x.config(command=self.hostable.xview)
        scrol_y.config(command=self.hostable.yview)
        self.hostable.heading("ID", text="ROLL NO.")
        self.hostable.heading("NAME", text="STUDENT NAME")
        self.hostable.heading("ROOM_NO", text="ROOM NO")
        self.hostable.heading("ACADEMIC_YEAR", text="ACADEMIC YEAR")
        self.hostable.heading("BRANCH", text="BRANCH")
        self.hostable.heading("STATE", text="STATE")
        self.hostable['show']='headings'
        self.hostable.column("ID", width=80)
        self.hostable.column("NAME", width=135)
        self.hostable.column("ROOM_NO", width=30)
        self.hostable.column("ACADEMIC_YEAR", width=120)
        self.hostable.column("BRANCH", width=80)
        self.hostable.column("STATE", width=100)
        self.hostable.pack(fill=BOTH, expand=1)
        self.hostable.bind("<ButtonRelease-1>", self.hos_get_cursor)
        self.hos_fetch_data()

    ########################################################################################################################
    def add_hostel(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        try:
            cur.execute("insert into hostel(ID,NAME,ROOM_NO,ACADEMIC_YEAR,BRANCH,STATE) VALUES(:1,:2,:3,:4,:5,:6)",
                        (self.ID_var.get(),
                         self.NAME_var.get(),
                         self.room.get(),
                         self.ACADEMIC_YEAR_var.get(),
                         self.BRANCH_var.get(),
                         self.STATE_var.get()))
            con.commit()
            self.hos_fetch_data()
            self.clear_hostel()
            con.close()
            messagebox.showinfo("Success", "Record Added...!!!", parent=self.top3)

        except cx_Oracle.IntegrityError as ac:
            error1,=ac.args
            if error1.code == 1:
                messagebox.showinfo("Error", "Roll No. Already Exist...!!!", parent=self.top3)
            if error1.code == 1400:
                messagebox.showinfo("Error", "Field Can't Be Empty...!!!", parent=self.top3)

        except cx_Oracle.DatabaseError as ab:
            error,=ab.args
            if error.code == 1438:
                messagebox.showerror("Error", "Size Exceeds...!!!", parent=self.top3)
            if error.code == 2290:
                messagebox.showerror("Error", "Give Valid Entry...!!!", parent=self.top3)
            if error.code == 1722:
                messagebox.showerror("Error", "Give Valid Format of Data...!!!", parent=self.top3)

    def hos_fetch_data(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute("select * from hostel")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.hostable.delete(*self.hostable.get_children())
            for row in rows:
                self.hostable.insert('', END, values=row)
            con.commit()
        con.close()

    def clear_hostel(self):
        self.ID_var.set("")
        self.NAME_var.set("")
        self.room.set("")
        self.ACADEMIC_YEAR_var.set("")
        self.BRANCH_var.set("")
        self.STATE_var.set("")

    def hos_get_cursor(self, ev):
        cursor_row=self.hostable.focus()
        content=self.hostable.item(cursor_row)
        row=content['values']
        self.ID_var.set(row[0])
        self.NAME_var.set(row[1])
        self.room.set(row[2])
        self.ACADEMIC_YEAR_var.set(row[3])
        self.BRANCH_var.set(row[4])
        self.STATE_var.set(row[5])

    def update_hostel(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        try:
            cur.execute("update hostel set NAME=:1,ROOM_NO=:2,ACADEMIC_YEAR=:3,BRANCH=:4,STATE=:5 where ID=:6",
                        (self.NAME_var.get(),
                         self.room.get(),
                         self.ACADEMIC_YEAR_var.get(),
                         self.BRANCH_var.get(),
                         self.STATE_var.get(),
                         self.ID_var.get()))
            con.commit()
            self.hos_fetch_data()
            self.clear_hostel()
            con.close()
            messagebox.showinfo("Success", "Record Updated...!!!", parent=self.top3)

        except cx_Oracle.IntegrityError as ac:
            error1,=ac.args
            if error1.code == 1:
                messagebox.showinfo("Error", "Roll No. Already Exist...!!!", parent=self.top3)
            if error1.code == 1400:
                messagebox.showinfo("Error", "Field Can't Be Empty...!!!", parent=self.top3)
        except cx_Oracle.DatabaseError as ab:
            error,=ab.args
            if error.code == 1438:
                messagebox.showerror("Error", "Size Exceeds...!!!", parent=self.top3)
            if error.code == 2290:
                messagebox.showerror("Error", "Give Valid Entry...!!!", parent=self.top3)
            if error.code == 1722:
                messagebox.showerror("Error", "Give Valid Format of Data...!!!", parent=self.top3)

    def delete_hostel(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute("delete from hostel where ID=:1", {'1': self.ID_var.get()})
        con.commit()
        con.close()
        self.hos_fetch_data()
        self.clear_hostel()
        messagebox.showinfo("Success", "Record Deleted...!!!", parent=self.top3)

    def hos_search(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()

        cur.execute(
            "select * from hostel where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.hostable.delete(*self.hostable.get_children())
            for row in rows:
                self.hostable.insert('', END, values=row)
            con.commit()
        con.close()

    ########################################################################################################################
    ################################################## Result Table ########################################################
    ########################################################################################################################

    def result(self):

        self.top4=Toplevel()
        self.top4.focus()
        self.top4.title("RESULT Record")
        self.top4.geometry("1350x700+0+0")
        title_result=Label(self.top4, text='RESULT RECORD', bd=10, relief=GROOVE, font=("times new roman", 40, 'bold'),
                           bg='gold', fg='brown')
        title_result.pack(side=TOP, fill=X)
        self.result_bg=PhotoImage(file="images.png")
        insert_result_lbl=Label(self.top4, image=self.result_bg).pack()

        btn4_frame=Frame(self.top4, bd=4, relief=RIDGE, bg='white')
        btn4_frame.place(x=1000, y=100, width=300, height=270)
        self.btnframe2=PhotoImage(file="images.png")
        btnfrm=Label(btn4_frame, image=self.btnframe2).pack()
        btn5_frame=Frame(btn4_frame, bg='white', bd=5, relief=RIDGE)
        btn5_frame.place(x=60, y=18)
        result_addbtn=Button(btn5_frame, text='ADD RECORD', width=20, command=self.add_result, bg='light coral',
                             fg='white').grid(row=0, column=0, padx=10, pady=10)
        result_updatebtn=Button(btn5_frame, text='UPDATE RECORD', width=20, command=self.update_result,
                                bg='light coral', fg='white').grid(row=1, column=0, pady=5)
        result_deletebtn=Button(btn5_frame, text='DELETE RECORD', width=20, command=self.delete_result,
                                bg='light coral', fg='white').grid(row=2, column=0, pady=10)
        result_clearbtn=Button(btn5_frame, text='CLEAR RECORD', width=20, command=self.clear_result, bg='light coral',
                               fg='white').grid(row=3, column=0, pady=5)
        result_exitbtn=Button(btn5_frame, text='Exit', command=self.top4.destroy, width=20, bg='light coral',
                              fg='white').grid(row=4, column=0, pady=10)

        insert_result_frame=Frame(self.top4, bd=4, relief=RIDGE, bg='purple')
        insert_result_frame.place(x=50, y=100, width=915, height=270)
        result_lbl1=Label(insert_result_frame, text='Roll No.', font=("times new roman", 20, 'bold'), bg='purple',
                          fg='white')
        result_lbl1.grid(row=0, column=0, padx=5)
        result_txt1=Entry(insert_result_frame, textvariable=self.ID_var, font=("times new roman", 15, 'bold'), bd=5,
                          relief=GROOVE)
        result_txt1.focus_set()
        result_txt1.grid(row=0, column=1, padx=10)
        result_lbl2=Label(insert_result_frame, text='Name', font=("times new roman", 20, 'bold'), bg='purple',
                          fg='white')
        result_lbl2.grid(row=0, column=2, padx=25)
        result_txt2=Entry(insert_result_frame, textvariable=self.NAME_var, font=("times new roman", 15, 'bold'), bd=5,
                          relief=GROOVE)
        result_txt2.grid(row=0, column=3, padx=15)
        result_lbl9=Label(insert_result_frame, text='Branch', font=("times new roman", 20, 'bold'), bg='purple',
                          fg='white')
        result_lbl9.grid(row=1, column=0, padx=5, pady=4)
        result_combo_branch=ttk.Combobox(insert_result_frame, textvariable=self.BRANCH_var,
                                         font=("times new roman", 14), state='readonly')
        result_combo_branch['values']=("CSE", "CIVIL", "ME", "ECE")
        result_combo_branch.grid(row=1, column=1)
        result_lbl10=Label(insert_result_frame, text='Academic_Year', font=("times new roman", 20, 'bold'), bg='purple',
                           fg='white')
        result_lbl10.grid(row=1, column=2, padx=2, pady=4)
        result_combo_year=ttk.Combobox(insert_result_frame, textvariable=self.ACADEMIC_YEAR_var,
                                       font=("times new roman", 14), state='readonly')
        result_combo_year['values']=("1", "2", "3", "4")
        result_combo_year.grid(row=1, column=3)
        result_lbl4=Label(insert_result_frame, text='First_Sem', font=("times new roman", 20, 'bold'), bg='purple',
                          fg='white')
        result_lbl4.grid(row=2, column=0, padx=5, pady=4)
        result_txt4=Entry(insert_result_frame, textvariable=self.First_Sem, font=("times new roman", 15, 'bold'), bd=5,
                          relief=GROOVE)
        result_txt4.grid(row=2, column=1, padx=5, pady=4)
        result_lbl5=Label(insert_result_frame, text='Second_Sem', font=("times new roman", 20, 'bold'), bg='purple',
                          fg='white')
        result_lbl5.grid(row=2, column=2, padx=45, pady=4)
        result_txt5=Entry(insert_result_frame, textvariable=self.Second_Sem, font=("times new roman", 15, 'bold'), bd=5,
                          relief=GROOVE)
        result_txt5.grid(row=2, column=3, padx=5, pady=4)
        result_lbl6=Label(insert_result_frame, text='Third_Sem', font=("times new roman", 20, 'bold'), bg='purple',
                          fg='white')
        result_lbl6.grid(row=3, column=0, padx=5, pady=4)
        result_txt6=Entry(insert_result_frame, textvariable=self.Third_Sem, font=("times new roman", 15, 'bold'), bd=5,
                          relief=GROOVE)
        result_txt6.grid(row=3, column=1, padx=5, pady=4)
        result_lbl7=Label(insert_result_frame, text='Fourth_Sem', font=("times new roman", 20, 'bold'), bg='purple',
                          fg='white')
        result_lbl7.grid(row=3, column=2, padx=45, pady=4)
        result_txt7=Entry(insert_result_frame, textvariable=self.Fourth_Sem, font=("times new roman", 15, 'bold'), bd=5,
                          relief=GROOVE)
        result_txt7.grid(row=3, column=3, padx=5, pady=4)
        result_lbl8=Label(insert_result_frame, text='Fivth_Sem', font=("times new roman", 20, 'bold'), bg='purple',
                          fg='white')
        result_lbl8.grid(row=4, column=0, padx=5, pady=4)
        result_txt8=Entry(insert_result_frame, textvariable=self.Fivth_Sem, font=("times new roman", 15, 'bold'), bd=5,
                          relief=GROOVE)
        result_txt8.grid(row=4, column=1, padx=5, pady=4)
        result_lbl11=Label(insert_result_frame, text='Sixth_Sem', font=("times new roman", 20, 'bold'), bg='purple',
                           fg='white')
        result_lbl11.grid(row=4, column=2, padx=45, pady=4)
        result_txt11=Entry(insert_result_frame, textvariable=self.Sixth_Sem, font=("times new roman", 15, 'bold'), bd=5,
                           relief=GROOVE)
        result_txt11.grid(row=4, column=3, padx=5, pady=4)
        result_lbl12=Label(insert_result_frame, text='Seventh_Sem', font=("times new roman", 20, 'bold'), bg='purple',
                           fg='white')
        result_lbl12.grid(row=5, column=0, padx=5, pady=4)
        result_txt12=Entry(insert_result_frame, textvariable=self.Seventh_Sem, font=("times new roman", 15, 'bold'),
                           bd=5, relief=GROOVE)
        result_txt12.grid(row=5, column=1, padx=5, pady=4)
        result_lbl13=Label(insert_result_frame, text='Eighth_Sem', font=("times new roman", 20, 'bold'), bg='purple',
                           fg='white')
        result_lbl13.grid(row=5, column=2, padx=45, pady=4)
        result_txt13=Entry(insert_result_frame, textvariable=self.Eighth_Sem, font=("times new roman", 15, 'bold'),
                           bd=5, relief=GROOVE)
        result_txt13.grid(row=5, column=3, padx=5, pady=4)

        dis_result_frame=Frame(self.top4, bd=4, relief=RIDGE, bg='purple')
        dis_result_frame.place(x=50, y=380, width=1250, height=300)
        result_searchlbl=Label(dis_result_frame, text='SEARCH BY', font=("times new roman", 20, 'bold'), bg='purple',
                               fg='white')
        result_searchlbl.grid(row=0, column=0, padx=10, pady=5)
        result_combo_search=ttk.Combobox(dis_result_frame, textvariable=self.search_by, font=("times new roman", 14),
                                         width=10, state='readonly')
        result_combo_search['values']=("ID", "NAME", "BRANCH", "ACADEMIC_YEAR")
        result_combo_search.grid(row=0, column=1, padx=10, pady=5)

        result_searchtxt=Entry(dis_result_frame, textvariable=self.search_txt, font=("times new roman", 10, 'bold'),
                               bd=5, relief=GROOVE)
        result_searchtxt.grid(row=0, column=3, padx=10, pady=5)
        result_searchbtn=Button(dis_result_frame, text='SEARCH', width=20, pady=3, command=self.search_result).grid(
            row=0, column=4, padx=10, pady=5)
        result_showbtn=Button(dis_result_frame, text='SHOW', width=20, pady=3, command=self.result_fetch_data).grid(
            row=0, column=5, padx=10, pady=5)
        tableframe_result=Frame(dis_result_frame, bd=4, relief=RIDGE, bg='purple')
        tableframe_result.place(x=10, y=45, width=1220, height=240)

        scrol_x=Scrollbar(tableframe_result, orient=HORIZONTAL)
        scrol_y=Scrollbar(tableframe_result, orient=VERTICAL)
        self.resulttable=ttk.Treeview(tableframe_result, columns=(
        "ID", "NAME", "BRANCH", "ACADEMIC_YEAR", "FIRST_SEM", "SECOND_SEM", "THIRD_SEM", "FOURTH_SEM", "FIVTH_SEM",
        "SIXTH_SEM", "SEVENTH_SEM", "EIGHTH_SEM"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_x.config(command=self.resulttable.xview)
        scrol_y.config(command=self.resulttable.yview)
        self.resulttable.heading("ID", text="ROLL NO.")
        self.resulttable.heading("NAME", text="STUDENT NAME")
        self.resulttable.heading("BRANCH", text="BRANCH")
        self.resulttable.heading("ACADEMIC_YEAR", text="ACADEMIC YEAR")
        self.resulttable.heading("FIRST_SEM", text=" FIRST SEM")
        self.resulttable.heading("SECOND_SEM", text=" SECOND SEM")
        self.resulttable.heading("THIRD_SEM", text="THIRD SEM")
        self.resulttable.heading("FOURTH_SEM", text="FOURTH SEM")
        self.resulttable.heading("FIVTH_SEM", text="FIVTH SEM")
        self.resulttable.heading("SIXTH_SEM", text="SIXTH SEM")
        self.resulttable.heading("SEVENTH_SEM", text="SEVENTH SEM")
        self.resulttable.heading("EIGHTH_SEM", text="EIGHT SEM")
        self.resulttable['show']='headings'
        self.resulttable.column("ID", width=80)
        self.resulttable.column("NAME", width=135)
        self.resulttable.column("THIRD_SEM", width=100)
        self.resulttable.column("FOURTH_SEM", width=100)
        self.resulttable.column("FIVTH_SEM", width=100)
        self.resulttable.column("SIXTH_SEM", width=100)
        self.resulttable.column("SEVENTH_SEM", width=100)
        self.resulttable.column("EIGHTH_SEM", width=100)
        self.resulttable.pack(fill=BOTH, expand=1)
        self.resulttable.column("BRANCH", width=80)
        self.resulttable.column("ACADEMIC_YEAR", width=120)
        self.resulttable.column("FIRST_SEM", width=100)
        self.resulttable.column("SECOND_SEM", width=100)
        self.resulttable.bind("<ButtonRelease-1>", self.get_cursor_result)
        self.result_fetch_data()

    ########################################################################################################################

    def add_result(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        try:
            cur.execute(
                "insert into result(ID,NAME,BRANCH,ACADEMIC_YEAR,FIRST_SEM,SECOND_SEM,THIRD_SEM,FOURTH_SEM,FIVTH_SEM,SIXTH_SEM,SEVENTH_SEM,EIGHTH_SEM) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)",
                (self.ID_var.get(),
                 self.NAME_var.get(),
                 self.BRANCH_var.get(),
                 self.ACADEMIC_YEAR_var.get(),
                 self.First_Sem.get(),
                 self.Second_Sem.get(),
                 self.Third_Sem.get(),
                 self.Fourth_Sem.get(),
                 self.Fivth_Sem.get(),
                 self.Sixth_Sem.get(),
                 self.Seventh_Sem.get(),
                 self.Eighth_Sem.get()))
            con.commit()
            self.result_fetch_data()
            self.clear_result()
            con.close()
            messagebox.showinfo("Success", "Record Added...!!!", parent=self.top4)

        except cx_Oracle.IntegrityError as ac:
            error1,=ac.args
            if error1.code == 1:
                messagebox.showinfo("Error", "Roll No. Already Exist...!!!", parent=self.top3)
            if error1.code == 1400:
                messagebox.showinfo("Error", "Field Can't Be Empty...!!!", parent=self.top3)
        except cx_Oracle.DatabaseError as ab:
            error,=ab.args
            if error.code == 1438:
                messagebox.showerror("Error", "Size Exceeds...!!!", parent=self.top3)
            if error.code == 2290:
                messagebox.showerror("Error", "Give Valid Entry...!!!", parent=self.top3)
            if error.code == 1722:
                messagebox.showerror("Error", "Give Valid Format of Data...!!!", parent=self.top3)

    def result_fetch_data(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute(
            "select ID, NAME, BRANCH, ACADEMIC_YEAR,nvl(FIRST_SEM,'0'),nvl(SECOND_SEM,'0'), nvl(THIRD_SEM,'0'), nvl(FOURTH_SEM,'0'), nvl(FIVTH_SEM,'0'), nvl(SIXTH_SEM,'0'), nvl(SEVENTH_SEM,'0'), nvl(EIGHTH_SEM,'0') from result")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.resulttable.delete(*self.resulttable.get_children())
            for row in rows:
                self.resulttable.insert('', END, values=row)
            con.commit()
        con.close()

    def clear_result(self):
        self.ID_var.set("")
        self.NAME_var.set("")
        self.BRANCH_var.set("")
        self.ACADEMIC_YEAR_var.set("")
        self.First_Sem.set("")
        self.Second_Sem.set("")
        self.Third_Sem.set("")
        self.Fourth_Sem.set("")
        self.Fivth_Sem.set("")
        self.Sixth_Sem.set("")
        self.Seventh_Sem.set("")
        self.Eighth_Sem.set("")

    def get_cursor_result(self, ev):
        cursor_row=self.resulttable.focus()
        content=self.resulttable.item(cursor_row)
        row=content['values']
        self.ID_var.set(row[0])
        self.NAME_var.set(row[1])
        self.BRANCH_var.set(row[2])
        self.ACADEMIC_YEAR_var.set(row[3])
        self.First_Sem.set(row[4])
        self.Second_Sem.set(row[5])
        self.Third_Sem.set(row[6])
        self.Fourth_Sem.set(row[7])
        self.Fivth_Sem.set(row[8])
        self.Sixth_Sem.set(row[9])
        self.Seventh_Sem.set(row[10])
        self.Eighth_Sem.set(row[11])

    def update_result(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        try:
            cur.execute(
                "update result set NAME=:1,BRANCH=:2,ACADEMIC_YEAR=:3, FIRST_SEM=:4,SECOND_SEM=:5,THIRD_SEM=:6,FOURTH_SEM=:7,FIVTH_SEM=:8,SIXTH_SEM=:9, SEVENTH_SEM=:10,EIGHTH_SEM=:11 where ID=:12",
                (self.NAME_var.get(),
                 self.BRANCH_var.get(),
                 self.ACADEMIC_YEAR_var.get(),
                 self.First_Sem.get(),
                 self.Second_Sem.get(),
                 self.Third_Sem.get(),
                 self.Fourth_Sem.get(),
                 self.Fivth_Sem.get(),
                 self.Sixth_Sem.get(),
                 self.Seventh_Sem.get(),
                 self.Eighth_Sem.get(),
                 self.ID_var.get()))
            con.commit()
            self.result_fetch_data()
            self.clear_result()
            con.close()
            messagebox.showinfo("Success", "Record Updated...!!!", parent=self.top4)

        except cx_Oracle.IntegrityError as ac:
            error1,=ac.args
            if error1.code == 1:
                messagebox.showinfo("Error", "Roll No. Already Exist...!!!", parent=self.top4)
            if error1.code == 1400:
                messagebox.showinfo("Error", "Field Can't Be Empty...!!!", parent=self.top4)

        except cx_Oracle.DatabaseError as ab:
            error,=ab.args
            if error.code == 1438:
                messagebox.showerror("Error", "Size Exceeds...!!!", parent=self.top4)
            if error.code == 2290:
                messagebox.showerror("Error", "Give Valid Entry...!!!", parent=self.top4)
            if error.code == 1722:
                messagebox.showerror("Error", "Give Valid Format of Data...!!!", parent=self.top4)

    def delete_result(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute("delete from result where ID=:1", {'1': self.ID_var.get()})
        con.commit()
        con.close()
        self.result_fetch_data()
        self.clear_result()
        messagebox.showinfo("Succcess1", "Record Deleted...!!!", parent=self.top4)

    def search_result(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute(
            "select * from result where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.resulttable.delete(*self.resulttable.get_children())
            for row in rows:
                self.resulttable.insert('', END, values=row)
            con.commit()
        con.close()

    ########################################################################################################################
    ############################################ FEES TABLE ################################################################
    ########################################################################################################################

    def fees(self):

        self.top5=Toplevel()
        self.top5.focus()
        self.top5.title("FEES Record")
        self.top5.geometry("1350x700+0+0")
        title_fees=Label(self.top5, text='FEES RECORD', bd=10, relief=GROOVE, font=("times new roman", 40, 'bold'),
                         bg='yellow', fg='red')
        title_fees.pack(side=TOP, fill=X)
        self.fees_bg=PhotoImage(file="images.png")
        insert_fees_lbl=Label(self.top5, image=self.fees_bg).pack()

        btn6_frame=Frame(self.top5, bd=4, relief=RIDGE, bg='white')
        btn6_frame.place(x=1000, y=100, width=300, height=270)
        self.btnframe3=PhotoImage(file="images.png")
        btnfrm=Label(btn6_frame, image=self.btnframe3).pack()
        btn7_frame=Frame(btn6_frame, bg='sky blue', bd=5, relief=RIDGE)
        btn7_frame.place(x=60, y=18)
        fees_addbtn=Button(btn7_frame, text='ADD RECORD', width=20, command=self.add_fees, bg='light coral',
                           fg='white').grid(row=0, column=0, padx=10, pady=10)
        fees_updatebtn=Button(btn7_frame, text='UPDATE RECORD', width=20, command=self.update_fees, bg='light coral',
                              fg='white').grid(row=1, column=0, pady=5)
        fees_deletebtn=Button(btn7_frame, text='DELETE RECORD', width=20, command=self.delete_fees, bg='light coral',
                              fg='white').grid(row=2, column=0, pady=10)
        fees_clearbtn=Button(btn7_frame, text='CLEAR RECORD', width=20, command=self.clear_fees, bg='light coral',
                             fg='white').grid(row=3, column=0, pady=5)
        fees_exitbtn=Button(btn7_frame, text='Exit', command=self.top5.destroy, width=20, bg='light coral',
                            fg='white').grid(row=4, column=0, pady=10)

        insert_fees_frame=Frame(self.top5, bd=4, relief=RIDGE, bg='purple')
        insert_fees_frame.place(x=50, y=100, width=915, height=270)
        fees_lbl1=Label(insert_fees_frame, text='Roll No.', font=("times new roman", 20, 'bold'), bg='purple',
                        fg='white')
        fees_lbl1.grid(row=0, column=0, padx=5, pady=10)
        fees_txt1=Entry(insert_fees_frame, textvariable=self.ID_var, font=("times new roman", 15, 'bold'), bd=5,
                        relief=GROOVE)
        fees_txt1.focus_set()
        fees_txt1.grid(row=0, column=1, padx=10, pady=10)
        fees_lbl2=Label(insert_fees_frame, text='Name', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        fees_lbl2.grid(row=0, column=2, padx=25, pady=10)
        fees_txt2=Entry(insert_fees_frame, textvariable=self.NAME_var, font=("times new roman", 15, 'bold'), bd=5,
                        relief=GROOVE)
        fees_txt2.grid(row=0, column=3, padx=15, pady=10)
        fees_lbl9=Label(insert_fees_frame, text='Branch', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        fees_lbl9.grid(row=1, column=0, padx=5, pady=10)
        fees_combo_branch=ttk.Combobox(insert_fees_frame, textvariable=self.BRANCH_var, font=("times new roman", 14),
                                       state='readonly')
        fees_combo_branch['values']=("CSE", "CIVIL", "ME", "ECE")
        fees_combo_branch.grid(row=1, column=1, padx=5, pady=10)
        fees_lbl10=Label(insert_fees_frame, text='Academic_Year', font=("times new roman", 20, 'bold'), bg='purple',
                         fg='white')
        fees_lbl10.grid(row=1, column=2, padx=5, pady=10)
        fees_combo_year=ttk.Combobox(insert_fees_frame, textvariable=self.ACADEMIC_YEAR_var,
                                     font=("times new roman", 14), state='readonly')
        fees_combo_year['values']=("1", "2", "3", "4")
        fees_combo_year.grid(row=1, column=3, padx=5, pady=10)
        fees_lbl4=Label(insert_fees_frame, text='Receipt No.', font=("times new roman", 20, 'bold'), bg='purple',
                        fg='white')
        fees_lbl4.grid(row=2, column=0, padx=5, pady=10)
        fees_txt4=Entry(insert_fees_frame, state='readonly', textvariable=self.receipt_no,
                        font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE)
        fees_txt4.grid(row=2, column=1, padx=5, pady=10)
        fees_lbl5=Label(insert_fees_frame, text='Tuition_Fees', font=("times new roman", 20, 'bold'), bg='purple',
                        fg='white')

        fees_lbl5.grid(row=2, column=2, padx=45, pady=10)
        tuition_fee=Entry(insert_fees_frame, textvariable=self.tuition_fees, font=("times new roman", 15, 'bold'),
                          state='readonly')
        tuition_fee.grid(row=2, column=3, padx=5, pady=10)
        fees_lbl6=Label(insert_fees_frame, text='Hostel_Fees', font=("times new roman", 20, 'bold'), bg='purple',
                        fg='white')
        fees_lbl6.grid(row=3, column=0, padx=5, pady=10)
        fees_txt6=Entry(insert_fees_frame, textvariable=self.hostel_fees, font=("times new roman", 15, 'bold'), bd=5,
                        relief=GROOVE, state='readonly')
        fees_txt6.grid(row=3, column=1, padx=5, pady=10)
        fees_lbl7=Label(insert_fees_frame, text='Status', font=("times new roman", 20, 'bold'), bg='purple', fg='white')
        fees_lbl7.grid(row=3, column=2, padx=45, pady=10)
        fees_combo_status=ttk.Combobox(insert_fees_frame, textvariable=self.status, font=("times new roman", 14),
                                       state='readonly')
        fees_combo_status['values']=("Paid", "Unpaid")
        fees_combo_status.grid(row=3, column=3, padx=5, pady=10)

        dis_fees_frame=Frame(self.top5, bd=4, relief=RIDGE, bg='purple')
        dis_fees_frame.place(x=50, y=380, width=1250, height=300)
        fees_searchlbl=Label(dis_fees_frame, text='SEARCH BY', font=("times new roman", 20, 'bold'), bg='purple',
                             fg='white')
        fees_searchlbl.grid(row=0, column=0, padx=10, pady=5)
        fees_combo_search=ttk.Combobox(dis_fees_frame, textvariable=self.search_by, font=("times new roman", 14),
                                       width=10, state='readonly')
        fees_combo_search['values']=("ID", "NAME", "RECEIPT_NO", "BRANCH", "ACADEMIC_YEAR", "STATUS")
        fees_combo_search.grid(row=0, column=1, padx=10, pady=5)
        fees_searchtxt=Entry(dis_fees_frame, textvariable=self.search_txt, font=("times new roman", 10, 'bold'), bd=5,
                             relief=GROOVE)
        fees_searchtxt.grid(row=0, column=3, padx=10, pady=5)
        fees_searchbtn=Button(dis_fees_frame, text='SEARCH', width=20, pady=3, command=self.search_fees).grid(row=0,
                                                                                                              column=4,
                                                                                                              padx=10,
                                                                                                              pady=5)
        fees_showbtn=Button(dis_fees_frame, text='SHOW', width=20, pady=3, command=self.fees_fetch_data).grid(row=0,
                                                                                                              column=5,
                                                                                                              padx=10,
                                                                                                              pady=5)

        tableframe_fees=Frame(dis_fees_frame, bd=4, relief=RIDGE, bg='purple')
        tableframe_fees.place(x=10, y=45, width=1220, height=240)
        scrol_x=Scrollbar(tableframe_fees, orient=HORIZONTAL)
        scrol_y=Scrollbar(tableframe_fees, orient=VERTICAL)
        self.feestable=ttk.Treeview(tableframe_fees, columns=(
        "ID", "NAME", "BRANCH", "ACADEMIC_YEAR", "RECIEPT_NO", "TUITION_FEE", "HOSTEL_FEE", "STATUS"),
                                    xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_x.config(command=self.feestable.xview)
        scrol_y.config(command=self.feestable.yview)
        self.feestable.heading("ID", text="ROLL NO.")
        self.feestable.heading("NAME", text="STUDENT NAME")
        self.feestable.heading("BRANCH", text="BRANCH")
        self.feestable.heading("ACADEMIC_YEAR", text="ACADEMIC YEAR")
        self.feestable.heading("RECIEPT_NO", text=" RECIEPT NO ")
        self.feestable.heading("TUITION_FEE", text="TUITION FEES")
        self.feestable.heading("HOSTEL_FEE", text=" HOSTEL FEES")
        self.feestable.heading("STATUS", text="STATUS")
        self.feestable['show']='headings'
        self.feestable.column("ID", width=80)
        self.feestable.column("NAME", width=135)
        self.feestable.column("BRANCH", width=80)
        self.feestable.column("ACADEMIC_YEAR", width=120)
        self.feestable.column("RECIEPT_NO", width=100)
        self.feestable.column("TUITION_FEE", width=100)
        self.feestable.column("HOSTEL_FEE", width=100)
        self.feestable.column("STATUS", width=100)
        self.feestable.pack(fill=BOTH, expand=1)
        self.feestable.bind("<ButtonRelease-1>", self.get_cursor_fees)
        self.fees_fetch_data()

    def add_fees(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur1=con.cursor()
        cur2=con.cursor()
        try:
            cur1.execute("select max(receipt) from rec")
            self.receipt_max=cur1.fetchall()
            self.check=list()
            for i in self.receipt_max:
                self.check.append(i[0])
            self.a=self.check[0]
            if self.ACADEMIC_YEAR_var.get() == '1':
                self.tuition_fees.set("95000")
            elif self.ACADEMIC_YEAR_var.get() == '2':
                self.tuition_fees.set("105000")
            elif self.ACADEMIC_YEAR_var.get() == '3':
                self.tuition_fees.set("115000")
            elif self.ACADEMIC_YEAR_var.get() == '4':
                self.tuition_fees.set("125000")

            cur2.execute("select id,hostel from main")
            self.hostel_status=cur2.fetchall()
            for i in self.hostel_status:
                if self.ID_var.get() == i[0]:
                    if i[1] == 'Yes':
                        if self.ACADEMIC_YEAR_var.get() == '1':
                            self.hostel_fees.set("60000")
                        elif self.ACADEMIC_YEAR_var.get() == '2':
                            self.hostel_fees.set("62000")
                        elif self.ACADEMIC_YEAR_var.get() == '3':
                            self.hostel_fees.set("64000")
                        elif self.ACADEMIC_YEAR_var.get() == '4':
                            self.hostel_fees.set("64000")
                    else:
                        if self.ACADEMIC_YEAR_var.get() == '1':
                            self.hostel_fees.set("")
                        elif self.ACADEMIC_YEAR_var.get() == '2':
                            self.hostel_fees.set("")
                        elif self.ACADEMIC_YEAR_var.get() == '3':
                            self.hostel_fees.set("")
                        elif self.ACADEMIC_YEAR_var.get() == '4':
                            self.hostel_fees.set("")

            if self.status.get() == "Paid":
                self.a=self.a + 1
                cur.execute(
                    "insert into fees(ID,NAME,BRANCH,ACADEMIC_YEAR,ISNULL(RECEIPT_NO,''),TUITION_FEE,HOSTEL_FEE,STATUS) VALUES(:1,:2,:3,:4,:5,:6,:7,:8)",
                    (self.ID_var.get(),
                     self.NAME_var.get(),
                     self.BRANCH_var.get(),
                     self.ACADEMIC_YEAR_var.get(),
                     "AGC" + str(self.a),
                     self.tuition_fees.get(),
                     self.hostel_fees.get(),
                     self.status.get()))

                cur1.execute("update rec set receipt=" + str(self.a))
            else:
                cur.execute(
                    "insert into fees(ID,NAME,BRANCH,ACADEMIC_YEAR,TUITION_FEE,HOSTEL_FEE,STATUS) VALUES(:1,:2,:3,:4,:5,:6,:7)",
                    (self.ID_var.get(),
                     self.NAME_var.get(),
                     self.BRANCH_var.get(),
                     self.ACADEMIC_YEAR_var.get(),
                     self.tuition_fees.get(),
                     self.hostel_fees.get(),
                     self.status.get()))

            con.commit()
            self.fees_fetch_data()
            self.clear_fees()
            con.close()
            messagebox.showinfo("Success", "Record Added...!!!", parent=self.top5)

        except cx_Oracle.IntegrityError as ac:
            error1,=ac.args
            if error1.code == 1:
                messagebox.showinfo("Error", "Roll No. Already Exist...!!!", parent=self.top5)
            if error1.code == 1400:
                messagebox.showinfo("Error", "Field Can't Be Empty...!!!", parent=self.top5)

        except cx_Oracle.DatabaseError as ab:
            error,=ab.args
            if error.code == 1438:
                messagebox.showerror("Error", "Size Exceeds...!!!", parent=self.top5)
            if error.code == 2290:
                messagebox.showerror("Error", "Give Valid Entry...!!!", parent=self.top5)
            if error.code == 1722:
                messagebox.showerror("Error", "Give Valid Format of Data...!!!", parent=self.top5)

    def fees_fetch_data(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute(
            "select ID,NAME,BRANCH,ACADEMIC_YEAR,nvl(RECEIPT_NO,'0'),nvl(TUITION_FEE,'0'),nvl(HOSTEL_FEE,'0'),STATUS from fees ")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.feestable.delete(*self.feestable.get_children())
            for row in rows:
                self.feestable.insert('', END, values=row)
            con.commit()
        con.close()

    def clear_fees(self):
        self.ID_var.set("")
        self.NAME_var.set("")
        self.BRANCH_var.set("")
        self.ACADEMIC_YEAR_var.set("")
        self.receipt_no.set("")
        self.tuition_fees.set("")
        self.hostel_fees.set("")
        self.status.set("")

    def get_cursor_fees(self, ev):
        cursor_row=self.feestable.focus()
        content=self.feestable.item(cursor_row)
        row=content['values']
        self.ID_var.set(row[0])
        self.NAME_var.set(row[1])
        self.BRANCH_var.set(row[2])
        self.ACADEMIC_YEAR_var.set(row[3])
        self.receipt_no.set(row[4])
        self.tuition_fees.set(row[5])
        self.hostel_fees.set(row[6])
        self.status.set(row[7])

    def update_fees(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur1=con.cursor()
        cur2=con.cursor()
        try:
            cur1.execute("select max(receipt) from rec")
            self.receipt_max=cur1.fetchall()
            self.check=list()
            for i in self.receipt_max:
                self.check.append(i[0])
            self.a=self.check[0]
            if self.ACADEMIC_YEAR_var.get() == '1':
                self.tuition_fees.set("95000")
            elif self.ACADEMIC_YEAR_var.get() == '2':
                self.tuition_fees.set("105000")
            elif self.ACADEMIC_YEAR_var.get() == '3':
                self.tuition_fees.set("115000")
            elif self.ACADEMIC_YEAR_var.get() == '4':
                self.tuition_fees.set("12000")

            cur2.execute("select id,hostel from main")
            self.hostel_status=cur2.fetchall()
            for i in self.hostel_status:
                if str(i[0]) == str(self.ID_var.get()):
                    if str(i[1]) == 'Yes':
                        if self.ACADEMIC_YEAR_var.get() == '1':
                            self.hostel_fees.set("60000")
                        elif self.ACADEMIC_YEAR_var.get() == '2':
                            self.hostel_fees.set("62000")
                        elif self.ACADEMIC_YEAR_var.get() == '3':
                            self.hostel_fees.set("64000")
                        elif self.ACADEMIC_YEAR_var.get() == '4':
                            self.hostel_fees.set("64000")
                    if str(i[1]) == 'No':
                        if self.ACADEMIC_YEAR_var.get() == '1':
                            self.hostel_fees.set("0")
                        elif self.ACADEMIC_YEAR_var.get() == '2':
                            self.hostel_fees.set("0")
                        elif self.ACADEMIC_YEAR_var.get() == '3':
                            self.hostel_fees.set("0")
                        elif self.ACADEMIC_YEAR_var.get() == '4':
                            self.hostel_fees.set("0")

            if self.status.get() == "Paid":
                self.a=self.a + 1
                cur.execute(
                    "update fees set NAME=:1,BRANCH=:2,ACADEMIC_YEAR=:3,RECEIPT_NO=:4,TUITION_FEE=:5,HOSTEL_FEE=:6,STATUS=:7 where ID=:8",
                    (self.NAME_var.get(),
                     self.BRANCH_var.get(),
                     self.ACADEMIC_YEAR_var.get(),
                     "AGC" + str(self.a),
                     self.tuition_fees.get(),
                     self.hostel_fees.get(),
                     self.status.get(),
                     self.ID_var.get()))
                cur1.execute("update rec set receipt=" + str(self.a))
            else:
                cur.execute(
                    "update fees set NAME=:1,BRANCH=:2,ACADEMIC_YEAR=:3,TUITION_FEE=:4,HOSTEL_FEE=:5,STATUS=:6 where ID=:7",
                    (self.NAME_var.get(),
                     self.BRANCH_var.get(),
                     self.ACADEMIC_YEAR_var.get(),
                     self.tuition_fees.get(),
                     self.hostel_fees.get(),
                     self.status.get(),
                     self.ID_var.get()))

            con.commit()
            self.fees_fetch_data()
            self.clear_fees()
            con.close()
            messagebox.showinfo("Success", "Record Updated...!!!", parent=self.top5)

        except cx_Oracle.IntegrityError as ac:
            error1,=ac.args
            if error1.code == 1:
                messagebox.showinfo("Error", "Roll No. Already Exist...!!!", parent=self.top5)
            if error1.code == 1400:
                messagebox.showinfo("Error", "Field Can't Be Empty...!!!", parent=self.top5)

        except cx_Oracle.DatabaseError as ab:
            error,=ab.args
            if error.code == 1438:
                messagebox.showerror("Error", "Size Exceeds...!!!", parent=self.top5)
            if error.code == 2290:
                messagebox.showerror("Error", "Give Valid Entry...!!!", parent=self.top5)
            if error.code == 1722:
                messagebox.showerror("Error", "Give Valid Format of Data...!!!", parent=self.top5)

    def delete_fees(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute("delete from fees where ID=:1", {'1': self.ID_var.get()})
        con.commit()
        con.close()
        self.fees_fetch_data()
        self.clear_fees()
        messagebox.showinfo("Success", "Record Deleted...!!!", parent=self.top5)

    def search_fees(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute(
            "select * from fees where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.feestable.delete(*self.feestable.get_children())
            for row in rows:
                self.feestable.insert('', END, values=row)
            con.commit()
        con.close()


root=Tk()
obj=login_system(root)
root.mainloop()