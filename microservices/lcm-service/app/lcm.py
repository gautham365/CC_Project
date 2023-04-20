from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Lcm(Resource):
    def get(self, num1,num2):
        greater = max(num1, num2)
        smallest = min(num1, num2)
        for i in range(greater, num1*num2+1, greater):
            if i % smallest == 0:
                return {'result': i}

api.add_resource(Lcm, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5057)