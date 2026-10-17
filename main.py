import tkinter as tk
from tkinter import ttk, messagebox
from gym import Gym

# دالة مساعدة بسيطة لرسم الجداول
def create_table(parent, cols):
    table = ttk.Treeview(parent, columns=cols, show="headings")
    for c in cols:
        table.heading(c, text=c)
        table.column(c, width=100)
    table.pack(side="right", fill="both", expand=True)
    return table

class App:
    def __init__(self):
        self.gym = Gym()
        self.root = tk.Tk()
        self.root.title("Gym Management System")
        self.root.geometry("800x500")

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        # --- شاشة الأعضاء ---
        tab1 = ttk.Frame(self.tabs)
        self.tabs.add(tab1, text="Members")
        self.m_name = tk.StringVar(); self.m_phone = tk.StringVar(); self.m_trainer = tk.StringVar()
        self.build_inputs(tab1, ["Name", "Phone", "Trainer ID"], [self.m_name, self.m_phone, self.m_trainer], self.add_member)
        self.tbl_members = create_table(tab1, ["ID", "Name", "Phone", "Trainer ID"])

        # --- شاشة المدربين ---
        tab2 = ttk.Frame(self.tabs)
        self.tabs.add(tab2, text="Trainers")
        self.t_name = tk.StringVar(); self.t_phone = tk.StringVar(); self.t_spec = tk.StringVar()
        self.build_inputs(tab2, ["Name", "Phone", "Specialty"], [self.t_name, self.t_phone, self.t_spec], self.add_trainer)
        self.tbl_trainers = create_table(tab2, ["ID", "Name", "Phone", "Specialty"])

        # --- شاشة الاشتراكات ---
        tab3 = ttk.Frame(self.tabs)
        self.tabs.add(tab3, text="Memberships")
        self.ms_member = tk.StringVar(); self.ms_type = tk.StringVar()
        self.build_inputs(tab3, ["Member ID", "Type"], [self.ms_member, self.ms_type], self.add_ms)
        self.tbl_ms = create_table(tab3, ["ID", "Member ID", "Type", "Price", "Start", "End"])

        # --- شاشة الدفع ---
        tab4 = ttk.Frame(self.tabs)
        self.tabs.add(tab4, text="Payments")
        self.p_member = tk.StringVar(); self.p_amount = tk.StringVar(); self.p_method = tk.StringVar()
        self.build_inputs(tab4, ["Member ID", "Amount", "Method"], [self.p_member, self.p_amount, self.p_method], self.add_payment)
        self.tbl_payments = create_table(tab4, ["ID", "Member", "Amount", "Date", "Method"])

        # --- شاشة الحضور ---
        tab5 = ttk.Frame(self.tabs)
        self.tabs.add(tab5, text="Attendance")
        self.a_member = tk.StringVar()
        self.build_inputs(tab5, ["Member ID"], [self.a_member], self.add_attendance)
        self.tbl_att = create_table(tab5, ["ID", "Member", "Date", "Time"])

        self.refresh()

    def build_inputs(self, parent, labels, variables, cmd):
        f = ttk.Frame(parent)
        f.pack(side="left", fill="y", padx=10, pady=10)
        for lbl, var in zip(labels, variables):
            ttk.Label(f, text=lbl).pack(anchor="w")
            ttk.Entry(f, textvariable=var).pack(pady=2)
        ttk.Button(f, text="Add", command=cmd).pack(pady=10)

    def refresh(self):
        # تحديث بيانات الجداول
        tables_data = [
            (self.tbl_members, self.gym.members),
            (self.tbl_trainers, self.gym.trainers),
            (self.tbl_ms, self.gym.memberships),
            (self.tbl_payments, self.gym.payments),
            (self.tbl_att, self.gym.attendances)
        ]
        for tbl, data in tables_data:
            tbl.delete(*tbl.get_children())
            for item in data:
                tbl.insert("", "end", values=list(vars(item).values()))

    # --- دوال الأزرار ---
    def add_member(self):
        try: 
            self.gym.add_member(self.m_name.get(), self.m_phone.get(), self.m_trainer.get())
            self.refresh()
        except Exception as e: messagebox.showerror("Error", str(e))

    def add_trainer(self):
        try: 
            self.gym.add_trainer(self.t_name.get(), self.t_phone.get(), self.t_spec.get())
            self.refresh()
        except Exception as e: messagebox.showerror("Error", str(e))

    def add_ms(self):
        try: 
            self.gym.create_membership(self.ms_member.get(), self.ms_type.get())
            self.refresh()
        except Exception as e: messagebox.showerror("Error", str(e))

    def add_payment(self):
        try: 
            self.gym.record_payment(self.p_member.get(), self.p_amount.get(), self.p_method.get())
            self.refresh()
        except Exception as e: messagebox.showerror("Error", str(e))

    def add_attendance(self):
        try: 
            self.gym.record_attendance(self.a_member.get())
            self.refresh()
        except Exception as e: messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    App().root.mainloop()