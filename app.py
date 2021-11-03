from flask import Flask, json, render_template

app = Flask(__name__,static_folder='./static')

# read file
with open('./rushing.json', 'r') as myfile:
    data = myfile.read()

'''
endpoint for returning data from json
'''
@app.route('/somedata')
def datas(): 
    #parsing json string with json.loads method
    if data:
        json_data = json.loads(data) #json_data is a list with dictionaries (rushing.json)
    else: #if json is empty
        return {'data': []}
    
    return {'data': json_data}
        
'''
endpoint for rendering index page with table
'''
@app.route("/")
def index():
    return render_template('index.html', title="NFL Rush")

if __name__ == "__main__":
    app.run(debug=True)

