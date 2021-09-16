# Event Class script meant to be imported to the main file

class Event:
    """Contains information for an individual event."""
    def __init__(self, title, date, location, host):
        self.title = title
        self.date = date
        self.location = location
        self.host = host
        self.guests = []

    # Properties and setters
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title_info):
        self.__title = title_info

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, event_date):
        self.__date = event_date

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, place):
        self.__location = place

    @property
    def guests(self):
        return self.__guests

    @guests.setter
    def guests(self, guests_list):
        self.__guests = guests_list

    def add_guest(self, username):
        """Adds an account to the guest list"""
        if username not in self.guests:
            self.guests.append(username)
            
    def remove_guest(self, username):
        """Removes a guest from the guest list"""
        if username in self.guests:
            self.guests.remove(username)
