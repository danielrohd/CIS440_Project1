# Event Class script meant to be imported to the main file

class Event:
    """Contains information for an individual event."""

    def __init__(self, event_id, title, date, location, host):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.location = location
        self.host = host
        self.guests = []

    # Properties and setters
    @property
    def event_id(self):
        return self.__event_id

    @event_id.setter
    def event_id(self, e_id):
        self.__event_id = e_id

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
