import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0, 0)

        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.resize(900, 300)

        vbox = QVBoxLayout()

        self.time_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setStyleSheet("""
            QLabel {
                font-size: 100px;
                font-family: Calibri;
                font-weight: bold;

                color: white;
                border-radius: 15px;
                padding: 20px;
            }

            QPushButton {
                font-size: 30px;
                font-family: Calibri;
                font-weight: bold;
                padding: 15px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        if not self.timer.isActive():
            self.timer.start(10)  # Update every 10 ms

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        hundredths = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{hundredths:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    stopwatch = Stopwatch()
    stopwatch.show()

    sys.exit(app.exec_())