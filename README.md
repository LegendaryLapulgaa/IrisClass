# 🌸 Iris Flower Classification with Machine Learning

This project is a supervised machine learning solution to classify **Iris flower species** — *Setosa*, *Versicolor*, and *Virginica* — based on sepal and petal measurements. The project demonstrates a full ML pipeline, from data preprocessing to model deployment, using Python and Scikit-learn.

---

## 🎯 Objectives

- Load and explore the Iris dataset
- Visualize data distributions and relationships
- Train and compare classification models (e.g., Logistic Regression, Decision Trees, KNN)
- Evaluate model performance
- Save and load the best model using `joblib`
- Make predictions on new input data

---

## 🛠️ Technologies Used

- Python 3.x
- Scikit-learn
- Pandas & NumPy
- Matplotlib & Seaborn
- Joblib (for model serialization)
- Jupyter Notebook / VSCode

---

## 📊 Dataset

The dataset contains 150 rows of measurements and the corresponding species of the Iris flower. Features include:
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)
- Species (Target)

---

## 🚀 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/iris-flower-classification.git
   cd iris-flower-classification

   ---

   
## 🧠 Sample Prediction

# Load model and predict

import joblib

model = joblib.load('iris_model.pkl')

sample = [[5.1, 3.5, 1.4, 0.2]]

print(model.predict(sample))  # Output: ['setosa']

---

## 📄 Documentation

Iris_Classification_Project.docx: Contains a professional report overview of the project.

Iris_Classification_Presentation.pptx: Presentation slide deck for summary and sharing.


---

## 📝 License

This project is open source under the MIT License.

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## ✍️ Author

Github – @LegendaryLapulgaa
