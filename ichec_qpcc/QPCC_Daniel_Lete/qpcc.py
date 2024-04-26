import gspread
from string import ascii_uppercase, ascii_lowercase
from IPython.display import YouTubeVideo
from jupyterquiz import display_quiz
from jupytercards import display_flashcards



def submit(student_id, answer):
  with open('answers.txt','w') as answers_file:
    answers_file.write(student_id + "\n" + str(answer))
    
def qpcc_player(video_id = None):
    if video_id == 'Lec001':
        display(YouTubeVideo('S5x1N9vLM7g',width=1280, height=720))
    if video_id == 'Lec002':
        display(YouTubeVideo('WQme0EqcQ-k',width=1280, height=720))
    if video_id == 'Lec003':
        display(YouTubeVideo('o5IeqQi9n3s',width=1280, height=720))
    if video_id == 'Lec004':
        display(YouTubeVideo('CcVlVLLh8M0',width=1280, height=720))
    if video_id == 'Lec005':
        display(YouTubeVideo('7r1yrueMgZs',width=1280, height=720))
    if video_id == 'Lec006':
        display(YouTubeVideo('Lb2o6Qb8zxY',width=1280, height=720))
    if video_id == 'Lec007':
        display(YouTubeVideo('OSJUT5IHAuw',width=1280, height=720))
        

def qpcc_quiz(video_id = None):
    if video_id == 'Lec001':
        display_quiz('Material/questions_1.json')
    if video_id == 'Lec002':
        display_quiz('Material/questions_2.json')
    if video_id == 'Lec003':
        display_quiz('Material/questions_3.json')
    if video_id == 'Lec004':
        display_quiz('Material/questions_4.json')
    if video_id == 'Lec005':
        display_quiz('Material/questions_5.json')
    if video_id == 'Lec006':
        display_quiz('Material/questions_6.json')
    if video_id == 'Lec007':
        display_quiz('Material/questions_7.json')
    
    
def qpcc_cards(video_id = None):
    if video_id == 'Lec001':
        display_flashcards('Material/cards_1.json')
    if video_id == 'Lec002':
        display_flashcards('Material/cards_2.json')
    if video_id == 'Lec003':
        display_flashcards('Material/cards_3.json')
    if video_id == 'Lec004':
        display_flashcards('Material/cards_4.json')
    if video_id == 'Lec005':
        display_flashcards('Material/cards_5.json')
    if video_id == 'Lec006':
        display_flashcards('Material/cards_6.json')
    if video_id == 'Lec007':
        display_flashcards('Material/cards_7.json')
    