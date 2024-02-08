1. 프로젝트 디렉터리에 가상 환경을 생성
python -m venv venv

.\venv\Scripts\activate

(
  Unauthorized Access 에러발생 -> powershell 관리권한 실행 ->
  Set-ExecutionPolicy Unrestricted
)

3. requirements.txt: 프로젝트에 필요한 외부 라이브러리들을 나열하는 파일입니다. 이 파일은 pip freeze > requirements.txt 명령어를 통해 생성할 수 있습니다.

4. .ui 파일을 Python 코드로 변환
pyside6-uic form.ui -o output.py

5. 하나의 exe파일로 만들기
pyinstaller --clean --onefile --noconsole --windowed --name "카카오 자동 메세지" --icon=mango.ico --add-data "mango.ico;." .\Main.py