from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QGroupBox, QTextEdit
from Utilities import Utilities

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.utilities = Utilities()

        self.setWindowTitle("RMP Concensus Generator")
        self.setGeometry(1000, 100, 400, 300)

        self.profNameLabel = QLabel("Enter Prof Name:")
        self.uniNameLabel = QLabel("Enter Uni Name:")

        self.profNameBox = QLineEdit(self)
        self.profNameBox.returnPressed.connect(self.profUniEntered)
        self.uniNameBox = QLineEdit(self)
        self.uniNameBox.returnPressed.connect(self.profUniEntered)

        self.vBoxLayout = QHBoxLayout()
        self.hBoxProf = QHBoxLayout()
        self.hBoxUni = QHBoxLayout()
        # self.vBoxResponse = QVBoxLayout()
        self.profGroup = QWidget()
        self.uniGroup = QWidget()
        self.central = QWidget()
        self.grid = QGridLayout()
        self.frame = QGroupBox()
        self.responseText = QTextEdit()
        self.responseText.setReadOnly(True)
        self.frameLayout = QVBoxLayout()
        self.initApp()
    
    def initApp(self):
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
        self.grid.setRowStretch(0, 1)
        self.grid.setRowStretch(1, 1)
        self.grid.setColumnStretch(1, 1)
        self.central.setLayout(self.grid)
        self.setCentralWidget(self.central)

    def profUniEntered(self):
        if self.uniNameBox.text() and self.profNameBox.text():
            url = self.utilities.getURL(self.uniNameBox.text(), self.profNameBox.text())
            data = self.utilities.getProfReviews(url)
            concensus = self.utilities.generateResponse(data)
            self.responseText.setText(concensus)