import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E15_Walk_Out.pdf')
PARTS = [D + 's2e15_part1.txt', D + 's2e15_part2.txt', D + 's2e15_part3.txt']
EP = date(2006, 1, 30)
CODE = '2x15'
SEASON_LINE = 'Season 2, Episode 15'
TITLE = 'Walk Out'
COUNTERPART = "Episode 2x15. The counterpart of <i>Grey's Anatomy</i> 2x15 (the nurses' strike)."
DATES = 'Monday, January 30, 2006 (QGH nurses\' one-day strike), 5:56 AM through 11:58 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x14'
AGES_ON = 'Monday, January 30, 2006'

CAST = [
 ("Nurse Kendra Wallace", "Surgical Floor Nurse (on strike)", date(1980,5,30)), ("Nurse Yvette Banks", "CVICU Charge Nurse (on strike)", date(1963,12,1)),
 ("Nurse Gloria Pettiford", "Head ER Nurse (management)", date(1952,4,14)), ("Dr. Elxa Bullock", "Surgical Resident (38 weeks 5 days; desk duty)", date(1977,8,29)),
 ("Russell Jeffries", "Elxa's husband", date(1975,4,3)), ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)),
 ("Dr. Sylvia Rountree", "President and CEO", date(1951,12,2)), ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)),
 ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)), ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)),
 ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Bryce Kennerly", "Surgical Intern", date(1978,6,11)), ("Mrs. Lavinia Stroud (new)", "Patient: respiratory arrest; DNR/DNI", date(1914,10,8)),
 ("Josiah Wiggins (new)", "Patient, 16: pelvic and femur fractures, hemorrhagic shock", date(1989,9,9)), ("Brother Clifford Wiggins (new)", "Josiah's father", date(1961,6,12)),
 ("Sister Joyce Wiggins (new)", "Josiah's mother", date(1963,11,1)), ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)),
 ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)), ("Darius 'Dash' Duvall", "Patient: Status 1A, day 80", date(1971,8,8)),
 ("Glenda Duvall", "Dash's mother", date(1947,12,12)), ("Cora Stroud (new)", "Lavinia's daughter; retired principal", date(1939,4,30)),
 ("Dr. Cyrus Langley (new)", "Patient: valve replacement; Robert's Howard professor", date(1927,7,17)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Howard Divine", "Harmony's father (TWU, in solidarity)", date(1950,8,30)), ("Franklin Bassett, Esq.", "General Counsel", date(1958,10,28)),
 ("Justice Harold Dukes (V.O., new)", "Supreme Court, Queens County", date(1949,2,2)), ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)),
 ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)), ("Mrs. Eunice Langley (new)", "Cyrus's wife", date(1929,5,5)),
 ("Lillian Divine", "Harmony's mother", date(1952,2,14)), ("Mercy", "The House's pit bull puppy", date(2005,9,30)),
]
ALSO = ("<i>Also appearing: about 260 striking NYSNA nurses, 94 Premier Clinical Staffing replacement nurses, paramedics, an agency respiratory therapist, a chaplain and a fax machine. "
        "Mentioned: Marisol (Mrs. Stroud's regular nurse), Mrs. Ocasio (CVICU Bed 7), Dr. Hampton, Dr. Delphine Ware (d. 2003) and Malcolm Sloan (by email).</i>")

