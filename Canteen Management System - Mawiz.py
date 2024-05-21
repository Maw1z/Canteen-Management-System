#importing all necessary libraries
from ast import Delete
from pickle import FRAME
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import width
from types import new_class
import mysql.connector as mc

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Delete Details Window
def open_delete_window():

    def deleteproductdetails():
        def data_deleted():
            messagebox.showinfo("Product detail", "Product details have been deleted successfully ")

        def clear_text_entry():
            productcodedelete_entry.delete(0, 'end')    

        def deleteproductdetail():
            productcode_todelete=productcodedelete_entry.get()
            con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
            cur=con.cursor()
            cur.execute("delete from product_details where product_code=%s;",(productcode_todelete,))
            con.commit()
            data_deleted()
            clear_text_entry()
            cur.execute("select * from product_details;")
            records=cur.fetchall()
            print_records=""
            for record in records:
                print_records += str(record) + "\n"

            query_label=Label(deleteproduct_window, text=print_records, fg="#61647d", font="Menlo 12")
            query_label.place(x=10,y=130)
        
        deleteproduct_window=Toplevel()
        deleteproduct_window.title("Delete Product Details")
        deleteproduct_window.geometry("600x600+250+115")
        deleteproduct_window.resizable(width=False, height=False)

        Text16=Label(deleteproduct_window, text="Enter code of product to be deleted ", font="Menlo 14", fg="#61647d")
        Text16.place(x=10,y=10)

        productcodedelete_entry=Entry(deleteproduct_window, width=35)
        productcodedelete_entry.place(x=320,y=15)

        Text18=Label(deleteproduct_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
        Text18.place(x=10,y=100)

        Enter_btn=Button(deleteproduct_window, text="Enter", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=deleteproductdetail)
        Enter_btn.place(x=115,y=45)

        exit_button=Button(deleteproduct_window, text="                 Exit                ",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=deleteproduct_window.destroy)
        exit_button.place(x=235,y=45)

    def deleteworkerdetails():
        def data_deleted():
            messagebox.showinfo("Worker detail", "Worker Details have been deleted successfully ")

        def clear_text_entry():
            workerIDdelete_entry.delete(0, 'end')    

        def deleteworkerdetail():
            workerID_todelete=workerIDdelete_entry.get()
            con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
            cur=con.cursor()
            cur.execute("delete from worker_details where worker_id=%s;",(workerID_todelete,))
            con.commit()
            data_deleted()
            clear_text_entry()
            cur.execute("select * from worker_details;")
            records=cur.fetchall()
            print_records=""
            for record in records:
                print_records += str(record) + "\n"

            query_label=Label(deleteworker_window, text=print_records, fg="#61647d", font="Menlo 12")
            query_label.place(x=10,y=130)
        
        deleteworker_window=Toplevel()
        deleteworker_window.title("Delete Worker Details")
        deleteworker_window.geometry("600x600+250+115")
        deleteworker_window.resizable(width=False, height=False)

        Text16=Label(deleteworker_window, text="Enter ID of worker to be deleted ", font="Menlo 14", fg="#61647d")
        Text16.place(x=10,y=10)

        workerIDdelete_entry=Entry(deleteworker_window, width=35)
        workerIDdelete_entry.place(x=295,y=15)

        Text18=Label(deleteworker_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
        Text18.place(x=10,y=100)

        Enter_btn=Button(deleteworker_window, text="Enter", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=deleteworkerdetail)
        Enter_btn.place(x=115,y=45)

        exit_button=Button(deleteworker_window, text="                 Exit                ",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=deleteworker_window.destroy)
        exit_button.place(x=235,y=45)

    def deletestudentdetails():
        def data_deleted():
            messagebox.showinfo("Student detail", "Student details have been deleted successfully ")

        def clear_text_entry():
            IDdelete_entry.delete(0, 'end')    

        def deletestudentdetail():
            studentID_todelete=IDdelete_entry.get()
            con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
            cur=con.cursor()
            cur.execute("delete from student_details where student_id=%s;",(studentID_todelete,))
            con.commit()
            data_deleted()
            clear_text_entry()
            cur.execute("select * from student_details;")
            records=cur.fetchall()
            print_records=""
            for record in records:
                print_records += str(record) + "\n"

            query_label=Label(deletestudent_window, text=print_records, fg="#61647d", font="Menlo 12")
            query_label.place(x=10,y=130)
        
        deletestudent_window=Toplevel()
        deletestudent_window.title("Delete Student Details")
        deletestudent_window.geometry("600x600+250+115")
        deletestudent_window.resizable(width=False, height=False)

        Text16=Label(deletestudent_window, text="Enter ID of student to be deleted ", font="Menlo 14", fg="#61647d")
        Text16.place(x=10,y=10)

        IDdelete_entry=Entry(deletestudent_window, width=35)
        IDdelete_entry.place(x=295,y=15)

        Text18=Label(deletestudent_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
        Text18.place(x=10,y=100)

        Enter_btn=Button(deletestudent_window, text="Enter", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=deletestudentdetail)
        Enter_btn.place(x=115,y=45)

        exit_button=Button(deletestudent_window, text="                 Exit                ",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=deletestudent_window.destroy)
        exit_button.place(x=235,y=45)

    Delete_details_window=Toplevel()
    Delete_details_window.title("Delete details")
    Delete_details_window.geometry("600x500+250+115")
    Delete_details_window.resizable(width=False, height=False)

    Text6=Label(Delete_details_window, text="What would you like to delete details for?", font="Menlo 14", fg="#61647d")
    Text6.place(x=125,y=30)

    delete_student_details_btn=Button(Delete_details_window, text="Delete Student Details", padx=25, pady=25,font="Menlo 12", fg="#61647d", command=deletestudentdetails)
    delete_student_details_btn.place(x=195,y=70)

    delete_worker_details_btn=Button(Delete_details_window, text="Delete Worker Details ", padx=25, pady=25,font="Menlo 12" , fg="#61647d", command=deleteworkerdetails)
    delete_worker_details_btn.place(x=195,y=160)

    delete_product_details_btn=Button(Delete_details_window, text="Delete Product Details", padx=25, pady=25,font="Menlo 12" , fg="#61647d", command=deleteproductdetails)
    delete_product_details_btn.place(x=195,y=250)

    exit_button=Button(Delete_details_window, text="                 Exit                ",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=Delete_details_window.destroy)
    exit_button.place(x=195,y=340)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Update Details Window
def open_update_window():

    def updateproductdetails():
        def updateproduct_uncost():
            def data_updated():
                messagebox.showinfo("Product detail", "Product details have been updated successfully")

            def clear_text_entry():
                productcode_entry.delete(0, 'end')    
                newuncost_entry.delete(0, 'end')

            def query():
                product_codetofind=productcode_entry.get()
                new_uncost=newuncost_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update product_details set product_uncost=%s where product_code=%s",(new_uncost,product_codetofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from product_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateproductuncost_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)
                
            updateproductuncost_window=Toplevel()
            updateproductuncost_window.title("Update Product Unit Cost")
            updateproductuncost_window.geometry("600x600+250+115")
            updateproductuncost_window.resizable(width=False, height=False)

            Text16=Label(updateproductuncost_window, text="Enter code of product to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            productcode_entry=Entry(updateproductuncost_window, width=35)
            productcode_entry.place(x=278,y=15)

            Text17=Label(updateproductuncost_window, text="Enter new unit cost ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newuncost_entry=Entry(updateproductuncost_window,width=50)
            newuncost_entry.place(x=150,y=55)

            Text18=Label(updateproductuncost_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateproductuncost_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateproductuncost_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateproductuncost_window.destroy)
            exit_button.place(x=280,y=85)

        def updateproduct_unit():
            def data_updated():
                messagebox.showinfo("Product detail", "Product details have been updated successfully")

            def clear_text_entry():
                productcode_entry.delete(0, 'end')    
                newunit_entry.delete(0, 'end')

            def query():
                product_codetofind=productcode_entry.get()
                new_unit=newunit_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update product_details set product_unit=%s where product_code=%s",(new_unit,product_codetofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from product_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateproductunit_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updateproductunit_window=Toplevel()
            updateproductunit_window.title("Update Product Unit(s)")
            updateproductunit_window.geometry("600x600+250+115")
            updateproductunit_window.resizable(width=False, height=False)

            Text16=Label(updateproductunit_window, text="Enter code of product to be changed: ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            productcode_entry=Entry(updateproductunit_window, width=35)
            productcode_entry.place(x=278,y=15)

            Text17=Label(updateproductunit_window, text="Enter new unit number ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newunit_entry=Entry(updateproductunit_window,width=50)
            newunit_entry.place(x=180,y=55)

            Text18=Label(updateproductunit_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateproductunit_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateproductunit_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateproductunit_window.destroy)
            exit_button.place(x=280,y=85)

        def updateproduct_prod():
            def data_updated():
                messagebox.showinfo("Product detail", "Product details have been updated successfully")

            def clear_text_entry():
                productcode_entry.delete(0, 'end')    
                newprod_entry.delete(0, 'end')

            def query():
                product_codetofind=productcode_entry.get()
                new_prod=newprod_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update product_details set product_prod=%s where product_code=%s",(new_prod,product_codetofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from product_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateproductprod_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updateproductprod_window=Toplevel()
            updateproductprod_window.title("Update Product Producer")
            updateproductprod_window.geometry("600x600+250+115")
            updateproductprod_window.resizable(width=False, height=False)

            Text16=Label(updateproductprod_window, text="Enter code of product to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            productcode_entry=Entry(updateproductprod_window, width=35)
            productcode_entry.place(x=278,y=15)

            Text17=Label(updateproductprod_window, text="Enter new producer ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newprod_entry=Entry(updateproductprod_window,width=50)
            newprod_entry.place(x=150,y=55)

            Text18=Label(updateproductprod_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateproductprod_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateproductprod_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateproductprod_window.destroy)
            exit_button.place(x=280,y=85)

        def updateproduct_name():
            def data_updated():
                messagebox.showinfo("Product detail", "Product details have been updated successfully")

            def clear_text_entry():
                productcode_entry.delete(0, 'end')    
                newname_entry.delete(0, 'end')

            def query():
                product_codetofind=productcode_entry.get()
                new_name=newname_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update product_details set product_name=%s where product_code=%s",(new_name,product_codetofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from product_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateproductname_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updateproductname_window=Toplevel()
            updateproductname_window.title("Update Product Name")
            updateproductname_window.geometry("600x600+250+115")
            updateproductname_window.resizable(width=False, height=False)

            Text16=Label(updateproductname_window, text="Enter code of product to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            productcode_entry=Entry(updateproductname_window, width=35)
            productcode_entry.place(x=268,y=15)

            Text17=Label(updateproductname_window, text="Enter new name ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newname_entry=Entry(updateproductname_window,width=50)
            newname_entry.place(x=160,y=55)

            Text18=Label(updateproductname_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateproductname_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe" , command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateproductname_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateproductname_window.destroy)
            exit_button.place(x=280,y=85) 

        def updateproduct_code():
            def data_updated():
                messagebox.showinfo("Product detail", "Product details have been updated successfully")

            def clear_text_entry():
                productname_entry.delete(0, 'end')    
                newcode_entry.delete(0, 'end')

            def query():
                product_nametofind=str(productname_entry.get())
                new_code=newcode_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update product_details set product_code=%s where product_name=%s",(new_code,product_nametofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from product_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateproductcode_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updateproductcode_window=Toplevel()
            updateproductcode_window.title("Update Product Code")
            updateproductcode_window.geometry("600x600+250+115")
            updateproductcode_window.resizable(width=False, height=False)

            Text16=Label(updateproductcode_window, text="Enter name of product to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            productname_entry=Entry(updateproductcode_window, width=35)
            productname_entry.place(x=283,y=15)

            Text17=Label(updateproductcode_window, text="Enter new code ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newcode_entry=Entry(updateproductcode_window,width=50)
            newcode_entry.place(x=135,y=55)

            Text18=Label(updateproductcode_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateproductcode_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateproductcode_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateproductcode_window.destroy)
            exit_button.place(x=280,y=85) 

        updateproduct_window=Toplevel()
        updateproduct_window.title("Update Product Details")
        updateproduct_window.geometry("600x600+250+115")
        updateproduct_window.resizable(width=False, height=False)

        Text15=Label(updateproduct_window, text="Which product detail would you like to update?", font="Menlo 14", fg="#61647d")
        Text15.place(x=120,y=10)

        #Code
        Code_btn=Button(updateproduct_window, text="    Code   ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updateproduct_code)
        Code_btn.place(x=240,y=50)

        #Name
        Name_btn=Button(updateproduct_window, text="    Name  ", padx=25, pady=25, font="Menlo 12",fg="#61647d", command=updateproduct_name)
        Name_btn.place(x=240,y=140)

        #Producer
        Producer_btn=Button(updateproduct_window, text="Producer ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updateproduct_prod)
        Producer_btn.place(x=240,y=230)

        #Unit
        Unit_btn=Button(updateproduct_window, text="     Unit     ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updateproduct_unit)
        Unit_btn.place(x=240,y=320)

        #Unit Cost
        Uncost_btn=Button(updateproduct_window, text="Unit Cost ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updateproduct_uncost)
        Uncost_btn.place(x=240,y=410)

        #Exit
        exit_button=Button(updateproduct_window, text="     Exit     ",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=updateproduct_window.destroy)
        exit_button.place(x=240,y=500)
        
    def updateworkerdetails():
        def updateworker_contact():
            def data_updated():
                messagebox.showinfo("Worker Detail", "Worker details have been updated successfully")

            def clear_text_entry():
                workerID_entry.delete(0, 'end')    
                newcontact_entry.delete(0, 'end')

            def query():
                worker_IDtofind=workerID_entry.get()
                new_contact=newcontact_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update worker_details set contact_no=%s where worker_id=%s",(new_contact,worker_IDtofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from worker_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateworkercontact_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updateworkercontact_window=Toplevel()
            updateworkercontact_window.geometry("600x600+250+115")
            updateworkercontact_window.title("Update Worker Contact Number")
            updateworkercontact_window.resizable(width=False, height=False)

            Text16=Label(updateworkercontact_window, text="Enter ID of worker to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            workerID_entry=Entry(updateworkercontact_window, width=35)
            workerID_entry.place(x=268,y=15)

            Text17=Label(updateworkercontact_window, text="Enter new contact number ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newcontact_entry=Entry(updateworkercontact_window,width=50)
            newcontact_entry.place(x=200,y=55)

            Text18=Label(updateworkercontact_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateworkercontact_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateworkercontact_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateworkercontact_window.destroy)
            exit_button.place(x=280,y=85) 

        def updateworker_shift():
            def data_updated():
                messagebox.showinfo("Worker Detail", "Worker details have been updated successfully")

            def clear_text_entry():
                workerID_entry.delete(0, 'end')    
                newshift_entry.delete(0, 'end')

            def query():
                worker_IDtofind=workerID_entry.get()
                new_shift=newshift_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update worker_details set worker_shift=%s where worker_id=%s",(new_shift,worker_IDtofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from worker_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateworkershift_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updateworkershift_window=Toplevel()
            updateworkershift_window.geometry("600x600+250+115")
            updateworkershift_window.title("Update Worker Shift")
            updateworkershift_window.resizable(width=False, height=False)

            Text16=Label(updateworkershift_window, text="Enter ID of worker to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            workerID_entry=Entry(updateworkershift_window, width=35)
            workerID_entry.place(x=268,y=15)

            Text17=Label(updateworkershift_window, text="Enter new shift ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newshift_entry=Entry(updateworkershift_window,width=50)
            newshift_entry.place(x=135,y=55)

            Text18=Label(updateworkershift_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateworkershift_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateworkershift_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateworkershift_window.destroy)
            exit_button.place(x=280,y=85) 

        def updateworker_name():
            def data_updated():
                messagebox.showinfo("Worker Detail", "Worker details have been updated successfully")

            def clear_text_entry():
                workerID_entry.delete(0, 'end')    
                newname_entry.delete(0, 'end')

            def query():
                worker_IDtofind=workerID_entry.get()
                new_name=newname_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update worker_details set worker_name=%s where worker_id=%s",(new_name,worker_IDtofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from worker_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateworkername_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updateworkername_window=Toplevel()
            updateworkername_window.geometry("600x600+250+115")
            updateworkername_window.title("Update Worker Name")
            updateworkername_window.resizable(width=False, height=False)

            Text16=Label(updateworkername_window, text="Enter ID of worker to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            workerID_entry=Entry(updateworkername_window, width=35)
            workerID_entry.place(x=268,y=15)

            Text17=Label(updateworkername_window, text="Enter new name ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newname_entry=Entry(updateworkername_window,width=50)
            newname_entry.place(x=135,y=55)

            Text18=Label(updateworkername_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateworkername_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateworkername_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateworkername_window.destroy)
            exit_button.place(x=280,y=85) 

        def updateworkerId():
            def data_updated():
                messagebox.showinfo("Worker Detail", "Worker details have been updated successfully")

            def clear_text_entry():
                workername_entry.delete(0, 'end')    
                newID_entry.delete(0, 'end')

            def query():
                worker_nametofind=str(workername_entry.get())
                new_ID=newID_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update worker_details set worker_id=%s where worker_name=%s",(new_ID,worker_nametofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from worker_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updateworkerID_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updateworkerID_window=Toplevel()
            updateworkerID_window.geometry("600x600+250+115")
            updateworkerID_window.title("Update Worker ID")
            updateworkerID_window.resizable(width=False, height=False)

            Text16=Label(updateworkerID_window, text="Enter name of worker to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            workername_entry=Entry(updateworkerID_window, width=35)
            workername_entry.place(x=288,y=15)

            Text17=Label(updateworkerID_window, text="Enter new ID ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newID_entry=Entry(updateworkerID_window,width=50)
            newID_entry.place(x=120,y=55)

            Text18=Label(updateworkerID_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updateworkerID_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updateworkerID_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updateworkerID_window.destroy)
            exit_button.place(x=280,y=85) 
        
        updateworker_window=Toplevel()
        updateworker_window.title("Update Worker Details")
        updateworker_window.geometry("600x600+250+115")
        updateworker_window.resizable(width=False, height=False)

        Text15=Label(updateworker_window, text="Which worker detail would you like to update?", font="Menlo 14", fg="#61647d")
        Text15.place(x=120,y=10)

        #ID btn
        IDbtn1=Button(updateworker_window, text="    ID Number     ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updateworkerId)
        IDbtn1.place(x=195,y=50)

        #Name btn
        Name_btn=Button(updateworker_window, text="        Name         ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updateworker_name)
        Name_btn.place(x=195,y=140)

        #Shift btn
        Shift_btn=Button(updateworker_window, text="         Shift           ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updateworker_shift)
        Shift_btn.place(x=195,y=230)

        #Contact number btn
        Contact_btn=Button(updateworker_window, text="Contact Number", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updateworker_contact)
        Contact_btn.place(x=195,y=320)

        #Exit btn
        exit_button=Button(updateworker_window, text="          Exit           ",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=updateworker_window.destroy)
        exit_button.place(x=195,y=410)

    def updatestudentdetails():
        def updatestudent_Bill():
            def data_updated():
                messagebox.showinfo("Student detail", "Student details have been updated successfully")

            def clear_text_entry():
                studentID_entry.delete(0, 'end')    
                newbill_entry.delete(0, 'end')

            def query():
                student_IDtofind=studentID_entry.get()
                new_bill=newbill_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update student_details set net_bill=%s where student_id=%s",(new_bill,student_IDtofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from student_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updatestudentbill_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updatestudentbill_window=Toplevel()
            updatestudentbill_window.title("Update student's Net Bill")
            updatestudentbill_window.geometry("600x600+250+115")
            updatestudentbill_window.resizable(width=False, height=False)

            Text16=Label(updatestudentbill_window, text="Enter ID of student to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            studentID_entry=Entry(updatestudentbill_window, width=35)
            studentID_entry.place(x=258,y=15)

            Text17=Label(updatestudentbill_window, text="Enter new net bill ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newbill_entry=Entry(updatestudentbill_window,width=50)
            newbill_entry.place(x=150,y=55)

            Text18=Label(updatestudentbill_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updatestudentbill_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updatestudentbill_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updatestudentbill_window.destroy)
            exit_button.place(x=280,y=85) 

        def updatestudent_Contact():
            def data_updated():
                messagebox.showinfo("Student detail", "Student details have been updated successfully")

            def clear_text_entry():
                studentID_entry.delete(0, 'end')    
                newcontact_entry.delete(0, 'end')

            def query():
                student_IDtofind=studentID_entry.get()
                new_contact=newcontact_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update student_details set contact_no=%s where student_id=%s",(new_contact,student_IDtofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from student_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updatestudentcontact_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updatestudentcontact_window=Toplevel()
            updatestudentcontact_window.title("Update student's contact details")
            updatestudentcontact_window.geometry("600x600+250+115")
            updatestudentcontact_window.resizable(width=False, height=False)

            Text16=Label(updatestudentcontact_window, text="Enter ID of student to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            studentID_entry=Entry(updatestudentcontact_window, width=35)
            studentID_entry.place(x=258,y=15)

            Text17=Label(updatestudentcontact_window, text="Enter new contact number ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newcontact_entry=Entry(updatestudentcontact_window,width=50)
            newcontact_entry.place(x=210,y=55)

            Text18=Label(updatestudentcontact_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updatestudentcontact_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updatestudentcontact_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updatestudentcontact_window.destroy)
            exit_button.place(x=280,y=85) 

        def updatestudent_Class():
            def data_updated():
                messagebox.showinfo("Student detail", "Student details have been updated successfully")

            def clear_text_entry():
                studentID_entry.delete(0, 'end')    
                newclass_entry.delete(0, 'end')

            def query():
                student_IDtofind=studentID_entry.get()
                new_class=newclass_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update student_details set student_class=%s where student_id=%s",(new_class,student_IDtofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from student_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updatestudentclass_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)
            
            updatestudentclass_window=Toplevel()
            updatestudentclass_window.title("Update student's class")
            updatestudentclass_window.geometry("600x600+250+115")
            updatestudentclass_window.resizable(width=False, height=False)

            Text16=Label(updatestudentclass_window, text="Enter ID of student to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            studentID_entry=Entry(updatestudentclass_window, width=35)
            studentID_entry.place(x=258,y=15)

            Text17=Label(updatestudentclass_window, text="Enter new class ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newclass_entry=Entry(updatestudentclass_window,width=50)
            newclass_entry.place(x=138,y=55)

            Text18=Label(updatestudentclass_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updatestudentclass_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updatestudentclass_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updatestudentclass_window.destroy)
            exit_button.place(x=280,y=85) 

        def updatestudent_name():
            def data_updated():
                messagebox.showinfo("Student detail", "Student details have been updated successfully")

            def clear_text_entry():
                studentID_entry.delete(0, 'end')    
                newname_entry.delete(0, 'end')

            def query():
                student_IDtofind=studentID_entry.get()
                new_name=newname_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update student_details set student_name=%s where student_id=%s",(new_name,student_IDtofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from student_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updatestudentname_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)
            
            updatestudentname_window=Toplevel()
            updatestudentname_window.title("Update student's name")
            updatestudentname_window.geometry("600x600+250+115")
            updatestudentname_window.resizable(width=False, height=False)

            Text16=Label(updatestudentname_window, text="Enter ID of student to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            studentID_entry=Entry(updatestudentname_window, width=35)
            studentID_entry.place(x=258,y=15)

            Text17=Label(updatestudentname_window, text="Enter new name ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newname_entry=Entry(updatestudentname_window,width=50)
            newname_entry.place(x=150,y=55)

            Text18=Label(updatestudentname_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updatestudentname_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updatestudentname_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updatestudentname_window.destroy)
            exit_button.place(x=280,y=85) 

        def updatestudentID():
            def data_updated():
                messagebox.showinfo("Student detail", "Student details have been updated successfully")

            def clear_text_entry():
                studentname_entry.delete(0, 'end')    
                newID_entry.delete(0, 'end')

            def query():
                student_nametofind=str(studentname_entry.get())
                new_ID=newID_entry.get()
                con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
                cur=con.cursor()
                cur.execute("update student_details set student_id=%s where student_name=%s",(new_ID,student_nametofind))
                con.commit()
                data_updated()
                clear_text_entry()
                cur.execute("select * from student_details;")
                records=cur.fetchall()
                print_records=""
                for record in records:
                    print_records += str(record) + "\n"

                query_label=Label(updatestudentID_window, text=print_records, fg="#61647d", font="Menlo 12")
                query_label.place(x=10,y=180)

            updatestudentID_window=Toplevel()
            updatestudentID_window.title("Update student's ID")
            updatestudentID_window.geometry("600x600+250+115")
            updatestudentID_window.resizable(width=False, height=False)

            Text16=Label(updatestudentID_window, text="Enter name of student to be changed ", font="Menlo 12", fg="#61647d")
            Text16.place(x=10,y=10)

            studentname_entry=Entry(updatestudentID_window, width=35)
            studentname_entry.place(x=278,y=15)

            Text17=Label(updatestudentID_window, text="Enter new ID ", font="Menlo 12", fg="#61647d")
            Text17.place(x=10,y=50)

            newID_entry=Entry(updatestudentID_window,width=50)
            newID_entry.place(x=120,y=55)

            Text18=Label(updatestudentID_window, text="New details will be shown below ", font="Menlo 12", fg="#61647d")
            Text18.place(x=10,y=140)

            enter_button_query_search=Button(updatestudentID_window, text="  Enter ", padx=25, pady=10, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
            enter_button_query_search.place(x=160,y=85)
            
            exit_button=Button(updatestudentID_window, text="Cancel",font="Menlo 12", padx=25, pady=10, fg="#fc5d53", command=updatestudentID_window.destroy)
            exit_button.place(x=280,y=85) 

        updatestudent_window=Toplevel()
        updatestudent_window.title("Update Student Details")
        updatestudent_window.geometry("600x600+250+115")
        updatestudent_window.resizable(width=False, height=False)

        Text15=Label(updatestudent_window, text="Which student detail would you like to update?", font="Menlo 14", fg="#61647d")
        Text15.place(x=120,y=10)

        #ID
        IDbtn1=Button(updatestudent_window, text="    ID Number     ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updatestudentID)
        IDbtn1.place(x=195,y=50)

        #Name
        Name_btn=Button(updatestudent_window, text="        Name         ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updatestudent_name)
        Name_btn.place(x=195,y=140)

        #Class
        Class_btn=Button(updatestudent_window, text="        Class          ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updatestudent_Class)
        Class_btn.place(x=195,y=230)

        #Contact number
        Contact_btn=Button(updatestudent_window, text="Contact Number", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updatestudent_Contact)
        Contact_btn.place(x=195,y=320)

        #Net Bill
        Bill_btn=Button(updatestudent_window, text="       Net Bill         ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=updatestudent_Bill)
        Bill_btn.place(x=195,y=410)

        #Exit
        exit_button=Button(updatestudent_window, text="          Exit           ",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=updatestudent_window.destroy)
        exit_button.place(x=195,y=500)

    Update_details_window=Toplevel()
    Update_details_window.title("Update details")
    Update_details_window.geometry("600x500+250+115")
    Update_details_window.resizable(width=False, height=False)

    Text14=Label(Update_details_window, text="What would you like to update details for?", font="Menlo 14", fg="#61647d")
    Text14.place(x=125,y=20)

    update_student_details_btn=Button(Update_details_window, text="Update Student Details", padx=25, pady=25,font="Menlo 12" ,fg="#61647d", command=updatestudentdetails)
    update_student_details_btn.place(x=195,y=70)

    update_worker_details_btn=Button(Update_details_window, text="Update Worker Details", padx=25, pady=25,font="Menlo 12" ,fg="#61647d", command=updateworkerdetails)
    update_worker_details_btn.place(x=195,y=160)

    update_product_details_btn=Button(Update_details_window, text="Update Product Details", padx=25, pady=25,font="Menlo 12" ,fg="#61647d", command=updateproductdetails)
    update_product_details_btn.place(x=195,y=250)

    exit_button=Button(Update_details_window, text="                  Exit                ",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=Update_details_window.destroy)
    exit_button.place(x=195,y=340)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#View Details Window
def open_view_window():

    def viewallproduct_details():
        viewallproduct_details_window=Toplevel()
        viewallproduct_details_window.title("Viewing all products records")
        viewallproduct_details_window.geometry("600x500+250+115")
        viewallproduct_details_window.resizable(width=False, height=False)

        Text13=Label(viewallproduct_details_window, text="Records will be displayed below (if any)", font="Menlo 14", fg="#61647d")
        Text13.place(x=10,y=15)

        con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
        cur=con.cursor()
        cur.execute('select * from product_details order by product_name ASC;')
        records=cur.fetchall()
        print_records=""
        for record in records:
            print_records+= str(record) + "\n"
        
        allproduct_label=Label(viewallproduct_details_window, text=print_records, fg="#61647d", font="Menlo 12" )
        allproduct_label.place(x=30,y=50)

        exit_button=Button(viewallproduct_details_window, text="Exit",font="Menlo 12", padx=50, pady=25, fg="#fc5d53", command=viewallproduct_details_window.destroy)
        exit_button.place(x=450,y=10)

    def viewallworker_details():
        viewallworker_details_window=Toplevel()
        viewallworker_details_window.title("Viewing all workers records")
        viewallworker_details_window.geometry("600x500+250+115")
        viewallworker_details_window.resizable(width=False, height=False)
        Text13=Label(viewallworker_details_window, text="Records will be displayed below (if any)", font="Menlo 14", fg="#61647d")
        Text13.place(x=10,y=15)
        con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
        cur=con.cursor()
        cur.execute('select * from worker_details order by worker_name ASC;')
        records=cur.fetchall()
        print_records=""
        for record in records:
            print_records+= str(record) + "\n"
        allworker_label=Label(viewallworker_details_window, text=print_records, fg="#61647d", font="Menlo 12" )
        allworker_label.place(x=30,y=50)

        exit_button=Button(viewallworker_details_window, text="Exit",font="Menlo 12", padx=50, pady=25, fg="#fc5d53", command=viewallworker_details_window.destroy)
        exit_button.place(x=450,y=10)

    def viewallstudent_details():
        viewallstudent_details_window=Toplevel()
        viewallstudent_details_window.title("Viewing all students records")
        viewallstudent_details_window.geometry("600x500+250+115")
        viewallstudent_details_window.resizable(width=False, height=False)

        Text13=Label(viewallstudent_details_window, text="Records will be displayed below (if any)", font="Menlo 14", fg="#61647d", )
        Text13.place(x=10,y=15)

        con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
        cur=con.cursor()
        cur.execute('select * from student_details order by student_name ASC;')
        records=cur.fetchall()
        print_records=""
        for record in records:
            print_records+= str(record) + "\n"
        allstudent_label=Label(viewallstudent_details_window, text=print_records, fg="#61647d", font="Menlo 12" )
        allstudent_label.place(x=30,y=50)

        exit_button=Button(viewallstudent_details_window, text="Exit",font="Menlo 12", padx=50, pady=25, fg="#fc5d53", command=viewallstudent_details_window.destroy)
        exit_button.place(x=450,y=10)

    def viewsingleproduct_details():
        def query():
            productcode_tofind=productcode_tofind_entry.get()
            con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
            cur=con.cursor()
            cur.execute("select * from product_details where product_code=%s;",(productcode_tofind,))
            records=cur.fetchall()
            print_records=""
            for record in records:
                print_records+= str(record) + "\n"

            query_label=Label(viewsingleproduct_details_window, text=print_records, fg="#61647d", font="Menlo 12")
            query_label.place(x=10,y=90)

        viewsingleproduct_details_window=Toplevel()
        viewsingleproduct_details_window.title("Viewing single product's record")
        viewsingleproduct_details_window.geometry("600x500+250+115")
        viewsingleproduct_details_window.resizable(width=False, height=False)

        enter_code_number=Label(viewsingleproduct_details_window, text="Enter product code ", font="Menlo 14", fg="#61647d")
        enter_code_number.place(x=10,y=10)

        productcode_tofind_entry=Entry(viewsingleproduct_details_window, width=25)
        productcode_tofind_entry.place(x=185,y=15)

        Text12=Label(viewsingleproduct_details_window, text="Record will be displayed below (if found)", font="Menlo 13", fg="#61647d")
        Text12.place(x=10,y=60)

        enter_button_query_search=Button(viewsingleproduct_details_window, text=" Enter ", padx=25, pady=25, bg="#3a7ff6", fg="#e5fafe", font="Menlo 12", command=query)
        enter_button_query_search.place(x=360,y=10)

        exit_button=Button(viewsingleproduct_details_window, text="Cancel",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=viewsingleproduct_details_window.destroy)
        exit_button.place(x=475,y=10)

    def viewsingleworker_details():
        def query():
            workerid_tofind=workerid_tofind_entry.get()
            con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
            cur=con.cursor()
            cur.execute("select * from worker_details where worker_id=%s;",(workerid_tofind,))
            records=cur.fetchall()
            print_records=""
            for record in records:
                print_records+= str(record) + "\n"

            query_label=Label(viewsingleworker_details_window, text=print_records, fg="#61647d", font="Menlo 12")
            query_label.place(x=10,y=90)

        viewsingleworker_details_window=Toplevel()
        viewsingleworker_details_window.title("Viewing single worker's record")
        viewsingleworker_details_window.geometry("600x500+250+115")
        viewsingleworker_details_window.resizable(width=False, height=False)

        enter_id_number=Label(viewsingleworker_details_window, text="Enter worker id ", font="Menlo 14", fg="#61647d")
        enter_id_number.place(x=10,y=10)

        workerid_tofind_entry=Entry(viewsingleworker_details_window, width=30)
        workerid_tofind_entry.place(x=153,y=15)

        Text11=Label(viewsingleworker_details_window, text="Record will be displayed below (if found)", font="Menlo 13", fg="#61647d")
        Text11.place(x=10,y=60)

        enter_button_query_search=Button(viewsingleworker_details_window, text=" Enter ", padx=25, pady=25, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
        enter_button_query_search.place(x=360,y=10)

        exit_button=Button(viewsingleworker_details_window, text="Cancel",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=viewsingleworker_details_window.destroy)
        exit_button.place(x=475,y=10)

    def viewsinglestudent_details():
        def query():
            studentid_tofind=studentid_tofind_entry.get()
            con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
            cur=con.cursor()
            cur.execute("select * from student_details where student_id=%s;",(studentid_tofind,))
            records=cur.fetchall()
            print_records=""
            for record in records:
                print_records+= str(record) + "\n"

            query_label=Label(viewsinglestudent_details_window, text=print_records, fg="#61647d", font="Menlo 12")
            query_label.place(x=10,y=90)

        viewsinglestudent_details_window=Toplevel()
        viewsinglestudent_details_window.title("Viewing single student's record")
        viewsinglestudent_details_window.geometry("600x500+250+115")
        viewsinglestudent_details_window.resizable(width=False, height=False)

        enter_id_number=Label(viewsinglestudent_details_window, text="Enter student id ", font="Menlo 14", fg="#61647d")
        enter_id_number.place(x=10,y=10)

        studentid_tofind_entry=Entry(viewsinglestudent_details_window, width=30)
        studentid_tofind_entry.place(x=153,y=15)

        Text10=Label(viewsinglestudent_details_window, text="Record will be displayed below (if found)", font="Menlo 13", fg="#61647d", )
        Text10.place(x=10,y=60)

        enter_button_query_search=Button(viewsinglestudent_details_window, text=" Enter ", padx=25, pady=25, font="Menlo 12", bg="#3a7ff6", fg="#e5fafe", command=query)
        enter_button_query_search.place(x=360,y=10)

        exit_button=Button(viewsinglestudent_details_window, text="Cancel",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=viewsinglestudent_details_window.destroy)
        exit_button.place(x=475,y=10) 

    View_details_window=Toplevel()
    View_details_window.title("View details")
    View_details_window.geometry("600x500+250+115")
    View_details_window.resizable(width=False, height=False)

    Text6=Label(View_details_window, text="What would you like to view details for?", font="Menlo 14", fg="#61647d")
    Text6.place(x=125,y=30)

    #View single student
    viewsinglestudent_details_btn=Button(View_details_window, text="View One Student's Details", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=viewsinglestudent_details)
    viewsinglestudent_details_btn.place(x=10,y=90)

    #View single worker
    viewsingleworker_details_btn=Button(View_details_window, text="View One Worker's Details ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=viewsingleworker_details)
    viewsingleworker_details_btn.place(x=10,y=200)

    #View single product
    viewsingleproduct_details_btn=Button(View_details_window, text="View One Product's Details", padx=24, pady=25, font="Menlo 12", fg="#61647d", command=viewsingleproduct_details)
    viewsingleproduct_details_btn.place(x=10,y=310)

    #View all student 
    viewallstudent_details_btn=Button(View_details_window, text="View All Student's Details   ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=viewallstudent_details)
    viewallstudent_details_btn.place(x=310,y=90)

    #View all worker
    viewallworker_details_btn=Button(View_details_window, text="View All Worker's Details    ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=viewallworker_details)
    viewallworker_details_btn.place(x=310,y=200)

    #View all product
    viewallproduct_details_btn=Button(View_details_window, text="View All Product's Details   ", padx=24, pady=25, font="Menlo 12", fg="#61647d", command=viewallproduct_details)
    viewallproduct_details_btn.place(x=310,y=310)

    exit_button=Button(View_details_window, text="              Exit              ",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=View_details_window.destroy)
    exit_button.place(x=200,y=410)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Enter Details Window
def open_entry_window():

    def open_enter_product_details_window():
        con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
        cur=con.cursor()
        try:
            cur.execute('create table product_details(product_code int(9),product_name varchar(25), product_prod varchar(25), product_unit int(4), product_uncost float(3))')
            
        except:
            print("Retrieving Tables...")

        def data_entered():
            messagebox.showinfo("Product detail", "Product Details have been Entered into Database")

        def clear_text_entry():
            product_code_entry.delete(0, 'end')    
            product_name_entry.delete(0, 'end')
            product_prod_entry.delete(0, 'end')
            product_unit_entry.delete(0, 'end')
            product_uncost_entry.delete(0, 'end')

        def enter_product_sql():
            #Retrieving values from entry box
            product_code=int(product_code_entry.get())
            product_name=str(product_name_entry.get())
            product_prod=str(product_prod_entry.get())
            product_unit=int(product_unit_entry.get())
            product_uncost=float(product_uncost_entry.get())
            cur.execute("Insert into product_details values (%s,%s,%s,%s,%s);",(product_code, product_name, product_prod, product_unit, product_uncost))
            con.commit()
            data_entered()
            clear_text_entry()
        
        enter_product_details_window=Toplevel()
        enter_product_details_window.title("Product details")
        enter_product_details_window.geometry("600x500+250+115")
        enter_product_details_window.resizable(width=False, height=False)
        
        Text9=Label(enter_product_details_window, text="Please enter the details of the product below", font="Menlo 14", fg="#61647d")
        Text9.place(x=125,y=30)

        #Product code 
        product_code_entry=Entry(enter_product_details_window, width=30)
        product_code_entry.place(x=250,y=73)

        product_code=Label(enter_product_details_window, text="Enter Product's Code ", font="Menlo 12",fg="#61647d")
        product_code.place(x=10, y=73)

        #Product Name
        product_name_entry=Entry(enter_product_details_window, width=30)
        product_name_entry.place(x=250,y=133)

        product_name=Label(enter_product_details_window, text="Enter Product's Name ", font="Menlo 12", fg="#61647d")
        product_name.place(x=10, y=133)

        #Product producer
        product_prod_entry=Entry(enter_product_details_window, width=30)
        product_prod_entry.place(x=250,y=193)

        product_prod=Label(enter_product_details_window, text="Enter Product's Producer ", font="Menlo 12", fg="#61647d")
        product_prod.place(x=10, y=193)

        #Product unit
        product_unit_entry=Entry(enter_product_details_window, width=30)
        product_unit_entry.place(x=250,y=253)

        product_unit=Label(enter_product_details_window, text="Enter Product's unit(s) ", font="Menlo 12", fg="#61647d")
        product_unit.place(x=10, y=253)

        #product unit price
        product_uncost_entry=Entry(enter_product_details_window, width=30)
        product_uncost_entry.place(x=250,y=313)

        product_uncost=Label(enter_product_details_window, text="Enter Product's unit cost ", font="Menlo 12", fg="#61647d")
        product_uncost.place(x=10, y=313)

        Enter_btn=Button(enter_product_details_window, text="Enter",font="Menlo 12", padx=50, pady=10, bg="#3a7ff6", fg="#e5fafe", command=enter_product_sql)
        Enter_btn.place(x=75,y=400)

        exit_button=Button(enter_product_details_window, text="Cancel",font="Menlo 12", padx=50, pady=10, fg="#fc5d53", command=enter_product_details_window.destroy)
        exit_button.place(x=275,y=400)

    def open_enter_worker_details_window():
        con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
        cur=con.cursor()
        try:
            cur.execute('create table worker_details(worker_id int(6),worker_name varchar(25),worker_shift varchar(10),contact_no int(13))')
                
        except:
            print("Retrieving Tables...")

        def data_entered():
            messagebox.showinfo("Worker detail", "Worker Details have been Entered into Database")

        def clear_text_entry():
            worker_id_entry.delete(0, 'end')    
            worker_name_entry.delete(0, 'end')
            worker_shift_entry.delete(0, 'end')
            worker_contact_entry.delete(0, 'end')


        def enter_worker_sql():
            #Retrieving values from entry box
            worker_id=int(worker_id_entry.get())
            worker_name=str(worker_name_entry.get())
            worker_shift=str(worker_shift_entry.get())
            worker_contact=int(worker_contact_entry.get())
            cur.execute("Insert into worker_details values(%s,%s,%s,%s);",(worker_id, worker_name, worker_shift, worker_contact,))
            con.commit()
            data_entered()
            clear_text_entry()
        
        enter_worker_details_window=Toplevel()
        enter_worker_details_window.title("Worker details")
        enter_worker_details_window.geometry("600x500+250+115")
        enter_worker_details_window.resizable(width=False, height=False)
        
        Text8=Label(enter_worker_details_window, text="Please enter the details of the worker below", font="Menlo 14", fg="#61647d")
        Text8.place(x=125,y=30)

        #Worker ID number
        worker_id_entry=Entry(enter_worker_details_window, width=30)
        worker_id_entry.place(x=250,y=73)

        worker_id=Label(enter_worker_details_window, text="Enter Worker's I.D Number ", font="Menlo 12", fg="#61647d")
        worker_id.place(x=10, y=73)

        #Worker Name
        worker_name_entry=Entry(enter_worker_details_window, width=30)
        worker_name_entry.place(x=250,y=133)

        worker_name=Label(enter_worker_details_window, text="Enter Worker's Name ", font="Menlo 12", fg="#61647d")
        worker_name.place(x=10, y=133)

        #Worker Shift
        worker_shift_entry=Entry(enter_worker_details_window, width=30)
        worker_shift_entry.place(x=250,y=193)

        worker_shift=Label(enter_worker_details_window, text="Enter Worker's Shift ", font="Menlo 12", fg="#61647d")
        worker_shift.place(x=10, y=193)

        #Worker Contact Number
        worker_contact_entry=Entry(enter_worker_details_window, width=30)
        worker_contact_entry.place(x=250,y=253)

        worker_contact=Label(enter_worker_details_window, text="Enter Worker's Contact Number ", font="Menlo 12", fg="#61647d")
        worker_contact.place(x=10, y=253)

        Enter_btn=Button(enter_worker_details_window, text="Enter",font="Menlo 12", padx=50, pady=10, bg="#3a7ff6", fg="#e5fafe", command=enter_worker_sql)
        Enter_btn.place(x=75,y=400)

        exit_button=Button(enter_worker_details_window, text="Cancel",font="Menlo 12", padx=50, pady=10, fg="#fc5d53", command=enter_worker_details_window.destroy)
        exit_button.place(x=275,y=400)

    def open_enter_student_details_window():
        con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
        cur=con.cursor()
        try:
            cur.execute('create table student_details(student_id int(6), student_name varchar(25),student_class varchar(6),contact_no int(13),net_bill float(10))')
                
        except:
            print("Retrieving Tables...")

        def data_entered():
            messagebox.showinfo("Student detail", "Student Details have been Entered into Database")

        def clear_text_entry():
            student_id_entry.delete(0, 'end')    
            student_name_entry.delete(0, 'end')
            student_class_entry.delete(0, 'end')
            student_contact_entry.delete(0, 'end')
            student_net_bill_entry.delete(0, 'end')


        def enter_student_sql():
            #Retrieving values from entry box
            student_id=int(student_id_entry.get())
            student_name=str(student_name_entry.get())
            student_class=str(student_class_entry.get())
            student_contact=int(student_contact_entry.get())
            student_netbill=float(student_net_bill_entry.get())
            cur.execute("Insert into student_details values (%s,%s,%s,%s,%s);",(student_id, student_name, student_class, student_contact, student_netbill))
            con.commit()
            data_entered()
            clear_text_entry()
        
        enter_student_details_window=Toplevel()
        enter_student_details_window.title("Student details")
        enter_student_details_window.geometry("600x500+250+115")
        enter_student_details_window.resizable(width=False, height=False)
        
        Text7=Label(enter_student_details_window, text="Please enter the details of the student below", font="Menlo 14", fg="#61647d")
        Text7.place(x=125,y=30)

        #Student ID number
        student_id_entry=Entry(enter_student_details_window, width=30)
        student_id_entry.place(x=250,y=73)

        student_id=Label(enter_student_details_window, text="Enter Student's I.D Number ", font="Menlo 12", fg="#61647d")
        student_id.place(x=10, y=73)

        #Student Name
        student_name_entry=Entry(enter_student_details_window, width=30)
        student_name_entry.place(x=250,y=133)

        student_name=Label(enter_student_details_window, text="Enter Student's Name:", font="Menlo 12", fg="#61647d")
        student_name.place(x=10, y=133)

        #Student Class
        student_class_entry=Entry(enter_student_details_window, width=30)
        student_class_entry.place(x=250,y=193)

        student_class=Label(enter_student_details_window, text="Enter Student's Class ", font="Menlo 12", fg="#61647d")
        student_class.place(x=10, y=193)

        #Student Contact Number
        student_contact_entry=Entry(enter_student_details_window, width=30)
        student_contact_entry.place(x=250,y=253)

        student_contact=Label(enter_student_details_window, text="Enter Student's Contact Number ", font="Menlo 12", fg="#61647d")
        student_contact.place(x=10, y=253)

        #Student Net Bill
        student_net_bill_entry=Entry(enter_student_details_window, width=30)
        student_net_bill_entry.place(x=250,y=313)

        student_net_bill=Label(enter_student_details_window, text="Enter Student's Net Bill:", font="Menlo 12", fg="#61647d")
        student_net_bill.place(x=10, y=313)

        Enter_btn=Button(enter_student_details_window, text="Enter",font="Menlo 12", padx=50, pady=10, bg="#3a7ff6", fg="#e5fafe", command=enter_student_sql)
        Enter_btn.place(x=75,y=400)

        exit_button=Button(enter_student_details_window, text="Cancel",font="Menlo 12", padx=50, pady=10, fg="#fc5d53", command=enter_student_details_window.destroy)
        exit_button.place(x=275,y=400)

    Entry_details_window=Toplevel()
    Entry_details_window.title("Enter Details")
    Entry_details_window.geometry("600x450+250+115")
    Entry_details_window.resizable(width=False, height=False)

    Text6=Label(Entry_details_window, text="For what would you like to enter details for?", font="Menlo 14", fg="#61647d")
    Text6.place(x=125,y=30)

    Enter_studentdetails_btn=Button(Entry_details_window, text="Enter Student Details", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=open_enter_student_details_window)
    Enter_studentdetails_btn.place(x=195,y=70)

    Enter_workerdetails_btn=Button(Entry_details_window, text="Enter Worker Details ", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=open_enter_worker_details_window)
    Enter_workerdetails_btn.place(x=195,y=160)

    Enter_productdetails_btn=Button(Entry_details_window, text="Enter Product Details", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=open_enter_product_details_window)
    Enter_productdetails_btn.place(x=195,y=250)

    exit_button=Button(Entry_details_window, text="                Exit               ",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=Entry_details_window.destroy)
    exit_button.place(x=195,y=340)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Main Menu
def open_main_menu():
    MainMenu_window = Toplevel()
    MainMenu_window.title("Main Menu")
    MainMenu_window.geometry("800x200+250+115")
    MainMenu_window.resizable(width=False, height=False)

    Text5=Label(MainMenu_window, text="Welcome to Canteen Management System", font="Menlo 14", fg="#61647d")
    Text5.place(x=200,y=10)

    Enterdetails_btn=Button(MainMenu_window, text="Enter Details", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=open_entry_window)
    Enterdetails_btn.place(x=20,y=70)

    Viewdetails_btn=Button(MainMenu_window, text="View Details", padx=25, pady=25,font="Menlo 12", fg="#61647d", command=open_view_window)
    Viewdetails_btn.place(x=180,y=70)

    Updatedetails_btn=Button(MainMenu_window, text="Update Details", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=open_update_window)
    Updatedetails_btn.place(x=340,y=70)

    Deletedetails_btn=Button(MainMenu_window, text="Delete Details", padx=25, pady=25, font="Menlo 12", fg="#61647d", command=open_delete_window)
    Deletedetails_btn.place(x=515,y=70)

    exit_button=Button(MainMenu_window, text="Exit",font="Menlo 12", padx=25, pady=25, fg="#fc5d53", command=MainMenu_window.destroy)
    exit_button.place(x=685,y=70)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Login Window
def open_login():
    def get_userandpass():
        entered_username = username_entry.get()
        entered_password = password_entry.get()
        if entered_username=="User1" and entered_password=="1234":
            cur=con.cursor()
            open_main_menu()

    login_window = Toplevel()
    login_window.title("Login")
    login_window.geometry("800x300+250+115")
    login_window.resizable(width=False, height=False)

    about_cms_frame=LabelFrame(login_window, text="About Canteen Management System", font="Menlo 12 bold" , bg="#3a7ff6", fg="#e5fafe", width=350, height=500)
    about_cms_frame.place(x=0,y=0)

    Textcms=Label(about_cms_frame,
                  text="Canteen Management is a python based system \nbuilt using databases stored on MySQL \n with a graphical user interface built using \n tkinter.",
                  font="Menlo 10", fg="#e5fafe", bg="#3a7ff6")
    Textcms.place(x=10,y=20)

    Textcoder=Label(about_cms_frame, text="Built by Mohd Mawiz", font="Menlo 10", fg="#e5fafe", bg="#3a7ff6")
    Textcoder.place(x=10,y=250)

    Text2=Label(login_window, text="Login", font="Menlo 14 bold", fg="#61647d")
    Text2.place(x=400,y=10)

    Text3=Label(login_window, text="Username", font="Menlo 12", fg="#61647d")
    Text3.place(x=400,y=50)

    username_entry=Entry(login_window, width=40)
    username_entry.place(x=487,y=53)
    username_entry.get()

    Text4=Label(login_window, text="Password", font="Menlo 12", fg="#61647d")
    Text4.place(x=400,y=100)

    password_entry=Entry(login_window, width=40)
    password_entry.place(x=487,y=103)

    Enter_btn=Button(login_window, text="Enter",font="Menlo 12", padx=50, pady=10, command=get_userandpass, bg="#3a7ff6", fg="#e5fafe")
    Enter_btn.place(x=408,y=140)
    exit_button=Button(login_window, text="Cancel",font="Menlo 12", padx=50, pady=10, fg="#fc5d53", command=login_window.destroy)
    exit_button.place(x=570,y=140)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Starter window
def open_main_window():
    main_window=tk.Tk()
    main_window.title("Canteen Management System")
    main_window.geometry("1000x600+250+115")
    main_window.resizable(width=False, height=False)

    Text0=Label(main_window, text="CONNECTION ESTABLISHED", font="Menlo 14 bold", fg="#61647d")
    Text0.place(x=10,y=10)

    Text1=Label(main_window, text="Welcome to Canteen Management System", font="Menlo 14 bold", fg="#61647d")
    Text1.place(x=10, y=35)

    login_button=Button(main_window, text="Login",font="Menlo 12", padx=50, pady=50, fg="#61647d", command=open_login)
    login_button.place(x=250, y=250)

    exit_button=Button(main_window, text="Exit",font="Menlo 12", padx=50, pady=50, fg="#fc5d53", command=main_window.destroy)
    exit_button.place(x=500,y=250)

    main_window.mainloop()

#Python connectivity to MySQL
con=mc.connect(host='localhost',user='root',password='1234',database='CanteenManagement')
if con.is_connected():
    open_main_window()
cur=con.cursor()
