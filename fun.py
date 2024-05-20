from flask import Flask , render_template , request

a = Flask(__name__)

@a.route('/')
@a.route('/home')
def fun():
    return render_template('web.html')

@a.route('/submit',methods = ['POST'])
def f():
    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('age')
        return render_template ('sub.html',name=n,age=a)

    

if __name__ == '__main__':
    a.run(debug=True)
