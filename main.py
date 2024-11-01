from bdd_step_analyzer.step_analyzer import extract_steps_from_feature, find_similar_steps, generate_report
import glob

def analyze_feature_files():
    all_steps = []
    for file_path in glob.glob("data/**/*.feature", recursive=True):
        steps = extract_steps_from_feature(file_path)
        all_steps.extend(steps)
    
    similar_steps = find_similar_steps(all_steps)
    generate_report(similar_steps)

if __name__ == "__main__":
    analyze_feature_files()
