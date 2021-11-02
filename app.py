from flask import Flask, json, render_template,request,jsonify

app = Flask(__name__)

# read file
with open('./rushing.json', 'r') as myfile:
    data = myfile.read()



@app.route("/")
def index():
    #parsing json string with json.loads method
    #result creates a Python dictionary 
    json_data = json.loads(data)
    #json_data is a list with dictionaries
    return render_template('index.html', title="page", jsonfile=json_data)


if __name__ == "__main__":
    app.run(debug=True)

