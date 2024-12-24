
def get_price_prediction_answer(card_id):
    answers = {
    "8318": "105000",
    "8314": "46000",
    "8313": "30000",
    "8315": "353000",
    "8316": "10000",
    "8312": "22000",
    "8317": "23000",
    "8319": "87000",
    "8320": "25000",
    "8321": "13000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8304": "Pu Ru",
    "8306": "Yoshitomo Nara",
    "8303": "Andy Warhol",
    "8302": "Qi Baishi",
    "8305": "Robert Combas",
    "8307": "Lin Fengmian",
    "8310": "Sanyu",
    "8311": "Zhang Daqian",
    "8309": "Joan Mir\u00f3",
    "8308": "Banksy"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8292": "$205.6 million",
    "8293": "$552.6 million",
    "8296": "$2.1 billion",
    "8294": "$851.3 million",
    "8295": "$330.8 million",
    "8297": "$3.1 billion",
    "8301": "$2.1 billion",
    "8300": "$387.5 million",
    "8299": "$460.1 million",
    "8298": "$468.4 million"
}
    return answers.get(str(card_id), None)
