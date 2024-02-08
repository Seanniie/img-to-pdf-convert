
from ui.output import Ui_Form
from MainWindowData import MainWindowData
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt
import sys
import keyboard
from MouseMoveEventFilter import MouseMoveEventFilter as MMEventFilter

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    #self.data = MainWindowData()

    self.mouseMoveEventFilter = MMEventFilter(self.stopCoordinateSelection)
    QApplication.instance().installEventFilter(self.mouseMoveEventFilter)
        
    # 전역 중단 플래그 설정
    self.interrupt = False
    
    # Esc 키와 Ctrl+Z 이벤트 리스너 설정
    keyboard.add_hotkey('esc', self.stopCoordinateSelection)
    keyboard.add_hotkey('ctrl+z', self.set_interrupt_flag)

    # Ctrl+Z 이벤트 리스너 설정
    keyboard.add_hotkey('ctrl+z', self.set_interrupt_flag)
    
    # "좌표선택하기" 버튼 클릭시 동작을 연결
    self.ui.clickGridpushButton.clicked.connect(self.handleClickGrid)

    # 윈도우 아이콘 설정
    self.setWindowIcon(QIcon('./logo.ico'))

  def handleClickGrid(self):
    QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))
    QApplication.instance().installEventFilter(self.mouseMoveEventFilter)
    
  def set_interrupt_flag(self):
    # 중단 플래그를 True로 설정하여 루프 중단 시그널 전달
    self.interrupt = True
    
  def stopCoordinateSelection(self):
    QApplication.restoreOverrideCursor()# 커서 복원
    QApplication.removeEventFilter(self.mouseMoveEventFilter)# 이벤트 필터 제거
    QMessageBox.information(self, "좌표 선택 중단", "좌표 선택이 중단되었습니다.")
    
  def handleStart(self):
    # 작업 시작 전 중단 플래그 초기화
    self.interrupt = False
    startIdx=0
    endIdx=10
    for i in range(startIdx, endIdx):
      # 중단 플래그 체크
      if self.interrupt:
        # 중단 메시지 표시 및 루프 종료
        QMessageBox.warning(self, "작업 중단", "사용자에 의해 작업이 중단되었습니다.")
        break

    # 작업 완료 후 또는 중단 후 처리
    if self.interrupt:
        # 중단 관련 추가 처리
        pass
    else:
        # 정상 완료 처리
        QMessageBox.information(self, "작업 완료", "메시지 전송이 완료되었습니다.")

  def handleClose(self):
      # Ctrl+Z 리스너 해제
      keyboard.remove_hotkey('ctrl+z')
      sys.exit()