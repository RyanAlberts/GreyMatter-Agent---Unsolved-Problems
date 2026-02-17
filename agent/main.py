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
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(reports, f, indent=2)
        
    print(f"Report saved to {output_path}")

if __name__ == "__main__":
    main()
