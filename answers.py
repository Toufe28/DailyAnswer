
def get_price_prediction_answer(card_id):
    answers = {
    "8218": "52000",
    "8212": "27000",
    "8215": "26000",
    "8217": "13000",
    "8216": "440000",
    "8213": "18000",
    "8214": "137000",
    "8219": "12000",
    "8220": "221000",
    "8221": "489000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8207": "Pablo Picasso",
    "8202": "Pu Ru",
    "8204": "Lin Fengmian",
    "8206": "Qi Baishi",
    "8203": "Edgar Degas",
    "8205": "Zhang Daqian",
    "8208": "Wu Hufan",
    "8209": "Kim WhanKi",
    "8211": "Maurice de Vlaminck",
    "8210": "Fu Baoshi"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8192": "$205.6 million",
    "8193": "$2.1 billion",
    "8194": "$851.2 million",
    "8195": "$5.3 billion",
    "8196": "$16.0 billion",
    "8201": "$552.2 million",
    "8199": "$3.3 billion",
    "8197": "$467.4 million",
    "8198": "$460.1 million",
    "8200": "$330.8 million"
}
    return answers.get(str(card_id), None)
