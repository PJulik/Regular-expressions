from pprint import pprint
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = (r"(\+7|8)(\s*)(\(*)(\d{3})(\-*)(\)*)(\s*)(\d{3})(\-*)(\s*)(\d{2})(\-*)(\s*)(\d{2})(\s*)(\(*)(доб\.)*(\s*)(\d+)*(\)*)")
replace = r"+7(\4)\8-\11-\14\15\17\19"

new_list = []
final_list = []
for contact in contacts_list:
    fio = " ".join(contact[:3]).split()
    if fio != 3:
        fio.append("")
    fio_list = fio + contact[3:]
    contact_new = ",".join(fio_list)
    contact_new2 = re.sub(pattern, replace, contact_new)
    contact_list = contact_new2.split(",")
    new_list.append(contact_list)
    for current_contact in new_list:
        for contact_in_final_list in final_list:
            if contact_in_final_list[:1] == current_contact[:1]:
                final_list.remove(contact_in_final_list)
                current_contact = [x if x!="" else y for x, y in zip(contact_in_final_list, current_contact)]
        final_list.append(current_contact)

with open("phonebook.csv", "w", encoding="UTF-8") as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(final_list)