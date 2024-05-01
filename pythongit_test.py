
import sys
from PySide6.QtWidgets import (QWidget, QApplication,QPushButton,QLabel,QVBoxLayout,QComboBox, QLineEdit,QGroupBox,QHBoxLayout)
from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtGui import QPixmap
from PySide6.QtGui import Qt
from PIL import Image
from pprint import pprint
from glob import glob
from __feature__ import snake_case, true_property

app = QApplication([])
my_list = [ "None", "Sepia", "Negative",  "Grayscale", "Thumbnail" ]
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        label1 = QLabel('Enter nutrient info: ')

        self.my_combo_box = QComboBox(self)
        self.my_combo_box.add_items(my_list)

        self.my_combo_box2 = QComboBox(self)
        self.my_combo_box2.add_items(my_list)

        self.my_combo_box3 = QComboBox(self)
        self.my_combo_box3.add_items(my_list)

        self.my_combo_box4 = QComboBox(self)
        self.my_combo_box4.add_items(my_list)

        self.my_combo_box5 = QComboBox(self)
        self.my_combo_box5.add_items(my_list)
        
        my_btn= QPushButton('Submit')
        self.my_lbl=QLabel("")
        my_btn.clicked.connect(self.on_click)

        hbox1 = QHBoxLayout()
        hbox1.add_widget(label1)

        gbox1 = QGroupBox('')
        gbox1.set_layout(hbox1)

        hbox2 = QHBoxLayout() 
        hbox2.add_widget(self.my_combo_box)
        

        hbox3 = QHBoxLayout()
        hbox3.add_widget(self.my_lbl)
        hbox3.add_widget(my_btn)

        hbox4 = QHBoxLayout() 
        hbox4.add_widget(self.my_combo_box2)

        hbox5 = QHBoxLayout() 
        hbox5.add_widget(self.my_combo_box3)

        hbox6 = QHBoxLayout() 
        hbox6.add_widget(self.my_combo_box4)

        hbox7 = QHBoxLayout() 
        hbox7.add_widget(self.my_combo_box5)


        vbox2 = QVBoxLayout()
        vbox2.add_layout(hbox2)

        vbox3=QVBoxLayout()
        vbox3.add_layout(hbox3)

        vbox4=QVBoxLayout()
        vbox4.add_layout(hbox4)

        vbox5=QVBoxLayout()
        vbox5.add_layout(hbox5)

        vbox6=QVBoxLayout()
        vbox6.add_layout(hbox6)

        vbox7=QVBoxLayout()
        vbox7.add_layout(hbox7)

        gbox2 = QGroupBox("Veggies servings")
        gbox2.set_layout(vbox2)

        gbox3=QGroupBox("")
        gbox3.set_layout(vbox3)

        gbox4 = QGroupBox("Protein servings")
        gbox4.set_layout(vbox4)

        gbox5 = QGroupBox("Dairy servings")
        gbox5.set_layout(vbox5)

        gbox6 = QGroupBox("Grain servings")
        gbox6.set_layout(vbox6)

        gbox7 = QGroupBox("Fruit servings")
        gbox7.set_layout(vbox7)

        mbox = QVBoxLayout()
        mbox.add_widget(gbox1)
        mbox.add_widget(gbox2)
        mbox.add_widget(gbox4)
        mbox.add_widget(gbox5)
        mbox.add_widget(gbox6)
        mbox.add_widget(gbox7)
        mbox.add_widget(gbox3)

        self.set_layout(mbox)
        self.window_title = "Diet Tracker and Recommendations"



    @Slot()
    def on_click(self):
        return "hello"




win = MyWindow()
win.show()
sys.exit(app.exec())
print('hello')

print('Hello world')
from other_file import my_list
"""
I missed up the file of other_file as I got to this part and couldn't figure out what to do next.
"""
print(my_list)