import json
from request import Request
from holdings import Holdings
from manager import LoanDeskManager
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
        
    
    
    
    with open(config["holdings_file"],"r",encoding="utf-8") as file:
        holdings_data = json.load(file)
        
    holdings = Holdings(holdings_data)
    
    manager = LoanDeskManager(requests,holdings)
    
    manager.list_requests()
    
    manager.plan()

    manager.gap("Monday Seminar")

    manager.lend("Monday Seminar")

    manager.lend("Poetry Hour")

    print(
    "\nThe Little Prince borrowed:",
    holdings.books["The Little Prince"]["borrowed"]
    )
    
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
    
