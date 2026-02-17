import json
from orchestrator import Orchestrator
from researcher import run_research_campaign

def main():
    print("=== AI Research Agent Started ===")
    
    # 1. Orchestration (Discovery)
    orchestra = Orchestrator()
    candidates = orchestra.plan_research()
    
    # 2. Research (Verification)
    print("\n=== Starting Deep Dive Verification ===")
    reports = run_research_campaign(candidates)
    
    # 3. Synthesis (Output)
    print("\n=== Synthesis & Output ===")
    output_path = "../web-app/public/report.json"
    
    # Ensure directory exists (if running from agent dir)
    import os
    from datetime import datetime
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Load existing data
    existing_data = []
    if os.path.exists(output_path):
        try:
            with open(output_path, "r") as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            pass

    # Add timestamp to new reports
    today_str = datetime.now().strftime("%Y-%m-%d")
    for r in reports:
        r["date"] = today_str

    # Append new reports
    # In a real system, we'd check for duplicates here
    all_reports = existing_data + reports
    
    # Sort by Importance Score (Descending)
    all_reports.sort(key=lambda x: x.get("importance_score", 0), reverse=True)
    
    with open(output_path, "w") as f:
        json.dump(all_reports, f, indent=2)
        
    print(f"Report saved to {output_path}. Total items: {len(all_reports)}")

if __name__ == "__main__":
    main()
