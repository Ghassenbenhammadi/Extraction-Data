from BackEnd import *
from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin

server = Flask(__name__)
# CORS(server)

@server.route("/Extract_Data", methods=["POST"])
@cross_origin()
def extarctData():
    res = request.json
    urlOfDevis = res['urlOfDevis'] # C:\\Users\\asus\\Desktop\\Nouveau dossier\\PFE\\Backend-Pfe\\authUsers\\Uploaded Files\\file (5).pdf
    resultFunction1 = converterPDFToImage(urlOfDevis)
    getDataFromImage(resultFunction1)
    return send_from_directory(STATIC,'Images/ImagesAfterExtraction/image')

if __name__ == "__main__":
    server.run(debug=True)