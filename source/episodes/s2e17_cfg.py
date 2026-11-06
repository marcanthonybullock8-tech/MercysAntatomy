import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E17_Hold_On.pdf')
PARTS = [D + 's2e17_part1.txt', D + 's2e17_part2.txt', D + 's2e17_part3.txt']
EP = date(2006, 2, 5)
CODE = '2x17'
SEASON_LINE = 'Season 2, Episode 17 (Part Two of Two)'
TITLE = 'Hold On'
COUNTERPART = "Episode 2x17. The counterpart of <i>Grey's Anatomy</i> 2x17 (Part Two of the Code Black two-parter)."
DATES = 'Sunday, February 5, 2006 (Super Bowl XL), 6:22 PM through 11:59 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x16. Continues directly from 2x16.'
AGES_ON = 'Sunday, February 5, 2006'

CAST = [
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Det. Sgt. Isaac Burrell", "NYPD Bomb Squad (killed in the line of duty, 6:31 PM)", date(1961,9,14)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Dr. Edwin Mabry", "Chief of Anesthesiology", date(1957,6,24)),
 ("Dr. Elxa Bullock", "Surgical Resident (delivered 6:44 PM)", date(1977,8,29)), ("Dr. Harmony Divine", "Surgical Intern (delivered Tuck)", date(1979,6,19)),
 ("Dr. Hampton (V.O., then on-screen)", "Elxa's obstetrician", date(1950,4,20)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)), ("Darius 'Dash' Duvall", "Patient: Status 1A, day 86", date(1971,8,8)),
 ("Glenda Duvall", "Dash's mother", date(1947,12,12)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)),
 ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)), ("Dr. Victor Donohue", "Marc's grandfather", date(1933,5,30)),
 ("Lillian Divine", "Harmony's mother", date(1952,2,14)), ("Howard Divine", "Harmony's father", date(1950,8,30)),
 ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)), ("LaShawn Plummer", "Reggie's wife", date(1969,8,3)),
 ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)), ("Cedric Hall", "Architect; Monty's partner", date(1965,1,22)),
 ("Nurse Kendra Wallace", "Surgical Floor Nurse", date(1980,5,30)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Captain Neville Ashford (new)", "Commanding Officer, NYPD Bomb Squad", date(1949,12,8)), ("Danita Crews", "FDNY paramedic", date(1978,6,26)),
 ("Dr. Bryce Kennerly", "Surgical Intern", date(1978,6,11)), ("Hattie 'Miss Hattie' Lomax", "Cafeteria", date(1945,3,3)),
 ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)), ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)),
 ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)), ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)),
 ("Russell Jeffries", "Elxa's husband (post-craniectomy)", date(1975,4,3)), ("Angela Burrell (new)", "Isaac's widow", date(1963,7,22)),
 ("Imani Burrell (new)", "Isaac's daughter (turns 8 on February 7)", date(1998,2,7)), ("Reginald 'Reggie' Plummer", "Patient: shell removed", date(1967,10,30)),
 ("Dr. Grace Bullock (V.O.)", "Harvard Medical School student", date(1981,4,12)), ("Russell Harmon 'Tuck' Jeffries Jr. (born)", "Elxa and Russell's son", date(2006,2,5)),
 ("Mercy", "The House's pit bull puppy", date(2005,9,30)),
]
ALSO = ("<i>Also appearing: NYPD Bomb Squad officers and uniformed police (the honor lines), a NICU transport team, hospital staff along the loading-dock path, an old Monty's regular, a TV reporter, and Reggie and LaShawn's toddler son. "
        "On TV: Super Bowl XL (Willie Parker's 75-yard touchdown run; Steelers 21, Seahawks 10).</i>")

