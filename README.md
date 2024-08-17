# 이미지 필터링 애플리케이션

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-3776AB?style=for-the-badge&logo=python&logoColor=white)

이 프로젝트는 Python, OpenCV, Tkinter를 사용하여 다양한 이미지 필터를 적용할 수 있는 GUI 애플리케이션을 구현합니다.

## 📋 기능

- 사용자 친화적인 GUI로 쉽게 조작 가능
- 다양한 필터링 기법 지원:
  - 평균 필터 (Mean Filter)
  - 중간값 필터 (Median Filter)
  - 라플라시안 필터 (Laplacian Filter)
  - 중간값 + 라플라시안 필터 (Median + Laplacian Filter)
- 사용자 지정 필터 크기
- 필터링된 이미지의 실시간 미리보기

## 🛠️ 사용 기술

- Python
- 이미지 처리를 위한 OpenCV
- GUI를 위한 Tkinter

## 🚀 시작하기

### 필수 조건

- Python 3.x
- OpenCV
- Pillow

필요한 패키지 설치:

```bash
pip install opencv-python pillow
```

### 애플리케이션 실행

1. 저장소 클론:
   ```bash
   git clone https://github.com/Ghoney99/graphics-Vision.git
   ```

2. 프로젝트 디렉토리로 이동:
   ```bash
   cd graphics-Vision
   ```

3. ComputerVison_CVFilter.py 스크립트 실행:
   ```bash
   python ComputerVison_CVFilter.py
   ```

## 💻 사용 방법

1. 애플리케이션을 실행합니다.
2. 입력 필드에 원하는 필터 크기를 입력합니다.
3. 적용하고 싶은 필터 버튼을 클릭합니다.
4. 메시지가 표시되면 이미지 파일을 선택합니다.
5. 별도의 창에서 원본 이미지와 필터링된 이미지를 확인합니다.

## 📸 필터 예시

### Mean 필터
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FOfcxI%2FbtsI03eSh4Y%2FQz1srskCyFDr1kKFmaE1MK%2Fimg.png" alt="Mean" width="800"/>

### Median 필터
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbSEP6Z%2FbtsI0B4hqRj%2F8NmpP4KV861xCQH55Z2Ack%2Fimg.png" alt="Median" width="800"/>

### Laplacian 필터
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F03VZq%2FbtsI021j5FW%2FFZKoMD9I7UFyer8CpAeOg1%2Fimg.png" alt="Laplacian" width="800"/>

### Median + Laplacian 필터
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAn5HK%2FbtsI1gkITYg%2FCVHKBc2Wh4ZlRbPqq8IKrK%2Fimg.png" alt="Median + Laplacian" width="800"/>
