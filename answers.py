
def get_price_prediction_answer(card_id):
    answers = {
    "7762": "99000",
    "7763": "52000",
    "7770": "117000",
    "7771": "31000",
    "7765": "14000",
    "7769": "38000",
    "7764": "10000",
    "7767": "277000",
    "7768": "12000",
    "7766": "303000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "7752": "Maurice de Vlaminck",
    "7755": "Pu Ru",
    "7753": "Sanyu",
    "7754": "Andy Warhol",
    "7756": "Lin Fengmian",
    "7757": "Qi Baishi",
    "7759": "Pierre Bonnard",
    "7758": "Zhang Daqian",
    "7760": "David Hockney",
    "7761": "Camille Pissarro"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "7742": "$1.5 billion",
    "7743": "$8.6 billion",
    "7746": "$16.0 billion",
    "7748": "$205.6 million",
    "7745": "$2.1 billion",
    "7749": "$1.0 billion",
    "7750": "$798.9 million",
    "7751": "$330.8 million",
    "7744": "$851.2 million",
    "7747": "$482.0 million"
}
    return answers.get(str(card_id), None)
