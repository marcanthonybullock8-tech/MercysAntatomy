import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E16_Take_Cover.pdf')
PARTS = [D + 's2e16_part1.txt', D + 's2e16_part2.txt', D + 's2e16_part3.txt']
EP = date(2006, 2, 5)
CODE = '2x16'
SEASON_LINE = 'Season 2, Episode 16 (Part One of Two)'
TITLE = 'Take Cover'
COUNTERPART = "Episode 2x16. The counterpart of <i>Grey's Anatomy</i> 2x16 (Part One of the Code Black two-parter)."
DATES = 'Sunday, February 5, 2006 (Super Bowl XL), 5:31 AM through 6:22 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x15. Continued in 2x17.'
AGES_ON = 'Sunday, February 5, 2006'

CAST = [
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Elxa Bullock", "Surgical Resident (39 weeks 2 days; in labor)", date(1977,8,29)),
 ("Russell Jeffries", "Elxa's husband (car crash, subdural hematoma)", date(1975,4,3)), ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Bryce Kennerly", "Surgical Intern", date(1978,6,11)), ("Nurse Kendra Wallace", "Surgical Floor Nurse", date(1980,5,30)),
 ("Darius 'Dash' Duvall", "Patient: Status 1A, day 86", date(1971,8,8)), ("Glenda Duvall", "Dash's mother", date(1947,12,12)),
 ("Reginald 'Reggie' Plummer (new)", "Patient: unexploded 37mm projectile in the left flank", date(1967,10,30)), ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Danita Crews (new)", "FDNY paramedic", date(1978,6,26)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)), ("Det. Sgt. Isaac Burrell (new)", "NYPD Bomb Squad; ex-USMC EOD", date(1961,9,14)),
 ("Dr. Edwin Mabry (on-screen debut)", "Chief of Anesthesiology", date(1957,6,24)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Dr. Hampton (on-screen)", "Elxa's obstetrician, Jamaica Hospital", date(1950,4,20)), ("LaShawn Plummer (new)", "Reggie's wife; nurse's aide", date(1969,8,3)),
 ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)), ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)),
 ("Cedric Hall", "Architect; Monty's partner", date(1965,1,22)), ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)),
 ("Lillian Divine", "Harmony's mother", date(1952,2,14)), ("Howard Divine", "Harmony's father", date(1950,8,30)),
 ("Dr. Victor Donohue", "Marc's grandfather", date(1933,5,30)), ("Mercy", "The House's pit bull puppy", date(2005,9,30)),
]
ALSO = ("<i>Also appearing: a construction foreman, FDNY paramedics, NYPD Bomb Squad officers, uniformed police, an OR 2 CABG patient, L&D nurses, a TV reporter, onlookers, and Reggie and LaShawn's toddler son. "
        "On TV: Aretha Franklin and Aaron Neville (national anthem, Super Bowl XL). Mentioned: Dr. Okoye (a resident with the flu), Imani Burrell (turning 8), Danita's 4-year-old daughter, Alphonse (Widener Library).</i>")

MEDIA = [
 ("WCBS-TV / NY1 (breaking news crawl)", "Sunday, February 5, 2006, 11:05 AM",
  ["\"BOMB SQUAD AT QUEENS HOSPITAL. NYPD has locked down Queens Grace Hospital in Long Island City after a construction worker was brought in with what police describe as a 'live military projectile' lodged in his body. The device was apparently unearthed at a Queens West construction site.\" (A fictional event.)"]),
 ("THE NEW YORK TIMES (Sports): \"STEELERS AND SEAHAWKS MEET IN DETROIT\"", "Sunday, February 5, 2006",
  ["\"DETROIT -- Super Bowl XL kicks off tonight at 6:28 p.m. at Ford Field... Aretha Franklin, a Detroit native, will sing the national anthem with Aaron Neville, and the Rolling Stones will perform at halftime.\""]),
 ("QueensGraceConfidential (Blogger)", "Sunday, February 5, 2006, 2:44 PM",
  ["<i>\"WE ARE INSIDE AND WE ARE OKAY. This blog's author is in the building. We can't tell you where. We can tell you there is something in OR 1 that the NYPD won't say on the radio, and that every cell phone on the old wing has been turned off. "
   "L&D is evacuating into the stairwells. A doctor's husband came in from a car crash. Pray. That's all. Just pray.\"</i> Comments (4,410)."]),
 ("Police radio log (excerpt, paraphrased), NYPD Bomb Squad", "Sunday, February 5, 2006",
  ["\"10:41: units on scene. 10:49: radio silence within 100 feet, OR 1. 11:02: containment vessel requested from Rodman's Neck. 4:24 PM: evacuate 4th floor west. 4:57 PM: vessel delayed at the Triborough; portable pot authorized.\""]),
 ("Text message, Harmony Divine to Camille Toussaint (sent 4:33 PM, delivered 5:51 PM)", "Sunday, February 5, 2006",
  ["<b>Harmony:</b> \"stairwell C w elxa. shes crowning. pray for me choir\""]),
]

