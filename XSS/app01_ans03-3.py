from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import config

app = Flask(__name__)

# ตั้งค่า secret_key จากไฟล์คอนฟิก
app.config.from_object(config)

class SearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.query.data
        return render_template('search03.html', query=query)
    return render_template('index03.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
