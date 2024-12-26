
def get_price_prediction_answer(card_id):
    answers = {
    "8412": "111000",
    "8415": "10000",
    "8418": "16000",
    "8416": "38000",
    "8413": "130000",
    "8414": "70000",
    "8417": "14000",
    "8419": "6826000",
    "8420": "79000",
    "8421": "12000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8403": "Qi Baishi",
    "8402": "Pu Ru",
    "8404": "Lin Fengmian",
    "8405": "Zhang Daqian",
    "8409": "Kaws",
    "8410": "Alberto Giacometti",
    "8406": "Damien Hirst",
    "8408": "Cecily Brown",
    "8407": "Keith Haring",
    "8411": "Paul Signac"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8392": "$205.6 million",
    "8393": "$1.0 billion",
    "8394": "$851.3 million",
    "8396": "$552.6 million",
    "8395": "$825.7 million",
    "8399": "$1.9 billion",
    "8400": "$7.9 billion",
    "8401": "$16.0 billion",
    "8397": "$460.1 million",
    "8398": "$213.1 million"
}
    return answers.get(str(card_id), None)
