
def get_price_prediction_answer(card_id):
    answers = {
    "8370": "28000",
    "8363": "164000",
    "8362": "177000",
    "8364": "12000",
    "8366": "308000",
    "8365": "31000",
    "8367": "310000",
    "8368": "253000",
    "8369": "18000",
    "8371": "10000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8358": "Hurvin Anderson",
    "8357": "Ed Ruscha",
    "8359": "Alberto Giacometti",
    "8355": "Lin Fengmian",
    "8352": "Qi Baishi",
    "8354": "Pu Ru",
    "8353": "Zhang Daqian",
    "8360": "Damien Hirst",
    "8361": "Antony Gormley",
    "8356": "Huang Binhong"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8342": "$851.3 million",
    "8347": "$7.9 billion",
    "8343": "$1.4 billion",
    "8344": "$205.6 million",
    "8349": "$552.6 million",
    "8346": "$460.1 million",
    "8345": "$2.1 billion",
    "8348": "$256.9 million",
    "8351": "$1.0 billion",
    "8350": "$825.7 million"
}
    return answers.get(str(card_id), None)
