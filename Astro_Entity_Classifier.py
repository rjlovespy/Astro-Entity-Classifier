<<<<<<< HEAD
from Outliers import remove_outliers_with_isolation_forest
import tkinter.messagebox as tmsg
from tkinter import *
from joblib import load
import pandas as pd
import numpy as np

# Resets the features to 0
def resetFeatures():
    for i in range(8):
        tv[i].set(0)
        features[i].update()
    output["text"] = "Enter new astro entity details"
    
    
# Uses a Machine Learning(ML) model trained by Bagging Classifier Algorithm 
def predictEntity():
    try:
        if ((tv[0].get() >= 0) and (tv[0].get() <= 360)) and ((tv[1].get() >= -90) and (tv[1].get() <= 90)): 
            Model = load("E:\\Machine Learning\\Astro Entity Classifier\\Model.joblib")
            pre_processor = load("E:\\Machine Learning\\Astro Entity Classifier\\pre_processor.joblib")

            features = [tv[0].get(), tv[1].get(), tv[2].get(), tv[3].get(), tv[4].get(), tv[5].get(), tv[6].get(), tv[7].get()]
            features_nda = np.array([features])                                   
            features_df = pd.DataFrame(features_nda, columns=["alpha","delta","u","g","r","i","z","redshift"])  
            features_pp_nda = pre_processor.transform(features_df)  
            features_pp_df =  pd.DataFrame(features_pp_nda, columns=features_df.columns)         
            predicted_entity = Model.predict(features_pp_df)

            output["text"] = f"The astro entity with the given details is a \n{predicted_entity[0]}"
        elif ((tv[0].get() >= 0) and (tv[0].get() <= 360)) == False:
            tmsg.showinfo(title="Warning!", message="The value of alpha is invalid")
            output["text"] = "The value of alpha should lie between 0 and 360 degrees"
        else:
            tmsg.showinfo(title="Warning!", message="The value of delta is invalid")
            output["text"] = "The value of delta should lie between -90 and 90 degrees"
    except TclError:
        tmsg.showinfo(title="Warning!", message="Invalid details have been entered")
        output["text"] = "Enter valid details"
        

# Screen Customization
root = Tk()
root.geometry("950x750")
root.resizable(True, True)
root.minsize(900,750)
root.config(bg="#030303")
root.title("Astro Entity Classifier")           
root.iconbitmap("E:\\Machine Learning\\Astro Entity Classifier\\astro_entity.ico")


# Giving Title
f1 = Frame(root, bg="#030303", highlightbackground="thistle", highlightthickness=2)
f1.pack(fill=X, padx=50, pady=50)
Label(f1, text="Galaxy-Star-Quasar(GSQ) Identifier", fg="peachpuff", bg="#030303", font="Lucida 25 bold").pack(padx=10, pady=10)


# Creating Entries for Astro Entity Features
f2 = Frame(root, bg="#030303", highlightbackground="thistle", highlightthickness=2)
f2.pack(fill=X, ipadx=10, ipady=10, padx=50)
Label(f2, text="1. Enter aplha = Right Ascension angle (at J2000 epoch): "     , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=0, column=0, sticky=W, padx=15, pady=10)
Label(f2, text="2. Enter delta = Declination angle (at J2000 epoch):"          , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=1, column=0, sticky=W, padx=15)
Label(f2, text="3. Enter u = Ultraviolet filter in the photometric system:"    , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=2, column=0, sticky=W, padx=15, pady=10)
Label(f2, text="4. Enter g = Green filter in the photometric system:"          , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=3, column=0, sticky=W, padx=15)
Label(f2, text="5. Enter r = Red filter in the photometric system:"            , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=4, column=0, sticky=W, padx=15, pady=10)
Label(f2, text="6. Enter i = Near Infrared filter in the photometric system:"  , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=5, column=0, sticky=W, padx=15)
Label(f2, text="7. Enter z = Infrared filter in the photometric system:"       , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=6, column=0, sticky=W, padx=15, pady=10)
Label(f2, text="8. Enter redshift = Value based on the increase in wavelength:", bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=7, column=0, sticky=W, padx=15)

