import time
hp_pl = int(input('Введи HP игрока (0..100)>>> '))
d_pl = int(input('Введи урон игрока (0..100)>>> '))
shield_pl = int(input('Введи щит игрока (0..5)>>> ')
hp_npc = int(input('Введи HP NPC (0..100)>>> '))
d_npc = int(input('Введи урон NPC (0..100)>>> '))
hield_npc = int(input('Введи щит NPC (0..5)>>> ')

count = 0
round_log = []
while hp_pl > 0 and hp_npc > 0:
    hp_pl -= d_npc
    hp_npc -= d_pl
    count += 1
print('Идет бой')
time.sleep(5)
if hp_pl >= hp_npc:
    print(f'Победил игрок, бой длился {count} часа')
else:
    print(f'Победил игрок, бой длился {count} часа')   