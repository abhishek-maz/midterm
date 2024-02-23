# Import flask module to render the application.
from flask import Flask

# Create an app. 
app = Flask(__name__)
 
# App route created as per requirements.
@app.route('/')
def index():
    company_name = "Wild Rydes"
    developer_name = "Abhishek Mazumdar"
    student_id = "100938587"
    return f"Company Name: {company_name}<br>Developer: {developer_name}<br>Student ID: {student_id}"

# Run it on port 8080 on local host. 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)