import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Configuration SMTP
smtp_server = '' # A completer
smtp_port = 25  # ou 465 pour SSL # A completer

# Liste des participants avec emails
participants = [
    {"name": "nom1", "email": "nom1@domain.com"}, # A completer
    ]

# Mélanger la liste
random.shuffle(participants)

# Générer les paires
pairs = {participants[i]['name']: participants[(i + 1) % len(participants)]['name'] for i in range(len(participants))}

# Connexion au serveur SMTP
server = smtplib.SMTP(smtp_server, smtp_port)

# Envoyer les emails individuels
for participant in participants:
    giver = participant['name']
    receiver = pairs[giver]
    subject = "Secret Santa - Ton destinataire de cadeau !"

    # Template HTML pour l'email
    html = f"""
   <html>
    <head>
        <style>
            body {{ font-family: 'Aptos', sans-serif; background-color: #f0f0f0; color: #333; padding: 20px; }}
            .container {{ background: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }}
            .receiver {{ text-align: center; font-size: 25px; margin-top: 20px; }}
            .footer {{ text-align: center; margin-top: 30px; color: #444; }}
            .footer img {{ width: 50px; height: auto; }}
        </style>
    </head>
    <body>
        <div class="container">
        <h2 style="color: #d4423e;"><p class="greeting">Oh, oh, oooh, <strong>{giver}</strong>!</p></strong></h2>
        
        <p>En cette période festive, le Père Noël a besoin de ton aide pour répandre la joie et la surprise. Tu as été choisi pour offrir un cadeau secret à :</p>
       <center> <h2 style="color: green;"><strong>{receiver}</strong></h2></center>

        <div class="rules">
            <h3>Voici les règles enchantées du Secret Santa :</h3>
            <ul>
                <li>🎁 Garde le secret de ton destinataire jusqu'au grand dévoilement.</li>
                <li>🎄 Trouve un cadeau merveilleux d'environ 10€.</li>
                <li>🌟 Favorise un cadeau local et plein de créativité.</li>
                <li>⛄ Emballe ton cadeau avec soin et place-le sous le sapin avant le 21 décembre.</li>
                <li>✨ N'oublie pas, le plus important est de partager la magie de Noël et de s'amuser !</li>
            </ul>
        </div>

        <div class="footer">
            <p>Avec toute la magie de Noël,</p>
            <p>Le Père Noël 🎅</p>
        </div>
    </div>
</body>
</html>
    """
    # Préparation et envoi de l'email
    msg = MIMEMultipart('alternative')
    msg['From'] = "pere.noel@domain.com" # A completer
    msg['To'] = participant['email']
    msg['Subject'] = subject
    msg.attach(MIMEText(html, 'html'))
    server.send_message(msg)

# Préparer et envoyer l'email de récapitulatif à Alexis Kournwsky
subject_summary = "Récapitulatif du tirage au sort Secret Santa"
html_summary = "<html><body><h3>Récapitulatif du tirage au sort Secret Santa</h3><ul>"

for giver, receiver in pairs.items():
    html_summary += f"<li>{giver} offre un cadeau à {receiver}</li>"

html_summary += "</ul></body></html>"
msg_summary = MIMEMultipart('alternative')
msg_summary['From'] = "pere.noel@vdomain.com" # A completer
msg_summary['To'] = "mail@domain.com" # A completer 
msg_summary['Subject'] = subject_summary
msg_summary.attach(MIMEText(html_summary, 'html'))
server.send_message(msg_summary)

server.quit()
print("Tous les emails ont été envoyés, y compris le récapitulatif.")