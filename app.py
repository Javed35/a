from flask import Flask,request,render_template

app=Flask(_name_)

@app.route("/",methods=["get","post"])
def index():
  return(render_template("index.html"))

if_name_=="_main_":
  app.run()
