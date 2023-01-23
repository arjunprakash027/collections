from main import MyClass, CricketScore

api_key = 'your_api_key'
match_id = 'unique_id_of_the_match'
cricket_score = CricketScore(api_key)
cricket_score.print_score(match_id)
