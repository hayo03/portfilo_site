from flask import Flask, render_template, send_from_directory
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('Portfolio.html')
'''
#Serve static files (css, images)
@app.route('/static/<path:style.css>')
def serve_static(style.css):
    return send_from_directory('static','style.css')
'''

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')