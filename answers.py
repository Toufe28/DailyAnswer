
def get_price_prediction_answer(card_id):
    answers = {
    "8664": "14000",
    "8663": "28000",
    "8666": "10123000",
    "8662": "32000",
    "8665": "12000",
    "8669": "18000",
    "8668": "22000",
    "8667": "35000",
    "8670": "17000",
    "8671": "17000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8655": "Alex Katz",
    "8653": "Pu Ru",
    "8652": "Qi Baishi",
    "8654": "Damien Hirst",
    "8656": "Richard Prince",
    "8657": "Jeff Koons",
    "8658": "Jonas Wood",
    "8661": "Thomas Sch\u00fctte",
    "8659": "Dana Schutz",
    "8660": "Fernando Botero"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8644": "$205.6 million",
    "8642": "$851.3 million",
    "8643": "$460.1 million",
    "8646": "$545.1 million",
    "8645": "$606.9 million",
    "8650": "$1.0 billion",
    "8649": "$477.6 million",
    "8651": "$264.0 million",
    "8647": "$284.0 million",
    "8648": "$218.8 million"
}
    return answers.get(str(card_id), None)
