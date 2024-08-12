import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_email_content(ideas):
    email_body = '''
    <div style="word-break: break-word; color: rgb(34, 34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small; padding: 20px 20px 0px;">
        <h1 style="word-break: break-word; margin: 0px; font-family: 'Century Gothic', Avenir, 'Trebuchet MS', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif; 
        line-height: 1.5; text-align: center;">LitePapers</h1>
    '''

    for i, idea in enumerate(ideas):
        email_body += f"""
        <div style="word-break: break-word;">
        <table cellpadding="0" cellspacing="0" style="word-break: break-word; width: 891.008px; margin: 0px auto;">
        <tbody style="word-break: break-word;">
        <tr style="word-break: break-word;">
        <td style="margin: 0px; word-break: break-word; vertical-align: top;">
        <h1 style="word-break: break-word; margin: 0px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif; line-height: 1.5;">Paper {i+1}</h1>
        <p style="word-break: break-word; margin: 1em 0px; font-family: 'Century Gothic', Avenir, 'Trebuchet MS', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif; color: rgb(61, 61, 61); font-size: 18px; line-height: 1.5;"><strong>Title:</strong> "{idea['title']}"</p>
        <p style="word-break: break-word; margin: 1em 0px; font-family: 'Century Gothic', Avenir, 'Trebuchet MS', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif; color: rgb(61, 61, 61); font-size: 18px; line-height: 1.5;">{idea['summary']}</p>
        <h1 style="word-break: break-word; margin: 0px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif; line-height: 1.5;">Business Implications</h1>
        <p style="word-break: break-word; margin: 1em 0px; font-family: 'Century Gothic', Avenir, 'Trebuchet MS', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif; color: rgb(61, 61, 61); font-size: 18px; line-height: 1.5;">1. {idea['idea1']}</p>
        <p style="word-break: break-word; margin: 1em 0px; font-family: 'Century Gothic', Avenir, 'Trebuchet MS', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif; color: rgb(61, 61, 61); font-size: 18px; line-height: 1.5;">2. {idea['idea2']}</p>
        <p style="word-break: break-word; margin: 1em 0px; font-family: 'Century Gothic', Avenir, 'Trebuchet MS', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif; color: rgb(61, 61, 61); font-size: 18px; line-height: 1.5;">3. {idea['idea3']}</p>
        <table width="100%" style="word-break: break-word;">
        <tbody style="word-break: break-word;">
        <tr style="word-break: break-word;">
        <td align="left" style="margin: 0px; word-break: break-word; vertical-align: top;">
        <a href="{idea['link']}" rel="noopener noreferrer" style="color: rgb(255, 255, 255); word-break: break-word; border: 0px solid rgb(108, 206, 236); line-height: 1.5; background-color: rgb(108, 206, 236); box-sizing: border-box; display: inline-block; padding: 12px 20px; margin-top: 8px; margin-bottom: 8px; font-size: 16px; border-radius: 4px;">
        <strong style="word-break: break-word;">Full paper</strong></a></td>
        </tr>
        </tbody>
        </table>
        </td>
        </tr>
        </tbody>
        </table>
        </div>
        """
    email_body += '</div>'
    return email_body


def send_email(ideas, to_email):
    subject = "LitePapers - Your AI Research Digest"
    body = generate_email_content(ideas)

    msg = MIMEMultipart()
    msg['From'] = 'YOUR EMAIL'
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    # Use Gmail's SMTP server (replace with your SMTP server details)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('YOUR EMAIL', 'YOUR PASSWORD')
    text = msg.as_string()
    server.sendmail('EMAIL TO SEND TO', to_email, text)
    server.quit()

    print("Email sent successfully.")
