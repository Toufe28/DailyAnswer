
def get_price_prediction_answer(card_id):
    answers = {
    "8562": "55000",
    "8564": "13000",
    "8565": "18000",
    "8570": "14000",
    "8563": "30000",
    "8566": "20000",
    "8567": "46000",
    "8568": "40000",
    "8569": "113000",
    "8571": "48000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8558": "Sean Scully",
    "8552": "Pu Ru",
    "8557": "Damien Hirst",
    "8553": "Qi Baishi",
    "8555": "Peter Doig",
    "8554": "Salvador Dali",
    "8556": "Takashi Murakami",
    "8560": "Kaws",
    "8559": "Jonas Wood",
    "8561": "Alex Katz"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8544": "$460.1 million",
    "8542": "$851.3 million",
    "8546": "$799.1 million",
    "8543": "$205.6 million",
    "8547": "$1.4 billion",
    "8545": "$256.9 million",
    "8548": "$1.0 billion",
    "8550": "$551.3 million",
    "8549": "$213.1 million",
    "8551": "$472.8 million"
}
    return answers.get(str(card_id), None)
