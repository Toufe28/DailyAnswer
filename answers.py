
def get_price_prediction_answer(card_id):
    answers = {
    "8171": "59000",
    "8163": "1485000",
    "8165": "292000",
    "8164": "90000",
    "8162": "63000",
    "8166": "18000",
    "8170": "12000",
    "8169": "29000",
    "8168": "284000",
    "8167": "137000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8152": "Qi Baishi",
    "8154": "Amedeo Modigliani",
    "8153": "Zhang Daqian",
    "8155": "Huang Binhong",
    "8158": "Lin Fengmian",
    "8156": "Pu Ru",
    "8159": "Li Keran",
    "8161": "Guan Liang",
    "8157": "Sanyu",
    "8160": "Kim WhanKi"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8144": "$825.7 million",
    "8142": "$205.6 million",
    "8143": "$16.0 billion",
    "8146": "$1.4 billion",
    "8145": "$851.2 million",
    "8147": "$1.0 billion",
    "8149": "$460.1 million",
    "8148": "$330.8 million",
    "8150": "$180.1 million",
    "8151": "$2.1 billion"
}
    return answers.get(str(card_id), None)
