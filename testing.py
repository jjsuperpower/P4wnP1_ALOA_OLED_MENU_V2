
import math
import time
import datetime
from luma.core import cmdline
from luma.core.render import canvas 

#read in config file and setup device
parser = cmdline.create_parser(description=None)
conf = cmdline.load_config(displayConfPath)
args = parser.parse_args(conf)
device = cmdline.create_device(args)

while True:
    now = datetime.datetime.now()
    today_date = now.strftime("%d %b %y")
    today_time = now.strftime("%H:%M:%S")
    if today_time != today_last_time:
        today_last_time = today_time
        with canvas(device) as draw:
            now = datetime.datetime.now()
            today_date = now.strftime("%d %b %y")

            margin = 4

            cx = 30
            cy = min(device.height, 64) / 2

            left = cx - cy
            right = cx + cy

            hrs_angle = 270 + (30 * (now.hour + (now.minute / 60.0)))
            hrs = posn(hrs_angle, cy - margin - 7)

            min_angle = 270 + (6 * now.minute)
            mins = posn(min_angle, cy - margin - 2)

            sec_angle = 270 + (6 * now.second)
            secs = posn(sec_angle, cy - margin - 2)

            draw.ellipse((left + margin, margin, right - margin, min(device.height, 64) - margin), outline="white")
            draw.line((cx, cy, cx + hrs[0], cy + hrs[1]), fill="white")
            draw.line((cx, cy, cx + mins[0], cy + mins[1]), fill="white")
            draw.line((cx, cy, cx + secs[0], cy + secs[1]), fill="red")
            draw.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill="white", outline="white")
            draw.text((2 * (cx + margin), cy - 8), today_date, fill="yellow")
            draw.text((2 * (cx + margin), cy), today_time, fill="yellow")

        time.sleep(0.1)
