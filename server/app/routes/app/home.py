from flask import Blueprint, request, jsonify
import imaplib
import email

home_bp = Blueprint('home', __name__)

@home_bp.route('/get-latest-mail')
def get_latest_mail():
   status, emails = parse_mail_into_dictionary()
   if status == "NO":
         return jsonify({"message":"something went wrong"}), 500
   elif status == 'BAD':
         return jsonify({"message": "server error"}), 500
   latest_email = emails[-10:]
   return jsonify({"message":"sucessfully fetched the latest list", "emails":latest_email}), 200


def parse_mail_into_dictionary():
        EMAIL = "nishanpudke718@gmail.com"
        PASS = "ishannepal01@outlook.com"

        mail = imaplib.IMAP4_SSL("imap.gmail.com")  # Secure connection to Gmail
        mail.login(EMAIL,PASS)
        mail.select('inbox')

        status, messages =  mail.search(None, "ALL")
        if status != "OK":
              return (status, [])
        
        email_list = []
        email_ids = messages[0].split()

        for eid in email_ids:
              status, msg_data = mail.fetch(eid, "(RFC822)")
              if status != "OK":
                    continue
              raw_email = msg_data[0][1]
              msg = email.message_from_bytes(raw_email)
              sender = msg["From"]
              subject = msg["Subject"]
              body = ""
              if msg.is_multipart():
                    for part in msg.walk():
                          if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode(errors="ignore")
                                break
              else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

              email_list.append({
                "sender": sender,
                "subject": subject,
                "body": body
                })
              
        mail.logout()
        return ("OK", email_list)

