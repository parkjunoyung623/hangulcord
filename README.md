hangulcord
====
[![Supported Python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg)](#)
[![License](https://img.shields.io/badge/license-limited-red.svg)](#라이선스)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c814f3b50d4548eebcd52d6062d39d1a)](https://www.codacy.com/app/kpjhg0124/hangulcord?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=404-sdok/hangulcord&amp;utm_campaign=Badge_Grade)
[![Discord.py](https://img.shields.io/badge/discord.py-1.0.1-lightgrey.svg)](https://github.com/Rapptz/discord.py)
[![Beautifulsoup](https://img.shields.io/badge/beautifulsoup4-4.7.1-lightgrey.svg)](#)

![Hangulcord Logo](./logo.png)

```
메시지 도착하면:
  만약 메시지 = 안녕:
    메시지 보내기 (안녕)
```

한글코드는 2019 광주 SW 체험 축전 부스 참여를 위해 개발된 코드 컨버터입니다.

한글코드를 이용하여 디스코드 챗봇을 개발할 수 있으며, 지정된 한글 문자열을 파이썬 코드로 변환하여 챗봇 프로그래밍을 좀 더 쉽게 체험할 수 있게 합니다.

코딩 교육용, 체험용으로 활용할 수 있지만, 애플리케이션 구조 상 현업에서는 활용할 수 없습니다.

> -숭덕고등학교 IT동아리, 404 컴퓨터 못 찾음에 의해 개발됨

시작하기
----

### 환경구성
#### 파이썬 설치
[파이썬 설치 가이드](https://github.com/Make-openNAMU/openNAMU-Guide/blob/master/articles/ko-kr/install-python.md)를 참고하여 파이썬을 설치합니다.

#### 의존성 모듈 설치
Windows

```bash
pip install -r requirements.txt
```

Linux

```bash
pip3 install -r requirements.txt
```

#### 애플리케이션 요구 데이터 설정
[디스코드 개발자 포털](https://discordapp.com/developers/applications/)에서 챗봇 시크릿 키를 받아옵니다.

`key` 파일을 생성하고, 챗봇 시크릿 키를 작성합니다.

key
```
NDMOTA2TU1E4T2MAwODA3MOD.XMg0J7.p4FiPppgOugPSQF3s6ZWNtNhQI0
```

#### 실행
Windows

```bash
python app.py
```

Linux
```bash
python3 app.py
```

라이선스
----
SW 축전 일자까지 _개인목적으로만 사용_ 이용조건 하에 사용할 수 있습니다.
