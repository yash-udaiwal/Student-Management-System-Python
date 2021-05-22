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

        self.bg_icon=ImageTk.PhotoImage(file='G:\\images.jpg')
        self.user_icon=PhotoImage(file="G:\\usr.png")
        self.pass_icon=PhotoImage(file="G:\\pass.png")
        self.logo_icon=PhotoImage(file="G:\\icon.png")
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
        btn_log=Button(login_frame, text="Login", width=15, command=self.main, font=("Adobe Gothic Std B", 15, "bold"),
                       bg="light coral", fg="misty rose").grid(row=3, column=1, pady=7)


    def main(self):
        self.top1=Toplevel()
        self.top1.focus()
        self.top1.title("Main Frame")
        self.top1.geometry("1350x700+0+0")
        self.main_bg=ImageTk.PhotoImage(file="G:\\bckg.jpg")
        main_lbl=Label(self.top1, image=self.main_bg).pack()

        Main_frame=Frame(self.top1, bg="light blue")
        Main_frame.place(x=950, y=150)
        stu_btn=Button(Main_frame, text="Attandance", command=self.attandance, width=15,
                       font=("times new roman", 14, "bold"), bg="light coral", fg="white")
        stu_btn.focus_set()
        stu_btn=stu_btn.grid(row=0, column=0, pady=10)
        hostel_btn=Button(Main_frame, text="Attentive", width=15,
                          font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=1, column=0,
                                                                                                   pady=10)
        result_btn=Button(Main_frame, text="Uniform", width=15,
                          font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=2, column=0,
                                                                                                   pady=10)
        fees_btn=Button(Main_frame, text="Behaviour", width=15,
                        font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=3, column=0,
                                                                                                 pady=10)
        exit_btn=Button(Main_frame, text="Ethics", width=15,
                        font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=4, column=0,
                                                                                                 pady=10)
        english_btn=Button(Main_frame, text="English", width=15,
                        font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=5, column=0,
                                                                                                 pady=10)
        extra_btn=Button(Main_frame, text="Extra curriculum", width=15,
                        font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=6, column=0,
                                                                                                 pady=10)

    ########################################################################################################################
    ############################################ STUDENT TABLE #############################################################
    ########################################################################################################################

    def attandance(self):

        self.top2=Toplevel()
        self.top2.focus()
        self.top2.title("STUDENT Record")
        self.top2.geometry("1350x700+0+0")
        title_stu=Label(self.top2, text='STUDENT RECORD', bd=10, relief=GROOVE, font=("algerian", 40), bg="gold",
                        fg="brown")
        title_stu.pack(side=TOP, fill=X)
        self.stu_bg=ImageTk.PhotoImage(file="G:\\bgff.jpg")
        insert_stu_lbl=Label(self.top2, image=self.stu_bg).pack()

        btn_frame=Frame(self.top2, bd=4, relief=RIDGE)
        btn_frame.place(x=1000, y=100, width=300, height=270)
        self.btnframe=ImageTk.PhotoImage(file='G:\\bckg.jpg')
        btnfrm=Label(btn_frame, image=self.btnframe).pack()
        btn1_frame=Frame(btn_frame, bg='sky blue', bd=5, relief=RIDGE)
        btn1_frame.place(x=60, y=18)
        addbtn=Button(btn1_frame, text='ADD RECORD', width=20, command=self.add_student, bg="light coral",
                      fg="white").grid(row=0, column=0, padx=10, pady=10)
        exitbtn=Button(btn1_frame, text='Exit', command=self.top2.destroy, width=20, bg="light coral", fg="white").grid(
            row=1, column=0, pady=10)

        tableframe=Frame(self.top2, bd=4, relief=RIDGE, bg='purple')
        tableframe.place(x=30, y=100, width=240, height=300)
        scrol_x=Scrollbar(tableframe, orient=HORIZONTAL)
        scrol_y=Scrollbar(tableframe, orient=VERTICAL)
        self.stutable=ttk.Treeview(tableframe, columns=(
            "NAME", "CLASS"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
      #  scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_x.config(command=self.stutable.xview)
        scrol_y.config(command=self.stutable.yview)
        self.stutable.heading("NAME", text="NAME")
        self.stutable.heading("CLASS", text="CLASS")
        self.stutable['show']='headings'
        self.stutable.column("NAME", width=80)
        self.stutable.column("CLASS", width=135)
        self.stutable.pack(fill=BOTH, expand=1)
        self.stutable.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    ########################################################################################################################

    def fetch_data(self):
        con=cx_Oracle.connect("system/yash@localhost:1521/system")
        cur=con.cursor()
        cur.execute("select * from student")
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

    def get_cursor(self, ev):
        cursor_row=self.stutable.focus()
        content=self.stutable.item(cursor_row)
        row=content['values']
        self.ID_var.set(row[0])
        self.NAME_var.set(row[1])
    ########################################################################################################################
root=Tk()
obj=login_system(root)
root.mainloop()