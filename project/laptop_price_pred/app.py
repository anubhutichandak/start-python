from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Route for home page - shows the laptop table
@app.route('/')
def home():
    # Load CSV data
    df = pd.read_csv('laptop_data.csv')
    # Convert to HTML table (with Bootstrap styling)
    table_html = df.to_html(classes='table table-striped table-bordered', index=False, border=0)
    return render_template('index.html', table=table_html)

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# History page
@app.route('/history')
def history():
    return render_template('history.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Project page
@app.route('/project')
def project():
    return render_template('project.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
