class RoleBasedRouter:
    def db_for_read(self, model, **hints):
        """Direct read operations to the appropriate database."""
        role = hints.get('role')
        if role == 'student':
            return 'student'
        elif role == 'tutor':
            return 'tutor'
        return 'default'

    def db_for_write(self, model, **hints):
        """Direct write operations to the appropriate database."""
        role = hints.get('role')
        if role == 'student':
            return 'student'
        elif role == 'tutor':
            return 'tutor'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if both objects are in the same database."""
        db_set = {'default', 'student', 'tutor'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure migrations apply to the correct database."""
        if db == 'student' and app_label == 'your_app':  # Replace 'your_app' with your app's name
            return True
        elif db == 'tutor' and app_label == 'your_app':
            return True
        elif db == 'default':
            return True
        return False
