import time, requests, json, smtplib, schedule

# 40.169932, -105.243231 Longmont coordinates

# scheduling the program to run
def job():
    response = requests.get('https://api.darksky.net/forecast/481377e709cae4b4f3c4fb0f9c679d2b/40.1699,-105.2432?exclude=currently,minutely,hourly,alerts,flags')
    assert response.status_code == 200
    parsed_response_content = json.loads(response.content)
    # print(parsed_response_content)
    x = parsed_response_content['daily']['data']
    daily_low = (x[2]['temperatureLow'])
    print(daily_low)
    if daily_low < 33:
    # send alert email
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('example@example.com', 'password')
        smtpObj.sendmail('example@example.com', 'example2@example.com', 'Subject: Frost Alert!\nHi Wiley, the low temperature is going to drop dangerously low tonight, so please prepare your crops.\nExpected overnight low: %daily_low')
        smtpObj.quit()

schedule.every().day.at("16:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
