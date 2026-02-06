# main_rpi.py

from helper_functions import camera, computer_vision, sensehat
import time

def display_menu():
    """
    Display the main menu
    """
    print("\n" + "="*50)
    print("HOME SECURITY SYSTEM - MAIN MENU")
    print("="*50)
    print("1. Take Background Image")
    print("2. Arm Security System")
    print("3. Exit")
    print("="*50)


def main():
    camera_i = camera.get_camera()
    sense = sensehat.get_sensehat()
    
    interval = 10
    t1 = 480000000
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            countdown = int(input("Enter countdown time (seconds): "))
            preview_choice = input("Enable preview? (y/n): ").lower()
            preview = True if preview_choice == 'y' else False
            
            print(f"\nPreparing to take background image in {countdown} seconds...")
            print("Please clear the area!")
            
            camera.capture_image(camera_i, "data/images/background.jpg", countdown_time=countdown, preview=preview)
            print("Background image captured successfully!\n")
        
        elif choice == "2":
            interval = int(input("Enter monitoring interval (seconds): "))
            t1_input = input(f"Enter threshold value (default {t1}): ")
            if t1_input:
                t1 = int(t1_input)
            
            countdown = int(input("Enter countdown before monitoring starts (seconds): "))
            
            print(f"\nMonitoring will start in {countdown} seconds...")
            print("Please leave the monitored area!")
            
            for i in range(countdown, 0, -1):
                print(f"{i}...")
                time.sleep(1)
            
            print("\nMonitoring started! Press Ctrl+C to stop.\n")
            
            count = 0
            try:
                while True:
                    camera.capture_image(camera_i, "data/images/image%s.jpg" % count, countdown_time=interval)
                    person_detected = computer_vision.person_detected("data/images/background.jpg", "data/images/image%s.jpg" % count, t1)
                    
                    if person_detected:
                        print("Person Detected")
                        sensehat.alarm(sense, interval)
                    else:
                        print("No Person Detected")
                    
                    count += 1
            except KeyboardInterrupt:
                print("\n\nMonitoring stopped by user.")
        
        elif choice == "3":
            print("\nExiting security system. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()