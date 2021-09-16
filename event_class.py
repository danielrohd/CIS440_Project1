# Event Class script meant to be imported to the main file

class Event:
    """Contains information for an individual event."""
    def __init__(title, date, location, host, guests=[]):
        self.title = title
        self.date = date
        self.location = location
        self.host = host
        self.guests = guests
        
    def add_guest(username):
        """Adds an account to the guest list"""
        if username not in guests:
            guests.append(username)
            
    def remove_guest(username):
        """Removes a guest from the guest list"""
        if username in guests:
            guests.remove(username)
    