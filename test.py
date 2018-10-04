import pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640, 480))

print(pygame.font.get_fonts())

textFont = pygame.font.SysFont("comicsansms", 25)

nam = 'Link'
pe = 'Spyro'
ver = 'ate'
snac = 'doughnuts'

def madlib(name, pet, verb, snack):
    return ['Once upon a time,' + name + ' walked',
    ' with ' + pet + ', a trained dragon. ',
    'Suddenly, ' + pet + ' announced,',
    'I really want some ' + snack + '! ',
    name + ' complained. Where am I going to get that? ',
    'Then ' + name + "found a wizard's wand. ",
    'With a wave of the wand, ',
    pet + ' got ' + snack + '. ',
    'Perhaps surprisingly, ' + pet + ' ' + verb + ' ' + snack]

Story = madlib(nam, pe, ver, snac)
StoryLength = len(Story)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))

    num = -15
    for i in Story:
        surface = textFont.render(i, True, (0, 0, 0))
        num += 25
        screen.blit(surface, (0, num))

    pygame.display.flip()