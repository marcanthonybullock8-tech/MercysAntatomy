import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E20_Bandage.pdf')
PARTS = [D + 's2e20_part1.txt', D + 's2e20_part2.txt', D + 's2e20_part3.txt']
EP = date(2006, 3, 13)
CODE = '2x20'
SEASON_LINE = 'Season 2, Episode 20'
TITLE = 'Bandage'
COUNTERPART = "Episode 2x20. The counterpart of <i>Grey's Anatomy</i> 2x20."
DATES = 'Monday, March 13, 2006, 6:02 AM through 11:58 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x19'
AGES_ON = 'Monday, March 13, 2006'

CAST = [
 ("Dr. Elxa Bullock", "Surgical Resident (on leave; evaluation day)", date(1977,8,29)), ("Russell Jeffries", "Elxa's husband (pre-cranioplasty)", date(1975,4,3)),
 ("Russell Harmon 'Tuck' Jeffries Jr.", "Elxa's son (5 weeks)", date(2006,2,5)), ("Dr. Amond Baker", "Surgical Intern (post-call; babysitter)", date(1979,2,10)),
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Bryce Kennerly", "Surgical Intern", date(1978,6,11)), ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)),
 ("Dr. Nnamdi Okoye", "Surgical Resident (PGY-4)", date(1974,10,1)), ("Harlan Moody (new)", "Patient: retired NYPD sergeant; retained bullet migrating into the RV", date(1944,11,11)),
 ("Geneva Moody (new)", "Harlan's wife", date(1947,5,25)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Antoinette 'Toni' Graham (new)", "Patient: distal radius fracture; domestic violence", date(1971,10,17)), ("Vaughn Graham (new)", "Toni's husband", date(1967,12,2)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Dr. Victor Donohue (V.O.)", "Marc's grandfather", date(1933,5,30)), ("Celia Montague, LCSW", "Hospital Social Worker", date(1966,5,6)),
 ("Dr. Eugene Pratt", "Surgical Program Director", date(1948,11,14)), ("Dr. Malcolm Sloan", "Chief of Plastic Surgery", date(1968,2,14)),
 ("Darius 'Dash' Duvall", "Patient: LVAD, day 122, infection resolving", date(1971,8,8)), ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)),
 ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)), ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)),
 ("Lillian Divine", "Harmony's mother; P.S. 118 cafeteria", date(1952,2,14)), ("Hattie 'Miss Hattie' Lomax", "Cafeteria", date(1945,3,3)),
 ("Nurse Kendra Wallace", "Surgical Floor Nurse", date(1980,5,30)), ("Det. Rochelle Ames (new)", "NYPD 103rd Precinct", date(1964,9,9)),
 ("Dr. Faith Danforth", "Veterinarian", date(1972,11,2)), ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)),
 ("Dr. Paulette Greenidge", "Couples therapist", date(1955,8,1)), ("Glenda Duvall", "Dash's mother", date(1947,12,12)),
 ("Howard Divine", "Harmony's father", date(1950,8,30)), ("Franklin Bassett, Esq.", "General Counsel", date(1958,10,28)),
 ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)), ("Mercy", "The House's pit bull (5.5 months)", date(2005,9,30)),
 ("Ruth Bader Ginsburg (new)", "Faith's three-legged ex-racing greyhound", date(2001,3,1)),
]
ALSO = ("<i>Also appearing: a CT tech, a radiologist, scrub and CVICU nurses, two security guards, a Safe Horizon night manager and lunch-rush cafeteria diners. "
        "Mentioned: Gordon Parks (d. March 7, 2006), Denise (Toni's sister, Mount Vernon), Augustin Toussaint (his Mardi Gras words), Dr. Leonard Baker (photo) and Kennerly's statement (in the safe).</i>")

