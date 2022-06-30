# otp-verification
Overview


OTP verification with the help of twilio API

step to run the program:

1: install few packeges:
        1. pip install twilio
        2. pip install pyotp
        3. pip install timeit

2. run in vsc or any editor of your choice 
Note: Python 3 or anaconda should be install on your system

About

the project is all about MFA (Multifactor Authentication). its a module for MFA project which i'll make in future.
this module uses twilio rest API for sending OTP to user and uses pyotp's TOTP i.e time-based-OTP, which is an extenstion HOTP 
i.e, HMAC-based One-time Password.

The HOTP algorithm is based on an increasing counter value and a static symmetric key known only to the token and the validation
service.  In order to create the HOTP value, we will use the HMAC-SHA-1 algorithm.

Time-based OTP (TOTP for short), is based on HOTP but where the moving factor is time instead of the counter.
TOTP uses time in increments called the timestep, which is usually 30 or 60 seconds. This means that each OTP is valid for the duration of the timestep.
that ensures the secrecy of the one time Password.
