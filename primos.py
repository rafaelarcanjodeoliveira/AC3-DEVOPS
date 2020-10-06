import os
from flask import jsonify, Flask, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def numerosPrimos():

    limite = 100
    p = 1
    numero = 3
    primos = "2"

    while p < limite:
        primo = 1
        for i in range(2, numero):
            if numero % i == 0:
                primo = 0
        if (primo):
            primos = primos + ',' + str(numero)
            p += 1
        numero+=1
    primos = primos + '.'
    return primos




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
