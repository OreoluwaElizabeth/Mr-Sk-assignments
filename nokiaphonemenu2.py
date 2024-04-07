print("""
Nokia Phone Menu
1 -> Phone book
2 -> Messages
3 -> Chat
4 -> Call register
5 -> Tones
6 -> Settings
7 -> Call divert
8 -> Games
9 -> Calculator
10 -> Reminders
11 -> Clock
12 -> Profiles
13 -> SIM services
""")

userinput = int(input("Enter your choice: "))

if userinput == 1:
    print("Phone book")
    print("""
    Select an option
    1 -> Search
    2 -> Service Nos.
    3 -> Add name
    4 -> Erase
    5 -> Edit
    6 -> Assign tone
    7 -> Send b'card
    8 -> Options
    9 -> Speed dials
    10 -> Voice tags
    """)

    phonebookoption = int(input("Enter your choice: "))

    if phonebookoption == 1:
        print("Search")
    elif phonebookoption == 2:
        print("Service Nos.")
    elif phonebookoption == 3:
        print("Add name")
    elif phonebookoption == 4:
        print("Erase")
    elif phonebookoption == 5:
        print("Edit")
    elif phonebookoption == 6:
        print("Assign tone")
    elif phonebookoption == 7:
        print("Send b'card")
    elif phonebookoption == 8:
        print("Options")

        optionsoption = int(input("""
        Select an option
        1 -> Type of view
        2 -> Memory status
        """))

        if optionsoption == 1:
            print("Type of view")
        elif optionsoption == 2:
            print("Memory status")
        else:
            print("Invalid option")

    elif phonebookoption == 9:
        print("Speed dials")
    elif phonebookoption == 10:
        print("Voice tags")
    else:
        print("Back")

elif userinput == 2:
    print("Messages")
    messagesprompt = """
    Select an option
    1 -> Write messages
    2 -> Inbox
    3 -> Outbox
    4 -> Picture messages
    5 -> Templates
    6 -> Smileys
    7 -> Message settings
    8 -> Info service
    9 -> Voice mailbox number
    10 -> Service command editor
    """

    print(messagesprompt)
    messagesoption = int(input("Enter your choice: "))

    if messagesoption == 1:
        print("Write messages")
    elif messagesoption == 2:
        print("Inbox")
    elif messagesoption == 3:
        print("Outbox")
    elif messagesoption == 4:
        print("Picture messages")
    elif messagesoption == 5:
        print("Templates")
    elif messagesoption == 6:
        print("Simleys")
    elif messagesoption == 7:
        print("Message settings")
        messageprompt = """
        Select an option
        1 -> Set 1
        2 -> Common
        """

        print(messageprompt)
        messageoption = int(input("Enter your choice: "))
        if messageoption == 1:
            print("Set 1")
            setprompt = """
            Select an option
            1 -> Message centre number
            2 -> Message sent as
            3 -> Message validity
            """

            print(setprompt)
            setoption = int(input("Enter your choice: "))
            if setoption == 1:
                print("Message centre number")
            elif setoption == 2:
                print("Message sent as")
            elif setoption == 3:
                print("Message validity")
            else:
                print("Invalid option")
        elif messageoption == 2:
            print("Common")
            commonprompt = """
            Select an option
            1 -> Delivery reports
            2 -> Reply via same centre
            3 -> Character support
            """

            print(commonprompt)
            commonoption = int(input("Enter your choice: "))
            if commonoption == 1:
                print("Delivery reports")
            elif commonoption == 2:
                print("Reply via same centre")
            elif commonoption == 3:
                print("Character support")
            else:
                print("Invalid option")
    elif messagesoption == 8:
        print("Info service")
    elif messagesoption == 9:
        print("Voice mailbox number")
    elif messagesoption == 10:
        print("Service command editor")
    else:
        print("Back")

elif userinput == 3:
    print("Chat")

elif userinput == 4:
    print("Call register")
    callregisterprompt = """
    Select an option
    1 -> Missed calls
    2 -> Received calls
    3 -> Dialed numbers
    4 -> Erase recent call lists
    5 -> Show call duration
    6 -> Show call costs
    7 -> Call cost settings
    8 -> Prepaid credit
    """

    print(callregisterprompt)
    callregisteroption = int(input("Enter your choice: "))

    if callregisteroption == 1:
        print("Missed calls")
    elif callregisteroption == 2:
        print("Received calls")
    elif callregisteroption == 3:
        print("Dialed number")
    elif callregisteroption == 4:
        print("Erase recent call lists")
    elif callregisteroption == 5:
        print("Show call duration")

        calldurationprompt = """
        Select an option
        1 -> Last call duration
        2 -> All calls' duration
        3 -> Received calls' duration
        4 -> Dialed calls' duration
        5 -> Clear timers
        """

        print(calldurationprompt)
        calldurationoption = int(input("Enter your choice: "))

        if calldurationoption == 1:
            print("Last call duration")
        elif calldurationoption == 2:
            print("All calls' duration")
        elif calldurationoption == 3:
            print("Received calls' duration")
        elif calldurationoption == 4:
            print("Dialed calls' duration")
        elif calldurationoption == 5:
            print("Clear timers")
        else:
            print("You no get sense ni")
    elif callregisteroption == 6:
        print("Show call costs")

        callcostsprompt = """
        Select an option
        1 -> Last call cost
        2 -> All calls' cost
        3 -> Clear counters
        """

        print(callcostsprompt)
        callcostsoption = int(input("Enter your choice: "))

        if callcostsoption == 1:
            print("Last call cost")
        elif callcostsoption == 2:
            print("All calls' cost")
        elif callcostsoption == 3:
            print("Clear counters")
        else:
            print("You no get sense ni")
    elif callregisteroption == 7:
        print("Call cost settings")

        costsettingsprompt = """
        Select an option
        1 -> Call cost limit
        2 -> Show cost in
        """

        print(costsettingsprompt)
        costsettingsoption = int(input("Enter your choice: "))

        if costsettingsoption == 1:
            print("Call cost limit")
        elif costsettingsoption == 2:
            print("Show cost in")
        else:
            print("You no get sense ni")
    elif callregisteroption == 8:
        print("Prepaid credit")
    else:
        print("Back")

