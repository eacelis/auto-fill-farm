import random
import pyautogui
import time
import os
# pip install -r requirements.txt

CHECKBOX = 'img/checkbox.png'
EMPTY = "img/empty.png"
PAINT = "img/paint.png"
TRANSPARENT = "img/transparent.png"
LOGIN = "img/login.png"
GOOD = "img/good.png"
GOOGLE = "img/google.png"

def find_limits():
    puntos = []
    
    time.sleep(3)
    print("Haga clic en el primer punto...")
    x1, y1 = pyautogui.position()
    pyautogui.click()
    puntos.append((x1, y1))
    print(f"Punto 1: ({x1}, {y1})")

    time.sleep(3)
    print("Haga clic en el segundo punto...")
    x2, y2 = pyautogui.position()
    pyautogui.click()
    puntos.append((x2, y2))
    print(f"Punto 2: ({x2}, {y2})")
    
    time.sleep(3)
    return puntos

def find_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: No se encuentra {image_path}")
        exit()
    
    try:
        time.sleep(1)
        img_location = pyautogui.locateOnScreen(image_path, confidence=0.7)
             
        if img_location:
            center = pyautogui.center(img_location)            
            print("Se encontro la imagen")
            return center
            
    except pyautogui.ImageNotFoundException:
        print("No se pudo encontrar la imagen")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def click_image(position):
    if position is not None:
        print("Click")
        pyautogui.click(position)
        return True
    else:
        return False

def get_random_point(puntos):    
    x1, y1 = puntos[0]
    x2, y2 = puntos[1]

    factor = random.random()
    xR = x1 + factor * (x2 - x1)
    factor = random.random()
    yR = y1 + factor * (y2 - y1)
    
    return (int(round(xR, 2)), int(round(yR, 2)))

def login():
    if find_image(LOGIN):
        click_image(find_image(LOGIN))
        
        flag = False
        while not flag:
            if(find_image(CHECKBOX)):
                flag = True
                check_captcha()
            elif(find_image(GOOD)):
                flag = True
                
        image = find_image(GOOGLE)
        click_image(image)
        time.sleep(5)
    else:
        pass

def check_captcha():
    check = find_image(CHECKBOX)
    if check:
        click_image(check)
    else:
        pass
    
def verificar():
    login()
    check_captcha()


if __name__ == "__main__":
    
    puntos = find_limits()
   
    while True:
        if(find_image(EMPTY) == True):
            time.sleep(35)
        else:
            verificar()
            image = find_image(PAINT)
            click_image(image)
            verificar()
            image = find_image(TRANSPARENT)
            if image != None:
                click_image(image)
                click_image(get_random_point(puntos))
                verificar()           
            verificar()
            image = find_image(PAINT)
            click_image(image)
            