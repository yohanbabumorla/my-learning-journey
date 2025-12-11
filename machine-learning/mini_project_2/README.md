🏠 House Price Prediction
A mini project that predicts house prices using regression models.
Built with Python in a Jupyter Notebook, this project demonstrates data preprocessing, model training, evaluation, and visualization.

📌 Project Overview
The goal of this project is to predict house prices based on given features using machine learning techniques.
It applies regression modeling with scikit-learn, supported by data manipulation and visualization libraries.

⚙️ Tech Stack
- Language: Python
- Environment: Jupyter Notebook
- Libraries Used:
- pandas → for handling and manipulating data frames
- scikit-learn → for regression modeling, train-test split, and evaluation using r2_score
- numpy → for converting predicted prices from floating-point (double) to integers
- matplotlib → for plotting scatter plots between predicted and actual prices

🚀 Features
- Data preprocessing and cleaning with pandas
- Regression model implementation using scikit-learn
- Evaluation of model performance with R² score
- Conversion of predicted values to integers using numpy
- Visualization of predicted vs. actual prices with scatter plots

📊 Workflow
<img width="1024" height="1536" alt="workflow" src="https://github.com/user-attachments/assets/d3d74d7f-1122-48bb-a778-d978e9155b56" />

- Data Loading → Import dataset into pandas DataFrame
- Preprocessing → Handle missing values, feature selection
- Model Training → Train regression model using scikit-learn
- Evaluation → Measure accuracy with R² score
- Prediction Conversion → Convert floating-point predictions to integers using numpy
- Visualization → Plot scatter graph of predicted vs. actual prices

📈 Example Output
- Scatter Plot: Shows the relationship between predicted and actual house prices
- R² Score: Evaluates how well the regression model fits the data

🖥️ How to Run
- Clone this repository:
git clone https://github.com/yohanbabumorla/my-learning-journey/machine-learning/mini_project_2/house-price-prediction.git
- Navigate to the project folder:
cd house-price-prediction
- Install required libraries:
pip install pandas scikit-learn numpy matplotlib
- Open the Jupyter Notebook:
jupyter notebook HousePricePrediction.ipynb



📌 Future Improvements
- Add more advanced models (e.g., Random Forest, XGBoost)
- Hyperparameter tuning for better accuracy
- Deploy as a web app using Flask or Streamlit


🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

📜 License
This project is licensed under the MIT License.
