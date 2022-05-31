def ability_score(score):
    if score == 1:
        modifier = -5
    elif 2 <= score <= 3:
        modifier = -4
    elif 4 <= score <= 5:
        modifier = -3
    elif 6 <= score <= 7:
        modifier = -2
    elif 8 <= score <= 9:
        modifier = -1
    elif 10 <= score <= 11:
        modifier = 0
    elif 12 <= score <= 13:
        modifier = 1
    elif 14 <= score <= 15:
        modifier = 2
    elif 16 <= score <= 17:
        modifier = 3
    elif 18 <= score <= 19:
        modifier = 4
    elif 20 <= score <= 21:
        modifier = 5
    elif 22 <= score <= 23:
        modifier = 6
    elif 24 <= score <= 25:
        modifier = 7
    elif 26 <= score <= 27:
        modifier = 8
    elif 28 <= score <= 29:
        modifier = 9
    elif score == 30:
        modifier = 10
    return modifier
