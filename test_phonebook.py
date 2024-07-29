import My_Nokia_Phonebook as phonebook


def test_add_contact():
    assert phonebook.add_contact("Jeetendra Gupta", "9555613730") == "Contact Jeetendra Gupta added."
    assert phonebook.add_contact("Jeetendra Gupta", "9555613730") == "Contact already exists."


def test_search_contact():
    phonebook.add_contact("Jeetendra Gupta", "9555613730")
    assert phonebook.search_contact("Jeetendra Gupta") == "Phone number of Jeetendra Gupta is 9555613730."
    assert phonebook.search_contact("Sameer Gupta") == "Contact not found."


def test_delete_contact():
    phonebook.add_contact("Jeetendra Gupta", "9555613730")
    assert phonebook.delete_contact("Jeetendra Gupta") == "Contact Jeetendra Gupta deleted."
    assert phonebook.delete_contact("Jeetendra Gupta") == "Contact not found."


def test_list_contacts():
    phonebook.add_contact("Jeetendra Gupta", "9555613730")
    phonebook.add_contact("Sameer Gupta", "9729655878")
    assert phonebook.list_contacts() == "Jeetendra Gupta: 9555613730\nSameer Gupta: 9729655878"
    phonebook.delete_contact("Jeetendra Gupta")
    phonebook.delete_contact("Sameer Gupta")
    assert phonebook.list_contacts() == "Phonebook is empty."
