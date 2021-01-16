# -*- coding: utf-8 -*-
"""

"""
import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')


"""
st.title('Background reduction')

@st.cache(allow_output_mutation=True)
def get_cap():
    return cv2.VideoCapture(0)

cap = get_cap()

frameST = st.empty()
param=st.sidebar.slider('chose your value')

fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    # Stop the program if reached end of video
    if not ret:
        print("Done processing !!!")
        cv2.waitKey(3000)
        # Release device
        cap.release()
        break
    #st.write('### Source video:')
    #frameST.image(frame, channels="BGR")
    #st.write('### Background reduction :')
    fgmask = fgbg.apply(frame)
    frameST.image(fgmask, width=600)
"""
