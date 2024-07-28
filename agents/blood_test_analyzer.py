import json

class BloodTestAnalyzer:
    def analyze(self, report):
        findings = {}
        
        # Analyze Cholesterol
        cholesterol = report["tests"][2]["results"][0]["result"]
        if cholesterol > 200:
            findings['cholesterol'] = 'High cholesterol detected. Your level is {} mg/dL, which is above the normal range (less than 200 mg/dL).'.format(cholesterol)
        else:
            findings['cholesterol'] = 'Normal cholesterol level. Your level is {} mg/dL.'.format(cholesterol)
        
        # Analyze Glucose
        glucose = report["tests"][3]["results"][0]["result"]
        if glucose > 100:
            findings['glucose'] = 'High glucose levels detected. Your level is {} mg/dL, which is above the normal range (less than 100 mg/dL).'.format(glucose)
        else:
            findings['glucose'] = 'Normal glucose level. Your level is {} mg/dL.'.format(glucose)
        
        # Analyze Hemoglobin
        hemoglobin = report["tests"][0]["results"][0]["result"]
        if hemoglobin < 13 or hemoglobin > 17:
            findings['hemoglobin'] = 'Abnormal hemoglobin level detected. Your level is {} g/dL, which is outside the normal range (13.00 - 17.00 g/dL).'.format(hemoglobin)
        else:
            findings['hemoglobin'] = 'Normal hemoglobin level. Your level is {} g/dL.'.format(hemoglobin)
        
        # Analyze Vitamin D
        vitamin_d = report["tests"][5]["results"][0]["result"]
        if vitamin_d < 30:
            findings['vitamin_d'] = 'Low vitamin D levels detected. Your level is {} ng/mL, which is below the normal range (30 - 100 ng/mL).'.format(vitamin_d)
        else:
            findings['vitamin_d'] = 'Normal vitamin D level. Your level is {} ng/mL.'.format(vitamin_d)
        
        return findings

if __name__ == "__main__":
    with open('../data/sample_blood_test_report.json') as f:
        report = json.load(f)
    analyzer = BloodTestAnalyzer()
    findings = analyzer.analyze(report)
    print(findings)
