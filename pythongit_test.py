import sys
from PySide6.QtWidgets import (QWidget, QApplication,QPushButton,QLabel,QVBoxLayout,QComboBox, QLineEdit,QGroupBox,QHBoxLayout)
from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtGui import QPixmap
from PySide6.QtGui import Qt
from PIL import Image
from pprint import pprint
from glob import glob
from foodrecipes import foodrecipes
from __feature__ import snake_case, true_property
#https://github.com/pizzaflyinh/Project_multi.git
"""
Course: Multimedia programming, 
Names: Krishneet Raj, Daniel Loya, Felipe Lopez Ordaz and Carlos Fletes
Date: May 15,2024
Carlos, Daniel and Krishneet worked on the main. 
Daniel and Felipe worked on the image information and id files. 
Daniel did the image folder holding the images. All of us did review of the code to make sure it ran.
Abstract: The code takes in data about users daily deit and gives recmended recipes to help defiects in the diet
in another window.


"""
app = QApplication([])

"""
The list for data
"""
list_protein = ["Ounces","3 or lower", "4 ", "5 ",  "6 ", "7 or more" ]
list_fruit=["Palm size","1 or lower","2","3","4","5 or more"]
list_grain=["Serving","3 or lower","4","5","6","7 or more"]
list_veg=["1 cpu raw, 1/2 cup frozen", "1 or lower","2","3","4","5 or more"]
list_dairy=["Ounces","1","2","3","4","5 or more"]


class AnotherAnotherWindow(QWidget):
    def __init__(self,recipe,name ):
        super().__init__()
        layout = QVBoxLayout()
"""
The third window structure
"""
        #self.set_layout(layout)
        #layout=QHBoxLayout()
        ingredient_string = ""
        direction_string = ""
        for ingredient in recipe["ingredients"]:
            ingredient_string = ingredient_string + ingredient + "\n"

        for direction in recipe["directions"]:
            direction_string = direction_string + direction + "\n"

        self.label1 = QLabel("\nIngredients")
        layout.add_widget(self.label1)
        self.label2 = QLabel(ingredient_string)
        layout.add_widget(self.label2)
        self.label3 = QLabel("\n" + name + "\nDirections")
        layout.add_widget(self.label3)
        self.label4 = QLabel(direction_string)
        layout.add_widget(self.label4)

        self.set_layout(layout)
        layout=QHBoxLayout()
        

class Anotherwindow(QWidget):
    def __init__(self,ser_fru,ser_gra,ser_dar,ser_pro,ser_veg):
        super().__init__()
        
        """
        The second window sturcture showing lows and goods
        """
        
        layout = QVBoxLayout()
        self.label6 = QLabel("The Fruit serving are " + ser_fru)
        layout.add_widget(self.label6)
        self.label2 = QLabel("The Grain serving are " + ser_gra)
        layout.add_widget(self.label2)
        self.label3 = QLabel("The Dairy serving are " + ser_dar)
        layout.add_widget(self.label3)
        self.label4 = QLabel("The Protein serving are " + ser_pro)
        layout.add_widget(self.label4)
        self.label5 = QLabel("The Veggie servings are " + ser_veg)
        layout.add_widget(self.label5)
        self.set_layout(layout)
        layout=QHBoxLayout()
        

        """self.window_title = "Results"
        image_id = "smoothie-bowl.jpg"

        if ser_fru == "low":
            image_id = foodrecipes["fruits"]["Berry-Almond Smoothie Bowl"]["image_id"]

        self.label=QLabel(image_id)
        self.pixmap=QPixmap(image_id)
        self.pixmap=self.pixmap.scaled(400,400,Qt.KeepAspectRatio)
        self.label.pixmap=self.pixmap
        hbox = QHBoxLayout()
        hbox.add_widget(self.label)
        self.set_layout(hbox)"""

        




       
   




        

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        label1 = QLabel('Enter nutrient info: ')
"""
The first window structure
"""
        self.my_combo_box = QComboBox(self)
        self.my_combo_box.add_items(list_veg)

        self.my_combo_box2 = QComboBox(self)
        self.my_combo_box2.add_items(list_protein)

        self.my_combo_box3 = QComboBox(self)
        self.my_combo_box3.add_items(list_dairy)

        self.my_combo_box4 = QComboBox(self)
        self.my_combo_box4.add_items(list_grain)

        self.my_combo_box5 = QComboBox(self)
        self.my_combo_box5.add_items(list_fruit)
        
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
        """
        The data is transferred when submit is clicked
        """
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
        if Fru_ser>=2: #referring to the number 2, in index 2
            ser_fru = "Good"
        if Gra_ser >= 2: #referring to the number 4, in index 2
            ser_gra="Good"
        if Dar_ser>= 3: #referring to the number 3, in index 3
            ser_dar="Good"
        if pro_ser>=2: #referring to the number 3, in index 2
            ser_pro="Good"
        if veg_ser>=2 : #referring to the number 2, in index 2
            ser_veg="Good"
        """
        Sending data into windows
        """
        w= Anotherwindow(ser_fru,ser_gra,ser_dar,ser_pro,ser_veg)
        x= AnotherAnotherWindow(foodrecipes["fruits"]["Berry-Almond Smoothie Bowl"], "Berry-Almond Smoothie Bowl")
        y = AnotherAnotherWindow(foodrecipes["vegetables"]["Veggie-Packed Okonomiyaki"], "Veggie-Packed Okonomiyaki")
        z = AnotherAnotherWindow(foodrecipes["protein"]["Grilled Lemon-Herb Chicken"], "Grilled Lemon-Herb Chicken")
        a = AnotherAnotherWindow(foodrecipes["dairy"]["Triple Berry Banana Yogurt Smoothie"], "Triple Berry Banana Yogurt Smoothie")
        b = AnotherAnotherWindow(foodrecipes["grains"]["Slow-Cooker Quinoa Salad with Arugula & Feta"], "Slow-Cooker Quinoa Salad with Arugula and Feta")
        w.show()
        x.show()
        y.show()
        z.show()
        a.show()
        b.show()
        




win = MyWindow()
win.show()
sys.exit(app.exec())