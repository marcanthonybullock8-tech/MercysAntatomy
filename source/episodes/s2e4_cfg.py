import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E04_Deny_Everything.pdf')
PARTS = [D + 's2e4_part1.txt', D + 's2e4_part2.txt', D + 's2e4_part3.txt']
EP = date(2005, 10, 8)
CODE = '2x04'
SEASON_LINE = 'Season 2, Episode 4'
TITLE = 'Deny Everything'
COUNTERPART = "Episode 2x04. The counterpart of <i>Grey's Anatomy</i> 2x04."
DATES = 'Saturday, October 8, 2005, 5:41 AM through Sunday, October 9, 2005, 6:55 AM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x03'
AGES_ON = 'Saturday, October 8, 2005'

CAST = [
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Elxa Bullock", "Surgical Resident (22.5 weeks pregnant)", date(1977,8,29)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Dr. Amond Baker", "Surgical Intern (on medical leave)", date(1979,2,10)),
 ("Harriet Baker-Fenwick", "Amond's mother", date(1952,10,5)), ("Dr. Solomon Fenwick", "Amond's stepfather", date(1948,3,21)),
 ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)), ("Dr. Victor Donohue", "Founder, Victor Donohue Foundation", date(1933,5,30)),
 ("Lt. Tanisha 'Tee' Rollins", "FDNY EMS Lieutenant", date(1976,8,16)), ("Gwendolyn Monroe (on-screen debut)", "Alicia's mother; the Gaithers' neighbor", date(1951,10,10)),
 ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)), ("Dr. Raven Ellison", "Surgical Intern (post-call)", date(1979,12,3)),
 ("Dr. Arianna Cummings", "Surgical Intern (post-call)", date(1979,10,25)), ("Malik Ellerbe", "Patient: high-voltage electrical injury", date(1975,1,30)),
 ("Dr. Clayton Hartwell", "Fetal Surgeon; Esther's husband", date(1971,3,3)), ("Nadia Ellerbe", "Patient: PPROM after fetal surgery", date(1977,4,25)),
 ("Dr. Camille Toussaint (debut)", "Orthopedic Resident (PGY-3), displaced from Tulane", date(1976,7,21)), ("Harbormaster (new)", "World's Fair Marina", date(1949,4,4)),
 ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Dr. Bryce Kennerly", "Surgical Intern (medicine consults)", date(1978,6,11)), ("Pearl Gaither (new)", "Patient: carbon monoxide poisoning", date(1934,4,12)),
 ("Rhonda Gaither (new)", "Pearl's daughter; patient", date(1971,3,5)), ("Jayla Gaither (new)", "Patient, age 6", date(1999,5,14)),
 ("Curtis Lemieux", "Patient: heart transplant", date(1961,4,9)), ("Odile Lemieux", "Curtis's mother", date(1936,3,19)),
 ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)),
]
ALSO = ("<i>Also appearing: an NYPD officer, FDNY paramedics including Andre Fontaine, Marcus Gaither (9), an L&D nurse and charge nurse, a SICU nurse, Victor's driver and Monty's patrons. "
        "Mentioned: Councilman Leroy Comrie's office, Dr. Leonard Baker (in a photograph), Joan Mercer, Judge Kittredge and his wife, and Dr. Hampton.</i>")

