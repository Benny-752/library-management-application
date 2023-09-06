from tkinter import messagebox
from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk 
window1 = Tk()
window1.title("THE LIBRARY MANAGEMENT")
window1.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")

icon=PhotoImage(file="C:/Users/Benny Solomon/Desktop/qed.png")
label=Label(window1,image=icon)
label.place(relwidth=1,relheight=1)


def login():
    import tkinter as tk
    from tkinter import ttk 

    class Ag(tk.Frame):
       def __init__(self,master):
            
            
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()
            self.master.configure(background="pink")
            self.master.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
            self.master.title("THE LIBRARY MANAGEMENT")
        
            self.master.geometry('900x100')

        
       def create_widgets(self):
            l14=tk.Label(self,text="User Name",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
            l14.grid(row=0,column=0)
            l12=tk.Label(self,text=" Password",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
            l12.grid(row=0,column=2)
        
            title_text=tk.StringVar()
            NAME=Entry(self,textvariable=title_text)
            NAME.grid(row=0,column=1)

            t_text=tk.StringVar()
            PASS=Entry(self,textvariable=t_text)
            PASS.grid(row=0,column=3)

            def jk():
                import mysql.connector
                db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
                cursor=db.cursor()

                st="select * from stud_log where NAME='%s' and password='%s'" %(NAME.get(),PASS.get())
                cursor.execute(st)
                data=cursor.fetchall()
                for PA in data:
                    if PA[2]==NAME.get() and PA[9]==PASS.get() and PA[10]==PASS.get():
                        print("YOU ENTER YOUR WINDOW")
                        
                        window = Tk()
                        window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
                        window.title("THE LIBRARY MANAGEMENT")
                        window.configure(background="pink")
                        def we():
                            window = Tk()
                            window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
                            window.title("THE LIBRARY MANAGEMENT")
                            window.configure(background="#f21936")
                            l1=Label(window,width=50,bg="red")
                            l1.grid(row=0,column=0)
                            l1=Label(window,text="Hindustan ",width=50,bg="green",fg="white",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=1,column=0)
                            l1=Label(window,text="The Times of India",width=50,bg="#e6fb13",fg="violet",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=2,column=0)
                            l1=Label(window,text="The Hindu ",width=50,bg="green",fg="white",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=4,column=0)
                            l1=Label(window,text="Times India",width=50,bg="#e6fb13",fg="violet",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=6,column=0)

                            window.geometry('600x300')
                            window.mainloop()
                        def wq():
                            window = Tk()
                            window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
                            window.title("THE LIBRARY MANAGEMENT")
                            window.configure(background="#05d7fc")
                            l1=Label(window,bg="#05d7fc")
                            l1.grid(row=0,column=0)
                            l1=Label(window,text="Digit",width=40,bg="green",fg="white",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=1,column=0)
                            l1=Label(window,text="Business India ",width=40,bg="violet",fg="white",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=2,column=0)

                            window.geometry('545x300')
                            window.mainloop()
                        def waq():
                            window = Tk()
                            window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
                            window.title("THE LIBRARY MANAGEMENT")
                            window.configure(background="#0df922")
                            l1=Label(window,text="RD SHARMA --MATHS",width=50,bg="green",fg="white",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=0,column=0)
                            l1=Label(window,text="HC VERMA --PHYSICS",width=50,bg="#fbd813",fg="violet",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=2,column=0)
                            l1=Label(window,text="J.D. LEE --CHEMISTRY",width=50,bg="#fbd813",fg="violet",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=3,column=0)

                            window.geometry('596x300')
                            window.mainloop()
                            
                            
                        l1=Label(window,text="LIBRARY",width=70,bg="green",fg="white",font=("Britannic Bold",19,'bold'))
                        l1.grid(row=0,column=0)
                        l1=Label(window,text="# AVAILABLE ITEMS #",width=50,bg="cyan",fg="violet",font=("Britannic Bold",19,'bold'))
                        l1.grid(row=2,column=0)


                        bq=Button(window,text="* NEWS PAPER ",command=we,width=25,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
                        bq.grid(row=4,column=0)
                        bq=Button(window,text="* MAGAZINE ",command=wq,width=25,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
                        bq.grid(row=5,column=0)
                        bq=Button(window,text="* NEW GUIDES ",command=waq,width=25,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
                        bq.grid(row=6,column=0)

                        window.geometry('900x300')
                        window.mainloop()
                        break
           
                    
                else:
                        messagebox.showinfo("Error in entering","Can't ENTER - INCORRECT ENTRY")

                db.commit()
                

            bq=Button(self,text="Submit",command=jk,width=10,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
            bq.grid(row=0,column=4)

    if __name__=='__init__':
        print("fine")

    root = tk.Tk()

    app = Ag(master=root)
    
    app.mainloop()


def kl():

    window = Tk()
    window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
    window.title("THE LIBRARY MANAGEMENT")
    window.configure(background="#e20ef0")
    #defining entry
    def entry():
        try:
            import mysql.connector
            db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
            cursor=db.cursor()

            cursor.execute("insert into stud_log (GR_NO,ROLL_NO,NAME,STREAM,CLASS,SEC,ISSUE_DATE,SUB_DATE,SIGN,password,reenter_password,BOOK,ISBN)values({},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})".format(GR.get(),ROLL.get(),NAME.get(),STREAM.get(),CLASS.get(),SEC.get(),ISSUE.get(),SUB.get(),SIGN.get(),PASS.get(),REPASS.get(),bo.get(),isbn.get()))

            db.commit()
            
            print("your data has been added")

        except:
              messagebox.showinfo("Error in Adding","Can't add empty/Incorect data into Database",icon="warning")
       
    def eng():
        try:
         
            import mysql.connector

            db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
            cursor=db.cursor()
            cursor.execute("insert into stud_ext (title,isbn1)values('{}',{})".format(bo.get(),isbn.get()))

            db.commit()
            print("data ok")
        except:
              messagebox.showinfo("Error in Adding","Can't add empty/Incorect data into Database",icon="warning")

    l1=Label(window,text="Name",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    l1.grid(row=0,column=0)
    l2=Label(window,text="GR_NO.",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    l2.grid(row=0,column=2)
    l3=Label(window,text="Password",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    l3.grid(row=1,column=0)
    l4=Label(window,text="Class",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    l4.grid(row=1,column=2)
    l5=Label(window,text=" SECTION",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    l5.grid(row=1,column=4)
    l6=Label(window,text="Reenter Password",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    l6.grid(row=0,column=4)
    ls=Label(window,text=" Book",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    ls.grid(row=2,column=0)
    lf=Label(window,text=" Stream",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    lf.grid(row=2,column=2)
    ld=Label(window,text=" ISSUE_DATE",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    ld.grid(row=2,column=4)
    lj=Label(window,text=" SUB_DATE",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    lj.grid(row=3,column=0)
    lq=Label(window,text=" ISBN_NO.",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    lq.grid(row=3,column=2)
    lqq=Label(window,text=" ROLL_NO.",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    lqq.grid(row=3,column=4)
    lw=Label(window,text=" SIGNED",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
    lw.grid(row=4,column=0)

    title_text=StringVar()
    NAME=Entry(window,textvariable=title_text)
    NAME.grid(row=0,column=1)
    
    au_text=StringVar()
    
    GR=Entry(window,textvariable=au_text)
    GR.grid(row=0,column=3)

    ye_text=StringVar()
    PASS=Entry(window,textvariable=ye_text)
    PASS.grid(row=1,column=1)

    bn_text=StringVar()
    CLASS=Entry(window,textvariable=bn_text)
    CLASS.grid(row=1,column=3)

    t_text=StringVar()
    SEC=Entry(window,textvariable=t_text)
    SEC.grid(row=1,column=5)

    y_text=StringVar()
    REPASS=Entry(window,textvariable=y_text)
    REPASS.grid(row=0,column=5)

    rr_text=StringVar()
    bo=Entry(window,textvariable=rr_text)
    bo.grid(row=2,column=1)

    STE_text=StringVar()
    STREAM=Entry(window,textvariable=STE_text)
    STREAM.grid(row=2,column=3)

    iss_text=StringVar()
    ISSUE=Entry(window,textvariable=iss_text)
    ISSUE.grid(row=2,column=5)

    ifh_text=StringVar()
    SUB=Entry(window,textvariable=ifh_text)
    SUB.grid(row=3,column=1)

    iqq_text=StringVar()
    isbn=Entry(window,textvariable=iqq_text)
    isbn.grid(row=3,column=3)

    iqR_text=StringVar()
    ROLL=Entry(window,textvariable=iqR_text)
    ROLL.grid(row=3,column=5)

    iQ_text=StringVar()
    SIGN=Entry(window,textvariable=iQ_text)
    SIGN.grid(row=4,column=1)

    

    bq=Button(window,text="Submit",width=10,command=entry,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
    bq.grid(row=4,column=4)

    window.geometry('900x300')
    window.mainloop()

def erk():
        window3=Tk()
        window3.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
        window3.title("THE LIBRARY MANAGEMENT")
        window3.configure(background="yellow")
        def pwk():
            windowe=Tk()
            windowe.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
            windowe.title("THE LIBRARY MANAGEMENT")
            windowe.configure(background="grey")
            def eer():
              try:
                import mysql.connector
                db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
                cursor=db.cursor()

                cursor.execute("insert into admin (us_name,pass)values('{}','{}')".format(us.get(),ps.get()))
                db.commit()
                print("your data has been added")
              except:
                 messagebox.showinfo("Error in Adding","Can't add empty/Incorect data into Database",icon="error")
            l1=Label(windowe,text="User Name",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
            l1.grid(row=0,column=0)
            lw=Label(windowe,text="password",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
            lw.grid(row=0,column=3)
            
            title_text=StringVar()
            us=Entry(windowe,textvariable=title_text)
            us.grid(row=0,column=1)
            
            au_text=StringVar()
            
            ps=Entry(windowe,textvariable=au_text)
            ps.grid(row=0,column=4)
            
            bqw=Button(windowe,text="Submit",command=eer,width=10,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
            bqw.grid(row=1,column=1)

        def dfk():
            windowe=Tk()
            windowe.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
            windowe.title("THE LIBRARY MANAGEMENT")
            windowe.configure(background="grey")

            def eer1():
              try:
                
                import mysql.connector
                db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
                cursor=db.cursor()

                st="select * from admin where us_name='%s' and pass='%s'" %(us.get(),ps.get())
                cursor.execute(st)
                data=cursor.fetchall()
                
                for PA in data:
                    if us.get()=="" and ps.get()=="" :
                        messagebox.showinfo("Error in entering","Can't ENTER - INCORRECT ENTRY")
                        break
                    elif (not (us.get()==PA[0]) )and (not (ps.get()==PA[1])) :
                        
                        messagebox.showinfo("Error in password","Can't ENTER - INCORRECT ENTRY")
                        break
                    elif PA[0]==us.get() and PA[1]==ps.get() :
                        print("YOU ENTER YOUR WINDOW")
                        
                        window = Tk()
                        window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
                        window.title("THE LIBRARY MANAGEMENT")
                        window.configure(background="pink")
                        def opk():
                            window=Tk()

                            window.title("library")

                            window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
                            window.configure(background="cyan")

                            def ty():
                             try:
                                import mysql.connector
                                db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
                                cursor=db.cursor()

                                cursor.execute("insert into book_info (title,author,year,isbn)values('{}','{}',{},{})".format(e1.get(),e2.get(),e3.get(),e4.get()))
                                db.commit()
                                print("your data has been added")
                                
                             except:
                                 messagebox.showinfo("Error in Adding","Can't add empty data into Database")
                            def rt():#search
                              try:
                               if e1.get()=="" and e2.get()=="" and e3.get()=="" and e4.get()=="":
                                  messagebox.showinfo("Error in Searching","Can't search empty/Incomplete data into Database")
                               else:
                                df = Tk()

                                df.title("THE LIBRARY MANAGEMENT")

                                df.minsize(width=400,height=400)
                                df.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")


                                df.geometry("999x500")
                                df.configure(background="pink")

                                

                                y = 0.25

                                

                                Label(df,text="%-55s%-88s%-90s%-15s"%('TITLE','AUTHOR','YEAR','ISBN'),bg='green',fg='white',font=("Arial Narrow",10,'bold')).place(relx=0.07,rely=0.1)

                                Label(df, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='green',fg='white').place(relx=0.05,rely=0.2)

                                                               
                                import mysql.connector
                                db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
                                cur=db.cursor()
                                getBooks = "select * from book_info where title='%s' and author='%s' and year=%s and isbn=%s " %(e1.get(),e2.get(),e3.get(),e4.get())

                                cur.execute(getBooks)
                                data=cur.fetchall()
                                

                                

                                for i in data:

                                    Label(df,text="%-50s%-88s%-88s%-30s"%(i[0],i[1],i[2],i[3]),bg='yellow',fg='red').place(relx=0.07,rely=y)
                                    
                                    y += 0.1
                                db.commit()

                                

                                df.mainloop()
                                 
                                  
                              except:
                                 messagebox.showinfo("Error in Searching","Can't search empty/Incomplete data into Database")
                            def uy():
                              try:
                                    masw = Tk()

                                    masw.title("THE LIBRARY MANAGEMENT")

                                    masw.minsize(width=400,height=400)
                                    masw.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")


                                    masw.geometry("999x500")
                                    masw.configure(background="pink")

                                    

                                    y = 0.25

                                    

                                    Label(masw,text="%-55s%-88s%-90s%-15s"%('TITLE','AUTHOR','YEAR','ISBN'),bg='green',fg='white',font=("Arial Narrow",10,'bold')).place(relx=0.07,rely=0.1)

                                    Label(masw, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='green',fg='white').place(relx=0.05,rely=0.2)

                                                                      
                                    import mysql.connector
                                    db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
                                    cur=db.cursor()
                                    getBooks = "select * from book_info"

                                    cur.execute(getBooks)
                                    data=cur.fetchall()
                                    

                                    

                                    for i in data:

                                        Label(masw,text="%-50s%-88s%-88s%-30s"%(i[0],i[1],i[2],i[3]),bg='yellow',fg='red').place(relx=0.07,rely=y)
                                        
                                        y += 0.1
                                    db.commit()
                                    masw.mainloop()

    

                                    
                              except:
                               messagebox.showinfo("Error in Searching","Can't search empty/Incomplete data into Database")
                            #the speacil

                            l1=Label(window,text="Title",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=0,column=0)
                            
                            l2=Label(window,text="Author",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
                            l2.grid(row=0,column=2)
                            
                            l3=Label(window,text="Year",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
                            l3.grid(row=1,column=0)
                            
                            l4=Label(window,text="ISBN_No.",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
                            l4.grid(row=1,column=2)
                            
                            
                            title_text=StringVar()
                            e1=Entry(window,textvariable=title_text)
                            e1.grid(row=0,column=1)
                            au_text=StringVar()
                            e2=Entry(window,textvariable=au_text)
                            e2.grid(row=0,column=3)
                            ye_text=StringVar()
                            e3=Entry(window,textvariable=ye_text)
                            e3.grid(row=1,column=1)

                            isbn_text=StringVar()
                            e4=Entry(window,textvariable=isbn_text)
                            e4.grid(row=1,column=3)
                            
                            b1=Button(window,text="view all",command=uy,width=12,height=2,bg="white",fg="orange",font=("Britannic Bold",19,'italic'))
                            b1.grid(row=2,column=4)


                            b2=Button(window,text="search",command=rt,width=12,height=2,bg="white",fg="green",font=("Britannic Bold",19,'italic'))
                            b2.grid(row=3,column=4)

                            b3=Button(window,text="Add",command=ty,width=12,height=2,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
                            b3.grid(row=4,column=4)
                            window.mainloop()

                            # the
                        def ook():
                            window=Tk()

                            window.title("library")

                            window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
                            window.configure(background="#c8f10d")

                            def ty():
                             try:
                                import mysql.connector
                                db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
                                cursor=db.cursor()

                                cursor.execute("insert into book_info (title,author,year,isbn)values('{}','{}',{},{})".format(e1.get(),e2.get(),e3.get(),e4.get()))
                                db.commit()
                                print("your data has been added")
                             except:
                                 messagebox.showinfo("Error in Adding","Can't add empty data into Database")
                            def uy():
                              try:
                                df = Tk()

                                df.title("THE LIBRARY MANAGEMENT")

                                df.minsize(width=400,height=400)
                                df.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")


                                df.geometry("500x400")
                                df.configure(background="pink")

                                

                                y = 0.25

                                

                                Label(df,text="%-55s%-88s"%('BOOK','ISBN_NO.'),bg='green',fg='white',font=("Arial Narrow",10,'bold')).place(relx=0.07,rely=0.1)

                                Label(df, text="---------------------------------------------------------------------------------------------------",bg='green',fg='white').place(relx=0.05,rely=0.2)

                                 
                                import mysql.connector
                                db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
                                cur=db.cursor()
                                getBooks = "select * from stud_log where NAME='%s' and GR_NO=%s " %(e1.get(),e2.get())

                                cur.execute(getBooks)
                                data=cur.fetchall()
                                
                                for i in data:

                                    Label(df,text="%-50s%-88s"%(i[11],i[12]),bg='yellow',fg='red').place(relx=0.07,rely=y)
                                    
                                    y += 0.1
                                db.commit()

                                df.mainloop()
                              except:
                               messagebox.showinfo("Error in Searching","Can't search empty/Incomplete data into Database")
                            #the speacil
                            l1=Label(window,text="NAME",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
                            l1.grid(row=0,column=0)
                            
                            l2=Label(window,text="GR_NO.",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
                            l2.grid(row=0,column=2)

                            title_text=StringVar()
                            e1=Entry(window,textvariable=title_text)
                            e1.grid(row=0,column=1)
                            
                            au_text=StringVar()
                            e2=Entry(window,textvariable=au_text)
                            e2.grid(row=0,column=3)

                            b1=Button(window,text="Search",command=uy,width=12,height=2,bg="white",fg="orange",font=("Britannic Bold",19,'italic'))
                            b1.grid(row=2,column=3)

                            window.geometry("489x152")
                            window.mainloop()
           
                        l1=Label(window,text="# AVAILABLE  #",width=50,bg="cyan",fg="violet",font=("Britannic Bold",19,'bold'))
                        l1.grid(row=2,column=0)
                        l1=Label(window,width=50,bg="pink",fg="violet",font=("Britannic Bold",19,'bold'))
                        l1.grid(row=3,column=0)

                        bq=Button(window,text="* BOOKS EDIT ",command=opk,width=25,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
                        bq.grid(row=4,column=0)
                        bq=Button(window,text="* STUDENT RECORD ",command=ook,width=25,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
                        bq.grid(row=5,column=0)
  
                        window.geometry('700x200')
                        window.mainloop()
                    
                    else:
                        messagebox.showinfo("Error in entering","Can't ENTER - INCORRECT ENTRY")
                        
                    


              except:
                        messagebox.showinfo("Error in entering","Can't ENTER - INCORRECT ENTRY")

                

            l1=Label(windowe,text="User Name",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
            l1.grid(row=0,column=0)
            lw=Label(windowe,text="password",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
            lw.grid(row=0,column=3)
            
            title_text=StringVar()
            us=Entry(windowe,textvariable=title_text)
            us.grid(row=0,column=1)
            
            au_text=StringVar()
            
            ps=Entry(windowe,textvariable=au_text)
            ps.grid(row=0,column=4)
            
            bqw=Button(windowe,text="Submit",command=eer1,width=10,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
            bqw.grid(row=1,column=1)
        lk=Label(window3,bg="yellow")
        lk.grid(row=0,column=0)

        bq=Button(window3,text="Already an User",command=dfk,width=25,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
        bq.grid(row=1,column=0)
        l1=Label(window3,bg="yellow")
        l1.grid(row=2,column=0)
        l1=Label(window3,bg="yellow")
        l1.grid(row=3,column=0)
        bqw=Button(window3,text="NEW User",command=pwk,width=10,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
        bqw.grid(row=4,column=0)

        window3.geometry('325x200')
        window3.mainloop()
    
def admin():
    
        window2=Tk()
        window2.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
        window2.title("THE LIBRARY MANAGEMENT")
        
        def po():
          try:
            import mysql.connector
            db=mysql.connector.connect(host="localhost",user="root",passwd="ben",database="books")
            cursor=db.cursor()

            cursor.execute("insert into stud_log (title,author,year,isbn)values('{}','{}',{},{})".format(e7.get(),e4.get(),e3.get(),e4.get()))
            db.commit()
            print("your data has been added")
          except:
              messagebox.showinfo("Error in Adding","Can't add empty/Incorect data into Database")

        #vr
        l14=Label(window2,text="User Name",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
        l14.grid(row=0,column=0)
        l12=Label(window2,text=" Password",bg="brown",fg="white",font=("Britannic Bold",19,'bold'))
        l12.grid(row=0,column=2)

        title_text=StringVar()
        e7=Entry(window2,textvariable=title_text)
        e7.grid(row=0,column=1)

        t_text=StringVar()
        e4=Entry(window2,textvariable=t_text)
        e4.grid(row=0,column=3)

        bq=Button(window2,text="Submit",command=po,width=10,height=1,bg="white",fg="red",font=("Britannic Bold",19,'italic'))
        bq.grid(row=2,column=3)

        
        window2.geometry('800x500')
        window2.mainloop()

l1=Label(window1,text="LIBRARY MANAGEMENT",bg="#33c4e1",fg="#f30929",font=("Britannic Bold",19,'bold'))
l1.place(relwidth=1,relheight=0.12)

b1=tkinter.Button(window1,text="Sign Up",command=kl,width=35,height=50,bg="white",fg="#f8e907",font=("Britannic Bold",20,'italic'))
b1.grid(row=0,column=0,ipadx=60,pady=60)

mw=PhotoImage(file="C:/Users/Benny Solomon/Desktop/df.png")
b1.config(image=mw,compound=CENTER)
tm=mw.subsample(6,6)
b1.config(image=tm)
b1.grid(row=0,column=0,ipadx=60,pady=60)





b2=tkinter.Button(window1,text="Login",command=login,width=1,height=50,bg="#09f35b",fg="red",font=("Britannic Bold",20,'italic'))
b2.grid(row=0,column=4000,ipadx=85,pady=85)

mwJ=PhotoImage(file="C:/Users/Benny Solomon/Desktop/rts.png")
b2.config(image=mwJ,compound=LEFT)
WE=mwJ.subsample(6,6)
b2.config(image=WE)
b2.grid(row=0,column=4000)



b3=tkinter.Button(window1,text="Admin_User",command=erk,width=250,height=63,bg="white",fg="blue",font=("Britannic Bold",19,'italic'))
b3.grid(row=17,column=1)

mf=PhotoImage(file="C:/Users/Benny Solomon/Desktop/QWE.png")
b3.config(image=mf,compound=LEFT)
Wr=mf.subsample(6,6)
b3.config(image=Wr)
b3.grid(row=17,column=1)

window1.geometry('600x396')

window1.mainloop()



window=tkinter.Tk()
window.title("Library Management")
window.iconbitmap(r"C:/Users/Benny Solomon/Desktop/bo.ico")
window.configure(background="light blue")
icon=tkinter.PhotoImage(file="C:/Users/Benny Solomon/Desktop/PRO2.png")
label=tkinter.Label(window,image=icon)
s=tkinter.Button(text="* CLOSE  x  THE LIBRARY MANAGEMENT  *",command=window.destroy,fg="blue",bg="white",font=("Britannic Bold",19,'bold'),border=1)
s.pack(side="bottom")
label.pack()
window.geometry("850x450")
window.mainloop()

