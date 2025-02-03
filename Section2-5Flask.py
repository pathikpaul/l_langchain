from flask import Flask,render_template, request
import json
import random
app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def hello_world():
    if request.method == "POST":
        search_text = request.form.get("name")
        splitInp = search_text.split()
        mydict={}
        plist=[]
        mydict["hellostr"] = "Hello " + search_text
        mydict["persons"]=plist
        for i in range(1,random.randint(2,10)):
            age=random.randint(1,90)
            if len(splitInp) >= 2:
                pdict={"first_name": splitInp[0]+"_"+str(i),    "last_name": splitInp[1]+"_"+str(i),    "age": age}
            elif len(splitInp) >= 1:
                pdict = {"first_name": splitInp[0]+"_"+ str(i), "last_name": "", "age": age}
            else:
                pdict = {"first_name": "", "last_name": "", "age": age}
            plist.append(pdict)
    else:
        data_str = '''
        {"persons":[],"hellostr": ""}
        '''
        mydict = json.loads(data_str)
    return render_template('index1.html',person_list=mydict)


if __name__ == '__main__':
    app.run(debug=True,port=8080)