MEDIA = [
 ("THE NEW YORK TIMES: \"CITY RAISES ALERT AFTER SUBWAY THREAT\"", "Friday, October 7, 2005",
  ["\"Mayor Michael R. Bloomberg said Thursday that the city had received a specific threat against the subway system, and the police flooded stations with officers and began searching bags... Federal officials said the information was of 'doubtful credibility'...\""]),
 ("ASSOCIATED PRESS: \"MASSIVE QUAKE STRIKES PAKISTAN, INDIA\"", "Saturday, October 8, 2005",
  ["\"ISLAMABAD, Pakistan (AP) -- A magnitude-7.6 earthquake rocked Pakistan, India and Afghanistan on Saturday morning, flattening villages in Pakistani-held Kashmir... Officials feared the death toll could reach the tens of thousands...\""]),
 ("NY1: on-screen chyron", "Saturday, October 8, 2005, 8:40 PM",
  ["\"RECORD OCTOBER RAINFALL: FLOODING IN NEW JERSEY, WESTCHESTER; FLOOD WATCH FOR QUEENS THROUGH MONDAY\""]),
 ("QueensGraceConfidential (Blogger)", "Saturday, October 8, 2005, 11:58 PM",
  ["<i>\"Weekend dispatch: a Con Ed lineman with a 13,000-volt injury, a whole Hollis family poisoned by a landlord's generator, and a NEW ORTHO RESIDENT from Tulane who announced herself in the Pit like a brass band. "
   "Meanwhile, a certain intern's BOAT nearly sank at World's Fair Marina, and our sources say four other interns and a sump pump from Monty's saved it. Then Boston left with her husband. Under one umbrella. We're just reporting it.\"</i> Comments (402)."]),
 ("SMS, Motorola RAZR (Esther Smilley and Clayton Hartwell)", "Saturday, October 8, 2005, 5:49 AM",
  ["<b>Clayton:</b> \"Flood watch for Queens until Monday. The marina will be underwater. Come stay at mine. Couch. No conditions. -C\"", "<b>Esther:</b> \"im fine.\""]),
 ("SMS, Motorola RAZR (Arianna Cummings to Amond Baker)", "Saturday, October 8, 2005, 7:44 PM",
  ["<b>Arianna:</b> \"boat saved. smilley went w the husband. bullock coiling a cord like its a suture. dont tell him i told u\"", "<b>Amond:</b> \"Understood. Telling him anyway.\""]),
 ("Harriet Baker-Fenwick: Post-it notes (Amond's bedroom)", "Saturday, October 8, 2005",
  ["\"TAKE YOUR IRON.\" \"WALK 10 MIN 3X DAILY.\" \"NO LIFTING.\" \"CALL YOUR MOTHER.\" \"YOUR FRIENDS ARE GOOD PEOPLE. LET THEM.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x04", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>Esther and Clayton</b> (day 27): the Clarence nearly sank at World's Fair Marina. Harmony, Raven, Arianna and Marc saved it with Monty's sump pump (2,000 gallons an hour). Marc: 'Whatever you need, Es,' honoring his 'enough.' <b>Esther went to Clayton's sublet</b> (Remsen Street, Brooklyn Heights) and <b>they slept together</b>. 'It doesn't mean anything.' The second bedroom was untouched. Esther and Clayton had dinner on Thursday, October 6 (off screen).",
 "<b>Raven and Harmony saw Victor</b> holding Marc in the back of a black Mercedes on 49th Avenue at 11:16 PM. Harmony recognized 'Dr. Donohue, a friend of the hospital' from August 9. Raven: 'Who is Marc?' Harmony: 'He's Marc.' <b>Both now know something; neither knows what.</b> This sets up the reveal in 2x09.",
 "<b>Clayton suspects Elxa and Marc are siblings and the Chief's children</b> ('same cadence, same chin'). Elxa: 'Bullock's a common name.' Elxa's cervix is 4.1 cm and closed; she was having Braxton-Hicks at 22.5 weeks.",
 "<b>Whitlow confronted Robert</b> in the parking garage: 'Your son, Robert?' Robert: 'I don't discuss my family with you, Horace' (not a lie, not a door). <b>Victor revealed:</b> Whitlow applied to be a Mercer Scholar in 1974 (Penn) and was turned down after an interview with Victor and Joan in the Brookline library. Joan: 'That boy wants the house, Victor. Not the work.' Natasha forbade Victor from calling Judge Kittredge. Victor: 'We're hiding a boy who wanted to be judged on his own hands.' 'Sometimes not yet is just the polite word for no.'",
 "<b>Amond moved into the front second-floor bedroom</b> at the House on 49th Avenue (POD 4; no lifting for six weeks; staples out around October 14). Solomon brought Dr. Leonard Baker's photo, which Harriet gave him in 1991. Amond thanked Solomon for the first time in 17 years and apologized for how he treated him. Amond to Marc: 'I'm not fine either.' Marc: 'You're my day one.'",
 "<b>Dr. Camille Toussaint</b> (Callie Torres counterpart, PGY-3 orthopedics, displaced from Tulane, a Jackson Heights sublet with a cat and a singing radiator) makes her on-screen debut. She did Malik's fasciotomy with Harmony, nicknamed Harmony 'Choir,' asked whether there's a 'Mrs. Choir,' and met the gang at Monty's. This seeds Harmony and Camille (MA-005: their 2006 Vegas ceremony).",
 "<b>Arianna asked Raven to dinner.</b> Raven: 'Ask me again when it's not raining.' The forecast is Monday.",
 "<b>Malik Ellerbe</b> touched a downed 13 kV feeder on Francis Lewis Boulevard: entry right hand, exit left foot, frequent PVCs, CK 42,000 and myoglobinuria. Camille did a volar and dorsal forearm fasciotomy with carpal tunnel release. <b>Nadia Ellerbe had PPROM at 26w6d</b> (12:06 PM), treated with latency antibiotics and magnesium, with no rescue steroids yet. She reached 27w0d on October 9. Marc wheeled Malik's ICU bed to L&D, and Clayton authorized it after the fact.",
 "<b>Gwendolyn Monroe</b> appears on screen for the first time (a Muslim since 1985, Hollis neighbor of the Gaithers for 30 years). She saw how Harmony looks at Marc; Harmony: 'He's my roommate.' 'Allah hears the things we don't say too.'",
 "<b>Curtis Lemieux</b>'s rejection is resolving (grade 1A). Discharge is planned for Monday, October 10. <b>Odile is moving to New York</b> and has signed a lease on a ground-floor two-bedroom on West 141st Street.",
 "<b>Monty turns 43 on Monday, October 10.</b> 'Go save her boat. Don't go save her.'"])
CONT.append(p("Knowledge Tracker (as of October 9, 2005)", H2))
CONT.append(tbl([["Secret", "Who knows", "New pressure"],
 ["Marc's family", "Family, Bernie, Graves, Gloria, Mrs. Truitt, Amond, Big Ray, Arianna, Esther", "Whitlow (has connected him to Robert); Clayton (suspects the Chief and Elxa); Raven (suspects Elxa)"],
 ["Marc and Victor", "Same", "<b>Raven and Harmony saw Victor hug Marc</b> on 49th Avenue"],
 ["Esther slept with Clayton", "Esther, Clayton", "Marc doesn't know"],
 ["Harmony's feelings", "Raven, Esther, Gwendolyn (guessed)", "Camille has entered"]],
 [1.6*inch, 2.5*inch, 2.3*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Pearl Gaither", "4/12/1934 (71)", "CO poisoning, COHb 41%, GCS 8", "100% O2; hyperbaric oxygen (off site)", "Neuro intact"],
 ["Rhonda, Marcus and Jayla Gaither", "34, 9, 6", "CO poisoning, COHb 28%, 24% and 19%", "100% O2; hyperbaric for Rhonda", "Recovered. Landlord reported"],
 ["Malik Ellerbe", "1/30/1975 (30)", "13 kV electrical injury; forearm compartment syndrome; rhabdomyolysis", "Volar and dorsal fasciotomy, carpal tunnel release (Camille; Harmony)", "SICU telemetry; CK 42,000"],
 ["Nadia Ellerbe", "4/25/1977 (28)", "PPROM at 26w6d after open fetal surgery", "Ampicillin and erythromycin; magnesium (Clayton; Marc)", "27w0d, no labor"],
 ["Elxa Bullock", "8/29/1977 (28)", "Braxton-Hicks at 22.5 weeks", "TVUS cervical length 4.1 cm (Clayton)", "Sent home (didn't go)"],
 ["Curtis Lemieux", "4/9/1961 (44)", "Rejection resolving (grade 1A)", "Steroids (Robert)", "Home Monday"]],
 [1.15*inch, 0.85*inch, 1.7*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>The Gaithers</b> of 194th Street, Hollis: <b>Pearl</b> (b. April 12, 1934), <b>Rhonda</b> (b. March 5, 1971), <b>Marcus</b> (b. January 20, 1996) and <b>Jayla</b> (b. May 14, 1999).",
 "<b>Dr. Camille Toussaint</b> and <b>Gwendolyn Monroe</b> debut on screen (already in MA-005). <b>The World's Fair Marina harbormaster</b> (b. 1949)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["On October 6, 2005, Mayor Bloomberg announced a specific subway threat, and bag searches and police surges followed. The Kashmir earthquake (M7.6) struck at 8:50 AM local time on October 8 (late October 7 in New York), eventually killing more than 80,000. "
 "Record October rainfall hit the New York region from about October 7 to 12, 2005, with severe flooding in New Jersey. Con Edison runs overhead distribution lines in eastern Queens. Councilman Leroy Comrie represented southeast Queens in 2005.",
 "Medicine: pulse oximetry reads carboxyhemoglobin as oxygenated hemoglobin, so CO-oximetry is required. Hyperbaric oxygen is indicated for loss of consciousness or very high COHb. "
 "High-voltage injury causes deep muscle necrosis under small skin wounds, compartment syndrome (pressures over 30 mmHg), rhabdomyolysis and arrhythmias (24-hour telemetry). "
 "PPROM management: latency antibiotics (ampicillin and erythromycin), magnesium for neuroprotection under 32 weeks, and delivery for chorioamnionitis. A transvaginal cervical length of 4.1 cm is reassuring."])
