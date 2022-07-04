import pyotp # imporing potp library
from twilio.rest import Client # importing Client function from the twilio rest API
from timeit import default_timer as timer # importing timer function from the timeit library

# Provide ssid and Authentication token of twilio rest API
acc_ssid = "" # place your ssid here which you'll get from twilio website dashboard
auth_token = "" # place your authentication token here which you'll get from twilio website dashboard

client =  Client(acc_ssid,auth_token)

key = pyotp.random_base32() # generating base32 encryption using the pyotp library where SHA1 is used
otp = pyotp.TOTP(key) # creation of OTP using TOTP i.e time otp which will change in specific time interval 
current_otp = otp.now() # getting the current otp

# function to verify the OTP entered by the user
def verification(time_gap, entered_otp, new_otp, otp):
    if (time_gap)<30 and (entered_otp==new_otp): # the default time gap is 30 sec so waiting for 30 sec
        print("OTP Successfully Verified")

        # this will trigger the twilio API to send the confirmation message that the OTP is verified
        client.messages \
                .create(
                     body="OTP Verified Succsessfully",
                     from_='place the no. which you will get from twilio',
                     to='place the reciever no.'
                 )
        return
    elif (time_gap)<30 and (entered_otp!=new_otp):
        print("Entered OTP is not Verified, Sending you a new OTP")
        resend_otp(otp)
    elif (time_gap)>=30:
        print("Time's up!!!!")
        resend_otp(otp)

# resend_otp() :If the user inputs wrong otp or the time expires the function will send another OTP to the user
def resend_otp(otp):
    current_otp = otp.now()
    while True:
        new_current_otp = otp.now()
        if new_current_otp!=current_otp:
            print(f'Curent_otp : {new_current_otp}')
            # triggers the API and sends the new OTP
            client.messages \
                .create(
                     body=f"Your OTP is {new_current_otp}",
                     from_='place the no. which you will get from twilio',
                     to='place the reciever no.'
                 )
            start = timer() # the timer starts here
            enter_otp = input("Enter current otp : ")
            end = timer() # timer ends here
            resend_time_interval = end-start # evaluation the the time interval after resending the new otp
            print(f'Time taken: {resend_time_interval}')
            verification(resend_time_interval, enter_otp, new_current_otp, otp)
            break
            return

# infinite loop till user gets the otp and enters the otp back
while True:
    new_current_otp = otp.now()
    if new_current_otp !=current_otp:
        print(f'Current_otp: {new_current_otp}')
        #triggers the twilio API and sends very first otp
        client.messages \
                .create(
                     body=f"Your OTP is {new_current_otp}",
                     from_='place the no. which you will get from twilio',
                     to='place the reciever no.'
                 )
        start = timer() # the timer starts here
        enter_otp = input("Enter current_otp : ")
        end = timer() # timer ends here
        time_invl = end-start # evaluation the the time interval for printing the time the user enters the OTP
        print(f"Time taken : {time_invl}") # printing the time interval
        verification(time_invl, enter_otp, new_current_otp, otp) # calling the verification function
        break
