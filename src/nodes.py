import os
import time


from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch


class Nodes():
    def __init__(self):
        self.gmail=GmailToolkit

    def check_email(self,state):
        print("# Checking for new emails")  
        search=GmailSearch(api_resource=self.gmail.api_resource)
        emails = search('after : newer_than:1d')
        checked_emails = state['checked_emails_ids']  if state ['checked_emails_ids'] else []
        thread=[]
        new_emails=[]
        for email in emails:
            if (email['id'] not in checked_emails) and (email['threadId'] not in thread) and (os.environ['MY_EMAİL'] not in email ['sender']):
                thread.append(email['threadId'])
                new_emails.append(
                        {
                            "id":email['id'],
                            "threadId": email['threadId'],
                            "snippet" : email['snippet'],
                            "sender": email["sender"]
                        }
                )

                #Yeni E-postaları Arar: Son 1 gün içinde gelen e-postaları bulur.
                #Kontrol Edilmiş E-postaları ve Yeni E-postaları Listeler: Daha önce kontrol edilmemiş ve belirli koşulları sağlayan e-postaları listeler.
                #Yeni E-postaları İşler: E-posta bilgilerini alır ve yeni e-postaları bir listeye ekler.
                
    def wait_next_run(self,state):
        print("## waiting for 120 second")
        time.sleep(120)
        return state
    

    def new_emails(self,state):
        if len(state['emails'])==00:
            print("## No new emails")
            return "end"
        else:
            print("New emails")
            return "continue"




