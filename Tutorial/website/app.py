from flask import Flask , render_template 
  
app = Flask(__name__)
student = {"fname":"abebe","lname":"kebede"}
 
@app.route('/') 
def home():  
    return render_template('home.html' ,stud = student)
  
@app.route('/about') 
def about():  
    return render_template('about.html')
  
@app.route('/abebe') 
def abebe():  
    return render_template('abebe.html')
  
if __name__ =='__main__':  
    app.run(debug = True)