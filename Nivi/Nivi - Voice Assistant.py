import speech_recognition as sr
import pygame.mixer as pymix
from pywhatkit import playonyt,search
import turtle
import customtkinter as ctk
import tkinter as tk
import pygame
from math import factorial
from gtts import gTTS
from time import sleep,strftime
from random import choice,randint

# Common variables
pymix.init()
calculation = ""
calculation_text = ""
player = ""

# Main function
def runNivi():

    # Playing Music
    def play_music(type_music):
        pymix.init()
        base_string = r"C:/Users/Sounds/"
        if type_music == "activate":
            pymix.music.load(base_string + "activate2.mp3")
            pymix.music.play()
        elif type_music == "close":
            pymix.music.load(base_string + "closeSiri.mp3")
            pymix.music.play()
        elif type_music == "newTick":
            pymix.music.load(base_string + "newTick.mp3")
            pymix.music.play()
        elif type_music == "finish":
            pymix.music.load(base_string + "finish.mp3")
            pymix.music.play()
        elif type_music == "activate2":
            pymix.music.load(base_string + "activate2.mp3")
            pymix.music.play()
        else:
            pass

    # Output Response
    def speech(response):
        print(response)
        language = "en"
        output = gTTS(text=response, lang=language, slow=False)
        output.save(r"C:/Users/ravia/PycharmProjects/Project_files/output.mp3")
        pymix.music.load(r"C:/Users/ravia/PycharmProjects/Project_files/output.mp3")
        pymix.music.play()

    # Getting Input Voice
    def get_audio():
        recorder = sr.Recognizer()
        with sr.Microphone() as source:
            recorder.adjust_for_ambient_noise(source)

            try:
                print("listening..")
                pymix.init()
                pymix.music.load(r"C:/Users/Sounds/activate2.mp3")
                pymix.music.play()
                audio = recorder.listen(source)
                if not audio:
                    audio = recorder.listen(source, timeout=5)
            except UnboundLocalError:
                try:
                    """recorder = sr.Recognizer()
                    with sr.Microphone() as source:
                        recorder.adjust_for_ambient_noise(source)
                        audio = recorder.listen(source)"""
                    print("Coming here")
                except:
                    pass
        voice = recorder.recognize_google(audio, language="en-US")
        print(f"You said:{voice}")
        return voice

    text = get_audio()

    if "play" in text.lower():
        play_music("activate2")
        speech("playing for you on youtube")
        playonyt(text)

    elif "goodbye" in text.lower():
        speech("goodbye!")
        sleep(1)
        play_music('close')
        exit()

    elif "tic-tac-toe" in text.lower():
        # Music
        play_music("activate2")
        speech("opening tic tac toe. Enjoy playing.")

        def next_turn(row, column):
            global player

            # Check if button is empty and no winner
            if buttons[row][column]['text'] == "" and check_winner() is False:

                if player == players[0]:

                    # If current player is X, mark the button 'x'
                    buttons[row][column]['text'] = player

                    # Check if that move resulted in a win, tie or continue the game
                    if check_winner() is False:
                        player = players[1]  # Switching Turns
                        label.config(text=(players[1] + " turn"))

                    elif check_winner() is True:
                        label.config(text=(players[0] + " wins"))

                    elif check_winner() == "Tie":
                        label.config(text="Tie!")

                else:
                    # If current player is O, mark the button with 'o'
                    buttons[row][column]['text'] = player

                    # Check if the move resulted in a win, tie or continue the game
                    if check_winner() is False:
                        player = players[0]  # Switching turns
                        label.config(text=(players[0] + " turn"))

                    elif check_winner() is True:
                        label.config(text=(players[1] + " wins"))

                    elif check_winner() == "Tie":
                        label.config(text="Tie!")

        def check_winner():

            # Checking each row, column and diagonals for a win
            for row in range(3):
                if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                    buttons[row][0].config(bg="green")
                    buttons[row][1].config(bg="green")
                    buttons[row][2].config(bg="green")
                    return True

            for column in range(3):
                if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                    buttons[0][column].config(bg="green")
                    buttons[1][column].config(bg="green")
                    buttons[2][column].config(bg="green")
                    return True

            if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
                buttons[0][0].config(bg="green")
                buttons[1][1].config(bg="green")
                buttons[2][2].config(bg="green")
                return True

            elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
                buttons[0][2].config(bg="green")
                buttons[1][1].config(bg="green")
                buttons[2][0].config(bg="green")
                return True

            # Check if all spaces are filled resulting in a tie
            elif empty_spaces() is False:
                for row in range(3):
                    for column in range(3):
                        buttons[row][column].config(bg="yellow")
                return "Tie"

            # Continue the game if no winner or tie
            else:
                return False

        def empty_spaces():
            spaces = 9  # Total of 9 spaces

            for row in range(3):
                for column in range(3):
                    if buttons[row][column]['text'] != "":
                        spaces -= 1  # Decreasing the no. of spaces if a button is filled

            # False if no empty spaces, otherwise True
            if spaces == 0:
                return False
            else:
                return True

        def new_game():
            global player

            # Start a new game by randomly choosing a player
            player = choice(players)

            label.config(text=player + " turn")

            # Reset the buttons and restore default colors
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(text="", bg="#F0F0F0")

        # Window
        window = tk.Tk()
        window.title("Tic-Tac-Toe")

        # Players (X and O)
        players = ["x", "o"]
        player = choice(players)  # Randomly select who starts

        # 3x3 grid of buttons for the Tic-Tac-Toe board
        buttons = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

        # Label to show which player's turn
        label = tk.Label(text=player + " turn", font=('consolas', 40))
        label.pack(side="top")

        # Reset button to start a new game
        reset_button = tk.Button(text="restart", font=('consolas', 20), command=new_game)
        reset_button.pack(side="top")

        # Frame to hold the buttons
        frame = tk.Frame(window)
        frame.pack()

        # Create and place buttons in the grid
        for rows in range(3):
            for columns in range(3):
                buttons[rows][columns] = tk.Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                                   command=lambda row=rows, column=columns: next_turn(row, column))
                buttons[rows][columns].grid(row=rows, column=columns)

        # Mainloop
        window.mainloop()


    elif "good night" in text.lower():
        play_music("activate2")
        speech("Sleep tight")
        sleep(1)
        play_music("close")
        sleep(1)
        exit()

    elif "timer" in text.lower():
        try:
            # Music
            play_music("activate2")
            speech("Starting your timer.")
            sleep(2)

            # Window
            root = tk.Tk()
            root.geometry('400x300')
            root.title('Nivi Timer')
            root.config(bg='green')

            # Flag
            root.stop_loop = False

            # Function to update and display the current time on the label
            def Clock():
                display_time = strftime('%H:%M:%S %p')
                display_time_label.config(text=display_time)
                display_time_label.after(1000, Clock)

                # Function to stop and close the timer window

            def stop():
                root.destroy()

            def timer():
                # Convert hour, minute, and second values to seconds
                time_in_sec = int(hour_value) * 3600 + int(minute_value) * 60 + int(second_value)
                while time_in_sec > -1:
                    if time_in_sec == -2:
                        break
                    minutes = time_in_sec // 60
                    second = time_in_sec % 60
                    hour = 0
                    if minutes > 59:
                        hour = minutes // 60
                        minutes = minutes % 60

                    # Update the displayed hour, minute, and second values
                    hr.set(hour)
                    minute.set(minutes)
                    sec.set(second)
                    time_in_sec = time_in_sec - 1
                    root.update()

                    # Play ticking sound
                    pymix.music.load(r"C:\Users\ravia\PycharmProjects\Project_files\newTick.mp3")
                    pymix.music.play()
                    sleep(1)

                    # When the countdown reaches zero, reset the timer
                    if time_in_sec <= -1:
                        hr.set('00')
                        minute.set('00')
                        sec.set('00')
                        pymix.music.load(r"C:\Users\ravia\PycharmProjects\Project_files\finish.mp3")
                        pymix.music.play()
                        speech("You're time is up!")
                        stop()
                        root.destroy()
                        break

            # Time classifier to store hour, minute, and second values
            time_classifier = [0, 0, 0]

            # Parse the user input for hours, minutes, and seconds
            if "hour" in text.lower():
                current_time_value = ''
                time_digit_checklist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                x = text.lower()
                for i in range(len(x)):
                    if x[i] in time_digit_checklist:
                        current_time_value += x[i]
                    else:

                        # Extract hours from user input
                        if x[i:i + 4] == "hour":
                            time_classifier[0] = current_time_value
                            current_time_value = ''

                        # Extract minutes from user input
                        elif x[i:i + 4] == "minu":
                            time_classifier[1] = current_time_value
                            current_time_value = ''

                        # Extract seconds from user input
                        elif x[i:i + 4] == "seco":
                            time_classifier[2] = current_time_value
                            current_time_value = ''

            # If no hours but minutes are mentioned in the input
            elif "minute" in text.lower():
                current_time_value = ''
                time_digit_checklist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                x = text.lower()
                for i in range(len(x)):
                    if x[i] in time_digit_checklist:
                        current_time_value += x[i]
                    else:

                        # Extract minutes from user input
                        if x[i:i + 4] == "minu":
                            time_classifier[1] = current_time_value
                            current_time_value = ''

                        # Extract seconds from user input
                        elif x[i:i + 4] == "seco":
                            time_classifier[2] = current_time_value
                            current_time_value = ''
                print(time_classifier)

            # If only seconds are mentioned in the input
            elif "second" in text.lower():
                current_time_value = ''
                time_digit_checklist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                x = text.lower()
                for i in range(len(x)):
                    if x[i] in time_digit_checklist:
                        current_time_value += x[i]
                    else:

                        # Extract seconds from user input
                        if x[i:i + 4] == "seco":
                            time_classifier[2] = current_time_value
                            current_time_value = ''
            else:
                pass

            # Assign parsed values for hour, minute, and second
            hour_value = time_classifier[0]
            minute_value = time_classifier[1]
            second_value = time_classifier[2]

            # Timer window labels
            title_label = tk.Label(root, text='Nivi Timer', font='Arial 20 bold', fg='yellow', bg='green')
            title_label.pack()

            # Labels to show current time
            current_time = tk.Label(root, text='Current time: ', font='Arial 20 bold', fg='yellow', bg='green')
            current_time.place(x=30, y=70)

            display_time_label = tk.Label(root, text='', font='Times 20 bold', fg='yellow', bg='green')
            display_time_label.place(x=225, y=70)

            # Label for the timer
            timer_label = tk.Label(root, text='Timer: ', font='Arial 20 bold', fg='yellow', bg='green')
            timer_label.place(x=30, y=150)

            # StringVars to hold hour, minute, and second values for the timer
            hr = tk.StringVar()
            minute = tk.StringVar()
            sec = tk.StringVar()
            hr.set(str(hour_value))  # Set hour value
            minute.set(str(minute_value))  # Set minute value
            sec.set(str(second_value))  # Set second value

            # Entry fields to display and update the timer's hour, minute, and second values
            hr_entry = tk.Entry(root, textvariable=hr, width=2, font='Times 20 bold')
            hr_entry.place(x=125, y=150)

            min_entry = tk.Entry(root, textvariable=minute, width=2, font='Times 20 bold')
            min_entry.place(x=175, y=150)

            sec_entry = tk.Entry(root, textvariable=sec, width=2, font='Times 20 bold')
            sec_entry.place(x=225, y=150)

            # Start the clock and timer
            Clock()
            timer()

            # Mainloop
            root.mainloop()
        except:
            pass

    elif "space game" in text.lower():
        play_music("activate2")
        speech("Opening Space Game. Enjoy playing.")

        base_path = r'D:\\Data\\OneDrive\\Data\\Kids\\Sri Ranjani\\Animation\\Python\\'

        def Draw_bg():
            window.blit(bg, (0, 0))

        class Spaceship(pygame.sprite.Sprite):
            def __init__(self, x_cor, y, lives):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(base_path + 'spaceship.png')
                self.rect = self.image.get_rect()
                self.rect.center = [x_cor, y]
                self.lives_start = lives
                self.lives_remaining = lives
                self.last_shot = pygame.time.get_ticks()
                self.mask = pygame.mask.from_surface(self.image)

            def update(self):
                speed = 10
                game_over_check = 0
                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT] and self.rect.left > 0:
                    self.rect.x -= speed
                if key[pygame.K_RIGHT] and self.rect.right < 600:
                    self.rect.x += speed
                current_time_now = pygame.time.get_ticks()

                # Shooting bullets
                if key[pygame.K_SPACE] and current_time_now - self.last_shot > 500:
                    laser.play()
                    bullet = Bullet(self.rect.centerx, self.rect.top)
                    bullet_group.add(bullet)
                    self.last_shot = current_time_now

                # Updating the lives
                pygame.draw.rect(window, 'red', (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
                if self.lives_remaining > 0:
                    pygame.draw.rect(window, 'green', [self.rect.x, (self.rect.bottom + 10),
                                                       int(self.rect.width * self.lives_remaining / self.lives_start),
                                                       15])
                elif self.lives_remaining <= 0:
                    explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
                    explosion_group.add(explosion)
                    self.kill()
                    game_over_check = -1
                return game_over_check

        class Bullet(pygame.sprite.Sprite):
            def __init__(self, x_cor, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(base_path + 'bullet.png')
                self.rect = self.image.get_rect()
                self.rect.center = [x_cor, y]

            def update(self):
                self.rect.y -= 5
                if self.rect.bottom < 0:
                    self.kill()
                if pygame.sprite.spritecollide(self, alien_group, True):
                    self.kill()

                    # Explosion
                    explosion1.play()
                    explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
                    explosion_group.add(explosion)

        class Alien(pygame.sprite.Sprite):
            def __init__(self, x_cor, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(base_path + 'alien' + str(randint(1, 4)) + '.png')
                self.rect = self.image.get_rect()
                self.rect.center = [x_cor, y]
                self.move_counter = 0
                self.move_direction = 1

            def update(self):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if abs(self.move_counter) > 75:
                    self.move_direction *= -1
                    self.move_counter *= self.move_direction

        class AlienBullets(pygame.sprite.Sprite):
            def __init__(self, x_cor, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(base_path + 'alien_bullet.png')
                self.rect = self.image.get_rect()
                self.rect.center = [x_cor, y]

            def update(self):
                self.rect.y += 2
                if self.rect.top > 650:
                    self.kill()
                if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
                    self.kill()
                    spaceship.lives_remaining -= 1

                    # Explosion
                    explosion2.play()
                    explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
                    explosion_group.add(explosion)

        class Explosion(pygame.sprite.Sprite):
            def __init__(self, x_cor, y, size):
                pygame.sprite.Sprite.__init__(self)
                self.images = []
                for num in range(1, 6):
                    img = pygame.image.load(base_path + f"exp{num}.png")
                    if size == 1:
                        img = pygame.transform.scale(img, (20, 20))
                    if size == 2:
                        img = pygame.transform.scale(img, (40, 40))
                    if size == 3:
                        img = pygame.transform.scale(img, (160, 160))
                    self.images.append(img)
                    self.index = 0
                    self.counter = 0
                    self.image = self.images[self.index]
                    self.rect = self.image.get_rect()
                    self.rect.center = [x_cor, y]

            def update(self):
                self.counter += 1
                if self.counter >= 5:
                    self.counter = 0
                    self.index += 1
                    self.image = self.images[self.index]
                if self.index >= len(self.images) - 1:
                    self.kill()

        def Create_Aliens():
            for row in range(6):
                for col in range(5):
                    alien = Alien(100 + col * 100, 50 + row * 50)
                    alien_group.add(alien)

        def draw_text(content, font, text_col, x_cor, y):
            txt = font.render(content, True, text_col)
            window.blit(txt, (x_cor, y))

        pygame.init()

        # initialising mixer(sound)
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pymix.init()

        explosion1 = pygame.mixer.Sound(base_path + 'img_explosion.wav')
        explosion1.set_volume(0.25)

        explosion2 = pygame.mixer.Sound(base_path + 'img_explosion2.wav')
        explosion2.set_volume(0.25)

        laser = pygame.mixer.Sound(base_path + 'img_laser.wav')
        laser.set_volume(0.25)

        window = pygame.display.set_mode((600, 650))
        pygame.display.set_caption('Space War')
        clock = pygame.time.Clock()
        fps = 60
        last_alien_bullet = pygame.time.get_ticks()
        game_over = 0
        font40 = pygame.font.SysFont('Constantia', 40)

        bg = pygame.image.load(base_path + 'bgspace.png')

        spaceship_group = pygame.sprite.Group()
        spaceship = Spaceship(300, 550, 3)
        spaceship_group.add(spaceship)

        bullet_group = pygame.sprite.Group()

        alien_group = pygame.sprite.Group()

        alien_bullet_group = pygame.sprite.Group()

        explosion_group = pygame.sprite.Group()

        Create_Aliens()

        while True:
            clock.tick(fps)

            # Draw backdrop
            Draw_bg()

            # Creating alien bullets randomly
            time_now = pygame.time.get_ticks()
            if time_now - last_alien_bullet > 1000 and len(alien_bullet_group) < 5:
                attacking_alien = alien_group.sprites()[0]
                try:
                    attacking_alien = choice(alien_group.sprites())
                except IndexError:
                    pass
                alien_bullet = AlienBullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
                alien_bullet_group.add(alien_bullet)
                last_alien_bullet = time_now

            # Game won
            if len(alien_group) == 0:
                game_over = 1

            # Checking for game over
            if game_over == 0:
                game_over = spaceship.update()
                bullet_group.update()
                alien_group.update()
                alien_bullet_group.update()
            else:
                if game_over == -1:
                    draw_text('GAME OVER!', font40, 'white', 185, 230)
                if game_over == 1:
                    draw_text('YOU WIN!', font40, 'white', 185, 230)
            # Drawing groups
            spaceship_group.draw(window)
            bullet_group.draw(window)
            alien_group.draw(window)
            alien_bullet_group.draw(window)
            explosion_group.draw(window)

            # Quit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print('Game Over')
                    pymix.quit()    # This is to avoid any conflicts between the mixer and the speech recognition module
                    pymix.init()
                    return

            # Updating group
            explosion_group.update()

            # Updating window
            try:
                pygame.display.update()
            except pygame.error:
                break

    elif "good morning" in text.lower():
        play_music("activate2")
        speech("Good morning. How can I help?")

    elif "good afternoon" in text.lower():
        play_music("activate2")
        speech("Good afternoon. How can I help?")

    elif "good evening" in text.lower():
        play_music("activate2")
        speech("Good evening. How can I help?")

    elif "time" in text.lower():
        play_music("activate2")
        time = strftime("%I:%M %p")
        speech("Current time is " + time)
        sleep(1)

    elif "your name" in text.lower():
        play_music("activate2")
        speech("my name is Nivi")

    elif "search" in text.lower():
        play_music("activate2")
        speech("Searching on google")
        search(text)

    elif "who is" in text.lower():
        play_music("activate2")
        speech("Searching on google for relevant information.")
        search(text)
        sleep(1)

    elif "date" in text.lower():
        play_music("activate2")
        today = strftime("%d/%m/%Y")
        speech("Today's date is " + today)
        sleep(2)

    elif "thank you" in text.lower():
        play_music("activate2")
        speech("You're Welcome")

    elif "about yourself" in text.lower():
        play_music("activate2")
        speech("My name is Nivi . I am your virtual voice assistant. I was created by Nikhil and Ravi.")
        sleep(5)

    elif "calculator" in text.lower():
        play_music("activate2")
        speech("Opening Calculator")

        # Window
        root = ctk.CTk()
        root.title('Nivi Calculator')
        root.geometry("400x330")
        text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), foreground='#000')
        text_result.grid(columnspan=8)

        # Variables
        calculation = ""
        calculation_text = ""

        # Functions
        def add_to_calculation(symbol):
            global calculation, calculation_text
            calculation += str(symbol)
            calculation_text += str(symbol)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation_text)


        def evaluate_calculation():
            global calculation, calculation_text
            try:
                result = str(eval(calculation))
                text_result.delete(1.0, "end")
                text_result.insert(1.0, result)
                calculation = ''
                calculation_text = ''
            except ZeroDivisionError:
                clear_field()
                text_result.insert(1.0, "Error")
            calculation_text = ""


        def power():
            global calculation, calculation_text
            calculation += str("**")
            calculation_text += str("^")
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation_text)


        def reciprocal():
            global calculation, calculation_text
            calculation += str("**(-1)")
            calculation_text += str("^-1")
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation_text)


        def clear_field():
            global calculation, calculation_text
            calculation = ""
            calculation_text = ""
            text_result.delete(1.0, "end")

        def Factorial():
            global calculation, calculation_text
            calculation_text += str("!")
            fact = factorial(int(calculation))
            calculation = str(fact)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation_text)


        def backspace():
            global calculation, calculation_text
            new_text = len(calculation) - 1
            calculation = calculation[:new_text]
            calculation_text = calculation_text[:new_text]
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation_text)

        # Buttons
        btn_1 = ctk.CTkButton(root, text="1", command=lambda: add_to_calculation(1), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_1.grid(row=3, column=1, padx=5, pady=5)
        btn_2 = ctk.CTkButton(root, text="2", command=lambda: add_to_calculation(2), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_2.grid(row=3, column=2, padx=5, pady=5)
        btn_3 = ctk.CTkButton(root, text="3", command=lambda: add_to_calculation(3), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_3.grid(row=3, column=3, padx=5, pady=5)
        btn_4 = ctk.CTkButton(root, text="4", command=lambda: add_to_calculation(4), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_4.grid(row=4, column=1, padx=5, pady=5)
        btn_5 = ctk.CTkButton(root, text="5", command=lambda: add_to_calculation(5), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_5.grid(row=4, column=2, padx=5, pady=5)
        btn_6 = ctk.CTkButton(root, text="6", command=lambda: add_to_calculation(6), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_6.grid(row=4, column=3, padx=5, pady=5)
        btn_7 = ctk.CTkButton(root, text="7", command=lambda: add_to_calculation(7), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_7.grid(row=5, column=1, padx=5, pady=5)
        btn_8 = ctk.CTkButton(root, text="8", command=lambda: add_to_calculation(8), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_8.grid(row=5, column=2, padx=5, pady=5)
        btn_9 = ctk.CTkButton(root, text="9", command=lambda: add_to_calculation(9), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_9.grid(row=5, column=3, padx=5, pady=5)
        btn_0 = ctk.CTkButton(root, text="0", command=lambda: add_to_calculation(0), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_0.grid(row=6, column=2, padx=5, pady=5)
        btn_plus = ctk.CTkButton(root, text="+", command=lambda: add_to_calculation("+"), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_plus.grid(row=3, column=4, padx=5, pady=5)
        btn_minus = ctk.CTkButton(root, text="-", command=lambda: add_to_calculation("-"), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_minus.grid(row=4, column=4, padx=5, pady=5)
        btn_mul = ctk.CTkButton(root, text="*", command=lambda: add_to_calculation("*"), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_mul.grid(row=5, column=4, padx=5, pady=5)
        btn_div = ctk.CTkButton(root, text="/", command=lambda: add_to_calculation("/"), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_div.grid(row=6, column=4, padx=5, pady=5)
        btn_open = ctk.CTkButton(root, text="(", command=lambda: add_to_calculation("("), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_open.grid(row=6, column=1, padx=5, pady=5)
        btn_close = ctk.CTkButton(root, text=")", command=lambda: add_to_calculation(")"), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_close.grid(row=6, column=3, padx=5, pady=5)
        btn_equals = ctk.CTkButton(root, text="=", command=evaluate_calculation, fg_color=('#b700ff', '#0373fc'), text_color='white', hover_color=('#9905f5', '#039dfc'), width=105, font=("Arial", 14))
        btn_equals.grid(row=7, column=4, columnspan=2, padx=5, pady=5)
        btn_clear = ctk.CTkButton(root, text="clr", command=clear_field, fg_color=('#b700ff', '#0373fc'), text_color='white', hover_color=('#9905f5', '#039dfc'), width=105, font=("Arial", 14))
        btn_clear.grid(row=7, column=1, columnspan=2, padx=5, pady=5)
        btn_dot = ctk.CTkButton(root, text=".", command=lambda: add_to_calculation("."), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_dot.grid(row=7, column=3, padx=5, pady=5)
        btn_fact = ctk.CTkButton(root, text="!", command=lambda: Factorial(), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_fact.grid(row=6, column=5, padx=5, pady=5)
        btn_recip = ctk.CTkButton(root, text="1/x", command=lambda: reciprocal(), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_recip.grid(row=5, column=5, padx=5, pady=5)
        btn_pow = ctk.CTkButton(root, text="xⁿ", command=lambda: power(), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_pow.grid(row=4, column=5, padx=5, pady=5)
        btn_backspace = ctk.CTkButton(root, text="⌫", command=backspace, fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_backspace.grid(row=3, column=5, padx=5, pady=5)
        btn_lm = ctk.CTkButton(root, text="light mode", command=lambda: ctk.set_appearance_mode('light'), fg_color='white', text_color='black', hover_color='#ddd', width=50, font=("Arial", 14))
        btn_lm.grid(row=8, column=1, columnspan=2, padx=5, pady=5)
        btn_dm = ctk.CTkButton(root, text="Dark mode", command=lambda: ctk.set_appearance_mode('Dark'), fg_color='black', text_color='white', hover_color='#222', width=50, font=("Arial", 14))
        btn_dm.grid(row=8, column=4, columnspan=2, padx=5, pady=5)

        root.mainloop()

    elif "open snake game" in text.lower():
        play_music("activate2")
        speech("Opening Snake Game.Enjoy playing.")

        try:

            # Leaderboard
            maxi = 0
            delay = 0.1
            score = 0
            high_score = maxi

            # Screen
            screen = turtle.Screen()
            screen.title("NIVI SNAKE GAME")
            screen.setup(width=700, height=700)
            screen.tracer(0)
            screen.bgcolor("green")
            turtle.speed(5)
            turtle.pensize(4)
            turtle.penup()
            turtle.goto(-310, 250)
            turtle.pendown()
            turtle.color("red")
            turtle.forward(600)
            turtle.right(90)
            turtle.forward(500)
            turtle.right(90)
            turtle.forward(600)
            turtle.right(90)
            turtle.forward(500)
            turtle.penup()
            turtle.hideturtle()

            # Snake
            snake = turtle.Turtle()
            snake.speed(0)
            snake.shape("square")
            snake.color("yellow")
            snake.penup()
            snake.goto(0, 0)
            snake.direction = "stop"

            # Snake Food
            food = turtle.Turtle()
            food.speed(0)
            food.shape("circle")
            food.color("red")
            food.penup()
            food.goto(0, 100)
            segments = []

            # Pen
            pen = turtle.Turtle()
            pen.speed(0)
            pen.shape("square")
            pen.color("white")
            pen.penup()
            pen.hideturtle()
            pen.goto(0, 260)
            pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

            # Snake Movements
            def go_up():
                if snake.direction != "down":
                    snake.direction = "up"
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

            def go_down():
                if snake.direction != "up":
                    snake.direction = "down"
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

            def go_left():
                if snake.direction != "right":
                    snake.direction = "left"
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

            def go_right():
                if snake.direction != "left":
                    snake.direction = "right"
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

            def move():
                pen.goto(0, 260)
                if snake.direction == 'up':
                    y_cor = snake.ycor()
                    snake.sety(y_cor + 20)
                if snake.direction == 'down':
                    y_cor = snake.ycor()
                    snake.sety(y_cor - 20)
                if snake.direction == 'right':
                    x_cor = snake.xcor()
                    snake.setx(x_cor + 20)
                if snake.direction == 'left':
                    x_cor = snake.xcor()
                    snake.setx(x_cor - 20)

            # Keyboard
            screen.listen()
            screen.onkeypress(go_up, "Up")
            screen.onkeypress(go_down, "Down")
            screen.onkeypress(go_left, "Left")
            screen.onkeypress(go_right, "Right")

            # Main
            while True:
                screen.update()

            # Checking For Collisions With Border
                if snake.xcor() > 270 or snake.xcor() < -290 or snake.ycor() > 230 or snake.ycor() < -230:
                    sleep(1)
                    snake.goto(0, 0)
                    snake.direction = 'stop'

                    for segment in segments:
                        segment.goto(1000, 1000)
                    segments.clear()

                    # Resetting Score
                    pen.clear()
                    pen.goto(0, 270)
                    pen.write("\tGame Over\nScore: {} High Score: {}".format(score,
                    high_score), align="center",font=("Courier", 24, "normal"))
                    score = 0

                # Check Food Collision
                if snake.distance(food) < 20:
                    x_c = randint(-290, 270)
                    y_c = randint(-230, 230)
                    food.goto(x_c, y_c)

                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    new_segment.color("blue")
                    new_segment.penup()
                    segments.append(new_segment)

                # Shorten Delay
                    delay -= 0.001

                # Update Score
                    score += 10
                    if score > high_score:
                        high_score = score
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

                # Move End To First
                for index in range(len(segments) - 1, 0, -1):
                    xc = segments[index - 1].xcor()
                    yc = segments[index - 1].ycor()
                    segments[index].goto(xc, yc)

                # Move Segment 0 To Head
                if len(segments) > 0:
                    xc = snake.xcor()
                    yc = snake.ycor()
                    segments[0].goto(xc, yc)
                move()

                # Checking For Body Collision
                for segment in segments:
                    if segment.distance(snake) < 20:
                        sleep(1)
                        snake.goto(0, 0)
                        snake.direction = "stop"
                        pen.clear()
                        pen.goto(0, 270)
                        pen.write("\tGame Over\nScore: {} High Score: {}".format(score,high_score), align="center",font=("Courier", 24, "normal"))
                        score = 0

                        for segment_1 in segments:
                            segment_1.goto(1000, 1000)

                        # Clear
                        segments.clear()

                sleep(delay)
        except:
            pass

    elif "hello" in text.lower():
        play_music("activate")
        speech("Hi! How can I help?")

    else:
        speech("I can't understand.")
    sleep(1)

while True:
    try:
        runNivi()
    except UnboundLocalError:
        pass