""" 
Source: SDSS_DR18-SDSS_DR17.csv
97298: [358.095259, 56.24256139, 16.88485, 14.28269, 13.58865, 13.03581, 12.93735, -0.000260102, STAR]
"""
tv = [None]*8
features = [None]*8
initial_features = np.array([358.095259, 56.24256139, 16.88485, 14.28269, 13.58865, 13.03581, 12.93735, -0.000260102])
for i in range(8):
    tv[i] = DoubleVar()
    tv[i].set(initial_features[i])
    features[i] = Entry(f2, textvariable = tv[i], font="Lucida 14 normal", bg="thistle", relief=SUNKEN)
    if i%2 == 0:
        features[i].grid(row=i, column=1, sticky=NSEW, ipady=2,  padx=50, pady=10)
    else:
        features[i].grid(row=i, column=1, sticky=NSEW, ipady=2,  padx=50)

Button(f2, text="RESET", command=resetFeatures, font="Lucida 16 bold", activebackground="gold", bg="deepskyblue", width=15, bd=4, relief=SUNKEN).grid(row=10, column=0, sticky=W, padx=30, pady=10, ipady=3)
Button(f2, text="IDENTIFY", command=predictEntity, font="Lucida 16 bold", activebackground="gold", bg="lime", width=15, bd=4, relief=SUNKEN).grid(row=10, column=0, sticky=E, padx=30, pady=10, ipady=3)

for i in range(8):
    f2.grid_rowconfigure(i, weight=1, pad=5)
f2.grid_columnconfigure(1, weight=1)    


# Labelling the Predicted Entity
f3 = Frame(root, bg="#030303", highlightbackground="thistle", highlightthickness=2)
f3.pack(fill=X, padx=50, pady=20)
output = Label(f3, text="Press RESET for entering new astro entity details", fg="crimson", bg="#030303", font="Lucida 16 bold")
output.pack(padx=10, pady=10)


=======
from Outliers import remove_outliers_with_isolation_forest
import tkinter.messagebox as tmsg
from tkinter import *
from joblib import load
import pandas as pd
import numpy as np

# Resets the features to 0
def resetFeatures():
    for i in range(8):
        tv[i].set(0)
        features[i].update()
    output["text"] = "Enter new astro entity details"
    
    
# Uses a Machine Learning(ML) model trained by Bagging Classifier Algorithm 
def predictEntity():
    try:
        if ((tv[0].get() >= 0) and (tv[0].get() <= 360)) and ((tv[1].get() >= -90) and (tv[1].get() <= 90)): 
            Model = load("E:\\Machine Learning\\Astro Entity Classifier\\Model.joblib")
            pre_processor = load("E:\\Machine Learning\\Astro Entity Classifier\\pre_processor.joblib")

            features = [tv[0].get(), tv[1].get(), tv[2].get(), tv[3].get(), tv[4].get(), tv[5].get(), tv[6].get(), tv[7].get()]
            features_nda = np.array([features])                                   
            features_df = pd.DataFrame(features_nda, columns=["alpha","delta","u","g","r","i","z","redshift"])  
            features_pp_nda = pre_processor.transform(features_df)  
            features_pp_df =  pd.DataFrame(features_pp_nda, columns=features_df.columns)         
            predicted_entity = Model.predict(features_pp_df)

            output["text"] = f"The astro entity with the given details is a \n{predicted_entity[0]}"
        elif ((tv[0].get() >= 0) and (tv[0].get() <= 360)) == False:
            tmsg.showinfo(title="Warning!", message="The value of alpha is invalid")
            output["text"] = "The value of alpha should lie between 0 and 360 degrees"
        else:
            tmsg.showinfo(title="Warning!", message="The value of delta is invalid")
            output["text"] = "The value of delta should lie between -90 and 90 degrees"
    except TclError:
        tmsg.showinfo(title="Warning!", message="Invalid details have been entered")
        output["text"] = "Enter valid details"
        

