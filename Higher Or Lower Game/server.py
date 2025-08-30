from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def guess():
    return ('<html style = "text-align: center">'
            '<body>'
                '<h1> Higher Or Lower </h1>'
                '<p> Guess the number between 0 and 9.</p>'
                '<img src = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjBucW9nZnZjeDl0dnBlaWc1NWpkM2tnZ2Q3MTUxaDY3anF4NGhocyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UDU4oUJIHDJgQ/giphy.gif" width = 400 '
            '</body>'
            '</html>'
            )

random_number = random.randint(0,9)

@app.route("/<int:number>")
def user_input(number):
    if number < random_number:
        return ('<html style = "text-align: center">'
                '<body>'
                    f"<h1>{number} is too low. Try again.</h1>"
                    f"<img src = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWI2bDNoOXZjcXhrMmxhdG8wZ3FwcjBzOHdyNmtzb2l5ODB6dnRvOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nR4L10XlJcSeQ/giphy.gif'width = 400"
                '</body>'
                '</html>')
    elif number > random_number:
        return ('<html style = "text-align: center">'
                '<body>'
                    f"<h1>{number} is too high. Try again.</h1>"
                    f"<img src = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa25md3p3YjMwcms0N29yMWhncWhvNXBvMnd1dmd5cGRleWtvNTF2aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hECJDGJs4hQjjWLqRV/giphy.gif'width = 400"
                '</body>'
                '</html>')

    elif number == random_number:
        return ('<html style = "text-align: center">'
                '<body>'
                    f"<h1>{number} was correct guess.</h1>"
                    f"<img src = 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2UyNG16cnJidzI1ZWNrcTJpMzdqbXMzcHJxMGhrYXdreW9nMWM2NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kBZBlLVlfECvOQAVno/giphy.gif' width = 400"
                '</body>'
                '</html>')
    return ""


if __name__ =="__main__":
    app.run(debug= True)