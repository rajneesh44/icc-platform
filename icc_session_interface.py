import os
import hashlib
from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionMixin, SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer, BadSignature


COOKIE_TTL = int(os.getenv("COOKIE_EXPIRATION_TIME", 0))

class ICCSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.modified = False

class ICCSessionInterface(SecureCookieSessionInterface):
    salt = "cookie-session"
    session_class = ICCSession

    digest_method = staticmethod(hashlib.sha512)
    key_derivation = "hmac"

    def get_serializer(self, app):
        signer_kwargs = dict(
            key_derivation=self.key_derivation, digest_method=self.digest_method
        )
        if not app.secret_key:
            return None
        return URLSafeTimedSerializer(
            app.secret_key,
            salt=self.salt,
            signer_kwargs=signer_kwargs
        )
    
    def open_session(self, app, request):
        app.permanent_session_lifetime = COOKIE_TTL
        csession = self.get_serializer(app)
        if csession is None:
            return None
        val = request.cookies.get(app.session_cookie_name)
        if not val:
            return self.session_class()
        max_age = COOKIE_TTL
        try:
            data = csession.loads(val, max_age=max_age)
            return self.session_class(data)
        except BadSignature:
            self.session_class().clear()            
            return self.session_class()
        
    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            if session.modified:
                response.delete_cookie(app.session_cookie_name,
                                   domain=domain)
            return
        session.permanent = True
        expires = self.get_expiration_time(app, session)
        val = self.get_serializer(app).dumps(dict(session))
        response.set_cookie(app.session_cookie_name, val,
                            expires=expires, httponly=False,
                            domain=domain, samesite="None", secure=True)

  

# CHECK LOGOUT FLOW OF COOKIES