import requests



target_counts_response = requests.get("http://model:81/target_variable")
target_counts = target_counts_response.json()

class NaiveBayesPredictor:
    def __init__(self):
        pass

    def predict_from_summary(self, summary, query):
        scores = {}
        total_count = sum(target_counts.values())
        priors = {k: v / total_count for k, v in target_counts.items()}

        if query is None:
            print("query is None")
            return

        fixed_query = {}
        for feature, feature_value in query.items():
            try:
                fixed_value = int(feature_value)
            except ValueError:
                try:
                    fixed_value = float(feature_value)
                except ValueError:
                    fixed_value = feature_value
            fixed_query[feature] = fixed_value

        for target_value in summary:
            prob = priors.get(target_value, 0.0001)
            for feature, feature_value in fixed_query.items():
                feature_probs = summary[target_value].get(feature, {})
                value_prob = feature_probs.get(feature_value, 0.0001)  
                prob *= value_prob

            scores[target_value] = prob
        best_target = max(scores, key=scores.get)

        return best_target, scores
    

    