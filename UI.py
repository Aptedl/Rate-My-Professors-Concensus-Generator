from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QGroupBox, QTextEdit, QStackedWidget, QPushButton, QSpacerItem
from PyQt6.QtCore import Qt#For alignment flags
from Utilities import Utilities

class ProfScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.utilities = Utilities()

        self.profNameLabel = QLabel("Professor Name")
        self.uniNameLabel = QLabel("University Name")

        self.profNameBox = QLineEdit(self)
        self.profNameBox.setPlaceholderText("e.g. John Doe")
        self.profNameBox.returnPressed.connect(self.profUniEntered)
        self.uniNameBox = QLineEdit(self)
        self.uniNameBox.setPlaceholderText("e.g. McMaster University")
        self.uniNameBox.returnPressed.connect(self.profUniEntered)

        self.vBoxLayout = QHBoxLayout()
        self.hBoxProf = QHBoxLayout()
        self.hBoxUni = QHBoxLayout()
        self.profGroup = QWidget()
        self.uniGroup = QWidget()
        self.central = QWidget()
        self.grid = QGridLayout()
        self.frame = QGroupBox("Consensus")
        self.responseText = QTextEdit()
        self.responseText.setReadOnly(True)
        self.responseText.setPlaceholderText("Your consensus will appear here...")
        self.frameLayout = QVBoxLayout()
        self.initApp()

    def initApp(self):
        self.profNameLabel.setStyleSheet("font-weight: 600; color: #444;")
        self.uniNameLabel.setStyleSheet("font-weight: 600; color: #444;")

        self.hBoxProf.addWidget(self.profNameLabel)
        self.hBoxProf.addWidget(self.profNameBox)
        self.hBoxUni.addWidget(self.uniNameLabel)
        self.hBoxUni.addWidget(self.uniNameBox)
        self.frameLayout.addWidget(self.responseText)

        self.frame.setLayout(self.frameLayout)
        self.profGroup.setLayout(self.hBoxProf)
        self.uniGroup.setLayout(self.hBoxUni)

        self.grid.addWidget(self.profGroup, 0, 0)
        self.grid.addWidget(self.uniGroup, 1, 0)
        self.grid.addWidget(self.frame, 0, 1, 2, 1)
        self.grid.setSpacing(12)#12 px padding between elements in the grid
        self.grid.setContentsMargins(16, 16, 16, 16)#16 px padding between grid and outer edge on left, top, right, bottom
        self.setLayout(self.grid)

    def profUniEntered(self):
        if self.uniNameBox.text() and self.profNameBox.text():
            url = self.utilities.getURL(self.uniNameBox.text(), self.profNameBox.text())
            data = self.utilities.getProfReviews(url)
            concensus = self.utilities.generateResponse(data)
            self.responseText.setText(concensus)

class ClassScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.utilities = Utilities()

        self.classNameLabel = QLabel("Class Name")
        self.deptNameLabel = QLabel("Department")
        self.uniNameLabel = QLabel("University Name")

        self.classNameBox = QLineEdit(self)
        self.classNameBox.setPlaceholderText("e.g. 2DM3. Use only last 4 chars.")
        self.classNameBox.returnPressed.connect(self.profUniEntered)
        self.uniNameBox = QLineEdit(self)
        self.uniNameBox.setPlaceholderText("e.g. McMaster University")
        self.uniNameBox.returnPressed.connect(self.profUniEntered)

        self.vBoxLayout = QHBoxLayout()
        self.hBoxProf = QHBoxLayout()
        self.hBoxProfName = QHBoxLayout()
        self.profNameGroup = QWidget()
        self.deptNameLabel = QLabel("Department")
        self.deptNameBox = QLineEdit()
        self.deptNameBox.setPlaceholderText("e.g. Software Engineering")
        self.deptNameBox.returnPressed.connect(self.profUniEntered)
        self.hBoxUni = QHBoxLayout()
        self.profGroup = QWidget()
        self.uniGroup = QWidget()
        self.central = QWidget()
        self.grid = QGridLayout()
        self.frame = QGroupBox("Consensus")
        self.responseText = QTextEdit()
        self.responseText.setReadOnly(True)
        self.responseText.setPlaceholderText("Your consensus will appear here...")
        self.frameLayout = QVBoxLayout()
        self.initApp()

    def initApp(self):
        self.classNameLabel.setStyleSheet("font-weight: 600; color: #444;")
        self.deptNameLabel.setStyleSheet("font-weight: 600; color: #444;")
        self.uniNameLabel.setStyleSheet("font-weight: 600; color: #444;")

        self.hBoxProf.addWidget(self.classNameLabel)
        self.hBoxProf.addWidget(self.classNameBox)
        self.hBoxUni.addWidget(self.uniNameLabel)
        self.hBoxUni.addWidget(self.uniNameBox)
        self.hBoxProfName.addWidget(self.deptNameLabel)
        self.hBoxProfName.addWidget(self.deptNameBox)
        self.frameLayout.addWidget(self.responseText)

        self.frame.setLayout(self.frameLayout)
        self.profGroup.setLayout(self.hBoxProf)
        self.uniGroup.setLayout(self.hBoxUni)
        self.profNameGroup.setLayout(self.hBoxProfName)

        self.grid.addWidget(self.profGroup, 0, 0)
        self.grid.addWidget(self.uniGroup, 1, 0)
        self.grid.addWidget(self.profNameGroup, 2, 0)
        self.grid.addWidget(self.frame, 0, 1, 3, 1)
        self.grid.setSpacing(12)#12 px padding between elements in the grid
        self.grid.setContentsMargins(16, 16, 16, 16)#16 px padding between grid and outer edge on left, top, right, bottom
        self.setLayout(self.grid)

    def profUniEntered(self):
        if self.uniNameBox.text() and self.classNameBox.text() and self.deptNameBox.text():
            concensus = self.utilities.getReviewsAndResponse(self.uniNameBox.text(), self.deptNameBox.text(), self.classNameBox.text())
            self.responseText.setText(concensus)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RMP Consensus Generator")
        self.setGeometry(100, 100, 700, 400)
        self.stack = QStackedWidget()
        self.profScreen = ProfScreen()
        self.classScreen = ClassScreen()
        self.stack.addWidget(self.profScreen)
        self.stack.addWidget(self.classScreen)
        self.stack.setCurrentIndex(0)

        self.profBtn = QPushButton("Professor")
        self.classBtn = QPushButton("Class")
        self.profBtn.clicked.connect(lambda: self.switch_screen(0))
        self.classBtn.clicked.connect(lambda: self.switch_screen(1))

        self.btnBar = QHBoxLayout()
        self.btnBar.setContentsMargins(120, 0, 120, 0)
        self.btnBar.setSpacing(8)
        self.btnBar.addWidget(self.profBtn)
        self.btnBar.addWidget(self.classBtn)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.btnBar)
        self.mainLayout.addWidget(self.stack)

        self.central = QWidget()
        self.central.setLayout(self.mainLayout)
        self.setCentralWidget(self.central)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QWidget {
                background-color: #f5f5f5;
                font-family: Segoe UI, Arial, sans-serif;
                font-size: 13px;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 6px 10px;
                color: #222;
            }
            QLineEdit:focus {
                border: 1px solid #0078d4;
            }
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 8px;
                color: #222;
                line-height: 1.5;
            }
            QGroupBox {
                border: 1px solid #ddd;
                border-radius: 8px;
                margin-top: 6px;
                padding: 10px;
                font-weight: 600;
                color: #444;
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
            }
            QPushButton {
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 6px 18px;
                color: #333;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #7A003C;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #490024;
                border: 1px solid #005a9e;
                color: #ffffff;
            }
        """)

    def switch_screen(self, index):
        self.stack.setCurrentIndex(index)