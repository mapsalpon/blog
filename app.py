from flask import Flask, render_template, redirect, request

app = Flask(__name__)

posts = [{
        'name': 'Graviton',
        'text': """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.""",
        'date': '9 may'}] * 2


@app.route('/')
def index():
    global posts
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def adding():
    if (request.method == 'GET'):
        return render_template('add.html')

    # POST
    global posts

    posts.append({
        'name': request.form['name'],
        'text': request.form['text'],
        'date': request.form['date']})

    return redirect('/')


app.run()
