# Garbage-Classificaton

**About Project**

This kernel shows how to classify Garbage images into 12 different classes using transfer learning. I also created a webapp that can classify garbage images based on the model trained here.

Transfer learning means that instead of your model learning everything from scratch, it uses another model that was trained on a similar problem, so that you can "transfer" the learned "knowledge" of the pretrained model to your model, and then learn some new features.

The ImageNet Data set is huge data set consisting of more than 14 million images from more than 22,000 different categories, here we are using a smaller version of it which has 1000 different categories.

In this kernel we use an xception model which is pretrained on the ImageNet dataset and then build some layers on top of it to be able to classify the garbage images.

Transfer learning makes sense here because the ImageNet data set has a much larger number of images (14 million) than the Garbage Classification data set (around 15,500 image). This increases the speed of training for our model and the accuracy of our predictions.

**Dataset**

The dataset used in this project is available on Kaggle at [Garbage Classification (12 classes)](https://www.kaggle.com/datasets/mostafaabla/garbage-classification). It contains 15,150 images across 12 classes of household garbage:

- Paper
- Cardboard
- Biological
- Metal
- Plastic
- Green Glass
- Brown Glass
- White Glass
- Clothes
- Shoes
- Batteries
- Trash

The dataset was collected through web scraping and other sources, with the aim of providing a comprehensive set of images for training and testing the classification model.

**Project Structure**

The project consists of the following key components:

- **train(collab).ipynb**: This Jupyter Notebook contains the code for training the garbage classification model. It includes data preprocessing, model building, training, and evaluation steps.
- **app.py**: This Python script is used to create a web application for real-time garbage classification. It leverages the trained model to classify new images uploaded by users.
- **static/**: This directory contains static files used by the web application, including `styles.css` for styling and other assets.
- **templates/**: This directory contains HTML templates used by the web application, including `index.html` for the main page.
- **README.md**: This file provides an overview of the project, including instructions for setup, usage, and contributing.

**Setup**

To run this project, you will need the following:

1. **Python Environment**: Ensure you have Python installed on your system. We recommend using a virtual environment to manage dependencies.
2. **Dependencies**: Install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```
3. **Dataset**: Download the dataset from the Kaggle link provided and place it in the `data/` directory.

**Training the Model**

To train the model, follow these steps:

1. Open the `train(collab).ipynb` notebook in a Jupyter environment.
2. Run the cells sequentially to preprocess the data, build the model, train it, and evaluate its performance.

**Running the Web Application**

To run the web application, follow these steps:

1. Ensure you have the trained model saved in the `models/` directory.
2. Open a terminal and navigate to the project directory.
3. Run the following command to start the Flask server:
   ```bash
   python app.py
   ```
4. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

**Web Application Files**

- **index.html**: This file is the main HTML template for the web application. It provides a user interface for uploading images and displaying classification results.
- **styles.css**: This file contains the CSS styles for the web application, ensuring a visually appealing and user-friendly interface.

**Usage**

1. Upload an image of garbage through the web application.
2. The application will classify the image into one of the 12 categories and display the result.

**Contributing**

We welcome contributions to improve this project. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to merge your changes into the main repository.

**Acknowledgements**

- The dataset used in this project is sourced from [Garbage Classification (12 classes)](https://www.kaggle.com/datasets/mostafaabla/garbage-classification) on Kaggle.
- Special thanks to the original contributors of the dataset and the developers of the libraries and frameworks used in this project.

**License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance!
