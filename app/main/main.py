from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

result_list = []

@app.route('/')
def input():
    return render_template('main.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = {}
        result['이름'] = request.form.get('name')
        result['학번'] = request.form.get('StudentNumber')
        result['전공'] = request.form.get('major')
        result['이메일'] = request.form.get('email_id') + "@" + request.form.get('email_addr')
        result['성별'] = request.form.get('gender')
        result['프로그래밍 언어'] = request.form.get('languages')

        result_list.append(result)
        result_list.sort(key=lambda x: x['학번'])  # sort the result_list based on '학번' key
        return render_template('result.html', result_list=result_list)

@app.route('/add_row', methods=['POST'])
def add_row():
    if request.method == 'POST':
        global result_list
        result = {}
        return redirect('/')

    
@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        global result_list
        result_list = []
        return redirect('/')


@app.route('/deleterow', methods=['POST'])
def delete():
    global result_list
    student_numbers = request.json['student_numbers']
    new_result_list = [data for data in result_list if data['학번'] not in student_numbers]
    result_list = new_result_list
    return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)