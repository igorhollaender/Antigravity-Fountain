# Antigravity Fountain: Project Requirements & Logic

## Core Concept
The "Antigravity" effect is a **stroboscopic illusion**.
-   **Mechanism**: Water droplets are pumped at a precise frequency.
-   **Visual Effect**: 
    -   **Levitation**: Strobe frequency = Droplet frequency.
    -   **Rise (Antigravity)**: Strobe frequency slightly *higher* than droplet frequency.
    -   **Fall (Slow Motion)**: Strobe frequency slightly *lower* than droplet frequency.

## Hardware Configuration (Simulated)
-   **Microcontroller**: ESP32-S3 (MicroPython)
-   **Motors (Pumps)**: 3x DC Motors
    -   Pins: GPIO 4, 5, 6
    -   Control: PWM (Pulse Width Modulation) at ~60Hz base frequency.
-   **LEDs (Strobe)**: 3x Neopixels (WS2812B)
    -   Pin: GPIO 48 (Data)
    -   Control: High-speed flashing (millisecond pulses) to freeze motion.

## Logic Implementation Strategy
1.  **Sequencer Class**: A central controller to synchronize Pumps and LEDs.
2.  **Modes**:
    -   `LEVITATE`: Sync frequencies.
    -   `RISE`: Offset strobe +0.5Hz.
    -   `FALL`: Offset strobe -0.5Hz.
3.  **Adjustability**: The strobe frequency should be adjustable (e.g., via a variable or settings) to fine-tune the illusion.

## References
-   Based on "Antigravity: Hypothetical Force Explained" chat.
-   Simulation running in Wokwi (VS Code).
