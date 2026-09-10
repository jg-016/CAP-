from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.password_validation import validate_password


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)

        if password is not None:
            if not extra_fields.get('is_superuser', False):
                validate_password(password, usuario)

            usuario.set_password(password)
        else:
            usuario.set_unusable_password()

        usuario.full_clean()
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields["is_staff"] is not True:
            raise ValueError("Superuser deve ter is_staff=True.")

        if extra_fields["is_superuser"] is not True:
            raise ValueError("Superuser deve ter is_superuser=True.")

        return self.create_user(email, password, **extra_fields)