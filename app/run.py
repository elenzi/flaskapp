import os
from flask import Flask
app = Flask(__name__)
from System_Info import __main__

@app.route('/')

def main():
    print(__main__.main())
    return __main__.main()+""


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)