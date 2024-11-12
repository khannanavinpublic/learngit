# gui.py (using PyQt5)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class SimpleGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle('Simple PyQt5 GUI')
        self.setGeometry(100, 100, 300, 200)

        # Create a label and a button
        self.label = QLabel('Original Text', self)
        self.button = QPushButton('Click Me', self)

        # Connect the button to the function
        self.button.clicked.connect(self.change_text)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set the layout for the main window
        self.setLayout(layout)

    def change_text(self):
        self.label.setText('Button Clocked!')

# Run the application if this file is executed directly
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Initialize the PyQt application
    gui = SimpleGUI()             # Create the SimpleGUI window
    gui.show()                    # Show the window
    sys.exit(app.exec_())         # Start the application event loop

