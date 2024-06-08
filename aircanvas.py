import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe and OpenCV
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize hand tracking
with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as finger:

    # Create a canvas to draw on
    canvas = np.zeros((480, 640, 3), dtype="uint8")
    
    # Set default color and brush thickness
    color = (255, 0, 0)  # Blue color in BGR
    thickness = 5

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Flip the image horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = finger.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract the coordinates of the index finger tip
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, c = frame.shape
                cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

                # Draw on the canvas
                cv2.circle(canvas, (cx, cy), thickness, color, -1)

                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Overlay the canvas on the frame
        frame = cv2.add(frame, canvas)

        # Display instructions
        cv2.putText(frame, "Press 'q' to quit", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, "Press 'c' to change color", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, "Press 'e' to erase", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Display the result
        cv2.imshow('Air Canvas', frame)

        key = cv2.waitKey(1) & 0xFF

        # Handle keypress events
        if key == ord('q'):
            break
        elif key == ord('c'):
            # Change color
            color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        elif key == ord('e'):
            # Erase the canvas
            canvas = np.zeros((480, 640, 3), dtype="uint8")

    cap.release()
    cv2.destroyAllWindows()