CONT = [p("Continuity Sheet: Episode 2x16 (Part One)", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>THE CODE BLACK</b> (counterpart of Grey's 2x16 and 2x17): at 9:41 AM, excavator operator <b>Reggie Plummer</b> (38) at a Queens West site on the East River hit buried WWII-era ordnance (believed to be a Navy shipment dumped as landfill when the piers were built in 1945). A <b>37mm high-explosive projectile with an M54 point-detonating fuze</b> partially detonated (the booster fired, the main charge did not) and lodged in his left flank, anterior to the psoas, against the spine. <b>FDNY paramedic Danita Crews</b> (27) rode in with her hand on the shell. Lowery called the Code Black. <b>NYPD Bomb Squad Det. Sgt. Isaac Burrell</b> (44, ex-Marine EOD, Desert Storm) ordered no radios or phones within 100 feet, no cautery, no defibrillator, OR 1 (the old wing) isolated, and <b>the hospital locked down</b> (10:45 AM).",
 "<b>MARC TOOK THE SHELL</b> at 2:11 PM when Danita's hand gave out after 4.5 hours. She ran, and Kennerly and Arianna found her in Stairwell D. Mabry bagged the patient by hand (no electric ventilator). Lowery dissected with blunt instruments and silk, tying off a lumbar artery branch. The containment vessel from Rodman's Neck was stuck on the Triborough, so Burrell authorized a portable pot. <b>Cliffhanger at 6:22 PM: '...One.' Marc begins to lift.</b> Marc woke at 4:30 AM certain 'something goes wrong today.' Burrell's daughter Imani turns 8 on Tuesday and wants a pink Sidekick. 'Find yourself a Tuesday.'",
 "<b>ELXA IN LABOR</b> (39w2d): she came in to run the board 7-1 (Dr. Okoye had the flu). Clayton found her at 4 cm at 9:58 AM, her water broke at about noon, and she was at 6 cm at 12:09 PM and 8 cm at 2:39 PM. <b>Dr. Hampton was stopped at the perimeter</b>, per MA-005 ('or try to'), and coached by phone. <b>Elxa refused to push until she knew Russell was alive.</b> At 4:24 PM the NYPD ordered 4th floor west (L&D, above the old wing) evacuated by stairwell, with elevators down. <b>Elxa and Harmony are alone in Stairwell C</b> behind a lockdown-locked fire door; Elxa is crowning, Dr. Hampton is on speaker, and Harmony is delivering (her only prior delivery was 'Noelle,' a skills-lab mannequin, in September).",
 "<b>RUSSELL'S CRASH:</b> a livery cab hydroplaned through a red light at about 40 mph on Queens Boulevard at 11:52 AM and hit the driver's side (Harmony was on the phone with him). He had an acute right subdural hematoma with 9 mm shift and was herniating (GCS 10). <b>Esther got Graves through the perimeter</b> ('Tell him the patient is the Chief of Surgery's son-in-law'). Graves did a craniotomy with Esther in OR 5, the bone flap is banked, and an ICP monitor is in. Esther told Elxa at 4:07 PM. <b>Russell squeezed Esther's hand at 5:09 PM.</b>",
 "<b>Robert and Amond stayed in OR 2</b> to finish a CABG on bypass despite the evacuation order ('my turn to stay in a room I can't leave'). Amond told Robert that Marc was in OR 1 only after the patient was off pump. <b>Natasha told Robert about Widener Library and Alphonse</b>; now Robert and Elxa know. Natasha and Robert watched Marc through the scrub-room window, and Marc nodded to them. Robert remembered Marc sleeping on his chest as a baby. Amond: 'He's my day one... I'm going to tell him tonight.'",
 "<b>Outside the perimeter:</b> Camille (who drove from Augustin's in Bed-Stuy), Monty, Cedric, Lillian, Howard, Big Ray, LaShawn Plummer and her toddler, and <b>Victor Donohue</b>, who walked past a cop to put his hands on the barricade: 'My grandson is in there.' In CVICU, Raven promised Dash they would watch the game 'when' Marc walks out, and Glenda prayed."])
CONT.append(p("Knowledge Tracker (as of 6:22 PM, February 5, 2006)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Marc's hand is on the shell", "OR 1, Natasha, Robert, Amond, Big Ray, Monty, Victor (via Ray), Arianna, Kennerly, Danita"],
 ["Elxa delivering in Stairwell C", "Harmony, Elxa, Dr. Hampton (by phone), Camille (by delayed text); Natasha does NOT yet know"],
 ["Russell responsive", "Esther, Graves"],
 ["Natasha's Widener story", "Elxa, Robert"],
 ["Delphine Ware letter", "Unopened (Robert; Natasha has seen it)"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry (in progress)", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Status at 6:22 PM"],
 ["Reggie Plummer", "10/30/1967 (38)", "Penetrating injury, left flank; retained live 37mm HE projectile, damaged M54 fuze", "Laparotomy, blunt dissection (Lowery; Bullock holding the shell; Mabry hand-bagging)", "Shell free; removal begun"],
 ["Russell Jeffries", "4/3/1975 (30)", "Acute right SDH, 9 mm shift, herniating (T-bone MVC)", "Decompressive craniotomy, flap banked, ICP bolt (Graves; Smilley)", "Neuro ICU; squeezed a hand"],
 ["Dr. Elxa Bullock", "8/29/1977 (28)", "Term labor, 39w2d; SROM about noon", "Hartwell, then Divine (Hampton by phone)", "Crowning in Stairwell C"],
 ["CABG patient (OR 2)", "-", "Multivessel CAD", "CABG on bypass (R. Bullock; Baker)", "Off pump, in CVICU"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Det. Sgt. Isaac Burrell</b> (b. September 14, 1961), NYPD Bomb Squad, the counterpart of Dylan Young. <b>Danita Crews</b> (b. June 26, 1978), FDNY paramedic (counterpart of Hannah Davies), from Far Rockaway, mother of a 4-year-old. <b>Reggie</b> (b. October 30, 1967) and <b>LaShawn Plummer</b> (b. August 3, 1969).",
 "<b>Dr. Edwin Mabry</b> (Chief of Anesthesiology) and <b>Dr. Hampton</b> (first name Gwen, established here) make on-screen appearances (in MA-005)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["Super Bowl XL (Pittsburgh vs. Seattle) was played February 5, 2006 at Ford Field, Detroit, with a 6:28 PM ET kickoff. Aretha Franklin and Aaron Neville sang the anthem, and the Rolling Stones played at halftime. The NYPD Bomb Squad is based at the Rodman's Neck range in the Bronx and uses total containment vessels. "
 "Unexploded WWII-era ordnance is periodically found at U.S. construction and dredging sites. The Queens West ordnance discovery and the Queens Grace lockdown are fictional. The T-Mobile Sidekick was a popular phone in 2006.",
 "Medicine and EOD: old fuzes can be sensitive to shock, heat and possibly radio frequency, so radios, cautery and defibrillators are excluded. Anesthesia without electrical equipment means manual bag ventilation. An acute subdural with midline shift and a fixed or dilated pupil needs emergent decompressive craniotomy, often banking the bone flap. "
 "In active labor, cervical change and SROM proceed regardless of the mother's wishes. Precipitous delivery in a stairwell is managed by controlling the head, checking for a nuchal cord, and delivering the shoulders with gentle downward and then upward traction."])
