from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        
        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me!")
        
        self.setFixedSize(QSize(400, 300))
        
        # Set the central widget of the window
        self.setCentralWidget(button)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()