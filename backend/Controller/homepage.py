from flask_restful import Resource, abort

class HomePage(Resource):
    def get(self):
        try:
            return {"Message": "Welcome Ohaiyo!!!"}
        except Exception as exc:
            print("Error in Homepage", exc)
            return abort(401)

    def post(self):
        try:
            return {"Message": None}
        except Exception as exc:
            print("Error in Homepage", exc)
            return abort(401)