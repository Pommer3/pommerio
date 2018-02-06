from flask import Flask, jsonify
from ProgrammingDone import ProgrammingDone

app = Flask(__name__)

@app.route('/api')
def myFirst():
    return jsonify({'Det her virker':' yes'})

@app.route('/api/add_programming_hour/<user>')
def incrementPHours(user):
    programmingDone = ProgrammingDone()
    return programmingDone.incrementProgrammingHour(user)

if __name__ == '__main__':
    app.run()

