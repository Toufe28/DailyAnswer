
def get_price_prediction_answer(card_id):
    answers = {
    "7814": "51000",
    "7816": "265000",
    "7812": "43000",
    "7813": "10000",
    "7817": "22000",
    "7815": "13000",
    "7819": "55000",
    "7818": "13000",
    "7821": "15000",
    "7820": "239000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "7805": "Kim WhanKi",
    "7802": "Pu Ru",
    "7807": "Alexander Calder",
    "7806": "Josef Albers",
    "7804": "Xu Beihong",
    "7803": "Camille Pissarro",
    "7809": "Qi Baishi",
    "7808": "Zhang Daqian",
    "7811": "Takashi Murakami",
    "7810": "Wu Guanzhong"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "7795": "$622.9 million",
    "7793": "$1.0 billion",
    "7792": "$444.9 million",
    "7801": "$851.2 million",
    "7794": "$551.0 million",
    "7796": "$1.4 billion",
    "7798": "$315.0 million",
    "7797": "$1.9 billion",
    "7799": "$205.6 million",
    "7800": "$1.0 billion"
}
    return answers.get(str(card_id), None)
