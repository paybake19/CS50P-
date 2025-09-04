#import project modules
import json
import datetime, time
import os
from pyfiglet import figlet_format
from project import start_timer, log_session, session_statistics, alarm_display
import pytest

#remove json sessions for testing and assert statements.
if os.path.exists("sessions.json"):
    os.remove("sessions.json")

#test alarm with 1sec duraiton
def test_start_timer():
    start_timer(1)
    with open("sessions.json", "r") as file:
        data = json.load(file)
    assert data[-1]["duration"] ==1

# clear sessions files, log session for 5sec, assert/check that file is created
def test_log_session():
    log_session(5)
    assert os.path.exists("sessions.json")
#load saved session from above and read as file
    with open("sessions.json", "r") as file:
        data = json.load(file)
#once assert path exists, check it is a list, and last item in sequence
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[-1] ["duration"] == 5


# count sessions, ensure it is a dict, checks that at least 1x session was logged with test
def test_session_statistics():
    stats = session_statistics()
    assert isinstance(stats, dict)
    assert "total_sessions" in stats
    assert stats["total_sessions"] >= 1

#Just check that this block runs, assert True
def test_alarm_display():
    alarm_display()
    assert True


