# PASS-NICE

NICE 본인인증 자동화 파이썬 스크립트입니다.

> 이 프로젝트는 [necynice/PASS-NICE](https://github.com/necynice/PASS-NICE)를 기반으로 수정된 버전입니다.
> 
> 원작자: [@necynice](https://github.com/necynice)
> - Telegram: @sunr1s2_0
> - Discord: @necynice_

## 필독사항

**본 스크립트는 교육용 및 학습용으로만 사용해주세요.**
이 프로그램을 사용함으로써 발생하는 모든 책임은 사용자 본인에게 있습니다.

## 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/vgcac/PASS-NICE.git
cd PASS-NICE
```

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

## 사용 방법

1. example.py 파일에서 개인정보 입력:
```python
name, birthdate, phone, ISP = "홍길동", "0000000", "01012345678", "SK"
```

2. 통신사 코드 안내:
- SK = SKT
- KT = KT
- LG = LGT
- SM = SK알뜰폰
- KM = KT알뜰폰
- LM = LG알뜰폰

3. 실행
```bash
python example.py
```

4. 실행 후:
- 캡챠 이미지가 자동으로 열립니다
- 캡챠 코드를 입력하세요
- SMS로 전송된 인증번호를 입력하세요

## 기능

- SMS 본인인증
- MVNO(알뜰폰) 포함 모든 통신사 지원
- 캡챠 이미지 자동 열기

## 주의사항

- 본 스크립트는 학습 목적으로만 사용해주세요
- NICE신용평가 및 관련 기관의 요청 시 즉시 삭제될 수 있습니다
- 실제 서비스에 사용 시 관련 법규를 확인해주세요
- 개인정보 보호에 유의해주세요

## 라이선스

MIT License 