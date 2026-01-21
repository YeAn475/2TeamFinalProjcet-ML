# FastAPI 프로젝트

FastAPI 애플리케이션 프로젝트입니다.

## 프로젝트 구조

```
fastapi/
├── main.py                 # FastAPI 메인 애플리케이션
├── app/
│   ├── __init__.py
│   ├── models/            # 데이터 모델
│   ├── routers/           # API 라우터
│   ├── services/          # 비즈니스 로직
│   ├── static/            # 정적 파일 (JS, CSS 등)
│   └── templates/         # HTML 템플릿
│       └── index.html
├── requirements.txt       # Python 패키지 의존성
└── README.md
```

## 설치 방법

```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
uvicorn main:app --reload
```
