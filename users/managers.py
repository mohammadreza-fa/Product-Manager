from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password):
        if not email:
            raise ValueError('Enter your email')

        if not first_name:
            raise ValueError('Enter your first name')

        if not last_name:
            raise ValueError('Enter your last name')

        if not phone_number:
            raise ValueError('Enter your phone number')

        user = self.model(email=email, first_name=first_name, last_name=last_name, phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, phone_number, password):
        user = self.create_user(email, first_name, last_name, phone_number, password)
        user.is_admin = True
        user.is_staff = True
        user.role = 'manager'
        user.save()
        return user
