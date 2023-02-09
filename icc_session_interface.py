import os
from flask import session, request
from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionMixin, SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer, BadSignature


class ICCSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.modified = False

class ICCSessionInterface(SecureCookieSessionInterface):
    salt = os.getenv('SESSION_SALT')
    session_class = ICCSession

    def get_serializer(self, app):
        if not app.secret_key:
            return None
        return URLSafeTimedSerializer(app.secret_key,
                                      salt=self.salt)
    
    def open_session(self, app, request):
        csession = self.get_serializer(app)
        if csession is None:
            return None
        val = request.cookies.get(app.session_cookie_name)
        if not val:
            return self.session_class()
        max_age = 60*60*24*30        
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
        expires = self.get_expiration_time(app, session)
        val = self.get_serializer(app).dumps(dict(session))
        response.set_cookie(app.session_cookie_name, val,
                            expires=expires, httponly=True,
                            domain=domain)

  