MEDIA = [
 ("NEW YORK DAILY NEWS: \"NURSES WALK AT QUEENS GRACE\"", "Monday, January 30, 2006",
  ["\"Some 260 registered nurses at Queens Grace Hospital in Long Island City walked off the job at 7 a.m. today for a 24-hour strike over staffing ratios and mandatory overtime, after giving the 10-day notice federal law requires of health care unions. Hospital officials said 94 replacement nurses from an agency would keep 'all essential services' open.\" (A fictional strike at a fictional hospital.)"]),
 ("ASSOCIATED PRESS: \"SENATE CLEARS WAY FOR ALITO VOTE\" / \"ABC ANCHOR WOODRUFF HURT IN IRAQ\"", "Monday, January 30, 2006",
  ["\"WASHINGTON (AP) -- The Senate voted 72-25 to end debate on Samuel Alito's Supreme Court nomination, setting up a confirmation vote Tuesday...\" / \"ABC News co-anchor Bob Woodruff and a cameraman were seriously injured Sunday by a roadside bomb near Taji, Iraq...\""]),
 ("QueensGraceConfidential (Blogger)", "Monday, January 30, 2006, 7:12 PM",
  ["<i>\"DAY OF THE WALKOUT. We saw doctors emptying Foleys. We saw Nurse P. hold a picket sign for exactly thirty seconds on her dinner break ('the contract says I can'). We saw an intern's mother feed the line FOUR POTS OF CHILI and an MTA bus driver march with the nurses in his TWU jacket. "
   "We also heard a 91-year-old patient waved goodbye to the intern who took out her breathing tube. If you don't think nurses matter, come spend a day on Six North. Solidarity.\"</i> Comments (3,118)."]),
 ("Order of the Supreme Court of the State of New York, County of Queens (excerpt)", "Monday, January 30, 2006, 11:04 AM (by fax)",
  ["\"IN THE MATTER OF THE APPLICATION OF QUEENS GRACE HOSPITAL re: J.W., an infant... ORDERED, that the hospital is authorized to administer blood and blood products as medically necessary to preserve the life of the infant, and for no other purpose. -- Hon. Harold Dukes, J.S.C.\""]),
 ("Email: Malcolm Sloan to Clayton Hartwell", "Monday, January 30, 2006, 4:48 PM",
  ["\"Clay -- Starting the 13th. Rountree's put me in the corner office on Seven. If it's easier for her, I'll take the stairs on the east side and never use the west elevators. Tell her that. Tell her whatever she needs. -M.\""]),
 ("MOLST form (Lavinia Stroud), Section A", "Signed 2003",
  ["\"DO NOT RESUSCITATE (DNR). DO NOT INTUBATE (DNI).\" (The orange DNR bracelet was found in the wrong laundry drawer on January 30.)"]),
]

CONT = [p("Continuity Sheet: Episode 2x15", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>THE QGH NURSES' STRIKE</b> (fictional, NYSNA): about 260 RNs on a 24-hour strike from 7 AM January 30 to 7 AM January 31 over staffing ratios (Six North ran 1:8 on nights) and mandatory overtime. Ten-day notice was given January 20. Rountree brought in 94 agency nurses, and the residents and interns nursed. <b>Gloria (management) stayed in</b>, left hazelnut coffee on the barricade, and held a picket sign for 30 seconds on her dinner break ('the contract says I can'). Yvette Banks led the line with a bullhorn. Howard marched in his TWU jacket, and Lillian brought four pots of chili. Rountree threatened discipline for refusing overtime. Natasha argued that the strike is 'just when we finally noticed.'",
 "<b>MARC AND THE DNR</b> (Grey's 2x15 beat): at 7:16 AM Marc found Mrs. Lavinia Stroud (91) in respiratory arrest on Six North with no bracelet, no sign and no nurse (her regular nurse, Marisol, was on strike), and intubated her. Her MOLST (DNR/DNI, 2003) was on page one of the chart, buried at the station. Natasha told the daughter it was 'this hospital's' failure. Mrs. Stroud spelled 'LET ME GO' and then 'YOU.' <b>Marc did the terminal extubation at 3:00 PM.</b> She waved at him and died at 3:27 PM; Marc called it. The bracelet turned up in the wrong laundry drawer.",
 "<b>ARIANNA AND THE JEHOVAH'S WITNESS MINOR</b> (Grey's 2x15 beat): Josiah Wiggins (16, baptized at 13) was in a car crash on the Clearview (his mother was driving on black ice), with an open-book pelvis and femur fracture and a hemoglobin of 5.2. He and his parents refused blood. They accepted a cell saver and EPO. Bassett got an emergency order from <b>Justice Harold Dukes</b>, and <b>Arianna transfused</b> while Joyce prayed on the floor. 'It's my choice. Not yours. It's on me.' Arianna to Clifford: 'I've spent ten years wishing somebody had loved me enough to fight about anything.' Camille and Harmony did an ex-fix and an IM femoral nail. Josiah: 'I'm still mad at you... But I'm glad I'm going to see my sister's graduation.'",
 "<b>THE DELPHINE WARE ALLUSION</b> (counterpart of the Webber and Ellis allusion): <b>Dr. Cyrus Langley</b> (78), Robert's Howard professor in 1979 (he taught left-handed knots in the dark), had a valve replacement by Robert. Still confused from anesthesia, he told Robert and Amond, and then Natasha: 'That Ware girl. Chicago. Delphine... 1981... She used to wait for you outside the call room, Bobby.' <b>Natasha connected it to the Chicago postmark.</b> <b>Natasha found the sealed letter in Robert's glove compartment and did NOT open it</b> ('they're his to tell'). That night Robert gave the partial truth: 'She was a surgery resident at Howard... She died... a stroke.' Natasha: 'One day, I'm going to ask you that again.' <b>Amond overheard Langley</b> and chose not to tell Marc. Marc: 'Then it's his to tell.' The letter remains unopened.",
 "<b>Raven and Dash:</b> Raven nursed him all day (the amiodarone at 2 PM with crackers first, the Panthers blanket on his left side, hair washed on Mondays, all relayed by Yvette through Harmony from the picket line). She washed his hair and rested her forehead on his towel-wrapped head. Dash: 'I can't go back to you being Dr. Ellison.' Raven: 'Neither can I.' <b>Raven and Arianna:</b> a small truce in the locker room. Raven still keeps chocolate milk for her, 'since October.'",
 "<b>Malcolm emailed Clayton:</b> he starts on February 13 in the corner office on Seven and offered to use only the east stairs. Esther: 'That's not forgiveness. It's a fire drill... I want him to use the elevator... I'm just not there yet.' <b>Elxa (38w5d)</b> is on desk duty from January 30 (cushion and three phones), 2 cm dilated at Friday's visit with Dr. Hampton, and having prodromal contractions every 8 to 12 minutes. Russell: 'Please don't let him come during the Super Bowl.'",
 "<b>Kennerly apologized to Kendra</b> for using her to spread the rumor in September ('It's a correction'). His father is in Scottsdale with his third wife, and his mother is in Phoenix; they don't talk. Lillian told him to call both. Gloria: 'Two right things that can't stand in the same room.' She has worked eight-patient nights since 1984 and saw a nurse die of a stroke in the break room at 46."])
