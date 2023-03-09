import gettext
from pprint import pprint


#print(gettext.find("base", localedir="locales"))
ru = gettext.translation("base", localedir="locales", languages=["ru"])
_ = ru.gettext


if __name__ == "__main__":
    print(_("Hello world"))
    print(_("Sonya"))
    pprint(_("I love you"))
