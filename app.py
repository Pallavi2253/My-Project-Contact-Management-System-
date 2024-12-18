from flask import Flask,request,url_for,redirect,render_template
app=Flask(__name__)
users={"kousarnaazm@gmail.com":{"username":"kousarnaaz","phoneno":8753947201,"password":"k21@1234"}}
@app.route('/')
def home():
    return render_template('welcome.html') 
@app.route("/create",methods=["GET","POST"])
def create():
    if request.method=="POST":
        print(request.form)
        username=request.form["uname"]
        email=request.form["email"] 
        phoneno=request.form["phone"]
        password=request.form["pwd"]
        cpassword=request.form["cpwd"]
        if email not in users:
            users[email]={"username":username,"phoneno":phoneno,"password":password} #here email is key
            print(users)
            return redirect(url_for("login"))
        else:
            return "this account already exist"        
    return render_template("create.html")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        print(request.method)
        username=request.form["usname"]
        phoneno=request.form["phone"]
        password=request.form["pwd"]
        email=request.form["email"]
        print(email)
        if email in users:
            if username==users[email]["username"]:
                if phoneno==users[email]["phoneno"]:
                    if password==users[email]["password"]:
                        return redirect(url_for("dashboard",pemail=email))
                    else:
                        return "wrong password"
                else:
                    return "wrong phone number"
            else:
                return "wrong username"
        else:
            return "wrong email"
    return render_template("login.html")
@app.route("/dashboard/<pemail>")
def dashboard(pemail):
    return render_template("dashboard.html",pemail=pemail)
@app.route("/addcontacts/<pemail>",methods=["GET","POST"])
def addcontacts(pemail):
    if request.method=="POST":
        username=request.form["name"]
        email=request.form["email"]
        phoneno=request.form["phone"]
        if username in users:
            return "username already exists"
        elif email in users:
            return "email already exists"
        elif phoneno in users:
            return "phone number already exists"
        else:
            users[pemail]={"username":username,"email":email,"phoneno":phoneno}
            return render_template("dashboard.html",pemail=pemail)
    return render_template("add_contacts.html")
@app.route("/editcontact/<pemail>", methods=["GET", "POST"])
def editcontact(pemail):
    if request.method == "POST":
        username = request.form["name"]
        email = request.form["email"]
        phoneno = request.form["phone"]
        users[pemail]["username"] = username
        users[pemail]["email"] = email
        users[pemail]["phone"] = phoneno
        return render_template("dashboard.html", pemail=pemail)
    else:
        user_info = users.get(pemail)
        return render_template("edit_contact.html", user_info=user_info)
@app.route("/viewcontacts", methods=["GET"])  
def viewcontacts():
    return render_template('view_contacts.html',data=users)
@app.route('/delete/<pemail>')
def delete(pemail):
    users.pop(pemail)
    return redirect(url_for('home'))

app.run(use_reloader=True,debug=True) 

