
d = [{
    'id': '76604ea0-a822-4624-b5f4-cd9304f3405d',
    'from': '"TikTok" <noreply@account.tiktok.com>',
    'to': 'lsd5m8jb3g@wnbaldwy.com',
    'cc': None,
    'subject': '160899 is your verification code',
    'body_text': "Verification Code\n\nTo verify your account, enter this code in TikTok:\n\n160899\n\nVerification codes expire after 48 hours.\n\nIf you didn't request this code, you can ignore this message.\n\nTikTok Support Team\n\nTikTok Help Center: https://support.tiktok.com/\n\nHave a question?\nCheck out our help center or contact us in the app using Settings > Report a Problem.\nThis is an automatically generated email. Replies to this email address aren't monitored.\n\nThis email was generated for gogo.mamlambo.\nPrivacy Policy ( https://www.tiktok.com/en/privacy-policy?lang=en )\nTikTok, 10100 Venice Bivd, Culver City, CA 90232",
    'body_html': '<html class="en"> ... </html>',
    'created_at': '2025-08-10T22:50:56.89632Z',
    'attachments': []
}]

w = d[0]["body_text"]
username = w.split('This email was generated for')[1].split("\n")[0].strip().rstrip(".")
print(username) 
