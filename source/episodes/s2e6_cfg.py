import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E06_Collision.pdf')
PARTS = [D + 's2e6_part1.txt', D + 's2e6_part2.txt', D + 's2e6_part3.txt']
EP = date(2005, 10, 20)
CODE = '2x06'
SEASON_LINE = 'Season 2, Episode 6'
TITLE = 'Collision'
COUNTERPART = "Episode 2x06. The counterpart of <i>Grey's Anatomy</i> 2x06."
DATES = 'Thursday, October 20, 2005, 7:46 AM through 11:42 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x05'
AGES_ON = 'Thursday, October 20, 2005'

CAST = [
 ("Lorraine Fuller (new)", "Patient: impaled, aortic injury", date(1964,6,12)), ("Dwayne Ricks (new)", "Patient: impaled; Nassau County court officer", date(1967,2,27)),
 ("Dr. Amond Baker", "Surgical Intern (on leave); triage", date(1979,2,10)), ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)),
 ("Dr. Natasha Donohue", "Chief of Surgery; Incident Commander", date(1958,6,2)), ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)),
 ("Lt. Tanisha 'Tee' Rollins", "FDNY EMS Lieutenant", date(1976,8,16)), ("Dr. Elxa Bullock", "Surgical Resident (24 weeks pregnant)", date(1977,8,29)),
 ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)), ("Dr. Clayton Hartwell", "Fetal Surgeon", date(1971,3,3)),
 ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Tamar Wells (new)", "Patient: epidural hematoma, placental abruption", date(1974,8,18)), ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)), ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)),
 ("Dr. Bryce Kennerly", "Surgical Intern (medicine)", date(1978,6,11)), ("Keith Brantley (new)", "Lorraine's boyfriend; architect", date(1962,9,9)),
 ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)), ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)),
 ("Franklin Bassett, Esq.", "General Counsel", date(1958,10,28)), ("Monica Ricks (new)", "Dwayne's wife; postal clerk", date(1969,5,5)),
 ("Mrs. Evangeline Truitt", "Trustee", date(1934,12,1)), ("Rev. Isaac Ashworth", "Trustee", date(1937,3,30)),
 ("Judge Harold Kittredge (new)", "Trustee", date(1940,2,6)), ("Chairman Theodore Rawlings (new)", "Chairman, Board of Trustees", date(1938,7,1)),
 ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)), ("Dr. Victor Donohue", "(V.O.)", date(1933,5,30)),
]
ALSO = ("<i>Also appearing: FDNY firefighters and paramedics, a radiologist, an OB resident, a NICU nurse, an anesthesiologist, a scrub tech, crash victims, Baby Girl Wells (Hope), "
        "trustees Dexter Hollingsworth, Cora Edmonds, James Calloway, Dr. Augusta Freeman and Simeon Howell, and a restaurant host (V.O.).</i>")

