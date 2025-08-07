# Heart Disease Prediction Project

This project analyzes the Heart Disease dataset from the UCI Machine Learning Repository to predict the presence of heart disease in patients using various machine learning techniques.

## 📋 Project Overview

This is a comprehensive data science project that performs:
- **Data Exploration & Analysis**: Understanding the dataset structure and relationships
- **Feature Selection**: Identifying the most relevant features for prediction
- **Machine Learning**: Implementing various classification algorithms including:
  - K-Nearest Neighbors (KNN)
  - Logistic Regression
  - Random Forest
  - Decision Tree
- **Model Evaluation**: Comparing model performance and selecting the best approach

## 🚀 Quick Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

#### Option 1: Automated Setup (Recommended)
```bash
python3 setup.py
```
This will automatically install all dependencies and download the dataset.

#### Option 2: Manual Setup

1. **Clone or download this repository** to your local machine

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset** (if not already present):
   The dataset is already available as `heart.csv` in the project directory.

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

5. **Open the notebook:**
   Open `HeartCSV (2).ipynb` in your Jupyter environment

## 📊 Dataset Information

The dataset contains **303 patient records** with **14 attributes**:

### Features:
- **age**: Age in years
- **sex**: Gender (1 = male, 0 = female)
- **cp**: Chest pain type (0-3)
- **trestbps**: Resting blood pressure (mm Hg)
- **chol**: Serum cholesterol (mg/dl)
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina (1 = yes, 0 = no)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: Slope of the peak exercise ST segment (0-2)
- **ca**: Number of major vessels colored by fluoroscopy (0-3)
- **thal**: Thalium stress test result (3, 6, 7)

### Target:
- **num**: Heart disease status (0 = no disease, 1-4 = presence of disease)

## 🔧 Dependencies

The project requires the following Python packages (automatically installed via `requirements.txt`):

```
numpy>=1.21.0
pandas>=1.3.0
seaborn>=0.11.0
matplotlib>=3.4.0
scikit-learn>=1.0.0
mlxtend>=0.19.0
jupyter>=1.0.0
notebook>=6.4.0
```

## 📈 Analysis Workflow

1. **Data Import & Exploration**
   - Load and examine the dataset
   - Check for missing values
   - Basic statistical analysis

2. **Data Visualization**
   - Correlation analysis
   - Distribution plots
   - Feature relationships

3. **Feature Engineering**
   - Feature selection using various techniques
   - Data preprocessing for machine learning

4. **Model Training & Evaluation**
   - Multiple classification algorithms
   - Cross-validation
   - Performance metrics comparison

5. **Results & Conclusions**
   - Best performing model identification
   - Feature importance analysis
   - Clinical insights

## 🎯 Usage

1. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Open the main notebook:**
   - Navigate to `HeartCSV (2).ipynb`
   - Run cells sequentially from top to bottom

3. **Explore the analysis:**
   - Each section is clearly documented
   - Modify parameters to experiment with different approaches
   - View visualizations and model results

## 📝 Key Results

The notebook provides comprehensive analysis including:
- **Correlation matrices** showing relationships between variables
- **Feature selection results** identifying the most predictive variables
- **Model comparison** with accuracy metrics
- **Clinical insights** about heart disease risk factors

## 🤝 Contributing

Feel free to:
- Fork the repository
- Experiment with different models
- Add new visualizations
- Improve the analysis

## 📚 References

- **Dataset Source**: UCI Machine Learning Repository
- **Original Study**: Detrano, R. et al. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease.
- **Dataset Citation**: Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). Heart Disease [Dataset]. UCI Machine Learning Repository.

## 📞 Support

If you encounter any issues:
1. Ensure all dependencies are installed correctly
2. Check that `heart.csv` is in the project directory
3. Verify your Python version is 3.7 or higher
4. Make sure Jupyter is properly installed and running

---

**Author**: Analysis by Oluwadamilare Tobiloba  
**Project Type**: Data Science / Machine Learning  
**Domain**: Healthcare Analytics