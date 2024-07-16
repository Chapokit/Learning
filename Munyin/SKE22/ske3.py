death_report = {
    'Stable Boy Tomas': {'Age': 17, 'Cause of Death': "Horse kicking", 'Date': "1315 DR-03-03"},
    'Princess Elara': {'Age': 29, 'Cause of Death': "Falling", 'Date': "1315 DR-03-10"},
    'Bard Taliesin': {'Age': 29, 'Cause of Death': "Duel", 'Date': "1315 DR-03-15"},
    'Rogue Thief Kael': {'Age': 31, 'Cause of Death': "Executed", 'Date': "1315 DR-03-20"},
    'Hunter Finnian': {'Age': 20, 'Cause of Death': "Wolf Attack", 'Date': "1315 DR-03-25"},
    'Priestess Mirabel': {'Age': 37, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-03-30"},
    'Sellsword Bronn': {'Age': 39, 'Cause of Death': "Murdered", 'Date': "1315 DR-04-05"},
    'Sailor Roderic': {'Age': 41, 'Cause of Death': "Falling", 'Date': "1315 DR-04-10"},
    'Knight Commander Duncan': {'Age': 42, 'Cause of Death': "Battlefield Injury", 'Date': "1315 DR-04-15"},
    'Innkeeper Bess': {'Age': 24, 'Cause of Death': "Mysterious Illness", 'Date': "1315 DR-04-20"},
    'Lord Garrick': {'Age': 45, 'Cause of Death': "Garlic Allergy", 'Date': "1315 DR-04-25"},
    'Blacksmith Hrothgar': {'Age': 48, 'Cause of Death': "Forge Accident", 'Date': "1315 DR-04-30"},
    'Sir Reginald': {'Age': 51, 'Cause of Death': "Old Age", 'Date': "1315 DR-05-05"},
    'Merchant Galen': {'Age': 53, 'Cause of Death': "Murdered by Banana", 'Date': "1315 DR-05-10"},
    'Miss Seraphina': {'Age': 55, 'Cause of Death': "Old Age", 'Date': "1315 DR-05-15"},
    'Sorcerer Sellen': {'Age': 62, 'Cause of Death': "Magical Explosion", 'Date': "1315 DR-05-20"},
    'Dwarven Miner Thrain': {'Age': 75, 'Cause of Death': "Cave-in", 'Date': "1315 DR-05-25"},
    'Mage Apprentice Serin': {'Age': 23, 'Cause of Death': "Spell Backfire", 'Date': "1315 DR-05-30"},
    'Lady Aeliana': {'Age': 34, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-27"},
    'Blacksmith Luira': {'Age': 70, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-28"},
    'Madam Luika': {'Age': 70, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-28"},
    'Sir Luigi': {'Age': 70, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-28"},
    'Elven Archer Xenos': {'Age': 70, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-29"},
    'Elven Archer Lythiel': {'Age': 128, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-29"},
    'Knight Seenato': {'Age': 44, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-30"}
}

# Add the info of Lucatiel's sister to death_report
death_report["Lovely Girl Anri"] = {'Age': 16, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-07-01"}


filtered_report = {}
# for-loop here

for key, value in death_report.items():

    if "murdered" in value['Cause of Death'].lower():
        filtered_report[key] = value
print(filtered_report)