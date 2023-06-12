from flask import Flask
from Insurance.logger import logging

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("testing logging file")
    return "tested"

if __name__=="__main__":
    app.run(debug=True)