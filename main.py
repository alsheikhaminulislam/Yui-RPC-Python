from pypresence import Presence
import os
import time
from dotenv import load_dotenv
load_dotenv()

CLIENTID = os.getenv("CLIENTID")
STATE = os.getenv("STATE")
DETAILS = os.getenv("DETAILS")
LARGE_IMAGE = os.getenv("LARGE_IMAGE")
LARGE_TEXT = os.getenv("LARGE_TEXT")
SMALL_IMAGE = os.getenv("SMALL_IMAGE")


RPC = Presence(CLIENTID)
RPC.connect()

RPC.update(
    state=STATE,
    details=DETAILS,
    large_image=LARGE_IMAGE,
    small_image=SMALL_IMAGE,
    large_text=LARGE_TEXT,
    start=time.time()
)

while True:
    time.sleep(15)