MEDIA = [
 ("NEW YORK DAILY NEWS (front page): \"HERO\"", "Monday, February 6, 2006",
  ["\"Bomb Squad Sgt. Isaac Burrell, 44, a Marine veteran and 17-year NYPD officer, was killed Sunday evening when a World War II-era artillery shell he had just carried out of an operating room exploded in a service corridor at Queens Grace Hospital. Doctors had removed the shell from a construction worker, who survived... Commissioner Kelly called Burrell 'the bravest man in New York tonight.'\" (A fictional event.)"]),
 ("ASSOCIATED PRESS: \"STEELERS WIN FIFTH SUPER BOWL, 21-10\"", "Sunday, February 5, 2006",
  ["\"DETROIT (AP) -- Willie Parker broke the longest run in Super Bowl history, a 75-yard touchdown on the second play of the second half, and Antwaan Randle El threw a 43-yard touchdown pass to MVP Hines Ward as Pittsburgh beat Seattle 21-10...\""]),
 ("QueensGraceConfidential (Blogger)", "Monday, February 6, 2006, 12:41 AM",
  ["<i>\"WE LOST ONE OF THE GOOD ONES. Sergeant Isaac Burrell carried that thing out of OR 1 so nobody else had to. The staff lined the loading dock for him at 7:24 PM. If you were there, you know. If you weren't, ask somebody who was. "
   "And at 6:44 PM, thirteen minutes after the blast, a baby boy was born in Stairwell C, caught by an intern with her shoelaces. His middle name is HARMON. That's all we have tonight. Hold on to somebody.\"</i> Comments (6,902)."]),
 ("Bassinet card, QGH Newborn Nursery", "Sunday, February 5, 2006",
  ["\"JEFFRIES, RUSSELL HARMON JR. ('TUCK'). 7 LB 11 OZ. 20.5 IN. 6:44 PM. STAIRWELL C. DELIVERED BY: DR. H. DIVINE.\" (A small football is drawn in the corner.)"]),
 ("Engraving inside Victor Donohue's pocket watch (now Marc's)", "Given 1957; passed to Marc February 5, 2006",
  ["\"V.D. -- 1957 -- SPEND IT RIGHT.\""]),
 ("Last radio transmission, Sgt. Isaac Burrell (per Capt. Ashford)", "Sunday, February 5, 2006, about 6:25 PM",
  ["\"The doctor's clear. Starting my walk.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x17 (Part Two)", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>THE SHELL:</b> at 6:22 PM Marc lifted the 37mm projectile out of Reggie Plummer and placed it in Burrell's hands. Burrell sealed it in the portable pot ('Find yourself a Tuesday, son') and walked it down the old-wing service corridor toward the loading dock. <b>At 6:31 PM the pot failed and the shell detonated about 20 feet from the dock. Det. Sgt. Isaac Burrell was killed.</b> His last radio report: 'The doctor's clear. Starting my walk.' Marc was thrown under the scrub sink. He has a cut over his left eyebrow (Steri-Strips by Gloria), <b>intact eardrums and a temporary threshold shift</b> (hearing returning; tinnitus may last a week). No permanent injury. Reggie survived (Lowery and Mabry closed) and was extubated by 9:41 PM. He wants to 'name something after' Burrell.",
 "<b>TUCK IS BORN</b> per MA-005: <b>Russell Harmon 'Tuck' Jeffries Jr., 6:44 PM, February 5, 2006, Stairwell C, delivered by Harmony Divine</b>, 13 minutes after the blast (which shook the stairwell mid-push). There was a nuchal cord, reduced over the head by Harmony with Dr. Hampton coaching by phone. The cord was tied with Harmony's shoelaces and cut with bandage scissors. He weighed 7 lb 11 oz, measured 20.5 in, and had Apgars of 8 and 9. <b>Nickname origin:</b> Harmony swaddled him in her white coat ('tucked in like a burrito'). <b>Middle name 'Harmon' after Harmony</b>, chosen by Elxa on the landing. Natasha first held him on the stairs at 7:33 PM, when the lockdown lifted, and wept for the first time that day. Robert: 'He has my mother's chin.' This was Dr. Hampton's first delivery by phone in 28 years.",
 "<b>Russell</b> woke in the Neuro ICU, saw his son and lifted a thumb when Elxa told him the Steelers were winning. His ICP spiked to 28 at the blast and Esther controlled it. He is still intubated, with the bone flap banked.",
 "<b>The honor line</b> at 7:24 PM: bomb squad, police, then hospital staff (Big Ray, Mabry, Lowery, Miss Hattie, nurses) lined the loading-dock path as Burrell's flag-draped body was carried out. Marc laid his right hand, the hand that held the shell, over his heart. <b>Capt. Neville Ashford</b> (56) commands the squad; Burrell served under him for 11 years. <b>Marc told Angela and Imani Burrell</b> in the chapel about the pink Sidekick and Tuesday: 'He was walking toward Tuesday.' Angela: 'Thank you for holding it, so he only had to carry it a little way.' Monty's toasted Burrell at the final whistle (Steelers 21-10).",
 "<b>VICTOR GAVE MARC HIS FATHER'S GOLD POCKET WATCH</b> in the lobby (engraved 'V.D. -- 1957 -- SPEND IT RIGHT'), the watch V.J. asked for in 1985 and was refused: 'When you've earned it.' <b>Victor wants to move up the heir revelation</b> ('We said spring... I don't want to wait'). Natasha: 'Not this week. But soon.' The heir designation is still secret from Marc's friends.",
 "<b>Robert promised Natasha he'll tell her 'about Chicago, about 1981' THIS WEEK.</b> Natasha: 'I know there's something... Since the Chicago postmark. Maybe since 1982... when her husband comes home from a conference and holds her too tight.' Per MA-005 the Mariah reveal (the daughter) stays in Season 11. What Robert confesses next is the affair only, and he still hasn't opened the letter. <b>Amond: 'You're not my day one, Marc. You're my brother.'</b>",
 "<b>Harmony and Camille kissed publicly in the ambulance bay.</b> Howard: 'They named a baby after our baby.' Howard caught newborn Harmony left-handed 'like a fly ball.' <b>Whitlow brought flowers</b> to Natasha: 'I'm glad your son is alive... Whatever else is true between us.' <b>Esther held Marc in the shower; Clayton saw and left a coffee.</b> Clayton: 'I'm not going to make that into an October... I'm glad he's alive.' <b>Raven to Arianna, in honest order:</b> 'Marc first. Then you. Then him.' Arianna: 'Then I can work with it.' Raven watched Willie Parker's 75-yard run with Dash and Glenda as promised. Kennerly sat with Danita, and Marc told her: 'That's a relay.' Lowery broke down with Gloria. Big Ray fed and walked Mercy and brought her to Marc on the roof. Grace called from the Harvard library: 'Is our family insane?'"])
CONT.append(p("Knowledge Tracker (as of 11:59 PM, February 5, 2006)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Tuck's name, middle name and nickname origin", "Everyone (the bassinet card, the blog)"],
 ["Robert will confess 'Chicago, 1981' this week", "Robert, Natasha"],
 ["Victor wants to reveal the heir designation sooner", "Victor, Natasha"],
 ["The watch (Victor's father's)", "Marc, Victor, Natasha (and V.J.'s 1985 refusal)"],
 ["Esther and Marc in the shower", "Esther, Marc, Clayton"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Reggie Plummer", "10/30/1967 (38)", "Retained live 37mm projectile, left retroperitoneum", "Shell removed by hand (Bullock), handed to EOD; closure (Lowery; Mabry)", "Extubated; recovering"],
 ["Tuck Jeffries", "2/5/2006", "Term newborn; nuchal cord x1", "Stairwell delivery (Divine; Hampton by phone)", "Apgars 8/9; healthy"],
 ["Dr. Elxa Bullock", "8/29/1977 (28)", "SVD at 39w2d in a stairwell", "(Divine; Hartwell and Hampton after 7:33 PM)", "Well"],
 ["Russell Jeffries", "4/3/1975 (30)", "Post-craniectomy for acute SDH; ICP spike at the blast", "Propofol (Smilley; Graves)", "ICP 12; following commands"],
 ["Dr. Marc Bullock", "1/5/1979 (27)", "Blast exposure: left brow laceration, temporary threshold shift", "Steri-Strips; otoscopy (Pettiford)", "Hearing returning"],
 ["Det. Sgt. Isaac Burrell", "9/14/1961 (44)", "Blast injury", "-", "Killed in the line of duty, 6:31 PM"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Captain Neville Ashford</b> (b. December 8, 1949), NYPD Bomb Squad. <b>Angela Burrell</b> (b. July 22, 1963) and <b>Imani Burrell</b> (b. February 7, 1998). <b>Russell Harmon 'Tuck' Jeffries Jr.</b> (b. February 5, 2006), per MA-005."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["Super Bowl XL, February 5, 2006, Ford Field, Detroit: Pittsburgh 21, Seattle 10. Willie Parker's 75-yard run on the second play of the second half was the longest run in Super Bowl history at the time, and Hines Ward was MVP after a 43-yard touchdown pass from Antwaan Randle El. Ray Kelly was NYPD Commissioner in 2006. "
 "The Bomb Squad honor line, the shell and Sgt. Burrell are fictional.",
 "Medicine: blast overpressure can cause temporary threshold shift and tinnitus even with intact tympanic membranes, usually resolving within days. A nuchal cord found at delivery is reduced over the head if loose. With no clamp available, clean ties (e.g., shoelaces) are an accepted field improvisation for cord ligation. "
 "Elevated ICP after craniectomy is managed with sedation, osmotherapy and drainage. Newborn Apgars are scored at 1 and 5 minutes."])
