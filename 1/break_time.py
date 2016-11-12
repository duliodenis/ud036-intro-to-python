import time
import webbrowser

print("Our break started on "+time.ctime())
for x in range(0,3):
    time.sleep(10)
    # webbrowser.open("https://www.youtube.com/watch?v=e8xni3EcIbc")
    print(x)

print("Our break ended on "+time.ctime())
