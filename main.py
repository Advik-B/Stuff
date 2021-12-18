from functions.download import download_GUI
from functions.custom_progressbar import QCustomProgressBar
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
import sys
import asyncio

class App(QWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Downloader')
        self.setGeometry(300, 300, 700, 400)
        self.start_btn = QPushButton('Start', self)
        self.start_btn.move(100, 100)
        self.progress_bar = QCustomProgressBar(self)
        self.progress_bar.setGeometry(100, 500, 500, 25)
        self.start_btn.clicked.connect(self.down)
        self.progress_bar.move(100, 200)
        self.icon = QIcon('trading.png')
        self.setWindowIcon(self.icon)
        self.show()

    def down(self):
        zip_path = download_GUI(date=24, month=1, year=2020, progress_bar=self.progress_bar)
        asyncio.run(self.event_loop())
        
    async def event_loop(self):
        while True:
            if self.progress_bar.maximum() - self.progress_bar.value() == 396:
                mbox = QMessageBox()
                mbox.setWindowTitle('Downloader Alert')
                mbox.setText('Download complete!')
                mbox.setDefaultButton(QMessageBox.Ok)
                mbox.setIcon(QMessageBox.Information)
                mbox.setParent(self.parent())
                mbox.setGeometry(mbox.width(), mbox.height(), 500, 450)
                mbox.setWindowIcon(self.icon)
                self.progress_bar.setValue(0)
                mbox.exec_()
                break


def main():
    app = QApplication(sys.argv)
    ex = App()
    app.setActiveWindow(ex)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
