# VfsvisaOnline
<img src="https://www.vfsvisaonline.com/Netherlands-Global-Online-Tracking_Zone1/Image/RO_KN_Logo_Powerpoint_pos_en.png">

## The story behind VfsvisaOnline

June 2020 I needed to renew my passport for several reasons, however the appoinments for the agency were never available and when they were, they were quick to go as the agency told me. Everyday I would check for appointments but no dice. So I decided to automate this in a safe way to notify me of an available appointment ASAP. A month later, I got a notification on my gmail and I quickly booked the appointment!


## What is Vfsvisaonline?

Vfsvisaonline is an *__automated appointment availability*__ scraper.

It works by running every X minutes (time is optional) and navigating through the vfsvisaonline webpage to check if an appointment is available. This method uses chrome driver since the page would not load without JavaScript. To see how to set up this tool and to learn more, check out the tutorial I made:

Click image below!

[![YouTube video](https://img.youtube.com/vi/_VBkdNdnPyA/0.jpg)](https://www.youtube.com/watch?v=_VBkdNdnPyA)

## Usage

__*DISCLAIMER: ONLY WORKS WITH A GMAIL ACCOUNT*__ 

Go to your terminal/command prompt on your local machine:

1. `git clone https://github.com/alpharaoh/vfsvisaonline.git`
2. Install Chrome Driver at: https://chromedriver.chromium.org/downloads<br>
Make sure to drag your Chrome Driver in a safe place where it won't accidentaly get deleted
3. Open the main Python file and scroll down until you see `path = "/Users/USER/Documents/Appointment_checker_na/chromedriver"`. Change this location to the path of your chrome driver.
4. Run the python script.
5. You will be asked for your gmail account and for details on which appointment you want. Please follow them and the program should run as expected.

