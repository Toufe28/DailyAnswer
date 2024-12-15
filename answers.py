
def get_price_prediction_answer(card_id):
    answers = {
    "7862": "12000",
    "7868": "83000",
    "7867": "35000",
    "7871": "12000",
    "7864": "208000",
    "7865": "18000",
    "7870": "30000",
    "7869": "76000",
    "7866": "85000",
    "7863": "26000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "7853": "Huang Binhong",
    "7854": "Lee Ufan",
    "7852": "Zhang Daqian",
    "7855": "Zhou Chunya",
    "7859": "Georges Braque",
    "7860": "Camille Pissarro",
    "7857": "Qi Baishi",
    "7856": "Sanyu",
    "7858": "Banksy",
    "7861": "Pu Ru"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "7842": "$472.8 million",
    "7851": "$350.2 million",
    "7845": "$2.1 billion",
    "7844": "$1.2 billion",
    "7848": "$16.0 billion",
    "7847": "$460.1 million",
    "7849": "$871.3 million",
    "7850": "$551.0 million",
    "7843": "$851.2 million",
    "7846": "$142.2 million"
}
    return answers.get(str(card_id), None)
