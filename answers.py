
def get_price_prediction_answer(card_id):
    answers = {
    "8512": "47000",
    "8513": "33000",
    "8515": "11000",
    "8514": "13000",
    "8519": "23000",
    "8516": "61000",
    "8517": "22000",
    "8518": "45000",
    "8520": "113000",
    "8521": "22000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8502": "Qi Baishi",
    "8505": "Kaws",
    "8504": "John Currin",
    "8503": "Pu Ru",
    "8506": "Peter Doig",
    "8508": "Julie Mehretu",
    "8507": "Lee Ufan",
    "8510": "Thomas Sch\u00fctte",
    "8509": "Damien Hirst",
    "8511": "Alex Katz"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8493": "$205.6 million",
    "8492": "$851.3 million",
    "8494": "$460.1 million",
    "8495": "$472.8 million",
    "8498": "$1.0 billion",
    "8496": "$825.7 million",
    "8500": "$1.0 billion",
    "8497": "$16.0 billion",
    "8499": "$552.6 million",
    "8501": "$642.4 million"
}
    return answers.get(str(card_id), None)
