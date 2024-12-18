
def get_price_prediction_answer(card_id):
    answers = {
    "8012": "12000",
    "8013": "33000",
    "8014": "35000",
    "8015": "14000",
    "8016": "40000",
    "8017": "23000",
    "8018": "49000",
    "8019": "393000",
    "8020": "11000",
    "8021": "13000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8002": "Amedeo Modigliani",
    "8003": "Pu Ru",
    "8004": "Qi Baishi",
    "8005": "Zhang Daqian",
    "8006": "Fu Baoshi",
    "8007": "Guan Liang",
    "8008": "Henri Matisse",
    "8009": "Alexander Calder",
    "8010": "Lin Fengmian",
    "8011": "Marc Chagall"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "7992": "$205.6 million",
    "7993": "$552.2 million",
    "7994": "$851.2 million",
    "7995": "$2.1 billion",
    "7996": "$213.1 million",
    "7997": "$1.0 billion",
    "7998": "$837.3 million",
    "7999": "$256.9 million",
    "8000": "$460.1 million",
    "8001": "$218.6 million"
}
    return answers.get(str(card_id), None)
