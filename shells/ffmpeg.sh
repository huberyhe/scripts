#!/bin/bash

killall ffmpeg-298

# transcode RT HD x264 to SD x264, without errors, without spikes, bursts and clear video picture
# please try & assist

isbr=8000000;                    # input stream bitrate [bps], enter maximum value
isbd=$(( $isbr / 8 * 10 ))       # input stream buffer for decoding [bytes] for 10 seconds
isff=$(( $isbr / 8 / 188 * 10 )) # input stream fifo_size [ 1 = 188 byte packets ] for 10 seconds

osbr=1700000;                    # output stream bit rate [bytes]
osfs=25;                         # output stream FPS
osbe=$(( $osbr * 4 / $osfs ));   # output stream buffer for encoding [bytes]
#                      ^ this can be 3 or 4

ffmpeg \
-re -v 40 \
-f mpegts -i "http://192.168.0.169/hdmi_ext?buffer_size=$isbd&fifo_size=$isff" \
-pix_fmt yuv420p -vf "yadif=0:-1:0, scale=min(720\,iw):min(480\,ow)" \
-c:v libx264 -preset:v fast -profile:v main -level 3.1 \
-g 12 -bf 2 -flags +cgop -sc_threshold 1000000000 -b_strategy 0 -mpv_flags +strict_gop \
-maxrate $osbr -bufsize $osbe \
-c:a mp2 -ac 2 -b:a 96k \
-y -r $osfs -vsync 1 -async $osfs \
-f mpegts "udp://192.168.10.196:5681?pkt_size=1316"
