import sys
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow  # 새로 생성한 메인 윈도우 클래스

def main():
  app = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()