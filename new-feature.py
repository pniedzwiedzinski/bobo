import os

from bobo import send_msg

feat = os.popen('git log -1 --pretty=format:"<u>%s</u>%n%b"').read()

msg = f"<b>Nowy ficzer właśnie wleciał do bobo:</b>\n\n{feat}"

send_msg(msg)
