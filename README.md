The project developed in python. It is an console application uses that requires 2 parameters: City, [Country code]
The project check if there is internet connection otherwise it notify the user. if there is so it goes to the weather site "https://openweathermap.org/forecast5#name5" and perform a query using two api calls.

Steps:
1.Run the project , the main is sign as the main run configuration.
2. Answer the question2
3.Results retrived in the output pane.
4.check that the country you selected is the current one.

The project has one class that uses its own attributes and methods. it uses a common Import file to all of its files. that way we can do one import on each file.

The api Key is saved as encoded 64bit UFT-8 {Base64 is used to encode binary data into a text format . When there is a Text need to strings are typically represented using UTF-8 encoding. This ensures that all characters, including special characters}

In the begining there is a need to install packages using pip install: 
  #  python -m pip install requests
  #  install geopy
  # pip install geopy timezonefinder # PIp on terminal
  # pip install geopy timezonefinder pytz
  # pip install python-dotenv # halt due to conflicts
  # pip install file

later on when we use the pythone with those package or module s we need to import them:

so i created one file that shows the pack and moduls that were in my pc when my project was run\built. look on the file:requirements.txt.