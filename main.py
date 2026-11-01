import json
from request import Request
from holdings import Holdings
def main():
    
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
    
    print("LoanDesk configuration loaded.");4
    
    with open(config["request_file"], "r", encoding="utf-8") as file:
        request_data = json.load(file)
        
    requests = []

    for item in request_data:
        request = Request(item["name"], item["books"])
        requests.append(request)
        
    print("\nReading-list requests:")
    
    for number, request in enumerate(requests, start=1):
        print(f"{number}. {request.name}")
    
    
    with open(config["holdings_file"],"r",encoding="utf-8") as file:
        holdings_data = json.load(file)
        
    holdings = Holdings(holdings_data)
    
    print("\nLibrary book holdings:")
    
    

    for title, holding in holdings.books.items():
        copies = holding["copies"]
        borrowed = holding["borrowed"]
        on_shelf = holdings.get_on_shelf(title)

        print(
            f"{title}: "
            f"Owned: {copies}, "
            f"Borrowed: {borrowed}, "
            f"On shelf: {on_shelf}"
        )
    
    
    
if __name__ == "__main__":
    main()
    
