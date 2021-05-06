from statistics import mode
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import createPlaylist
import settings


def main():
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    classifier = load_model('EmotionDetectionModel.h5')
    class_labels = ['Angry', 'Happy', 'Neutral', 'Sad']
    cameraSettings = settings.getSettings()
    camera = int(cameraSettings[0])
    cap = cv2.VideoCapture(camera)

    emotions = []

    while len(emotions) < 70:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=6,
            minSize=(60, 60),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                preds = classifier.predict(roi)[0]
                label = class_labels[preds.argmax()]
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                emotions.append(label)
            else:
                cv2.putText(frame, 'No Face Found', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        # cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    finalEmotion = mode(emotions)
    print(finalEmotion)
    createPlaylist.main(finalEmotion)


if __name__ == "__main__":
    main()
