from PySide6.QtCore import QObject, QEvent

class MouseMoveEventFilter(QObject):
    def __init__(self, callback):
      super().__init__()
      self.callback = callback
      self.clickCount = 0

    def eventFilter(self, obj, event):
      if event.type() == QEvent.MouseMove:
        # 마우스 위치를 출력하거나 다른 처리를 수행
        pass
      elif event.type() == QEvent.MouseButtonPress:
        self.clickCount += 1
        if self.clickCount >= 2:
          self.callback()  # 두 번 클릭하면 콜백 함수를 호출
      return super(MouseMoveEventFilter, self).eventFilter(obj, event)
