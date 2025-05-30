# Wireless Sensor Network Attack Detection using Machine Learning
This project focuses on detecting various attacks in Wireless Sensor Networks (WSNs) using machine learning algorithms. The system uses a dataset of sensor network activities and classifies network behavior into normal or attack types (e.g., Blackhole, Grayhole, Wormhole, Sybil, Hello Flood) using multi-class classification. It includes a web-based interface for real-time predictions.

🧠 Features
Preprocessing and training on a labeled WSN dataset

Multiple machine learning models (e.g., Random Forest, Decision Tree)

Real-time prediction via web interface

Attack classification into 6 types

Accuracy metrics to evaluate models

Deployment using Flask (Python)

Visualizations of data and results

📁 Project Structure
php
Copy
Edit
wsn-attack-detection/
│
├── dataset/                  # Sensor network dataset (CSV)
├── models/                   # Trained ML models (.pkl files)
├── static/                   # CSS, JS, images
├── templates/                # HTML templates (UI)
├── app.py                    # Flask application
├── train_model.py            # Script to train and evaluate models
├── preprocess.py             # Data cleaning and preprocessing
└── README.md                 # Project documentation
⚙️ Technologies Used
Python 3.x

Scikit-learn

Pandas, NumPy

Matplotlib, Seaborn

Flask

HTML5, CSS3, JavaScript

📊 Machine Learning Models
Random Forest Classifier

Decision Tree

Naive Bayes

Logistic Regression

Evaluation using accuracy, precision, recall, and F1-score.

🚀 How to Run the Project
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/wsn-attack-detection.git
cd wsn-attack-detection
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Train the Model
bash
Copy
Edit
python train_model.py
4. Run the Web App
bash
Copy
Edit
python app.py
Open your browser and navigate to http://127.0.0.1:5000

🔍 Dataset
The dataset includes the following features:

Node ID, Neighbor count, Transmission range, Energy

Packet delivery ratio, Forwarding rate

Labeled as: Normal, Blackhole, Grayhole, Wormhole, Sybil, Hello Flood

📷 Screenshots
Add screenshots of your UI here (if available)

📚 Future Improvements
Integrate deep learning models

Extend to real-time sensor network simulations

Add user authentication for the web interface

Improve dataset size and variety

👨‍💻 Authors
Gokul Raj M

Final Year Student, Anna University

📜 License
This project is licensed under the MIT License.
