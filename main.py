from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)

app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html> 
        <head>
            <style>
                form{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius:10px;
                }
                textarea{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
        <form method='post'>
        <label>Rotate by:
        <input type="text" name="rot" value="0"/>
        </label>
        <textarea name="text" ></textarea>
        <input type="submit">
        </body>
    </html>"""            


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    text=request.form["text"]
    
    rot=request.form["rot"]
    

    rotated=rotate_string(text,int(rot))
    
    return "<h1>{0}</h1>".format(rotated)
    



app.run()    