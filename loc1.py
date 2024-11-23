import geocoder
import smtplib
import beepy
import time
import winsound
from datetime import datetime

#-> beep
# Frequency and duration of the beep
frequency = 1000  # Frequency in Hertz
duration = 2000    # Duration in milliseconds
# Make a beep sound

end_time = time.time() + 5
# <- beep

# Function to get current location
def get_current_location():
    g = geocoder.ip('me')  # Uses your IP address to get an approximate location
    return g.latlng

# Function to create a Google Maps URL
def create_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps?q={latitude},{longitude}"

# Function to send an email with the location link
def send_email(subject, body, to_email):
    from_email = "dheerajvarshney74@gmail.com"
    from_password = "covy hwpu izhi ufgp"
    
    # Set up the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Replace with your SMTP server and port
    server.starttls()
    server.login(from_email, from_password)
    
    # Create the email
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(from_email, to_email, message)
    server.quit()

def send(text):
    coordinates = get_current_location()
    
    if coordinates:
        latitude, longitude = coordinates
        google_maps_link = create_google_maps_link(latitude, longitude)
        # print(f"Google Maps Link: {google_maps_link}")
        
        # Email details
        current_time = datetime.now()
        subject = f"Your Vehicle {text} Found At This Location on {current_time.strftime('%H:%M:%S')}"
        body = f"Here is your vehicle current location: {google_maps_link}"
        to_email = "dheerajvarshney20@gmail.com"
        
        # Send the email
        send_email(subject, body, to_email)
        # print("Email with Google Maps link sent successfully!")
    else:
        print("Unable to retrieve location.")

# ## <- testing 
# nump = "UP81BX6915"
# num = "UP81BX6915"
# ## -> testing 

# # Main program
# if nump==num:
#     while time.time() < end_time:
#         beepy.beep(sound=1)
#     send()
        