MEDIA = [
 ("THE NEW YORK TIMES: \"GORDON PARKS, 93, DIES; PHOTOGRAPHER, FILMMAKER, PIONEER\"", "March 8, 2006",
  ["\"Gordon Parks, the photographer, filmmaker and composer who chronicled Black American life for Life magazine and directed 'Shaft,' died Tuesday at his home in Manhattan. He was 93...\""]),
 ("ASSOCIATED PRESS: \"MILOSEVIC FOUND DEAD IN HIS CELL\"", "Saturday, March 11, 2006",
  ["\"THE HAGUE, Netherlands (AP) -- Slobodan Milosevic, the former Yugoslav president on trial for war crimes, was found dead in his prison cell...\" Also from the week: the Dubai Ports World deal collapsed March 9, and on March 5 'Crash' won Best Picture and Three 6 Mafia won Best Original Song."]),
 ("QueensGraceConfidential (Blogger)", "Monday, March 13, 2006, 12:34 PM",
  ["<i>\"THE CAFETERIA KISS: DR. K & NURSE W GO PUBLIC (FINALLY). At 12:31 PM, at the CENTER TABLE, in the TIE. In September he told this cafeteria something that wasn't his. Today he told it something that was. Character development, people. "
   "Also: an intern sewed a purse string around a BULLET in a BEATING HEART this morning. And a certain post-call intern is reportedly babysitting a certain five-week-old in St. Albans. We hope he's okay. We hope the baby's okay. We're mostly worried about the intern.\"</i> Comments (3,904)."]),
 ("Photograph on Elxa and Russell's refrigerator (one-hour print, Linden Boulevard)", "Taken Monday, March 13, 2006, 1:07 PM",
  ["Dr. Amond Baker asleep on the sofa in a stained shirt, Tuck asleep face down on his chest, a cardiology journal open to the heart on the floor. Elxa wrote on the border: \"TRICUSPID VALVE. EVERY TIME.\""]),
 ("Contents of the General Counsel's safe (per Bassett)", "As of March 13, 2006, 9:41 PM",
  ["1) A manila envelope, red tape: the sworn statement of Dr. Bryce Kennerly (December 1, 2005). 2) A small yellowed envelope: 'Robert Bullock -- Personal' (from the Estate of Dr. Delphine A. Ware). Both SEALED. Opening the second requires Robert, Natasha and Bassett together."]),
 ("SMS, Motorola RAZR (Amond Baker to Marc Bullock)", "Monday, March 13, 2006, 11:58 AM",
  ["<b>Amond:</b> \"explosive event. calling harmonys mother. do not tell your father\"", "<b>Marc:</b> \"already told him\""]),
]

CONT = [p("Continuity Sheet: Episode 2x20", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>AMOND BABYSAT TUCK</b> (counterpart of Cristina babysitting for Bailey) from 8:29 AM to 1:07 PM, post-call after 40 minutes of sleep, with six pages of instructions. Tuck refused the bottle until Amond played Coltrane's 'My Favorite Things.' After 'an explosive event,' Amond called <b>Lillian Divine</b> at P.S. 118 ('A diaper's just a dressing with tabs... two fingers' room, like a blood pressure cuff'). He read the heart anatomy, and both fell asleep 'at the tricuspid valve.' <b>Elxa photographed them</b>; the print is on her refrigerator. Robert admitted he has played Coltrane at Amond on purpose since August: 'It builds character.'",
 "<b>ELXA NAMED 2007-08 ADMINISTRATIVE CHIEF RESIDENT</b>, a year early and a first at QGH, by Dr. Pratt, cosigned by Lowery and Graves. Natasha had recused herself from Elxa's file on November 9 and <b>did not know</b>. Elxa: 'Nobody can ever say a Donohue handed it to me.' Natasha: 'You took it. The way you took a stairwell.' Her record: 419 cases, in-service technical scores in the 96th percentile, and Gloria's evaluations 'terrifying,' 'fair,' 'best in the building.'",
 "<b>MARC AND FAITH:</b> first date Saturday, March 4, at Taverna Kyclades (she ordered in Greek, sent back a corked wine, then a midnight Vespa ride over the Pulaski Bridge and goodnight on the stoop). Since then he's been humming 'Isn't She Lovely.' <b>Second date March 13</b> at her apartment above the clinic: chili, and her three-legged ex-racing greyhound <b>Ruth Bader Ginsburg</b> (Palm Beach; Faith drove 1,100 miles for her), who bonded with Mercy. Marc told her about the 'white' startle and Mondays with Bynum. Faith: 'You told me where it hurts... Eat your chili.' <b>First kiss.</b> <b>Esther watched them leave on the Vespa</b> from the lobby, and Big Ray noticed.",
 "<b>ESTHER AND CLAYTON:</b> at his March 2 lunch with Malcolm (Red Sox for 40 minutes, Esther for 5, Clayton paid), Clayton said he and Esther are 'both just holding very still so nothing moves.' Malcolm told Esther. <b>Esther: 'We're a bandage. Over a bullet hole.'</b> She is not leaving 'tonight,' but she wants to open it 'even if it's the end of us.' Clayton: 'Then let's open it. Properly... Boston. Malcolm. Marc... Everything.' <b>The marriage is in genuine crisis</b>; it is honest and unresolved.",
 "<b>THE SEALED LETTER</b> was placed on Greenidge's coffee table in session 3 and not opened. Natasha: 'I want to be strong enough to read it and still be sober.' <b>It now sits in Bassett's safe beside Kennerly's sworn statement</b>, and opening it requires Robert, Natasha and Bassett together. Natasha briefly took Robert's hand. <b>Victor and Natasha agreed the heir revelation will come in June 2006</b>, when the intern year ends. Victor photographed for Life by Gordon Parks in 1968: 'Start smiling like you built it.'",
 "<b>Harlan Moody</b>, a retired NYPD sergeant shot Christmas Eve 1988 with a .38 left in his chest wall at Jamaica Hospital as 'safer,' had the bullet migrate into the RV free wall and erode it, causing tamponade in CT. <b>Raven placed the pledgeted purse-string sutures and tied down</b> as Robert lifted it out of the beating heart. Robert: 'All it needed was somebody to stop leaving it alone.' Geneva: 'Thank you for not leaving it alone.' The bullet will be returned to him.",
 "<b>Harmony and Toni Graham:</b> she spotted fingertip bruises ('My mother taught me to look at sleeves'). <b>Vaughn Graham grabbed Harmony's arm in the ER</b>; she called it out loudly, Marc intervened and Big Ray removed him (on camera). Toni gave a statement to Det. Rochelle Ames: 'My husband hits me... I thought it would be louder.' Harmony took her to a Safe Horizon shelter, and she goes to her sister Denise in Mount Vernon this weekend. <b>Augustin's Mardi Gras words</b> (February 28): 'I cannot bless it... But I will not lose you over it. And the girl is welcome at my table.' That is tolerance, not acceptance, consistent with MA-005. Camille: 'It's a bandage.'",
 "<b>Dash</b> (day 122, afebrile, driveline healing, doing two-pound curls): 'When I've got a heart, then I'll ask [you to choose].' Arianna brought crackers and watched a Panthers highlight show with him. Glenda (born in Harlem, per this episode) baked pound cake 'for all three of you.' <b>Kennerly and Kendra kissed publicly in the cafeteria</b> (third date). Monty knows who writes QueensGraceConfidential and will 'take it to my grave.' Russell's cranioplasty is Monday, March 20. Howard's cough worsened; the June CT stands."])
