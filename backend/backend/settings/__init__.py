from .common import *

try:
    from .secrets import *
except:
    from .secrets_template import *

DOMAIN_ROOT = ALLOWED_HOSTS[0]
if DEBUG:
    DOMAIN_ROOT = "http://" + DOMAIN_ROOT
else:
    DOMAIN_ROOT = "https://" + DOMAIN_ROOT


if os.environ.get("ALLOWED_HOSTS") is not None:
    try:
        ALLOWED_HOSTS += os.environ.get("ALLOWED_HOSTS").split(",")
    except Exception as e:
        print("Cant set ALLOWED_HOSTS, using default instead")

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {"client_id": GOOGLE_CLIENT_ID, "secret": GOOGLE_SECRET, "key": GOOGLE_KEY},
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    "microsoft": {
        "APP": {"client_id": MICROSOFT_CLIENT_ID, "secret": MICROSOFT_SECRET, "key": MICROSOFT_KEY},
        "SCOPE": [
            "User.Read",
            "User.ReadBasic.All",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
}
