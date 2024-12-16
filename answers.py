
def get_price_prediction_answer(card_id):
    answers = {
    "7915": "11000",
    "7919": "33000",
    "7916": "202000",
    "7918": "1054000",
    "7921": "19000",
    "7912": "234000",
    "7913": "10000",
    "7914": "10000",
    "7917": "61000",
    "7920": "60000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "7902": "Pu Ru",
    "7903": "Qi Baishi",
    "7907": "Georg Baselitz",
    "7904": "Sam Francis",
    "7906": "Lin Fengmian",
    "7905": "Pablo Picasso",
    "7909": "Zhang Daqian",
    "7910": "Sanyu",
    "7908": "Jean-Paul Riopelle",
    "7911": "Huang Binhong"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "7892": "$205.6 million",
    "7896": "$16.0 billion",
    "7894": "$256.9 million",
    "7899": "$472.5 million",
    "7893": "$851.2 million",
    "7895": "$1.9 billion",
    "7897": "$1.4 billion",
    "7898": "$472.8 million",
    "7900": "$2.1 billion",
    "7901": "$467.4 million"
}
    return answers.get(str(card_id), None)