CONT.append(p("Knowledge Tracker (as of March 13, 2006)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Marc and Faith dating", "The housemates, Esther, Big Ray, the blog"],
 ["Esther's 'bandage' talk with Clayton", "Esther, Clayton (Malcolm partially)"],
 ["Elxa chief resident 2007-08", "Elxa, Natasha, Russell, Pratt, Lowery, Graves"],
 ["The sealed letter (in the safe)", "Robert, Natasha, Bassett, Dr. Greenidge; contents unknown to all"],
 ["Heir revelation set for June 2006", "Victor, Natasha"],
 ["Who writes QueensGraceConfidential", "Monty (and the author)"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Harlan Moody", "11/11/1944 (61)", "Retained .38 bullet (1988) migrated into the RV free wall; pericardial effusion and tamponade", "Emergent pericardiocentesis; sternotomy, pledgeted purse string, bullet removal (R. Bullock; Ellison; Kennerly)", "Stable in CVICU"],
 ["Antoinette 'Toni' Graham", "10/17/1971 (34)", "Distal radius fracture; IPV injuries (fingertip bruising, facial contusion)", "Splint, then cast (Lowery; Divine); social work (Montague)", "Statement to NYPD; Safe Horizon"],
 ["Darius 'Dash' Duvall", "8/8/1971 (34)", "LVAD driveline infection, resolving", "IV antibiotics", "Afebrile; waiting"],
 ["Hysterectomy patient", "-", "Gynecologic malignancy", "Radical hysterectomy (Donohue)", "Stable"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Harlan</b> (b. November 11, 1944) and <b>Geneva Moody</b> (b. May 25, 1947). <b>Antoinette 'Toni' Graham</b> (b. October 17, 1971), secretary at P.S. 40, and <b>Vaughn Graham</b> (b. December 2, 1967). <b>Det. Rochelle Ames</b> (b. September 9, 1964), 103rd Precinct.",
 "<b>Ruth Bader Ginsburg</b>, Faith's greyhound (about 5 years old)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["Gordon Parks died March 7, 2006, at 93. Slobodan Milosevic died in his cell at The Hague on March 11, 2006. The Dubai Ports World deal collapsed March 9, 2006, and at the March 5, 2006 Oscars 'Crash' won Best Picture and Three 6 Mafia won Best Original Song. Safe Horizon runs domestic violence shelters in New York City. Palm Beach Kennel Club was a Florida greyhound track.",
 "Medicine: retained bullets left in place for safety can migrate years later, including into the heart, causing pericardial effusion, tamponade or embolization. Removal from the beating RV uses pledgeted purse-string or mattress sutures placed before extraction. A distal radius fracture plus patterned fingertip bruising and injuries of different ages should prompt intimate partner violence screening, done privately, away from the partner."])
