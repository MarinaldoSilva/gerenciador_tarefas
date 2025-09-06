from django.core.management.utils import get_random_secret_key
secret_key = get_random_secret_key()
print(f"Sua chave para testar o meu projeto foi gerada: {secret_key}")
print("Crie seu arquivo '.env' e crie sua variavel 'SECRET_KEY' e atribua e ela em aspas o valor da chave")
