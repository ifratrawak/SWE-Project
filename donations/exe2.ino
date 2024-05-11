#include <Servo.h>

// Define servo objects for the arm components
Servo baseServo;    // Base servo
Servo elbowServo;
Servo wristServo;   // Wrist servo
Servo gripperServo; // Gripper servo

// Define servo positions
const int baseHomePosition = 25;    // Home position for the base servo
const int elbowHomePosition = 0;
const int wristHomePosition = 0;   // Home position for the wrist servo
const int gripperHomePosition = 0;  // Home position for the gripper servo

// Function to move a servo to a specific position
void moveToPosition(Servo servo, int position) {
  servo.write(position);
  delay(150); // Adjust delay as needed for servo movement
}

void setup() {
  // Attach servo pins
  baseServo.attach(8);    // Pin 9 for the base servo
  elbowServo.attach(7);
  wristServo.attach(10);  // Pin 10 for the wrist servo
  gripperServo.attach(9);// Pin 11 for the gripper servo
  
  // Move all servos to home positions during initialization
  moveToPosition(baseServo, baseHomePosition);
  moveToPosition(elbowServo, elbowHomePosition);
  moveToPosition(wristServo, wristHomePosition);
  moveToPosition(gripperServo, gripperHomePosition);
}

void loop() {
  // Pick and place routine
  // Move arm to pick up object
  moveToPosition(baseServo, 0);  // Move base servo to pick up position
  delay(150);
  moveToPosition(elbowServo, 50);  // Move base servo to pick up position
  delay(150);
  moveToPosition(wristServo, 0); // Adjust wrist for picking
  delay(150);
  moveToPosition(gripperServo, 100); // Activate gripper to grasp object
  
  
  // Lift object
  // Move arm to desired location for placing the object
  moveToPosition(baseServo, 20); // Move base servo to target position
  delay(150);
  moveToPosition(elbowServo, 55);  // Move base servo to pick up position
  delay(150);
  moveToPosition(wristServo, 0); // Adjust wrist for placing
  delay(150);
  moveToPosition(gripperServo, 0); // Release object
  delay(150);
  
  // Return arm to home position
  moveToPosition(baseServo, baseHomePosition);
  moveToPosition(elbowServo, elbowHomePosition);
  moveToPosition(wristServo, wristHomePosition);
  moveToPosition(gripperServo, gripperHomePosition);
  
  delay(150); // Delay between each pick and place operation
}