MEDIA = [
 ("NY1: BREAKING NEWS chyron", "Thursday, October 20, 2005, 8:02 AM",
  ["\"BREAKING: LIRR TRAINS COLLIDE EAST OF WOODSIDE; 'MANY INJURED'; MAIN LINE SERVICE SUSPENDED\""]),
 ("NEW YORK DAILY NEWS (front page): \"HORROR ON THE MAIN LINE\"", "Friday, October 21, 2005",
  ["\"Eleven people were killed and more than 140 injured yesterday when an eastbound Long Island Rail Road work train and a westbound Huntington commuter train collided just east of Woodside during the morning rush... "
   "Queens Grace Hospital in Long Island City, the nearest Level I trauma center, treated 104 victims. Among them were two strangers impaled on a single steel handrail; one survived... The NTSB has opened an investigation.\" "
   "<i>(Note: the collision is fictional, an in-world event of Mercy's Anatomy.)</i>"]),
 ("ASSOCIATED PRESS: \"SADDAM HUSSEIN PLEADS INNOCENT AS TRIAL OPENS\" / \"WILMA BECOMES STRONGEST ATLANTIC HURRICANE ON RECORD\"", "October 19-20, 2005",
  ["\"BAGHDAD (AP) -- A defiant Saddam Hussein pleaded innocent Wednesday as his trial opened...\" / \"MIAMI (AP) -- Hurricane Wilma's central pressure fell to 882 millibars, the lowest ever recorded in the Atlantic basin...\""]),
 ("QueensGraceConfidential (Blogger)", "Thursday, October 20, 2005, 11:30 PM",
  ["<i>\"No jokes tonight. 104 patients through our doors. The pole couple: he lived, she didn't. Dr. X was with her for three hours and told her boyfriend himself. "
   "The Scary Intern, on MEDICAL LEAVE, tagged 104 people in the ambulance bay sitting on a wall, and wasn't wrong once. A 33-week baby named Hope was born in OR 6 while two surgeons operated on her mother's head and belly at the same time. "
   "And something happened on the twelfth floor at 6 PM, and Bernie's not talking, and Bernie always talks. Hug somebody.\"</i> Comments (1,206)."]),
 ("Board of Trustees: sealed executive-session minutes (cover sheet only)", "Thursday, October 20, 2005",
  ["\"Executive session, 5:02-6:04 PM. Motion (Dr. H. Whitlow): review of Victor Donohue Foundation relationships with medical staff. Vote: 4 in favor, 4 opposed. MOTION FAILS. "
   "Disclosure by the Chief of Surgery received and SEALED. Nondisclosure agreements executed by all trustees present. -- F. Bassett, Counsel.\""]),
 ("SMS, Motorola RAZR (Raven Ellison to Harmony Divine)", "Thursday, October 20, 2005, 3:41 PM",
  ["<b>Raven:</b> \"i kissed her\"", "<b>Raven:</b> \"in a supply room\"", "<b>Harmony:</b> \"RAVEN\"", "<b>Harmony:</b> \"i asked camille out. saturday. i went first\"", "<b>Raven:</b> \"WHO ARE WE\""]),
]

CONT = [p("Continuity Sheet: Episode 2x06", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>The Woodside LIRR collision</b> (fictional in-world event): at 7:48 AM, October 20, 2005, an eastbound work train hit a westbound Huntington commuter train on the Main Line just east of Woodside. 11 dead, about 140 injured, and 104 treated at QGH. Natasha served as Incident Commander.",
 "<b>Lorraine Fuller</b> (41, a Bloomingdale's shoe and handbag buyer) and <b>Dwayne Ricks</b> (38, a Nassau court officer) were impaled on one vestibule handrail. The pole had transfixed her infrarenal aorta and was 'corking' it. Dwayne was freed first; Lorraine's calcified aorta split above the clamp, and Marc held it with his fingers. <b>Time of death 11:04 AM</b>, called by Marc. "
 "She told Keith Brantley 'I love you' for the first time at 10:26 AM ('Rainy'; he rode a bike over the Queensboro Bridge). Dwayne survived. This is the counterpart of Grey's Bonnie and Tom.",
 "<b>Marc said 'I've got it, Dad' on the table</b> in front of Robert, Elxa and Lowery. <b>Lowery has known since about August 3</b> ('Bullock's a common name. Not that common') and will keep it. Marc finally cried in the on-call room with his hand on Elxa's belly at 24 weeks (viability).",
 "<b>THE BOARD VOTE: 4 to 4, the motion fails.</b> In favor: Hollingsworth, Edmonds, Calloway and Judge Kittredge. Opposed: Truitt, Dr. Augusta Freeman, Simeon Howell and Rev. Ashworth. <b>Natasha disclosed in sealed executive session</b>, with Marc's consent ('Tell them... Don't let Whitlow say it first'), that Marc is her and Robert's son and Victor's grandson. "
 "She presented her January 9, 2005 recusal letter (Graves ranked the class), the NRMP match list and the Foundation comptroller's certification (no Foundation money to resident salaries since 1978). <b>The will and heir designation were NOT disclosed.</b> All trustees signed NDAs and the minutes are sealed. Whitlow heard the disclosure. Ashworth: 'That wasn't a confession. That was a testimony.'",
 "<b>Whitlow:</b> 'Secrets are like aortas. Once you open them, they don't close the way they used to.' Natasha told him about Joan's 1974 verdict to his face. Kennerly likely knows by tonight.",
 "<b>Marc has promised Raven and Harmony he'll tell them 'soon.'</b> 'Not not yet. Soon.' This sets up the 2x09 Thanksgiving reveal.",
 "<b>Amond (on leave) triaged 104 patients</b> in the ambulance bay, with none under-triaged and five re-triaged up. He sat when Arianna told him to and said 'Yes, sir' to Robert: 'I pressed the button.' Arianna re-checked his one black tag (a 19-year-old in a Hofstra sweatshirt).",
 "<b>Esther and Clayton</b>: a simultaneous cesarean and craniotomy on Tamar Wells in OR 6 (Graves allowed it: 'Policy 4.12 never met a train crash'). Baby Girl Wells, 'Hope,' was born at 33 weeks, 4 lb. Esther disclosed to Clayton that she wanted to comfort Marc; Clayton: 'I'm jealous... that's my problem, not yours.'",
 "<b>Raven and Arianna's first kiss</b>, in a Pit supply room ('I didn't see it raining'). <b>Harmony asked Camille out</b> for Saturday, October 22 ('I'm going first'). Harmony and Camille's first date was Friday, October 14 (they danced).",
 "Amond's return from leave remains about October 25. Arianna turns 26 on October 25."])
