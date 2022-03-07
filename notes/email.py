from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def sendpassword(username,password,receiver):
    # Creating message subject and sender
    subject = 'NoteBook Password Reset'
    sender = 'Notebook.com'

    #passing in the context vairables
    text_content = render_to_string('email/sendpassword.txt',{"username": username, "password":password})
    html_content = render_to_string('email/sendpassword.html',{"username": username,  "password":password})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
    
def subscribed(username,receiver):
    subject = 'Email Subscription'
    sender = 'NoteBook.com'

    #passing in the context vairables
    text_content = render_to_string('email/subscription.txt',{"username": username})
    html_content = render_to_string('email/subscription.html',{"username": username})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def notes_created(username,title,receiver):
    subject = 'Email Subscription'
    sender = 'NoteBook.com'
    #passing in the context vairables
    text_content = render_to_string('email/notes_created.txt',{"username": username, "title":title})
    html_content = render_to_string('email/notes_created.html',{"username": username, "title":title})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()