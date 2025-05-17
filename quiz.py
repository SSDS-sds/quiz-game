import pgzrun

WIDTH = 870
HEIGHT = 650
TITLE = "QUIZ MASTER"

marquee_box = Rect(0,0,880,80)
skip_box = Rect(0,0,150,330)
timer_box = Rect(0,0,150,150)
question_box = Rect(0,0,650,150)
ans_box1 = Rect(0,0,300,150)
ans_box2 = Rect(0,0,300,150)
ans_box3 = Rect(0,0,300,150)
ans_box4 = Rect(0,0,300,150)
score_box = Rect(0,0,150,30)

score = 0
timer_left = 10
marquee_msg = ""
question_file_name = "questions.txt"
is_game_over = False

answer_boxes = [ans_box1,ans_box2,ans_box3,ans_box4]
questions = []
question_count = 0
question_index = 0

marquee_box.move_ip(0,0)
skip_box.move_ip(700,270)
timer_box.move_ip(700,100)
question_box.move_ip(20,100)
ans_box1.move_ip(20,270)
ans_box2.move_ip(370,270)
ans_box3.move_ip(20,450)
ans_box4.move_ip(370,450)
score_box.move_ip(700,50)