from PyQt5.QtWidgets import QProgressBar

class QCustomProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QProgressBar {
                border: 1px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #7289DA;
                width: 10px;
                margin: 0.5px;
            }
        """)
        self.setTextVisible(False)
    
    def step(self, value: int=1):
        self.setValue(self.value() + value)
