from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


#  класс для формы регистрации
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # модель связанная с формой
        model = User
        # поля и их порядок в форме
        fields = ('first_name', 'last_name', 'username', 'email')
