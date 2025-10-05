from sys import maxsize


class Contact:
    def __init__(self, firstName=None, lastName=None, nickname=None, company=None, address=None,
                 phone_home=None, phone_mobile=None, phone_work=None, fax=None, all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page=None,
                webpage=None, title=None,
                 bday=None, bmonth=None, byear=None, an_day=None, an_month=None, an_year=None,
                 id=None):
        self.firstName = firstName
        self.lastName = lastName
        self.nickname = nickname
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.webpage = webpage
        self.title = title
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.an_day = an_day
        self.an_month = an_month
        self.an_year = an_year
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstName == other.firstName and self.lastName == other.lastName

    def __repr__(self):
        return "%s:%s:%s" %(self.id, self.firstName, self.lastName)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize