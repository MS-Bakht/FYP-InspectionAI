import cv2

# Input video file
input_video_path = 'Data\Adeen.mp4'

# Output video file
output_video_path = 'output_video.mp4'

# Open the input video file
input_video = cv2.VideoCapture(input_video_path)

# Get the frames per second (FPS) of the input video
fps = int(input_video.get(cv2.CAP_PROP_FPS))

# Get the video frame width and height
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to write the output video
fourcc = cv2.VideoWriter_fourcc(*'H264')
output_video = cv2.VideoWriter(output_video_path, fourcc, fps*2, (frame_width, frame_height))

while True:
    ret, frame = input_video.read()
    if not ret:
        break

    # Duplicate the frame (write it twice)
    output_video.write(frame)
    output_video.write(frame)

# Release the video objects
input_video.release()
output_video.release()

cv2.destroyAllWindows()
