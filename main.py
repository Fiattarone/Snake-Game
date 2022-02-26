from turtle import Screen
import snake
import food
import scoreboard

screenolio = Screen()
screenolio.setup(width=600, height=600)
screenolio.bgcolor("black")
screenolio.title("SNAKE GAME")
screenolio.tracer(0)

segments = []

# player, food and scoreboard:
playerSnake = snake.Snake()
snakeFood = food.Food()
scorecounter = scoreboard.Scoreboard()
scorecounter.load_high_score()
scorecounter.write_score()

screenolio.listen()
screenolio.onkeypress(key="Up", fun=playerSnake.up)
screenolio.onkeypress(key="Down", fun=playerSnake.down)
screenolio.onkeypress(key="Left", fun=playerSnake.left)
screenolio.onkeypress(key="Right", fun=playerSnake.right)


game_playing = True

while game_playing:
    playerSnake.move_forward()
    screenolio.update()

    if playerSnake.head.distance(snakeFood) < 15:
        print("NOOOOOOOOOOOM")
        # Randomly generate food new location
        snakeFood.new_location()
        # increase snake segments
        playerSnake.new_segment()
        # increase score
        scorecounter.increase_score()

    if playerSnake.head.xcor() > 280 or playerSnake.head.xcor() < -280 or playerSnake.head.ycor() > 280 or playerSnake.head.ycor() < -280:
        # Trigger game over sequence
        game_playing = False
        scorecounter.game_over()
        # Check if space was hit for reset

    # Detect collision with tail
    for seg in playerSnake.segments:
        if seg != playerSnake.head:
            if playerSnake.head.distance(seg) < 10:
                game_playing = False
                scorecounter.game_over()
                # Check if space was hit for reset

screenolio.exitonclick()
