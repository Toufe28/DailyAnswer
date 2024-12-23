
def get_price_prediction_answer(card_id):
    answers = {
    "8262": "38000",
    "8263": "22000",
    "8265": "19777000",
    "8267": "166000",
    "8264": "24000",
    "8268": "52000",
    "8266": "13000",
    "8271": "12000",
    "8269": "52000",
    "8270": "59000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8252": "Qi Baishi",
    "8255": "Huang Binhong",
    "8253": "Pu Ru",
    "8254": "Yoshitomo Nara",
    "8258": "Guan Liang",
    "8259": "Kim WhanKi",
    "8256": "Zhang Daqian",
    "8257": "Lin Fengmian",
    "8260": "Edgar Degas",
    "8261": "Sanyu"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8245": "$205.6 million",
    "8242": "$552.6 million",
    "8244": "$851.3 million",
    "8246": "$929.4 million",
    "8243": "$772.1 million",
    "8248": "$1.0 billion",
    "8247": "$460.1 million",
    "8251": "$16.0 billion",
    "8249": "$96.5 million",
    "8250": "$2.1 billion"
}
    return answers.get(str(card_id), None)
