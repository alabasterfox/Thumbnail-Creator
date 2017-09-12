#!/usr/bin/env python

import cv2
import datetime
import os
import sys

def SaveThumbnail(
    VIDEOFILENAME = None,
    THUMBNAIL_HEIGHT = 100, # default height
    THUMBNAIL_WIDTH = 175): # default width
    '''
    A Python utility that saves a thumbnail
    from the first frame of a video
    '''

    if len(sys.argv) > 1:
        VIDEOFILENAME = str(sys.argv[1])
        video_file = os.path.join(
                os.path.abspath(
                    os.path.dirname(__file__)
                    ),
                VIDEOFILENAME
                )
        if not os.path.isfile(video_file):
            print("\n Video '%s' does not exist. \n\n Please ensure "
                "video exists and run \n\n"
                "'python %s %s' \n" %
                  (video_file,
                   os.path.basename(__file__),
                   video_file
                   )
            )
            sys.exit(0)
    else:
        # show help
        print("\n\n"
              "COMMAND SYNTAX: \n"
              "\n"
              "\t %s VIDEOFILENAME THUMBNAIL_HEIGHT THUMBNAIL_WIDTH \n"
              "\n"
              "\t Saves a thumbnail from the first frame of the \n"
              "\t specified video to the script's directory with \n"
              "\t a specified height and width \n"
              "\n"
              "PARAMETERS: \n"
              "\n"
              "\t VIDEOFILENAME : string, name of the video file \n"
              "\t THUMBNAIL_HEIGHT : int, height of thumbnail to save \n"
              "\t\t\t (optional, default: %d) \n"
              "\t THUMBNAIL_WIDTH : int, width of thumbnail to save \n"
              "\t\t\t (optional, default: %d) \n"
              "\n"
              "EXAMPLES: \n"
              "\n"
              "\t %s video.mp4 \n"
              "\n"
              "\t\t Saves a thumbnail from video.mp4 with a default \n"
              "\t\t height and width \n"
              "\n"
              "\t %s /path/to/video.mp4 \n"
              "\n"
              "\t\t Saves a thumbnail from the absolute path with a \n"
              "\t\t default height and width \n"
              "\n"
              "\t %s video.mp4 80 \n"
              "\n"
              "\t\t Saves a thumbnail from video.mp4 with a height of \n"
              "\t\t 80px and default width \n"
              "\n"
              "\t %s video.mp4 80 125 \n"
              "\n"
              "\t\t Saves a thumbnail from video.mp4 with a height of \n"
              "\t\t 80px and a width of 125px \n"
              "\n" %
                  (
                  "python " + os.path.basename(__file__),
                  THUMBNAIL_HEIGHT,
                  THUMBNAIL_WIDTH,
                  "python " + os.path.basename(__file__),
                  "python " + os.path.basename(__file__),
                  "python " + os.path.basename(__file__),
                  "python " + os.path.basename(__file__)
                  )
              )
        sys.exit(0)
    if len(sys.argv) > 2:
        THUMBNAIL_HEIGHT = int(sys.argv[2])
    if len(sys.argv) > 3:
        THUMBNAIL_WIDTH = int(sys.argv[3])
    try:
        cap = cv2.VideoCapture(video_file)
        ret, frame = cap.read()
        thumbnail = cv2.resize(
            frame,
            (THUMBNAIL_WIDTH,
             THUMBNAIL_HEIGHT)
            )
        cv2.imwrite(
            os.path.join(
                os.path.dirname(__file__),
                "thumbail_%s.jpg" % datetime.datetime.now() # thumbnail filename
                ),
            thumbnail
            )
    finally:
        cap.release()

SaveThumbnail()
