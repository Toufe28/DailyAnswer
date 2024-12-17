
def get_price_prediction_answer(card_id):
    answers = {
    "7962": "568000",
    "7967": "16000",
    "7965": "16000",
    "7964": "491000",
    "7963": "159000",
    "7966": "13000",
    "7971": "1051000",
    "7969": "61000",
    "7968": "29000",
    "7970": "16000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "7958": "Sanyu",
    "7952": "Zhang Daqian",
    "7953": "Pu Ru",
    "7954": "Sam Francis",
    "7955": "Yoshitomo Nara",
    "7956": "Guan Liang",
    "7959": "Jean-Paul Riopelle",
    "7957": "Alberto Giacometti",
    "7960": "Andy Warhol",
    "7961": "Huang Binhong"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "7944": "$851.2 million",
    "7942": "$205.6 million",
    "7943": "$2.6 billion",
    "7947": "$1.5 billion",
    "7951": "$3.1 billion",
    "7945": "$256.9 million",
    "7946": "$460.1 million",
    "7948": "$1.1 billion",
    "7950": "$2.1 billion",
    "7949": "$330.8 million"
}
    return answers.get(str(card_id), None)
