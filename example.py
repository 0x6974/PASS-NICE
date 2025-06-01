import asyncio
from src.PASS_NICE import PASS_NICE
import os
import webbrowser

async def main():
    # ISP
    name, birthdate, phone, ISP = "홍길동", "0000000", "01012345678", "SK"
    # SK = SKT, KT = KT, LG = LGT
    # SM = SK알뜰폰, KM = KT알뜰폰, LM = LG알뜰폰
    
    try:
        verification = PASS_NICE(ISP)
    except:
        return {"Success": False, "Message": "올바른 ISP 값을 입력해주세요."}
    
    initResult = await verification.initSession()
    if not initResult['Success']:
        return {"Success": False, "Message": initResult['Message']}

    captchaResult = await verification.getCaptcha()
    if not captchaResult['Success']: 
        return {"Success": False, "Message": captchaResult['Message']}
    
    # 캡챠 이미지 저장 및 열기
    captcha_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'captcha.png')
    try:
        with open(captcha_path, 'wb') as f:
            f.write(captchaResult['Content'])
        webbrowser.open(captcha_path)
    except Exception as e:
        return {"Success": False, "Message": "캡챠 이미지를 처리하는 중 오류가 발생하였습니다."}

    captchaCode = input("캡챠 코드를 입력해주세요: ")
    sendResult = await verification.sendSMS(name, birthdate, phone, captchaCode)
    if not sendResult['Success']:
        return {"Success": False, "Message": sendResult['Message']}
    
    smsCode = input("SMS로 전송된 코드를 입력해주세요: ")
    checkResult = await verification.checkSMS(smsCode)
    if not checkResult['Success']:
        return {"Success": False, "Message": checkResult['Message']}

    print("인증이 성공적으로 완료되었어요!")
    return {"Success": True, "Message": "인증이 성공적으로 완료되었습니다."}

if __name__ == "__main__":
    print(asyncio.run(main()))