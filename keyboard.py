import pyxhook
import rospy
from rosrover.msg import direction

dirpub = rospy.Publisher('keyboard', direction, queue_size= 10)
rospy.init_node('keyboard', anonymous = True)
rate = rospy.Rate(1000)

def OnKeyPress(event):
  direct = direction()
  key = event.Key
  if key == "Up":
    direct.direction = "Forward"
  elif key == "Down":
    direct.direction = "Backward"
  elif key == "Right":
    direct.direction = "Right"
  elif key == "Left":
    direct.direction = "Left"
  elif key == "space":
    direct.direction = "Stop"

  elif key == "w":
    direct.direction = "servoup"
  elif key == "s":
    direct.direction = "servodown"
  elif key == "a":
    direct.direction = "servoleft"
  elif key == "d":
    direct.direction = "servoright"

  elif key == "x":
      direct.direction = "speedup"
  elif key == "z":
      direct.direction = "speeddown"

  elif key == "Escape": #96 is the ascii value of the grave key (`)
    direct.direction = "turnoff"
    new_hook.cancel()

  rospy.logdebug(direct)
  dirpub.publish(direct)

new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
