
def get_price_prediction_answer(card_id):
    answers = {
    "8062": "41000",
    "8063": "61000",
    "8064": "513000",
    "8065": "78000",
    "8066": "39000",
    "8067": "58000",
    "8068": "84000",
    "8069": "61000",
    "8070": "19000",
    "8071": "30000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8052": "Pu Ru",
    "8053": "Qi Baishi",
    "8054": "Andy Warhol",
    "8055": "Sanyu",
    "8056": "Yayoi Kusama",
    "8057": "Huang Binhong",
    "8058": "Maurice de Vlaminck",
    "8059": "Salvador Dali",
    "8060": "Zhang Daqian",
    "8061": "Jeff Koons"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8042": "$460.1 million",
    "8043": "$851.2 million",
    "8044": "$96.5 million",
    "8045": "$256.9 million",
    "8046": "$205.6 million",
    "8047": "$552.2 million",
    "8048": "$1.2 billion",
    "8049": "$2.1 billion",
    "8050": "$1.3 billion",
    "8051": "$472.5 million"
}
    return answers.get(str(card_id), None)
