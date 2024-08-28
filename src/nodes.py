import os
import time
from langchain_google_community import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch

class Nodes():
    def __init__(self):
        self.gmail_toolkit = GmailToolkit()  # GmailToolkit'in bir örneğini oluşturun

    def check_email(self, state):
        print("# Checking for new emails")
        
        # GmailToolkit örneğinden api_resource'u alın
        gmail_api_resource = self.gmail_toolkit.get_tools()[0].api_resource
        
        search = GmailSearch(api_resource=gmail_api_resource)
        emails = search.run('after:newer_than:1d')  # run() metodunu kullanın
        
        checked_emails = state['checked_emails_ids'] if 'checked_emails_ids' in state else []
        thread = []
        new_emails = []
        
        for email in emails:
            if (email['id'] not in checked_emails) and (email['threadId'] not in thread) and (os.environ['MY_EMAIL'] not in email['sender']):
                thread.append(email['threadId'])
                new_emails.append({
                    "id": email['id'],
                    "threadId": email['threadId'],
                    "snippet": email['snippet'],
                    "sender": email["sender"]
                })
        
        # Yeni e-postaları state'e ekleyin
        state['emails'] = new_emails
        state['checked_emails_ids'] = list(set(checked_emails + [email['id'] for email in new_emails]))
        
        return state

    def wait_next_run(self, state):
        print("## waiting for 120 seconds")
        time.sleep(120)
        return state

    def new_emails(self, state):
        if len(state.get('emails', [])) == 0:
            print("## No new emails")
            return "end"
        else:
            print("New emails")
            return "continue"