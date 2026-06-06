import sys
from UI import UI
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()