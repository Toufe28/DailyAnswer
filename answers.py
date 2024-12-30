
def get_price_prediction_answer(card_id):
    answers = {
    "8612": "500000",
    "8613": "202000",
    "8615": "35000",
    "8614": "30000",
    "8617": "27000",
    "8621": "45000",
    "8616": "11000",
    "8619": "22000",
    "8618": "13000",
    "8620": "34000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8602": "Qi Baishi",
    "8610": "Andy Warhol",
    "8603": "Pu Ru",
    "8604": "Damien Hirst",
    "8606": "Hurvin Anderson",
    "8605": "Jonas Wood",
    "8607": "Alex Katz",
    "8609": "Jeff Koons",
    "8608": "Yoshitomo Nara",
    "8611": "Ed Ruscha"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8592": "$205.6 million",
    "8593": "$851.3 million",
    "8594": "$460.1 million",
    "8596": "$545.1 million",
    "8600": "$344.7 million",
    "8595": "$1.0 billion",
    "8598": "$642.4 million",
    "8597": "$841.3 million",
    "8599": "$269.1 million",
    "8601": "$1.0 billion"
}
    return answers.get(str(card_id), None)
