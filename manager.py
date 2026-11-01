class LoanDeskManager:
    """Coordinates the requests and library holdings."""

    def __init__(self, requests, holdings):
        self.requests = requests
        self.holdings = holdings

    def list_requests(self):
        """Display all reading-list requests."""

        print("\nReading-list requests:")

        for number, request in enumerate(self.requests, start=1):
            print(f"{number}. {request.name}")
