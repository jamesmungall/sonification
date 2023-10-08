# NASA-Hackathon-2023

This code takes an image of the sun seen by Solar Orbiter, puts it into greyscale, finds all pixel values on that image (by assigning the image with rows and columns, and iterating through them from left to right) and then saves the pixel values and frequencies which can be viewed on a table on the front-end, or downloadable via CSV.

"Pixel Value" represents the intensity value of the pixels in the grayscale image (ranging from 0 to 255). "Frequency" represents how many pixels in the image have that particular intensity value.

The image I have been using to test this is just a 17 nanometer sun image taken off of Google:
[Source](https://www.esa.int/ESA_Multimedia/Images/2022/03/The_Sun_in_high_resolution)


If you want to use this tool on your local desktop (As I have not had time to upload the backend to any online hosting system yet)
You will need to ensure you have installed Python and the following packages via a pip install:

pip install Flask opencv-python-headless matplotlib

Also, to run the app, use the VSCode terminal (or your preferred IDE) and type: python app.py

It should open up in your browser, running on http://127.0.0.1:5000 or whatever your port set up is. 