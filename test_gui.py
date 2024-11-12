# test_gui.py

import sys
import unittest
from PyQt5.QtWidgets import QApplication
from gui import SimpleGUI

class TestSimpleGUI(unittest.TestCase):

    def setUp(self):
        # Create a QApplication instance (required by PyQt)
        self.app = QApplication(sys.argv)

        # Create the SimpleGUI window
        self.window = SimpleGUI()

    def tearDown(self):
        # Clean up the application and window after each test
        self.window.close()
        self.app.quit()

    def test_button_click_changes_label_text(self):
        # Check initial label text
        self.assertEqual(self.window.label.text(), "Original Text")

        # Simulate button click
        self.window.change_text()

        # Check if label text was updated
        self.assertEqual(self.window.label.text(), "Button Clicked!")

if __name__ == "__main__":
    unittest.main()

