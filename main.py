import json

def main():
    
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file);
    
    print("LoanDesk configuration loaded.");4
    
    with open(config["request_file"], "r", encoding="utf-8") as file:
        requests = json.load(file);
        
    print("\nReading-list requests:")
    
    for number, request in enumerate(requests, start=1):
        print(f"{number}. {request['name']}")
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
    
