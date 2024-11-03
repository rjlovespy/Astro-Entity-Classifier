# Astro Entity Classifier

## __Overview__
In astronomy, stellar classification is the classification of stars based on their spectral characteristics. The classification scheme of galaxies, quasars, and stars is one of the most fundamental in astronomy. The early cataloguing of stars and their distribution in the sky has led to the understanding that they make up our own galaxy and, following the distinction that Andromeda was a separate galaxy to our own, numerous galaxies began to be surveyed as more powerful telescopes were built.       
The __Astro Entity Classifier__ is a machine learning application developed using Python and Tkinter, designed to classify astronomical entities as stars, quasars, or galaxies based on their celestial coordinates, photometric color indices, and redshift. 

## __Features__
- User-friendly GUI built with Tkinter.
- Inputs for celestial co-ordinates, photometric color indices, and redshift.
- Predicts the class of the celestial object using the Bagging Classifier algorithm.
- Application has been packaged into an executable file using cx_Freeze.

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
This project was developed by [Rishikesh G. Jha](https://github.com/rjlovespy) as part of an initiative to leverage machine learning techniques for astronomical classifications. The model was trained on data sourced from the [SDSS DR17 via kaggle](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17).

## __License__
This project is licensed under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en) License. See the [LICENSE](https://github.com/rjlovespy/Astro-Entity-Classifier?tab=License-1-ov-file#readme) file for more details.
