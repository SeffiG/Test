import webbrowser
import subprocess
import os
url = 'https://app.thespaghettidetective.com/printers/'
url2 = 'https://video.nest.com/live/PL1NROnIGK'


webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
webbrowser.get('chrome').open(url)
webbrowser.get('chrome').open(url2)

subprocess.call('C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeMX\STM32CubeMX.exe')