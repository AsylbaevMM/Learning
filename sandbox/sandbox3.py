


PERMISSIONS_WITH_DESCRIPTIONS = {
    'PERM_1_CODENAME': ['perm 1 name', 'Description for permission 1'],
    'PERM_2_CODENAME': ['perm 2 name', 'Description for permission 2'],
    'PERM_3_CODENAME': ['perm 3 name', 'Description for permission 3'],
    'PERM_4_CODENAME': ['perm 4 name', 'Description for permission 4'],
    'PERM_5_CODENAME': ['perm 5 name', 'Description for permission 5'],
    }

# это можно передать в метакласс
PERMISSIONS = [(codename, info[0]) for codename, info in PERMISSIONS_WITH_DESCRIPTIONS.items()]

print(*PERMISSIONS, sep='\n')