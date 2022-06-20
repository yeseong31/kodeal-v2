import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    Generate Tokens
    """
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp)) + six.text_type(user.is_active)


def message(domain, uidb64, token):
    """
    Active를 담당하는 Endpoint URL 주소를 메시지로 Send
    """
    return f"아래 링크를 클릭하면 회원가입 인증이 완료됩니다.\n\n" \
           f"회원가입 링크 : http://{domain}/common/activate/{uidb64}/{token}\n\n" \
           f"감사합니다."


account_activation_token = AccountActivationTokenGenerator()
