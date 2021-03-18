from flask.globals import request
from flask_restful import Resource, abort
from Controller import nb_model, label_encode
import requests
from core import text_preprocess
from newspaper import Article

class DetectCategory(Resource):
    def post(self):
        try:
            res = {}
            url = request.json.get("url")
            article = Article(url)
            article.download()
            article.parse()
            document = article.text 
            document = text_preprocess(document)
            print("Data", document)
            if document == "":
                category_list_predict = [] 
                for idx in range(0,18):
                    temp_dict = {}
                    temp_dict["label"] = label_encode[idx] 
                    temp_dict["y"] = 0
                    category_list_predict.append(temp_dict)
                res["category"] = category_list_predict
            else:
                label_predict_index = nb_model.predict_proba([document])
                category_list_predict = [] 
                for idx in range(0,18):
                    temp_dict = {}
                    temp_dict["label"] = label_encode[idx] 
                    temp_dict["y"] = round(label_predict_index[0][idx], 2)
                    category_list_predict.append(temp_dict)
                res["category"] = category_list_predict
            return res
        except Exception as exc:
            print("Error in DetectCategory", exc)
            return abort(401)
