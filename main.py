from agents.blood_test_analyzer import BloodTestAnalyzer
from agents.web_search_agent import WebSearchAgent
from agents.health_recommendation_agent import HealthRecommendationAgent
import json

def main():
    analyzer = BloodTestAnalyzer()
    search_agent = WebSearchAgent()
    recommender = HealthRecommendationAgent()
    
    with open('data/sample_blood_test_report.json') as f:
        report = json.load(f)
    
    findings = analyzer.analyze(report)
    queries = [f"{key} health tips" for key in findings.keys()]
    articles = search_agent.search(queries)
    recommendations = recommender.recommend(findings, articles)
    
    print("Findings:", findings)
    print("Recommendations:", recommendations)
    
    output = {
        "findings": findings,
        "recommendations": recommendations
    }
    with open('output/recommendations.json', 'w') as f:
        json.dump(output, f, indent=4)

if __name__ == "__main__":
    main()
