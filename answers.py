
def get_price_prediction_answer(card_id):
    answers = {
    "8470": "34000",
    "8462": "29000",
    "8471": "23000",
    "8466": "253000",
    "8463": "17000",
    "8464": "241000",
    "8465": "13000",
    "8467": "26000",
    "8468": "12000",
    "8469": "187000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8452": "Pu Ru",
    "8453": "Qi Baishi",
    "8455": "Fernand Leger",
    "8457": "Keith Haring",
    "8454": "Lin Fengmian",
    "8456": "Damien Hirst",
    "8458": "Peter Doig",
    "8459": "Jonas Wood",
    "8460": "Alex Katz",
    "8461": "George Condo"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8444": "$1.0 billion",
    "8442": "$851.3 million",
    "8443": "$205.6 million",
    "8445": "$460.1 million",
    "8448": "$825.7 million",
    "8446": "$552.6 million",
    "8449": "$799.1 million",
    "8450": "$551.3 million",
    "8447": "$1.3 billion",
    "8451": "$296.0 million"
}
    return answers.get(str(card_id), None)
