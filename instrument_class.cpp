#include <iostream>

// Bicycle class
class Instrument
{
// public acces specifier
public:
  // declare constructors (init version) (needs to be the name of the classs)
  Instrument();
  Instrument(int sound);
  Instrument(int sound, int steps);

  // methods (class function)
  void makeSound();
  void sequence();

  // fields (class variables)
  int soundChoice; // range [0, 7]  (8th neighborhood)
  int sequenceSteps; // the number of times to pedal
};

Instrument::Instrument()
{
  std::cout << "\n Instrument constructor - creating a Instrument object\n";
  std::cout << "default sound: 0" << std::endl;
  std::cout << "default sequenceSteps: 1" << sequenceSteps << std::endl;
  // assign default direction and speed
  soundChoice = 0;
  sequenceSteps = 1;
}

Instrument::Instrument(int sound)
{
  std::cout << "\n Instrument constructor - creating a Instrument object\n";
  std::cout << "\n soundChoice: " << sound << std::endl;
  std::cout << "default sequenceSteps: 1" << sequenceSteps << std::endl;
  // assign direction
  soundChoice = sound;
  // assign default sequenceSteps
  sequenceSteps = 1;
}

Instrument::Instrument(int sound, int sequenceSteps)
{
  std::cout << "\n Instrument constructor - creating a Instrument object\n";
  std::cout << "soundChoice: " << sound << std::endl;
  std::cout << "sequenceSteps: " << sequenceSteps << std::endl;
  // assign direction and pedalSteps
  soundChoice = sound;
  /* you need to use the 'this-pointer' if the
   * parameter name equals the field name (variable name)
   */
  this->sequenceSteps = sequenceSteps;
}

void Instrument::sequence()
{
  std::cout << "\nGoing to play the sequence! " <<
    "sequenceSteps: " << sequenceSteps << std::endl;
  // depending on the speed, pedal #speed times
  for(int i = 0; i < sequenceSteps; i++) {
    std::cout << i << " - sequence, in soundChoice: " << soundChoice << std::endl;
  }
}

void Instrument::makeSound()
{
 std::cout << "" << soundChoice << std::endl;
}

int main()
{
    // creating a Instrument object, variable name: instrument1
    // type and variable name
    Instrument instrument1(4, 3);
    instrument1.sequence();
    instrument1.makeSound();

    // end main
    return 0;
}
