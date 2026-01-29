class EmployeeAuthentication:

    def __init__(self, db):
        self.db = db

    def createEmployee(self, name, email, password):
        return self.db.createEMP(name, email, password)

    def empLogin(self, email):
        return self.db.searchEMP(email)
