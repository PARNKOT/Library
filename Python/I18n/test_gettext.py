import gettext
import os
from pprint import pprint


#print(gettext.find("ru", localedir="locales"))
ru = gettext.translation("base", localedir="locales", languages=["ru"])
_ = ru.gettext

if __name__ == "__main__":
    print(_("Hello world"))
