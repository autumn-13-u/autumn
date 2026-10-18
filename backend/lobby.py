def lobby():

    choice = input("""
 1. Login
 2. Signup

 Choose an option: """)

    if choice == "1":
        from backend.auth import login#imports login
        import main#imports main

        username = login.login()
        main.autumn(username)

    elif choice == "2":
     from backend.auth import signup
     signup.signup()
