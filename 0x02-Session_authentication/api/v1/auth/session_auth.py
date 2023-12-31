#!/usr/bin/env python3
"""session_auth module"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        self.user_id = str(uuid.uuid4())
        self.user_id_by_session_id[self.user_id] = user_id
        return self.user_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns User instance based on cookie value"""
        cookie = self.session_cookie(request)
        userID = self.user_id_for_session_id(cookie)
        user = User.get(userID)
        return user

    def destroy_session(self, request=None):
        """deletes the user session / logout:"""
        if not request:
            return False
        sesh_id = self.session_cookie(request)
        if not sesh_id:
            return False
        u_id = self.user_id_for_session_id(sesh_id)
        if not u_id:
            return False
        del self.user_id_by_session_id[sesh_id]
        return True
