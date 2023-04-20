from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Gcd(Resource):
    def get(self, num1, num2):
        if(num1 == 0):
            return num2
        elif(num2 == 0):
            return num1
        while (num1 != num2):
            if (num1 > num2):
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return {'result': num1}

api.add_resource(Gcd, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5056)