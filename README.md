# PyKonfig
Python code to read and write KDE Plasma Desktop configs for quick configuration.

```python
import input
import telemetry

repeat_delay = input.get_repeat_delay()
if repeat_delay < 500:
    input.set_repeat_delay(repeat_delay + 100)

# An enum for the amount/type of data sent (BASIC_SYSTEM_INFORMATION)
print(telemetry.get_feedback_level())

# A dict with options and the keys assigned to them ({'compose': ['menu']})
print(input.get_keyboard_options())

# A list of all layouts; consisting of a layout type ('us') and type ('euro')
print(input.get_layout_list())
```
