from flask import Flask,render_template

fai=Flask(__name__)

@fai.route('/mahesh')
def mahesh():
    return render_template('mahesh.html')

@fai.route('/pavan')
def pavan():
    return render_template('pavan kalyan.html')
    
fai.run(debug=True)
