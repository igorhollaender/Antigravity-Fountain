import machine, neopixel, time
import math

# --- Configuration ---
MOTOR_PINS = [4, 5, 6]  # GPIO pins for Motors
NEOPIXEL_PIN = 48       # GPIO pin for Neopixel data
NUM_PIXELS = 3          # Number of Neopixels

# --- Setup ---
# Initialize Motors (PWM)
motors = []
for pin_num in MOTOR_PINS:
    pwm = machine.PWM(machine.Pin(pin_num))
    pwm.freq(1000) # 1 kHz frequency
    pwm.duty(0)    # Start off
    motors.append(pwm)

# Initialize Neopixels
np = neopixel.NeoPixel(machine.Pin(NEOPIXEL_PIN), NUM_PIXELS)

# --- Loop ---
print("Starting Antigravity Fountain Simulation...")
print(f"Motors on pins: {MOTOR_PINS}")
print(f"Neopixels on pin: {NEOPIXEL_PIN}")

def set_motor_speed(index, speed_percent):
    """Set motor speed (0-100%)"""
    duty = int(speed_percent / 100 * 1023)
    motors[index].duty(duty)

def set_pixel_color(index, r, g, b):
    np[index] = (r, g, b)
    np.write()

t = 0
while True:
    # Animate Motors (Sine wave patterns)
    for i in range(3):
        # Phase shift each motor
        phase = i * (2 * math.pi / 3)
        val = (math.sin(t + phase) + 1) / 2 # 0.0 to 1.0
        speed = int(val * 100)
        set_motor_speed(i, speed)
    
    # Animate Neopixels (Rainbow effect)
    for i in range(3):
        hue = (t + i) % 6.0
        # Simple Hue to RGB (approximate)
        r, g, b = 0, 0, 0
        if hue < 1: r, g, b = 255, int(hue*255), 0
        elif hue < 2: r, g, b = int((2-hue)*255), 255, 0
        elif hue < 3: r, g, b = 0, 255, int((hue-2)*255)
        elif hue < 4: r, g, b = 0, int((4-hue)*255), 255
        elif hue < 5: r, g, b = int((hue-4)*255), 0, 255
        else: r, g, b = 255, 0, int((6-hue)*255)
        
        # Dim for simulation (optional)
        scale = 0.5
        np[i] = (int(r*scale), int(g*scale), int(b*scale))
    
    np.write()
    
    time.sleep(0.05)
    t += 0.1
