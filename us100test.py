import machine
import utime
import us100

uart = machine.UART(1)
sensor = us100.US100UART(uart)

while True:
    print(sensor.distance())
    utime.sleep_ms(50)