CONT.append(p("Knowledge Tracker (as of October 20, 2005)", H2))
CONT.append(tbl([["Who knows Marc is Natasha's son and Victor's grandson", "How"],
 ["Family, Bernie, Graves, Gloria, Mrs. Truitt, Amond, Big Ray, Arianna, Esther", "Earlier episodes"],
 ["<b>Dr. Lowery</b>", "Since about August 3; confirmed by 'Dad' on the table"],
 ["<b>All 8 trustees and Chairman Rawlings; Franklin Bassett</b>", "Natasha's sealed disclosure, October 20"],
 ["<b>Dr. Whitlow</b> (and likely Kennerly)", "In the room for the disclosure"],
 ["Suspect: Raven, Harmony, Clayton, Monty", "Raven and Harmony have been promised 'soon'"],
 ["Heir designation", "Still only Victor, Marc, V.J., the Foundation board (sealed letter) and Natasha"]],
 [3.0*inch, 3.4*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Lorraine Fuller", "6/12/1964 (41)", "Transfixing pole injury through the infrarenal aorta", "Ex-lap, aortic control, supraceliac clamp (Robert; Marc)", "Died 11:04 AM"],
 ["Dwayne Ricks", "2/27/1967 (38)", "Pole through the RLQ: bowel injury, flank", "Ex-lap, bowel repair (Elxa; Lowery)", "Survived"],
 ["Tamar Wells", "8/18/1974 (31)", "Temporal epidural hematoma; placental abruption at 33 weeks", "Simultaneous craniotomy (Graves; Esther) and cesarean (Clayton)", "Both survived; Hope, 4 lb"],
 ["Transit worker", "-", "Hemothorax (crush)", "Chest tube (Marc; Gloria)", "Stable"],
 ["Mass casualty", "-", "104 patients; 31 fractures (Camille)", "Triage (Amond)", "11 dead on the line"]],
 [1.05*inch, 0.9*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Lorraine Fuller</b> (1964-2005), <b>Keith Brantley</b> (b. September 9, 1962), <b>Dwayne Ricks</b> (b. February 27, 1967), <b>Monica Ricks</b> (b. May 5, 1969), <b>Tamar Wells</b> (b. August 18, 1974) and Hope Wells (b. October 20, 2005).",
 "<b>QGH Board of Trustees:</b> Chairman Theodore Rawlings (b. 1938), Judge Harold Kittredge (b. 1940), Dexter Hollingsworth (b. 1945), Cora Edmonds (b. 1947), James Calloway (b. 1961), Dr. Augusta Freeman (b. 1934), Simeon Howell (b. 1942), Mrs. Truitt and Rev. Ashworth."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["<b>The LIRR collision is fictional.</b> No such crash occurred on October 20, 2005. Real background: Saddam Hussein's trial opened October 19, 2005, and Hurricane Wilma reached 882 mb on October 19, a record Atlantic low. The Port Washington Branch stops at Woodside; the Main Line carries Huntington and Port Jefferson trains through Woodside.",
 "Medicine: a transfixing object is left in place until the OR, where proximal and distal vascular control comes before extraction. A calcified aorta may fracture at the clamp site, and supraceliac clamping is a salvage measure. "
 "Simultaneous cesarean delivery and craniotomy for a pregnant trauma patient has been reported. Twenty-four weeks is the conventional threshold of viability. Resident salaries are funded mainly by Medicare GME."])
