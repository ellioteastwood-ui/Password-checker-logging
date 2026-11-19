import hashlib

import logging

 

 

def passchecker():

 

    logging.basicConfig(

        filename="security.log",

        level=logging.INFO,

        format="%(asctime)s - %(levelname)s - %(message)s"

    )

 

    logging.info("Program started")

 

    U = "Admin"

    P = "Password123"

    C = 3

    Y = 0

 

    hashed_password = hashlib.sha256(P.encode()).hexdigest()

 

    while C > 0:

        UA = input("Username: ")

        PA = input("Password: ")

 

        hashed_attempt = hashlib.sha256(PA.encode()).hexdigest()

 

        if UA.upper().strip() == U.upper().strip() and hashed_password == hashed_attempt:

 

            print("Access granted in", Y + 1, "attempts")

 

            logging.info(f"Successful login for: {UA}")

 

            break

 

        else:

            Y += 1

            C -= 1

 

            print("Incorrect details,", 3 - Y, "attempts remaining")

 

            logging.warning(f"Failed login attempt for: {UA}")

 

    if C == 0:

        print("Account locked")

 

        logging.critical(f"Account locked after 3 failed attempts for: {UA}")

 

 

passchecker()
