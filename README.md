Our project uses a STM32F303K8 Nucleo board to record temperature from a thermistor. The
goal was to build a station that can detect changes in the weather from the STM32 and send that data to
a raspberry pi computer. The readings are sent to a Raspberry Pi via UART protocol which then
generates a plot showing the changes. The graph is displayed through a flask webpage running on the
raspberry pi. Using an FSM configuration on the STM32, LEDs are used to indicate when the heater or AC
is activated when it meets the conditions. We approached the problem by breaking it up into modules of
software (for each device) and circuit analysis.