CONT.append(p("Knowledge Tracker (as of January 30, 2006)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Delphine Ware's name and Chicago", "Natasha (suspects an old relationship), Amond (overheard Langley), Robert"],
 ["The sealed letter's existence", "Robert; Natasha (saw it, didn't open it; Robert doesn't know she saw it)"],
 ["Mariah Pettaway", "No one. Locked until Season 11"],
 ["Raven and Dash", "Deepening; Glenda, Arianna, Harmony, Marc and Yvette all aware"],
 ["Malcolm's start date (February 13)", "Esther, Clayton, Natasha, Rountree; the blog soon"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Mrs. Lavinia Stroud", "10/8/1914 (91)", "Respiratory arrest; DNR/DNI not visible", "Intubation 7:16 AM; terminal extubation 3:00 PM (Bullock)", "Died at 3:27 PM, comfort care"],
 ["Josiah Wiggins", "9/9/1989 (16)", "Open-book pelvis, right femur fracture, hemorrhagic shock (Hgb 5.2)", "Pelvic binder, ex-fix, IM nail (Toussaint; Divine); court-ordered transfusion, 2 units (Cummings)", "Stable; HR 98"],
 ["Dr. Cyrus Langley", "7/17/1927 (78)", "Valve replacement, post-op", "(R. Bullock; Baker; Ellison as nurse)", "Recovering; confused from anesthesia"],
 ["Darius 'Dash' Duvall", "8/8/1971 (34)", "Status 1A, day 80; amiodarone", "Nursed by Ellison", "Stable"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Dr. Cyrus Langley</b> (b. July 17, 1927), professor of surgery at Howard (taught Robert in 1979), and <b>Mrs. Eunice Langley</b> (b. May 5, 1929). <b>Mrs. Lavinia Stroud</b> (b. October 8, 1914) and <b>Cora Stroud</b> (b. April 30, 1939), a retired principal.",
 "<b>Josiah Wiggins</b> (b. September 9, 1989; Bayside High School), with <b>Brother Clifford</b> (b. June 12, 1961) and <b>Sister Joyce Wiggins</b> (b. November 1, 1963). <b>Justice Harold Dukes</b> (b. February 2, 1949; voice only). Kendra Wallace and Yvette Banks lead the picket."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["The NLRA's Section 8(g) requires unions at health care institutions to give 10 days' notice before a strike, and one-day strikes with agency replacement nurses are common in New York (NYSNA). On January 30, 2006, the Senate invoked cloture on Samuel Alito's nomination 72-25 (he was confirmed January 31), and on January 29 ABC's Bob Woodruff was badly injured in Iraq. "
 "Super Bowl XL (Steelers vs. Seahawks) was played in Detroit on February 5, 2006. The Shoreham is a Washington hotel. Howard University Hospital replaced Freedmen's in 1975.",
 "Medicine: a MOLST/DNR order must be honored, and a misplaced bracelet or chart is a system failure. A patient with capacity may refuse continued ventilation, and terminal extubation with comfort medication is ethically equivalent to withholding. Jehovah's Witnesses refuse whole blood and major components, but many accept a cell saver in continuous circuit, EPO and iron. "
 "For minors facing imminent death, New York courts routinely authorize transfusion over parental and minor objection. Open-book pelvic fractures are stabilized with a binder, then external fixation. Prodromal labor can produce irregular contractions for days."])
