import json, os
from datetime import date, datetime, timedelta
from models import Member, Trainer, Membership, Payment, Attendance

class Gym:
    def __init__(self):
        self.file = "gym_data.json"
        self.members, self.trainers, self.memberships = [], [], []
        self.payments, self.attendances = [], []
        self.load()

    def load(self):
        if not os.path.exists(self.file): 
            return
        with open(self.file, "r") as f:
            data = json.load(f)
            self.members = [Member(**m) for m in data.get("members", [])]
            self.trainers = [Trainer(**t) for t in data.get("trainers", [])]
            self.memberships = [Membership(**m) for m in data.get("memberships", [])]
            self.payments = [Payment(**p) for p in data.get("payments", [])]
            self.attendances = [Attendance(**a) for a in data.get("attendances", [])]

    def save(self):
        data = {
            "members": [vars(m) for m in self.members],
            "trainers": [vars(t) for t in self.trainers],
            "memberships": [vars(m) for m in self.memberships],
            "payments": [vars(p) for p in self.payments],
            "attendances": [vars(a) for a in self.attendances]
        }
        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)

    def gen_id(self, prefix, lst):
        # دالة بسيطة لعمل ID جديد
        return f"{prefix}{len(lst) + 1:03d}"

    def add_member(self, name, phone, trainer_id=""):
        if not name or not phone: 
            raise ValueError("Name and phone are required!")
        new_id = self.gen_id("M", self.members)
        self.members.append(Member(new_id, name, phone, trainer_id))
        self.save()

    def add_trainer(self, name, phone, specialty):
        new_id = self.gen_id("T", self.trainers)
        self.trainers.append(Trainer(new_id, name, phone, specialty))
        self.save()

    def create_membership(self, m_id, m_type):
        prices = {"Monthly": (30, 300), "Quarterly": (90, 800), "Annual": (365, 2800)}
        if m_type not in prices: 
            raise ValueError("Type must be Monthly, Quarterly, or Annual")
        
        days, price = prices[m_type]
        start = date.today()
        end = start + timedelta(days=days)
        new_id = self.gen_id("MS", self.memberships)
        
        self.memberships.append(Membership(new_id, m_id, m_type, price, str(start), str(end)))
        self.save()

    def record_payment(self, m_id, amount, method):
        new_id = self.gen_id("P", self.payments)
        self.payments.append(Payment(new_id, m_id, float(amount), str(date.today()), method))
        self.save()

    def record_attendance(self, m_id):
        new_id = self.gen_id("A", self.attendances)
        now = datetime.now()
        self.attendances.append(Attendance(new_id, m_id, str(now.date()), now.strftime("%H:%M")))
        self.save()