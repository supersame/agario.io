import pygame
import random
pygame.init()
win = pygame.display.set_mode((700,500))

x = 350
y = 250
r = 50

x2 = 200
y2 = 400
r2 = 50



foods = [
  (350,250), 
  (450,350),
  (300,300), 
  (160,290), 
  (500,350),
  (200,400), 
  (332,410), 
  (300,250), 
]

while True:
  win.fill((0,0,0))
  pygame.time.delay(11)
  
  for food in foods:
    # draw food
    # food looks like (300, 250)
    xfood, yfood = food
    pygame.draw.circle(win, (255,255,255), (food), 10)
    distance = ((xfood-x)**2+(yfood-y)**2)**0.5
    if distance < r:
      # remove this food
      # remove this food from the list of foods. 
      try: 
        foods.remove(food)
      except:
        pass
      # make radius grow
      r = r + 8
      newfoodatrandomlocation = (random.randint(0,700),random.randint(0,500))
      foods.append(newfoodatrandomlocation)

    distance = ((xfood-x2)**2+(yfood-y2)**2)**0.5
    if distance < r2:
      # remove tsahis food
      # remove this food from the list of foods. 
      try: 
        foods.remove(food)
      except:
        pass
      # make radius grow
      r2 = r2 + 8
      newfoodatrandomlocation = (random.randint(0,700),random.randint(0,500))
      foods.append(newfoodatrandomlocation)

  playerdistance = ((x-x2)**2+(y-y2)**2)**0.5
  if playerdistance < r:
    # player 1 is eating player 2
    r += r2
    r2 = 0
  if playerdistance < r2:
    # player 2 is eating player 1
    
    r2 += r
    r = 0
  pygame.draw.circle(win,(255,255,255),(x,y),r)
  pygame.draw.circle(win,(255,0,255),(x2,y2),r2)
  pygame.display.update()

  pygame.event.pump()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    y = y - 10
  if keys[pygame.K_DOWN]:
    y = y + 10
  if keys[pygame.K_RIGHT]:
    x = x + 10
  if keys[pygame.K_LEFT]:
    x = x - 10
  if keys[pygame.K_w]:
    y2 = y2 -10
  if keys[pygame.K_s]:
    y2 = y2 + 10
  if keys[pygame.K_a]:
    x2 = x2 - 10
  if keys[pygame.K_d]:
    x2 = x2 + 10  


  
