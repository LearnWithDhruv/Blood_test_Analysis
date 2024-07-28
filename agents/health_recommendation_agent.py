class HealthRecommendationAgent:
    def recommend(self, findings, articles):
        recommendations = {}
        if 'cholesterol' in findings:
            recommendations['cholesterol'] = {
                "summary": findings['cholesterol'],
                "advice": "Consider adopting a low-cholesterol diet, including foods rich in fiber such as oats, beans, and fruits. Regular exercise can also help lower cholesterol levels.",
                "articles": [article for article in articles if 'cholesterol' in article['title'].lower()]
            }
        if 'glucose' in findings:
            recommendations['glucose'] = {
                "summary": findings['glucose'],
                "advice": "Monitor your glucose levels regularly. Incorporate foods with a low glycemic index into your diet, such as whole grains, vegetables, and legumes. Regular physical activity can also help manage glucose levels.",
                "articles": [article for article in articles if 'glucose' in article['title'].lower()]
            }
        if 'hemoglobin' in findings:
            recommendations['hemoglobin'] = {
                "summary": findings['hemoglobin'],
                "advice": "Ensure you have a diet rich in iron, such as lean meats, beans, and spinach. Consider taking iron supplements if recommended by your healthcare provider.",
                "articles": [article for article in articles if 'hemoglobin' in article['title'].lower()]
            }
        if 'vitamin_d' in findings:
            recommendations['vitamin_d'] = {
                "summary": findings['vitamin_d'],
                "advice": "Consider spending more time in sunlight and incorporating vitamin D-rich foods such as fatty fish, cheese, and egg yolks into your diet. Vitamin D supplements may also be beneficial.",
                "articles": [article for article in articles if 'vitamin d' in article['title'].lower()]
            }
        return recommendations

# Example usage:
if __name__ == "__main__":
    recommender = HealthRecommendationAgent()
    findings = {
        'cholesterol': 'High cholesterol detected. Your level is 220 mg/dL, which is above the normal range (less than 200 mg/dL).',
        'glucose': 'High glucose levels detected. Your level is 95 mg/dL, which is above the normal range (less than 100 mg/dL).'
    }
    articles = [
        {'title': 'How to manage high cholesterol', 'link': 'http://example.com/article1'},
        {'title': 'Diet tips for glucose control', 'link': 'http://example.com/article2'}
    ]
    recommendations = recommender.recommend(findings, articles)
    print(recommendations)