# Screen Customization
root = Tk()
root.geometry("950x750")
root.resizable(True, True)
root.minsize(900,750)
root.config(bg="#030303")
root.title("Astro Entity Classifier")           
root.iconbitmap("E:\\Machine Learning\\Astro Entity Classifier\\astro_entity.ico")


# Giving Title
f1 = Frame(root, bg="#030303", highlightbackground="thistle", highlightthickness=2)
f1.pack(fill=X, padx=50, pady=50)
Label(f1, text="Galaxy-Star-Quasar(GSQ) Identifier", fg="peachpuff", bg="#030303", font="Lucida 25 bold").pack(padx=10, pady=10)


# Creating Entries for Astro Entity Features
f2 = Frame(root, bg="#030303", highlightbackground="thistle", highlightthickness=2)
f2.pack(fill=X, ipadx=10, ipady=10, padx=50)
Label(f2, text="1. Enter aplha = Right Ascension angle (at J2000 epoch): "     , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=0, column=0, sticky=W, padx=15, pady=10)
Label(f2, text="2. Enter delta = Declination angle (at J2000 epoch):"          , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=1, column=0, sticky=W, padx=15)
Label(f2, text="3. Enter u = Ultraviolet filter in the photometric system:"    , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=2, column=0, sticky=W, padx=15, pady=10)
Label(f2, text="4. Enter g = Green filter in the photometric system:"          , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=3, column=0, sticky=W, padx=15)
Label(f2, text="5. Enter r = Red filter in the photometric system:"            , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=4, column=0, sticky=W, padx=15, pady=10)
Label(f2, text="6. Enter i = Near Infrared filter in the photometric system:"  , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=5, column=0, sticky=W, padx=15)
Label(f2, text="7. Enter z = Infrared filter in the photometric system:"       , bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=6, column=0, sticky=W, padx=15, pady=10)
Label(f2, text="8. Enter redshift = Value based on the increase in wavelength:", bg="#030303", fg="peachpuff", font=("Lucida", 14, "normal")).grid(row=7, column=0, sticky=W, padx=15)

""" 
Source: SDSS_DR18-SDSS_DR17.csv
97298: [358.095259, 56.24256139, 16.88485, 14.28269, 13.58865, 13.03581, 12.93735, -0.000260102, STAR]
"""
tv = [None]*8
features = [None]*8
initial_features = np.array([358.095259, 56.24256139, 16.88485, 14.28269, 13.58865, 13.03581, 12.93735, -0.000260102])
for i in range(8):
    tv[i] = DoubleVar()
    tv[i].set(initial_features[i])
    features[i] = Entry(f2, textvariable = tv[i], font="Lucida 14 normal", bg="thistle", relief=SUNKEN)
    if i%2 == 0:
        features[i].grid(row=i, column=1, sticky=NSEW, ipady=2,  padx=50, pady=10)
    else:
        features[i].grid(row=i, column=1, sticky=NSEW, ipady=2,  padx=50)

Button(f2, text="RESET", command=resetFeatures, font="Lucida 16 bold", activebackground="gold", bg="deepskyblue", width=15, bd=4, relief=SUNKEN).grid(row=10, column=0, sticky=W, padx=30, pady=10, ipady=3)
Button(f2, text="IDENTIFY", command=predictEntity, font="Lucida 16 bold", activebackground="gold", bg="lime", width=15, bd=4, relief=SUNKEN).grid(row=10, column=0, sticky=E, padx=30, pady=10, ipady=3)

for i in range(8):
    f2.grid_rowconfigure(i, weight=1, pad=5)
f2.grid_columnconfigure(1, weight=1)    


# Labelling the Predicted Entity
f3 = Frame(root, bg="#030303", highlightbackground="thistle", highlightthickness=2)
f3.pack(fill=X, padx=50, pady=20)
output = Label(f3, text="Press RESET for entering new astro entity details", fg="crimson", bg="#030303", font="Lucida 16 bold")
output.pack(padx=10, pady=10)


>>>>>>> 4c06689ce079fb078cb564cdd988ca913f7008bb
root.mainloop()