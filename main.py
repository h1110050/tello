from TelloSDKPy.djitellopy import Tello
import cv2
import time


def main():
    tello = Tello()

    tello.connect()
    tello.takeoff()

    tello.move_left(100)
    tello.rotate_counter_clockwise(45)

    tello.land()
    tello.end()

if __name__ == "__main__":
    main()
