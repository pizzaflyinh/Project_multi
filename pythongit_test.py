
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
my_list = [ "Ounces","3 or lower", "4 ", "5 ",  "6 ", "7 or more" ]
list=["Palm size","1 or lower","2","3","4","5 or more"]
list_grain=["Serving","3 or lower","4","5","6","7 or more"]
list_veg=["1 cpu raw, 1/2 cup frozen", "1 or lower","2","3","4","5 or more"]
list_dairy=["Ounces","1","2","3","4","5 or more"]
class Anotherwindow(QWidget):
    def __init__(self,ser_fru,ser_gra,ser_dar,ser_pro,ser_veg):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("The Fruit serving are " + ser_fru)
        layout.add_widget(self.label)
        self.label2 = QLabel("The Grain serving are " + ser_gra)
        layout.add_widget(self.label2)
        self.label3 = QLabel("The Dariy serving are " + ser_dar)
        layout.add_widget(self.label3)
        self.label4 = QLabel("The Protein serving are " + ser_pro)
        layout.add_widget(self.label4)
        self.label5 = QLabel("The Veggie servings are " + ser_veg)
        layout.add_widget(self.label5)
        self.set_layout(layout)
        self.window_title = "Results"

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        label1 = QLabel('Enter nutrient info: ')

        self.my_combo_box = QComboBox(self)
        self.my_combo_box.add_items(list_veg)

        self.my_combo_box2 = QComboBox(self)
        self.my_combo_box2.add_items(my_list)

        self.my_combo_box3 = QComboBox(self)
        self.my_combo_box3.add_items(list_dairy)

        self.my_combo_box4 = QComboBox(self)
        self.my_combo_box4.add_items(list_grain)

        self.my_combo_box5 = QComboBox(self)
        self.my_combo_box5.add_items(list)
        
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
        veg_ser = self.my_combo_box.current_index
        pro_ser = self.my_combo_box2.current_index
        Dar_ser = self.my_combo_box3.current_index
        Gra_ser = self.my_combo_box4.current_index
        Fru_ser = self.my_combo_box5.current_index
        ser_fru="Low "
        ser_gra="Low"
        ser_dar="Low"
        ser_pro="Low"
        ser_veg="Low"
        if Fru_ser>=2:
            ser_fru = "Good"
        if Gra_ser >= 4:
            ser_gra="Good"
        if Dar_ser>= 3:
            ser_dar="Good"
        if pro_ser>=3:
            ser_pro="Good"
        if veg_ser>=2 :
            ser_veg="Good"
        
        w= Anotherwindow(ser_fru,ser_gra,ser_dar,ser_pro,ser_veg)
        w.show()
        




win = MyWindow()
win.show()
sys.exit(app.exec())
