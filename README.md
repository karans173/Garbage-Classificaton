# Garbage-Classificaton

**Introduction**

This project aims to classify different types of household garbage into 12 distinct categories using machine learning techniques. The goal is to improve the recycling process by accurately sorting garbage into groups that share similar recycling processes.

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
