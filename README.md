<!-- ########### Example ########### -->
    - https://youtu.be/TP1eUsSMoBs?si=pW1v3e3p2M26bULp

<!-- ssh -->
    ** ลบ ssh-keygen
        - ssh-keygen -R 192.168.10.7
    ** remote ssh
        - ssh joker@192.168.10.7
    ** ส่งไฟล์
        - scp VideoPlayer.py joker@192.168.10.7:/home/joker/Desktop
        
<!-- ########### compile project ########### -->
    - pyside6-uic weight.ui > ui_weight.py
    - pyside6-rcc resource.qrc -o resource_rc.py
    ** convert ui_weight.py flie to UTF-8 before

    - cd my_project
    ** windows
        - python -m venv env
        - env\Scripts\activate
    ** linux
        - python3 -m venv env
        - source env/bin/activate

<!-- ########### Libraries ########### -->
    ** pyside6
        - pip install pyside6

    ** Keyboard
        - python -m pip install pynput

    ** Install front kanit
        .assets/fronts/kanit.zip

    ** google
        - pip install google-api-python-client
        - pip install google-auth-oauthlib
        - pip install pywifi
        - pip install comtypes
        - pip install requests
        - pip install pyserial
        - pip install pynput