from flask import Flask
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    return 'hello world'

@app.route('/myname',methods=['GET','POST'])
def show_my_name():
    return 'yuanmengni'

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)
