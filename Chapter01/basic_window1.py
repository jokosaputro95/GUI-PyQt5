# 1. Import necessary modules
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([]) # 2. Create QApplication object

# Create a Qt widget, which will be our window
window = QWidget() # 3. Create window from QWidget object
window.show() # 4. Call show to display GUI window

# Start the even loop
app.exec_() # 5. Start the event loop.