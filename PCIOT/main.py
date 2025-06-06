import cv2
import mediapipe as mp
import time
import numpy as np
import pygame
import threading

# Inicializações MediaPipe
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_detection
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7)
face = mp_face.FaceDetection(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Inicializações do pygame para som
pygame.mixer.init()
alarme_ativo = False

cap = cv2.VideoCapture(0)
apagao_ativo = False
tempo_escuro = None

def dedos_levantados(hand_landmarks):
    dedos = []

    # Polegar (compara x)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        dedos.append(1)
    else:
        dedos.append(0)

    # Outros dedos (compara y)
    for tip_id in [8, 12, 16, 20]:
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            dedos.append(1)
        else:
            dedos.append(0)

    return dedos

def tocar_alarme():
    global alarme_ativo
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("alarme.mp3")
        pygame.mixer.music.play(-1)  # Repetição infinita
        alarme_ativo = True

def parar_alarme():
    global alarme_ativo
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        alarme_ativo = False


while True:
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results_hands = hands.process(frame_rgb)
    results_face = face.process(frame_rgb)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brilho_medio = np.mean(gray)

    # Modo noturno: inverter imagem se escuro
    if brilho_medio < 10:
        frame = cv2.bitwise_not(frame)

    # Apagão após 5 segundos de escuridão
    if brilho_medio < 10 and not apagao_ativo:
        if tempo_escuro is None:
            tempo_escuro = time.time()
        elif time.time() - tempo_escuro >= 5:
            apagao_ativo = True
            if not alarme_ativo:
                threading.Thread(target=tocar_alarme).start()
    elif brilho_medio >= 10:
        tempo_escuro = None

    if apagao_ativo:
        cv2.putText(frame, 'APAGAO DETECTADO!', (50, 250),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)

    # Detecção facial
    if results_face.detections:
        cv2.putText(frame, 'Pessoa detectada', (10, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    else:
        cv2.putText(frame, 'Nenhuma pessoa visivel', (10, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)

    # Detecção de mão
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            dedos = dedos_levantados(hand_landmarks)
            dedos_levantados_total = sum(dedos)

            # Mão aberta → cancela apagão e alarme
            if dedos_levantados_total == 5:
                cv2.putText(frame, 'Mao aberta detectada', (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                if apagao_ativo and brilho_medio > 10:
                    apagao_ativo = False
                if pygame.mixer.music.get_busy():
                    parar_alarme()


            # Gesto de socorro (2 dedos: indicador + médio)
            elif dedos[1] == 1 and dedos[2] == 1 and dedos[0] == 0 and dedos[3] == 0 and dedos[4] == 0:
                cv2.putText(frame, 'GESTO DE SOCORRO DETECTADO!', (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                if not alarme_ativo:
                    threading.Thread(target=tocar_alarme).start()

            else:
                cv2.putText(frame, 'Outro gesto detectado', (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Mostrar imagem
    cv2.imshow("Sistema de Gestos - Apagao", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Encerramento
parar_alarme()
cap.release()
cv2.destroyAllWindows()
