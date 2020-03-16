# crypto-trade-alerter
Script for sending text message alerts on crypto price changes from the past 24 hours based on a threshold.

<img src="https://i.kym-cdn.com/photos/images/newsfeed/000/549/435/a97.jpg" alt="dolan plz" width="60%"/>


## Requirements

### requirements.txt
* `python` >= 3.6.0
* `requests`

### Environment variables
Set the following environment variables:
* export `GMAIL_USER`=BOT_EMAIL_WITH_UNSAFE_ENABLED@gmail.com
* export `GMAIL_PASS`=RavioliRavioliGiveMeTheFormuoli
* export `ALERT_PHONE_NUMBER_EMAIL`=1234567890@msgs.carrier.com
    * AT&T: number@txt.att.net (SMS) number@mms.att.net (MMS)
    * T-Mobile: number@tmomail.net (SMS & MMS)
    * Verizon: number@vtext.com (SMS), number@vzwpix.com (MMS)
    * Sprint: number@messaging.sprintpcs.com (SMS), number@pm.sprint.com (MMS)
    * XFinity Mobile: number@vtext.com (SMS), number@mypixmessages.com (MMS)
    * Virgin Mobile: number@vmobl.com (SMS), number@vmpix.com (MMS)
    * Tracfone: number@mmst5.tracfone.com (MMS)
    * Metro PCS: number@mymetropcs.com (SMS & MMS)
    * Boost Mobile: number@sms.myboostmobile.com (SMS), number@myboostmobile.com (MMS)
    * Cricket: number@sms.cricketwireless.net (SMS), number@mms.cricketwireless.net (MMS)
    * Republic Wireless: number@text.republicwireless.com (SMS)
    * Google Fi (Project Fi): number@msg.fi.google.com (SMS & MMS)
    * U.S. Cellular: number@email.uscc.net (SMS), number@mms.uscc.net (MMS)
    * Ting: number@message.ting.com
    * Consumer Cellular: number@mailmymobile.net
    * C-Spire: number@cspire1.com
    * Page Plus: number@vtext.com


## Usage
Percent threshold is optional

`python crypto-alerter.py [percent threshold ?= 7]` or

`python3 crypto-alerter.py [percent threshold ?= 7]` or w/e

### Crontab example
Calls the script every 30 minutes with the proper secret environment

`*/30 * * * * . ~/.env && python3 ~/code/crypto-alerter/crypto-alerter.py > /dev/null 2>&1`

### Setting desired crypto alerts
Set strings containing coin names in the `COINS_TO_CHECK` list at the top of the script
