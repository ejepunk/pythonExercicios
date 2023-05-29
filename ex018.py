'''import math
an = float(input('digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o Seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(an, tan))'''

from math import radians, sin, cos, tan
an = float(input('digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o Seno de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tan = tan(radians(an))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(an, tan))
