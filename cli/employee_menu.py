def employeeSignup():
    print("Employee Signup")

    name = input("Enter username: ")
    if emp_db.user_exists_by_name(name):
        print("❌ Username already exists")
        return

    email = input("Enter email: ")
    if not email_vali(email=email):
        print("❌ Invalid email format")
        return

    if emp_db.user_exists_by_email(email):
        print("❌ Email already registered")
        return

    password = getpass("Enter password: ")
    confirm = getpass("Confirm password: ")

    if password != confirm:
        print("❌ Passwords do not match")
        return

    if not password_vali(password):
        print("❌ Weak password")
        return

    hashed = password_hasher(password)
    emp_auth.createEmployee(name, email, hashed)

    print("✅ Signup successful")
