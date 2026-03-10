"""
Module for managing user settings through locking.
"""

def create_user_settings():
    """
    Creates and returns a function to manage settings.
    Demonstrates locking (providing access to the settings dictionary).
    """

    settings = {
        "theme": "dark",
        "language": "en",
        "notifications": True
    }

    def manage_settings(action: str, key: str = None, value=None):
        """
        Controls settings: 'get' (get all),
        'set' (change) or 'view' (show one).
        """

        if action == "get":
            return settings

        if action == "set" and key in settings:
            settings[key] = value
            return f"Setting '{key}' changed to '{value}'"

        if action == "view" and key in settings:
            return settings[key]

        return "Incorrect action or key"

    return manage_settings

if __name__ == "__main__":

    user_settings = create_user_settings()

    print(f"Current settings: {user_settings('get')}")
    print(user_settings('set', 'theme', 'light'))
    print(f"Language: {user_settings('view', 'language')}")
    print(f"Settings: {user_settings('get', 'notifications', False)}")
