
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

    def find_request(self, request_name):
        """Find a request by name, ignoring letter case."""

        for request in self.requests:
            if request.name.lower() == request_name.lower():
                return request

        return None

    def get_missing_copies(self, request):
        """Calculate missing copies for one request."""

        missing = {}

        for title, quantity_needed in request.books.items():

            available = self.holdings.get_on_shelf(title)

            if available < quantity_needed:
                missing[title] = quantity_needed - available

        return missing

    def plan(self):
        """Find and display requests the library can fulfil."""

        lendable_requests = []

        for request in self.requests:

            missing = self.get_missing_copies(request)

            if not missing:
                lendable_requests.append(request)

        print("\nRequests the desk can lend:")

        if not lendable_requests:
            print("No request can be lent with the current shelves.")
            return []

        for request in lendable_requests:
            print(f"- {request.name}")

        return lendable_requests

    def gap(self, request_name):
        """Display the missing copies for a request."""

        request = self.find_request(request_name)

        if request is None:
            print(f"Request '{request_name}' not found.")
            return {}

        missing = self.get_missing_copies(request)

        print(f"\nMissing copies for '{request.name}':")

        if not missing:
            print(f"No missing copies for '{request.name}'.")
            return {}

        for title, quantity in missing.items():
            print(f"- {title}: {quantity}")

        return missing

    def lend(self, request_name):
        """Lend a request if every required book is available."""

        request = self.find_request(request_name)

        if request is None:
            print(f"Request '{request_name}' not found.")
            return False

        missing = self.get_missing_copies(request)

        if missing:
            print(f"Cannot lend '{request.name}'. Missing copies:")

            for title, quantity in missing.items():
                print(f"- {title}: {quantity}")

            return False

        for title, quantity in request.books.items():
            self.holdings.borrow(title, quantity)

        print(
            f"Successfully lent '{request.name}'. "
            "Holdings have been updated."
        )

        return True
