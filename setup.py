""" 
@Note:- 
1. cx_Freeze 7.2.4 has compatibilty issues with python 3.13.0 so I used python 3.12.5 which works well with cx_Freeze 7.2.4
2. If you this issue too then just uninstall python 3.13.0 and install python 3.12.5

@Note:- To create .exe file from .py file, follow these steps:
        step-1: Do the necessary changes mentioned in the comments in this setup.py file only
        step-2: Open powershell or cmd in your ML project folder and run the follwoing command:
                python setup.py build
"""
import sys, os
from cx_Freeze import setup, Executable


# Give the absolute path of your .py file whose .exe you want
script_file = "E:\\Machine Learning\\Astro Entity Classifier\\Astro_Entity_Classifier.py"


# Include necessary files such as .ico file, .joblib files, your_own_defined_package.py(like here Outliers.py)
include_files = [
    "E:\\Machine Learning\\Astro Entity Classifier\\astro_entity.ico",  
    "E:\\Machine Learning\\Astro Entity Classifier\\Model.joblib",
    "E:\\Machine Learning\\Astro Entity Classifier\\pre_processor.joblib",
    "E:\\Machine Learning\\Astro Entity Classifier\\Outliers.py",
    "C:\\Windows\\System32\\vcomp140.dll"  # Don't touch this line: It includes vcomp140.dll for sklearn 
]


# Add the packages your project uses
packages = ["tkinter", "joblib", "pandas", "matplotlib", "numpy", "scienceplots", "sklearn", "ctypes"]    # Don't touch ctypes


# Add the submodule you use in your project
build_exe_options = {
    "include_files": include_files,
    "packages": packages,
    "includes": [
        "sklearn.ensemble",
        "sklearn.preprocessing",
        "sklearn.impute",
        "sklearn.model_selection",
        "sklearn.pipeline",
        "sklearn.metrics",
        "sklearn.tree",
        "pandas.plotting",
        "matplotlib.pyplot",
        "ctypes",
        "tkinter.messagebox"
    ],
    "include_msvcr": True                # Don't touch this line
}


""" 
Prevents black console from appearing
"""
base = None
if sys.platform == "win32":
    base = "Win32GUI"


# Change application anme, version, dexcription and icon file absolute path
setup(
    name="Astro Entity Classifier",
    version="1.0",
    description="A Tkinter GUI that uses an ML model trained on Bagging Classifier",
    options={"build_exe": build_exe_options},
    executables=[Executable(script_file, base=base, icon="E:\\Machine Learning\\Astro Entity Classifier\\astro_entity.ico")]
)