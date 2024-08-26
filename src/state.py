import datatime
from typing import TypedDict

class EmailState(TypedDict):
        checked_emailsids: list[str]
        emails: list[dict]
        action_required_emails: dict

        ##Bu yapı, e-postaları yönetmek ve analiz etmek için gereken bilgileri organize eder.






