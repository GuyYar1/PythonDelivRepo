# Abstrct:
The project developed in python. It is an console application uses that requires 2 parameters: City, [Country code]
The project check if there is internet connection otherwise it notify the user. if there is so it goes to the weather site "https://openweathermap.org/forecast5#name5" and perform a query using two api calls.

# Steps:
# Run it using streamlit:
    1. Open the phaycharm or python terminal 
    2. type: streamlit run app.py
    3. GUI is running locally and connection to restfull api retrived data.
    note: if you want to see the entire support with date TZ you should run the console app. yet not supported at streamlit.

    <img width="618" alt="image" src="https://github.com/GuyYar1/PythonDelivRepo/assets/132554415/1ed3ff3f-7018-4bef-b1cd-141fe4e454e9">

# Run it locally using Phycharm or python 311 interpreter(fully completed according to requiremnts) :
    1.Run the project , the main is sign as the main run configuration.
    2.Answer the two question, click enter (case sensative key1&Key2 uniqness) .
    3.Results retrived in the output pane.
        3.1. if there is no internet, use mem or persistance cache.
        3.2. If more than 2 hours have passed since the last query from the cache, perform a new restfull api query.
    4.check that the country you selected is the current one, otherwise click 1 to continue.
    5. The service is console currently and provide option to do multiple queries.
    
# General:    
The project has one class that uses its own attributes and methods. it uses a common Import file to all of its files. that way we can do one import on each file.
    Files:
            1.common_imports.py - gather all the import module or packs into one file and later on use one import all from this collection.
            2.TimeUtils.py - time utilities that handles the time zone and simmilar.
            3.requirements.txt - output of the moduls and pack that installed on developer pc. (should consider in future to clean dependencies to knwo which are used)
            4.gitignore - ignore not relevant files that related to dev IDE or others irrlevant.
            5.IpNetUtils.py - allow to check network, replace an ip in case of blocking from web api service.
            6. WeatherForecast.py - include the functionality of the program using inheritance.
 
    
    # class WeatherForecast(CacheBase) 
        # Superclass (Base Class): CacheBase
            This is the class from which WeatherForecast inherits. It contains the methods and attributes related to caching that will be shared among different subclasses.
            
        # Subclass (Derived Class): WeatherForecast
            This is the class that inherits from CacheBase. It extends the functionality of CacheBase by adding weather-specific methods and attributes.   
            Files: 
                1.Cach.py - cache class with all the regular method CRUD.
                2.cache_file.pkl - module that save cach to file. file is saved on the project folder
        
# key Gen Data Privacy 
The api Key is saved as encoded 64bit UFT-8 {Base64 is used to encode binary data into a text format . When there is a Text need to strings are typically represented using UTF-8 encoding. This ensures that all characters, including special characters}
    Files: 
        1.EncodingUtils.py - File that holds the utilities of encoding and encoding. read fromfile combinewithdecode, extract api  using regex.

# Prerequisite:
# 1.
   In the begining there is a need to install packages using pip install: 
      python -m pip install requests
     install geopy
     pip install geopy timezonefinder # PIp on terminal
     pip install geopy timezonefinder pytz
     pip install python-dotenv # halt due to conflicts
     pip install file

     e.g: look on requirements.txt.

# 2.   look also on the commit file name Common_Import save time import on each file.
        later on when we use the pythone with those package or module s we need to import them:
        so i created one file that shows the pack and moduls that were in my pc when my project was run\built. look on the file:requirements.txt.
