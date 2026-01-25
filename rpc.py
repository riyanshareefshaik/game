# ===================== IMPORTS =====================
import sys
import os
import cv2
import mediapipe as mp
import numpy as np

# ===================== AI SETUP =====================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ===================== CAMERA =====================
cap = cv2.VideoCapture(0)

# Warn if not using project virtualenv
try:
    project_venv = os.path.join(os.path.dirname(__file__), "rps_env", "bin", "python3")
    if os.path.abspath(sys.executable) != os.path.abspath(project_venv):
        print("WARNING: You're not running the project's virtualenv.")
        print(f"Current interpreter: {sys.executable}")
        print(f"Recommended: {project_venv}")
        print("To run with the venv: ./rps_env/bin/python3 rpc.py")
except Exception:
    pass

# ===================== GESTURE LOGIC =====================
def get_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb (x-axis check)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (y-axis check)
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

def get_gesture(fingers):
    if fingers == [0,0,0,0,0]:
        return "ROCK"
    if fingers == [1,1,1,1,1]:
        return "PAPER"
    if fingers == [0,1,1,0,0]:
        return "SCISSORS"
    return "UNKNOWN"

def decide_winner(p1, p2):
    if p1 == p2:
        return "DRAW"
    if (p1 == "ROCK" and p2 == "SCISSORS") or \
       (p1 == "SCISSORS" and p2 == "PAPER") or \
       (p1 == "PAPER" and p2 == "ROCK"):
        return "PLAYER 1 WINS"
    return "PLAYER 2 WINS"

# ===================== MAIN LOOP =====================
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gestures = []

    if result.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            fingers = get_fingers(hand_landmarks)
            gesture = get_gesture(fingers)
            gestures.append(gesture)

            cv2.putText(
                frame,
                f"Player {idx+1}: {gesture}",
                (10, 40 + idx * 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )

    if len(gestures) == 2:
        winner = decide_winner(gestures[0], gestures[1])
        cv2.putText(
            frame,
            winner,
            (180, 430),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.8,
            (0, 255, 0),
            4
        )

    cv2.imshow("AI Rock Paper Scissors - Dual Player", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# ===================== CLEANUP =====================
cap.release()
cv2.destroyAllWindows()