elif userinput == 5:
    print("Tones")

    tonesprompt = """
    Select an option
    1 -> Ringing tone
    2 -> Ringing volume
    3 -> Incoming call alert
    4 -> Composer
    5 -> Message alert tone
    6 -> Keypad tones
    7 -> Warning and game tones
    8 -> Vibrating alert
    9 -> Screen saver
    """

    print(tonesprompt)
    tonesoption = int(input("Enter your choice: "))

    if tonesoption == 1:
        print("Ringing tone")
    elif tonesoption == 2:
        print("Ringing volume")
    elif tonesoption == 3:
        print("Incoming call alert")
    elif tonesoption == 4:
        print("Composer")
    elif tonesoption == 5:
        print("Message alert tone")
    elif tonesoption == 6:
        print("Keypad tones")
    elif tonesoption == 7:
        print("Warning and game tones")
    elif tonesoption == 8:
        print("Vibrating alert")
    elif tonesoption == 9:
        print("Screen saver")
    else:
        print("Back")

elif userinput == 6:
    print("Settings")

    settingsprompt = """
    Select an option
    1 -> Call settings
    2 -> Phone settings
    3 -> Security settings
    4 -> Restore factory settings
    """
    print(settingsprompt)
    settingsoption = int(input("Enter your choice: "))

    if settingsoption == 1:
        print("Call settings")

        callsettingsprompt == """
        Select an option
        1 -> Automatic redial
        2 -> Speed dialling
        3 -> Call waiting options
        4 -> Own number sending
        5 -> Phone line in use
        6 -> Automatic answer
        """

        print(callsettingsprompt)
        callsettingsoption = int(input("Enter your choice: "))

        if callsettingsoption == 1:
            print("Automatic redial")
        elif callsettingsoption == 2:
            print("Speed dialling")
        elif callsettingsoption == 3:
            print("Call waiting options")
        elif callsettingsoption == 4:
            print("Own number sending")
        elif callsettingsoption == 5:
            print("Phone line in use")
        elif callsettingsoption == 6:
            print("Automatic answer")
        else:
            print("You don't have sense ni")
    elif settingsoption == 2:
        print("Phone settings")

        phonesettingsprompt = """
        Select an option
        1 -> Language
        2 -> Cell info display
        3 -> Welcome note
        4 -> Network selection
        5 -> Lights
        6 -> Confirm SIM service actions
        """

        print(phonesettingsprompt)
        phonesettingsoption = int(input("Enter your choice: "))

        if phonesettingsoption == 1:
            print("Language")
        elif phonesettingsoption == 2:
            print("Cell info display")
        elif phonesettingsoption == 3:
            print("Welcome note")
        elif phonesettingsoption == 4:
            print("Network selection")
        elif phonesettingsoption == 5:
            print("Lights")
        elif phonesettingsoption == 6:
            print("Confirm SIM service actions")
        else:
            print("You don't have sense ni")
    elif settingsoption == 3:
        print("Security settings")

        securitysettingsprompt = """
        Select an option
        1 -> PIN code request
        2 -> Call barring service
        3 -> Fixed dialling
        4 -> Closed user group
        5 -> Phone security
        6 -> Change access codes
        """

        print(securitysettingsprompt)
        securitysettingsoption = int(input("Enter your choice: "))

        if securitysettingsoption == 1:
            print("PIN code requset")
        elif securitysettingsoption == 2:
            print("Call barring service")
        elif securitysettingsoption == 3:
            print("Fixed dialling")
        elif securitysettingsoption == 4:
            print("Closed user group")
        elif securitysettingsoption == 5:
            print("Phone security")
        elif securitysettingsoption == 6:
            print("Change access codes")
        else:
            print("You don't have sense ni")
    elif settingsoption == 4:
        print("Restore factory settings")
    else:
        print("Back")

elif userinput == 7:
    print("Call divert")
elif userinput == 8:
    print("Games")
elif userinput == 9:
    print("Calculator")
elif userinput == 10:
    print("Reminders")
elif userinput == 11:
    print("Clock")

    clockprompt = """
    Select an option
    1 -> Alarm clock
    2 -> Clock settings
    3 -> Date setting
    4 -> Stopwatch
    5 -> Countdown timer
    6 -> Auto update of date and time
    """

    print(clockprompt)
    clockoption = int(input("Enter your choice: "))

    if clockoption == 1:
        print("Alarm clock")
    elif clockoption == 2:
        print("Clock settings")
    elif clockoption == 3:
        print("Date setting")
    elif clockoption == 4:
        print("Stopwatch")
    elif clockoption == 5:
        print("Countdown timer")
    elif clockoption == 6:
        print("Auto update of date and time")
    else:
        print("Back")

elif userinput == 12:
    print("Profiles")
elif userinput == 13:
    print("SIM services")
else:
    print("Back")


        


    
