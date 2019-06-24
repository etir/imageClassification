from tkinter import *
from tkinter import filedialog
import ctypes
import PIL
import math
import csv
import ctypes
from tkinter.filedialog import askopenfilename
import os
from keras import models
from PIL import ImageTk, Image

root=Tk()

root.title("Welcome To Flower Classification")
pictures = None
weights = None
file_additionPic = None


def create_window():
    root2 = Tk()
    scrollbar = Scrollbar(root2)
    scrollbar.pack(side=RIGHT, fill=Y)
    global listbox
    listbox = Listbox(root2, height=100, width=100)
    listbox.pack()
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)



def openFilePic():
    root.sourceFolder = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
    #file_1 = filedialog.askopenfilename( filetypes= (("Python files" , "*.py"), ("All files", "*.*")))
    PathToPicDirectory=Label(text=root.sourceFolder)
    PathToPicDirectory.grid(row=1, column=1)
    global pictures
    pictures=root.sourceFolder

def openFileTrain():
    file_2 = filedialog.askopenfilename(  title='Please select a file')
    lab2=Label(text=file_2)
    lab2.grid(row=3, column=1)
    global weights
    weights=file_2

def predict():
    if (pictures==None) & (file_additionPic==None):
        ctypes.windll.user32.MessageBoxW(0, "You need to select a folder or image file with an image", "Error", 1)
    elif (weights == None):
        ctypes.windll.user32.MessageBoxW(0, "You need to select the Training file", "Error", 1)
    elif ((pictures==None) & (file_additionPic==None) & (weights == None)) | ((pictures=="") & (file_additionPic=="") & (weights == "")) :
        ctypes.windll.user32.MessageBoxW(0, "You need to select the Training file and a folder or image file with an image", "Error", 1)

    if ((weights!=None) &((file_additionPic!=None) | (pictures!=None)))&(weights!="")&((file_additionPic!="") | (pictures!="")):
        if (pictures!=None):
            create_window()
        load();
        global str
        str=""
        with open('result.csv', mode='w',newline="\n") as result_file:
            j = 6
            if (file_additionPic!=None):
                    path = file_additionPic
                    from keras.preprocessing import image
                    test_image = image.load_img(path, target_size=(128, 128))
                    test_image = image.img_to_array(test_image)
                    import numpy as np
                    test_image = np.expand_dims(test_image, axis=0)
                    result = model.predict(test_image)
                    i = 0
                    count = 0
                    for a in result:
                        max = 0
                        for aa in a:
                            if aa > max:
                                max = aa
                                count = i
                            i = i + 1
                    if count == 0:
                        label_6 = Label(root, text=file_additionPic)
                        label_6.grid(row=2, column=1)
                        lab_7=Label(root,text=" Result is: daisy", font='Helvetica 18 bold')
                        lab_7.grid(row=2, column=3)
                        lableToWrite = Label(root, text="daisy")
                        j = j + 1
                    if count == 1:
                        label_6 = Label(root, text=file_additionPic)
                        label_6.grid(row=2, column=1)
                        lableToWrite = Label(root, text="dandelion")
                        lab_7 = Label(root, text=" Result is: dandelion", font='Helvetica 18 bold')
                        lab_7.grid(row=2, column=3)
                        j = j + 1
                    if count == 2:
                        label_6 = Label(root, text=file_additionPic)
                        label_6.grid(row=2, column=1)
                        lab_7 = Label(root, text=" Result is: rose", font='Helvetica 18 bold')
                        lab_7.grid(row=2, column=3)
                        j = j + 1
                    if count == 3:
                        label_6 = Label(root, text=file_additionPic )
                        label_6 = Label(root, text=file_additionPic)
                        label_6.grid(row=2, column=1)
                        lab_7 = Label(root, text=" Result is: sunflower", font='Helvetica 18 bold')
                        lab_7.grid(row=2, column=3)
                        j = j + 1
                    if count == 4:
                        label_6 = Label(root, text=file_additionPic )
                        label_6.grid(row=2, column=1)
                        lab_7 = Label(root, text=" Result is: tulip", font='Helvetica 18 bold')
                        lab_7.grid(row=2, column=3)
                        j = j + 1

            if (pictures!=None):
                for filename in os.listdir(pictures):
                    path = pictures + "/" + filename
                    from keras.preprocessing import image
                    test_image = image.load_img(path, target_size=(128, 128))
                    test_image = image.img_to_array(test_image)
                    import numpy as np
                    test_image = np.expand_dims(test_image, axis=0)
                    result = model.predict(test_image)
                    i = 0
                    count = 0
                    for a in result:
                        max = 0
                        for aa in a:
                            if aa > max:
                                max = aa
                                count = i
                            i = i + 1
                    if count == 0:

                        a = filename + " daisy"
                        label_5 = Label(root, text=filename + " daisy")
                        #label_5.grid(row=j, column=1)
                        lableToWrite = Label(root, text="daisy")
                        str=label_5['text']
                        listbox.insert(END, str)
                        listbox.insert(END, '\n')

                        j = j + 1
                    if count == 1:
                        label_5 = Label(root, text=filename + " dandelion")
                        #label_5.grid(row=j, column=1)
                        str=label_5['text']
                        listbox.insert(END, str)
                        listbox.insert(END, '\n')

                        lableToWrite = Label(root, text="dandelion")
                        j = j + 1
                    if count == 2:
                        label_5 = Label(root, text=filename + " rose")
                        #label_5.grid(row=j, column=1)
                        str=label_5['text']
                        listbox.insert(END, str)
                        listbox.insert(END, '\n')

                        lableToWrite = Label(root, text="rose")
                        j = j + 1
                    if count == 3:
                        label_5 = Label(root, text=filename + " sunflower")
                        #label_5.grid(row=j, column=1)
                        str = label_5['text']
                        listbox.insert(END, str)
                        listbox.insert(END, '\n')

                        lableToWrite = Label(root, text="sunflower")
                        j = j + 1
                    if count == 4:
                        label_5 = Label(root, text=filename + " tulip")
                        #label_5.grid(row=j, column=1)
                        str = label_5['text']
                        listbox.insert(END, str)
                        listbox.insert(END, '\n')

                        lableToWrite = Label(root, text="tulip")
                        j = j + 1
                    result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    result_writer.writerow([filename, lableToWrite['text']])
            result_file.close()


