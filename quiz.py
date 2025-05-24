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
score_box = Rect(0,0,150,50)

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

def draw():
    global marquee_msg
    screen.clear()
    screen.fill(color = "#DDD8B8")
    screen.draw.filled_rect(marquee_box, "#21897E")
    screen.draw.filled_rect(skip_box, "#52AA8A")
    screen.draw.filled_rect(timer_box, "#4E8098")
    screen.draw.filled_rect(score_box, "#4E8098")
    screen.draw.filled_rect(question_box, "#75B8C8")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "#77CBB9")

    marquee_msg = f"Welcome to quizmaster... Q: {question_index} out of {question_count}"
    screen.draw.textbox(marquee_msg, marquee_box, color = "#C7A27C")
    screen.draw.textbox("SKIP", skip_box, color = "#C7A27C", angle = -90)
    screen.draw.textbox(f"{timer_left}", timer_box, color = "#CCA43B", shadow = (0.5,0.5), scolor = "#DBEBC0")
    screen.draw.textbox(f"Score: {score}", score_box, color = "#FFBF00")

    screen.draw.textbox("question", question_box, color = "#CDE5D7", shadow = (0.5,0.5), scolor = "#ECE2D0")

def update():
    pass

pgzrun.go()