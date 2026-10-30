# Social Media Sentiment Analysis — Beginner Project

## What this project does
- Accepts a text post typed by the user.
- Uses NLP TF-IDF features and a Logistic Regression classifier to predict positive, negative, or neutral.
- Shows counts from a small included teaching dataset.
- Offers a simple holdout evaluation and confusion matrix.

## Important limitation
The included CSV is a small educational sample made for demonstrating the project workflow. It is not a representative social-media dataset and its scores must not be reported as research findings. For a research paper, use a suitable larger labelled dataset with permission and document its source.

## Run on Windows
1. Install Python (preferably Python 3.11 or 3.12 for broad library compatibility) and VS Code.
2. Extract this ZIP to a folder.
3. Open the extracted folder in VS Code.
4. Open Terminal → New Terminal.
5. Create a virtual environment:
   `py -m venv .venv`
6. Activate it in PowerShell:
   `.\.venv\Scripts\Activate.ps1`
   If PowerShell blocks activation, try Command Prompt terminal and run:
   `.venv\Scripts\activate.bat`
7. Install dependencies:
   `python -m pip install -r requirements.txt`
8. Run the app:
   `python -m streamlit run app.py`
9. A browser tab should open with the dashboard. If not, copy the local URL shown in the terminal into your browser.

## If installation fails
Copy the full error message and send it for troubleshooting. Avoid installing many packages one by one without checking the error.

## Technologies
- Python
- pandas for loading the dataset
- scikit-learn for TF-IDF and Logistic Regression
- Streamlit for the interactive interface
- Matplotlib for a confusion-matrix visualization

## Suggested next improvements
- Replace sample data with a suitable, licensed labelled social-media dataset.
- Compare Naive Bayes, Logistic Regression, and SVM.
- Add error analysis and discuss sarcasm, negation, slang, and multilingual text.
