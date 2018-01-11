from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/api')
def myFirst():
    return jsonify({'Det her lort virker sku':'fuck yes'})

if __name__ == '__main__':
    app.run()

