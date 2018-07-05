from faker import Faker

def product_note(name, number):
    fake = Faker("zh_CN")
    with open(name, "w") as f_n:
        f_n.write("""<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export3.dtd">
    <en-export export-date="20180705T160756Z" application="Evernote" version="Evernote Mac 7.2.1 (456793)">""")
        note_format = """
        <note>
            <title>{}</title>
            <content>
                <![CDATA[<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note><div>{}</div></en-note>]]>
            </content>
        </note>"""
        for i in range(1, number + 1):
            title = "{:0>3d} {}".format(i, fake.sentence())
            content = fake.text()
            note = note_format.format(title, content)
            f_n.write(note)
        f_n.write("""\n</en-export>""")

product_note("1000_notes.enex", 1000)
product_note("2000_notes.enex", 2000)
product_note("5000_notes.enex", 5000)
product_note("10000_notes.enex", 10000)
