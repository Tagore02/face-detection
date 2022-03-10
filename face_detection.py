import cv2
import face_recognition

image_to_detect = cv2.imread('image_path/image.jpg')

all_face_locations = face_recognition.face_locations(image_to_detect)

print('there are {} faces in this image'.format(len(all_face_locations)))

for index, current_face_location in enumerate(all_face_locations):
    # splitting the tuple to get the four positions value

    top_pos, right_pos, bottom_pos, left_pos = current_face_location
    print('found face {} at top:{}, right:{}, bottom:{}, left:{} '.format(index+1, top_pos, right_pos, bottom_pos, left_pos))
    #current_face_image = image_to_detect[top_pos:bottom_pos, left_pos:right_pos]
    cv2.rectangle(image_to_detect, (left_pos, top_pos), (right_pos, bottom_pos), (255,0,0), 2)

    cv2.imshow("face no ",image_to_detect)
    cv2.waitKey(0)