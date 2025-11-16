


class BhyveSession():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'bhyve_account_roles' : self.bhyve_account_roles,
            'bhyve_account_id' : self.bhyve_account_id,
            'bhyve_account_groups' : self.bhyve_account_groups,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'orbit_session_token' : self.orbit_session_token,
            'roles' : self.roles,
            'require_password_change' : self.require_password_change,
            'user_id' : self.user_id,
            'user_name' : self.user_name
        }

        
    @property
    def bhyve_account_roles(self) -> list[str] | None:
        return self._data.get('bhyve_account_roles')


    @property
    def first_name(self) -> str | None:
        return self._data.get('first_name')


    @property
    def bhyve_account_id(self) -> str | None:
        return self._data.get('bhyve_account_id')


    @property
    def bhyve_account_groups(self) -> str | None:
        return self._data.get('bhyve_account_groups')


    @property
    def orbit_session_token(self) -> str | None:
        return self._data.get('orbit_session_token')


    @property
    def roles(self) -> list[str] | None:
        return self._data.get('roles')


    @property
    def require_password_change(self) -> bool | None:
        return self._data.get('require_password_change')


    @property
    def last_name(self) -> str | None:
        return self._data.get('last_name')


    @property
    def user_id(self) -> str | None:
        return self._data.get('user_id')


    @property
    def user_name(self) -> str | None:
        return self._data.get('user_name')