def load():
    global model
    from keras.models import load_model
    model = load_model(weights)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

def openFilePic2():
    global file_additionPic
    file_additionPic = filedialog.askopenfilename(title='Please select a file')
    labadd = Label(text=file_additionPic)
    labadd.grid(row=2, column=1)
    if file_additionPic!="":
        image = Image.open(file_additionPic)
        photo = ImageTk.PhotoImage(image)
        label = Label(root,image=photo)
        label.grid(row=2, column=3)
        label.image = photo





label_1=Label(root, text="Flower Classification")

label_2=Label(root, text="Select a folder of pictures")
entry_1=Entry(root)
button_1=Button(root, text="Browser", command=openFilePic)


label_addition=Label(root, text="Select a file of one picture")
entry_1add=Entry(root)
button_1add=Button(root, text="Browser", command=openFilePic2)


label_3=Label(root, text="Select a file of training")
entry_2=Entry(root)
button_2=Button(root, text="Browser", command=openFileTrain)

button_3=Button(root, text="Predict" ,command=predict)
label_4=Label(root, text="Results:")


label_1.grid(columnspan=2)
label_2.grid(row=1, column=0)
entry_1.grid(row=1, column=1)
button_1.grid(row=1, column=2)

label_addition.grid(row=2, column=0)
entry_1add.grid(row=2, column=1)
button_1add.grid(row=2, column=2)

label_3.grid(row=3, column=0)
entry_2.grid(row=3, column=1)
button_2.grid(row=3, column=2)

button_3.grid(row=4, column=0)


label_4.grid(row=5, column=0)



root.mainloop()
