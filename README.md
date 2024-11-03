# Astro Entity Classifier

## __Overview__
In astronomy, stellar classification is the classification of stars based on their spectral characteristics. The classification scheme of galaxies, quasars, and stars is one of the most fundamental in astronomy. The early cataloguing of stars and their distribution in the sky has led to the understanding that they make up our own galaxy and, following the distinction that Andromeda was a separate galaxy to our own, numerous galaxies began to be surveyed as more powerful telescopes were built. In our present work, we present __Astro Entity Classifier__ , a machine learning application developed using [Python](https://www.python.org/downloads/release/python-3125/) and [Tkinter](https://docs.python.org/3/library/tkinter.html), designed to classify astronomical entities as stars, quasars, or galaxies based on their celestial coordinates, photometric color indices, and redshift. 

## __Features__
- User-friendly GUI built with [Tkinter](https://docs.python.org/3/library/tkinter.html).
- Inputs for celestial co-ordinates, photometric color indices, and redshift.
- Predicts the class of the celestial object using the [Bagging Classifier](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.BaggingClassifier.html) algorithm.
- Application has been packaged into an executable file using [cx_Freeze](https://cx-freeze.readthedocs.io/en/stable/).

## __Installation__
To run the application:
1. Download the build folder and locate the Astro_Entity_Classifier.exe file which is present inside the exe.win-amd64-3.12 folder.
2. Double click on it.

## __Usage__
1. Launch the executable file.
2. Enter the required parameters:
* Right Ascension (alpha)
* Declination (delta)
* Photometric indices (u, g, r, i, z)
* Redshift value
3. Click "IDENTIFY" to classify the astronomical entity.
4. Press "RESET" to clear the inputs for new data.

## __Development__
This project was developed by [Rishikesh G. Jha](https://github.com/rjlovespy) and [Abhishek G. Jha](https://github.com/govind663) as part of an initiative to leverage machine learning techniques for astronomical classifications. The model was trained on data sourced from the [SDSS DR17 via kaggle](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17).

## __License__
This project is licensed under the [CC BY-NC 4.0](https://github.com/rjlovespy/Astro-Entity-Classifier?tab=License-1-ov-file#readme) License.

## __Acknowledgments__
* [Sloan Digital Sky Survey (SDSS)](https://www.sdss4.org/science/image-gallery/) for providing the data used in training the model.
* [Scikit-learn](https://scikit-learn.org/stable/) for machine learning algorithms.
* [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
* [cx_Freeze](https://cx-freeze.readthedocs.io/en/stable/) for creating the executable file.
