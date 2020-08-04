from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

#print(url_for('static', filename='home.ico'))  #{{}} in html is an expression for python execution, check index.html
@app.route('/')
def homepage():
	return render_template('index.html')
    #return 'Hello, HTC!'


def write_to_file(data):
	with open('database.txt', mode= 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
	with open('database.csv', mode = 'a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])



@app.route('/<string:htmlname>')
def hello_world(htmlname):
	return render_template(htmlname)
    #return 'Hello, HTC!'

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		#write_to_file(data)
		write_to_csv(data)
		return redirect('/thank_you.html')
