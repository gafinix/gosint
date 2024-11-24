import requests
import whois

def lookup_email(email):
    try:
        domain = email.split('@')[-1]
        domain_info = whois.whois(domain)
        return {
            "Domain": domain,
            "Registrar": domain_info.registrar,
            "Creation Date": domain_info.creation_date,
            "Expiration Date": domain_info.expiration_date,
        }
    except Exception as e:
        return {"Error": str(e)}
