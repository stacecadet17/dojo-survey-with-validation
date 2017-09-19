from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'concealdontfeeldontletitshow'

@app.route('/')
def form():
    return render_template('survery.html')

@app.route('/results', methods=['POST'])
def results():
    if len(request.form['name']) < 1:
        flash("must enter a name!")

    elif len(request.form['comment']) < 1:
        flash("must enter a comment!")

    elif len(request.form['comment']) > 120:
        flash("comment is too long!")

    else:
        return render_template('results.html', Name = session['name'], Location = session['location'], Language = session['language'], Comment = session['comment'])
    return redirect('/')

app.run(debug=True)
