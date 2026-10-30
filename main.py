import json

def main():
    
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file);
    
    print("LoanDesk configuration loaded.");
    print("Requests file:", config["request_file"]);
    print("Holdings file:", config["holdings_file"]);
    print("Report file:", config["report_file"]);
    
    
    
    
    
if __name__ == "__main__":
    main()
    
