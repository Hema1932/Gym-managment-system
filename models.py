class Member:
    def __init__(self, m_id, name, phone, trainer_id=""):
        self.member_id = m_id
        self.name = name
        self.phone = phone
        self.trainer_id = trainer_id

class Trainer:
    def __init__(self, t_id, name, phone, specialty):
        self.trainer_id = t_id
        self.name = name
        self.phone = phone
        self.specialty = specialty

class Membership:
    def __init__(self, ms_id, m_id, m_type, price, start, end):
        self.membership_id = ms_id
        self.member_id = m_id
        self.type = m_type
        self.price = price
        self.start_date = start
        self.end_date = end

class Payment:
    def __init__(self, p_id, m_id, amount, p_date, method):
        self.payment_id = p_id
        self.member_id = m_id
        self.amount = amount
        self.date = p_date
        self.method = method

class Attendance:
    def __init__(self, a_id, m_id, a_date, time):
        self.attendance_id = a_id
        self.member_id = m_id
        self.date = a_date
        self.time = time