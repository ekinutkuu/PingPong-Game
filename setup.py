import cx_Freeze
from cx_Freeze import *

setup(
    name="pingpong",
    options={'build_exe':{'packages':['pygame']}},
    executables=[
        Executable(
            "pingpong.py",
    


            )


        ]

    )
