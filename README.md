# 🛡️ Wireless Sensor Network (WSN) Attack Detection using Machine Learning

This project focuses on detecting various cyberattacks in **Wireless Sensor Networks (WSNs)** using supervised machine learning. It features a trained model deployed through a **Flask-based web application** that classifies input data into either normal behavior or one of several types of attacks.

---

## 📁 Project Structure

For the website only

project/

├── static/

│ └── style.css

├── templates/

│ ├── about.html

│ ├── contact.html

│ ├── dashboard.html

│ ├── home.html

│ ├── login.html

│ ├── predict.html

│ └── signup.html

├── app.py

└── model.pkl



---

## 🚀 Features

- ⚙️ Real-time attack prediction via web interface
- 🔐 User authentication (Login & Signup)
- 📊 Dashboard with prediction history and analysis
- 🧠 Integrated ML model trained on labeled WSN dataset
- 📂 Visualization using Matplotlib and Power BI
- 🗂️ SQL Server database connectivity

---

## 🧠 Machine Learning Algorithms Used

1. **Logistic Regression**
   - Used as a baseline model
   - Efficient and interpretable
   - Good for binary and multiclass tasks

2. **Random Forest Classifier** ✅ *(Best Performer)*
   - Ensemble of decision trees
   - Achieved accuracy > 95%
   - Robust and scalable

3. **AdaBoost Classifier**
   - Boosts weak learners to improve accuracy
   - Effective on complex and imbalanced data
   - Second-best performance

---

## 🔧 Tech Stack

- **Backend:** Python 3.10+, Flask
- **Frontend:** HTML5, CSS3, Bootstrap, JavaScript
- **ML Libraries:** scikit-learn, pandas, numpy
- **Database:** SQL Server (via pyodbc)
- **Visualization:** Matplotlib, Power BI

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

git clone https://github.com/your-username/wsn-attack-detection.git
cd project



2. Create a Virtual Environment (Optional)

       python -m venv venv
       venv\Scripts\activate   # For Windows



3. Install Dependencies

         pip install -r requirements.txt




4. Configure SQL Server in app.py

pyodbc.connect(

    'DRIVER={ODBC Driver 17 for SQL Server};'
    
    'SERVER=YourServerName;'
    
    'DATABASE=WSN_Database;'
    
    'Trusted_Connection=yes;'
)




5. Start the Web App

       python app.py




📊 Dataset Info
✅ 300,000+ labeled records

✅ Features include:

Distance to Cluster Head

Energy Usage

Packet Transmission Stats

Node Role (CH or not)

✅ Attack Classes:

Normal

Blackhole

Grayhole

Flooding

Scheduling (TDMA)



📷 Screenshots
![flow](https://github.com/user-attachments/assets/2dfd2946-90ca-4fe3-b503-92f0338efc32)
![signup](https://github.com/user-attachments/assets/8ce68810-4187-494c-858b-02025c2a9c90)
![Login page](https://github.com/user-attachments/assets/57ed8899-4e3c-44a3-8e87-4537f9dff1ce)
![Home page](https://github.com/user-attachments/assets/bf533838-48cb-4b3b-ad22-aa3996aec7de)
![Prediction page](https://github.com/user-attachments/assets/939c207d-bb9e-4baf-b107-ccb25888fd59)



🔮 Future Enhancements
Live WSN data integration

Deep learning model support (CNN, LSTM)

Deployment on edge devices

Interactive dashboards using Plotly or Dash

Integration with alerting systems

👨‍💻 Author

Jayashree V

Gokul Raj M

Divkar G

🎓 Final Year Student,Dhanalakshmi College of Engineering

📧 Email: your-gimzrofficial@gmail.com





