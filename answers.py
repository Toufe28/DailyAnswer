
def get_price_prediction_answer(card_id):
    answers = {
    "8112": "46000",
    "8114": "10000",
    "8115": "37000",
    "8113": "29000",
    "8116": "830000",
    "8118": "29000",
    "8117": "2436000",
    "8119": "43000",
    "8120": "14000",
    "8121": "14000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8105": "Lee Ufan",
    "8102": "Brice Marden",
    "8106": "Guan Liang",
    "8104": "Pu Ru",
    "8103": "Qi Baishi",
    "8107": "Huang Zhou",
    "8108": "Zhang Daqian",
    "8109": "Henry Moore",
    "8110": "Marc Chagall",
    "8111": "Li Keran"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8093": "$851.2 million",
    "8092": "$330.8 million",
    "8094": "$472.8 million",
    "8096": "$552.2 million",
    "8095": "$205.6 million",
    "8098": "$460.1 million",
    "8097": "$2.1 billion",
    "8099": "$48.8 million",
    "8100": "$1.0 billion",
    "8101": "$96.5 million"
}
    return answers.get(str(card_id), None)
