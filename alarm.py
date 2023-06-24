import time
from datetime import datetime
import requests
import coolsms
    
while(True):
    current_time = datetime.now()
    week_day = datetime.today().weekday()
    print(current_time.strftime('%H:%M:%S'))
    
    if week_day != 6:
        if current_time.strftime('%H:%M') == "18:00":
            headers = coolsms.get_headers("API KEY","API SECRET") 
            url = "http://api.coolsms.co.kr/messages/v4/send"
            data = '{"message":{"to":"수신자 전화번호","from":"발신자 전화번호","text":"불이 켜졌습니다"}}'
            print("SMS 보내기")

            response = requests.post(url, headers=headers, data=data)
            print(response.status_code)
            print(response.text)
   
    time.sleep(60)

        