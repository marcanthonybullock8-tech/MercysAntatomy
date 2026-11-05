import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E05_Choose.pdf')
PARTS = [D + 's2e5_part1.txt', D + 's2e5_part2.txt', D + 's2e5_part3.txt']
EP = date(2005, 10, 11)
CODE = '2x05'
SEASON_LINE = 'Season 2, Episode 5'
TITLE = 'Choose'
COUNTERPART = "Episode 2x05. The counterpart of <i>Grey's Anatomy</i> 2x05."
DATES = 'Tuesday, October 11, 2005, 5:31 AM through 11:52 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x04'
AGES_ON = 'Tuesday, October 11, 2005'

CAST = [
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Harriet Baker-Fenwick", "Amond's mother", date(1952,10,5)),
 ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)), ("Dr. Elxa Bullock", "Surgical Resident (23 weeks pregnant)", date(1977,8,29)),
 ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)), ("Nikki Chambers (new)", "Patient: CIPA, open forearm fracture", date(1998,8,2)),
 ("LaTonya Chambers (new)", "Nikki's mother; school bus driver", date(1974,1,15)), ("Dr. Isaiah Crump", "Chief of Pediatric Surgery", date(1944,3,11)),
 ("Dr. Camille Toussaint", "Orthopedic Resident (PGY-3)", date(1976,7,21)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Rev. Isaac Ashworth (new)", "QGH trustee; pastor, Greater Bethel Baptist", date(1937,3,30)), ("Dorian Batiste", "Bridge Fund patient", date(1997,2,15)),
 ("Dr. Clayton Hartwell", "Fetal Surgeon; Esther's husband", date(1971,3,3)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Dr. Amond Baker", "Surgical Intern (on medical leave)", date(1979,2,10)), ("Dr. Solomon Fenwick", "Amond's stepfather", date(1948,3,21)),
 ("Dr. Leland Graves", "Chief of Neurosurgery; hearing chair", date(1953,4,18)), ("Dr. Marlene Fisk", "Director, Employee Health; hearing panel", date(1947,10,3)),
 ("Franklin Bassett, Esq.", "General Counsel; hearing panel", date(1958,10,28)), ("Dr. Bryce Kennerly", "Surgical Intern (hearing respondent)", date(1978,6,11)),
 ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Booker Haines", "Clinic patient: post-MVD", date(1941,5,16)), ("Mae Haines", "Booker's wife", date(1943,2,8)),
 ("Odile Lemieux", "Curtis's mother", date(1936,3,19)), ("Curtis Lemieux", "Former patient: heart transplant", date(1961,4,9)),
 ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)), ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson (43 since Oct 10)", date(1962,10,10)),
 ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)), ("Russell Jeffries", "Elxa's husband", date(1975,4,3)),
]
ALSO = ("<i>Also appearing: Rochelle Batiste, Bridge Fund families, a union representative, an OR team, Kendra Wallace, Deb Lyons, Tee Rollins, Andre Fontaine and Monty's party guests. "
        "Mentioned: Victor Donohue, Judge Kittredge, Dr. Greenidge, Malcolm Sloan, Simone Pettigrew (Collegiate, 1990s), Yvonne (Monty, 1987), and a CIPA family network run by a mother in Ohio.</i>")

MEDIA = [
 ("ASSOCIATED PRESS: \"ANGELS ELIMINATE YANKEES IN GAME 5\"", "Monday, October 10, 2005",
  ["\"ANAHEIM, Calif. (AP) -- The Los Angeles Angels beat the New York Yankees 5-3 on Monday night to win their American League division series in five games, ending another Yankees season without a championship...\""]),
 ("QueensGraceConfidential (Blogger)", "Tuesday, October 11, 2005, 6:02 PM",
  ["<i>\"It's official. Day 30. Boston is staying with Boston. Our roof spy (we have a roof spy now) says Dr. X went up at 4:00, said something nobody could hear, and came down at 4:06 with the face of a man who'd asked a question and gotten an answer. "
   "We're not making jokes tonight. We're just saying: he asked. Most people never do. Also, the Kennerly hearing: probation. Chief of Medicine Whitlow testified FOR him, which is... a choice.\"</i> Comments (881)."]),
 ("GME Committee: hearing summary (Bassett)", "Tuesday, October 11, 2005",
  ["\"RE: Dr. Bryce Kennerly (PGY-1). Finding: conduct unbecoming and harassment of a colleague (distribution of approximately 300 copies of a personal image, September 2005). Sanction: probation through June 30, 2006; mandatory professionalism training; letter to file. "
   "Note: Dr. H. Whitlow addressed the committee unsolicited. Dr. L. Graves, chair, so noted.\""]),
 ("SMS, Motorola RAZR (Esther Smilley to Marc-Anthony Bullock)", "Tuesday, October 11, 2005, 5:31 AM",
  ["<b>Esther:</b> \"roof at 4? day 30. i want you to hear it from me first. like i promised.\""]),
 ("SMS, Motorola RAZR (Marc-Anthony Bullock to Natasha Donohue)", "Tuesday, October 11, 2005, 4:47 PM",
  ["<b>Marc:</b> \"kennerly knows collegiate. he's working for whitlow.\"", "<b>Natasha:</b> \"My office. Now.\""]),
 ("Collegiate School yearbook, 1997 (senior page)", "1997",
  ["\"MARC-ANTHONY BULLOCK. Varsity Basketball (Capt.). Debate. Model U.N. 'Bullock is a common name.' -- Princeton? Howard. Definitely Howard.\""]),
 ("SMS, Motorola RAZR (Raven Ellison to Harmony Divine)", "Tuesday, October 11, 2005, 6:14 PM",
  ["<b>Raven:</b> \"it stopped raining\"", "<b>Raven:</b> \"she asked again\"", "<b>Raven:</b> \"i said yes\"", "<b>Harmony:</b> \"!!!!!!!!!!!!!\"", "<b>Harmony:</b> \"i said yes too. friday. camille\"", "<b>Raven:</b> \"HARMONY DIVINE\""]),
]

CONT = [p("Continuity Sheet: Episode 2x05", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>Day 30 (Tuesday, October 11, 2005): Esther chooses to stay married to Clayton</b> and make a real try. This is the counterpart of Derek choosing Addison. She told Marc first on the roof at 4:00 PM, as promised, and told him she slept with Clayton on October 8. Her conditions for Clayton: weekly sessions with Dr. Greenidge, no secrets ('If Malcolm calls you, I know that day'), she stays 'Dr. Smilley' at work, and she stays on the boat until she's ready. She now wears the ring on her finger and withdrew her Policy 4.12 form.",
 "<b>Marc's 'Choose me' speech</b> on the roof is the counterpart of Meredith's 'pick me, choose me, love me.' Its key lines: 'not yet is sometimes the polite word for no' (Victor), 'the one who told you the truth sober,' and 'Choose me.' Marc: 'Be happy, Es. Or come tell me if you're not.' To Clayton: 'Be good to her... Then you and I won't ever have a problem.' To Monty: 'I choose the guy who asked.'",
 "<b>Harmony said yes to Camille</b>: dinner Friday, October 14, 7:30 PM, at a Creole restaurant in Fort Greene ('wear something you can dance in'). 'I thought I'd start with me.' <b>Raven and Arianna's first date</b> was October 11 at the Greek restaurant under Arianna's apartment (she lives above a Greek bakery on 30th Avenue, Astoria). They came home holding hands, and Marc, Amond and Harmony know.",
 "<b>Whitlow has Marc's 1997 Collegiate yearbook</b> ('Bullock is a common name,' Basketball captain), from his godson's older brother. Kennerly, with a cousin at Dalton, confronted Marc: 'Not at Collegiate it isn't.' Collegiate tuition in 1997 was $17,900. <b>Whitlow has a lunch with Judge Kittredge</b> at the Harvard Club, Monday, October 17, 1:00 PM: 'a family photograph, of sorts.' Bernie saw the yearbook on his desk. Robert: 'Let him bring that to the board.'",
 "<b>Kennerly hearing outcome:</b> probation through June 30, 2006, professionalism training and a letter to file. Whitlow testified unsolicited, and Graves noted it on the record. Esther compared the copies to her father's crime-scene photos in the 1987 Boston Globe.",
 "<b>Rev. Isaac Ashworth</b> (an undecided trustee) toured the Bridge Fund pharmacy: 312 children served since September 8. Dorian asked him to thank God for the dog. 'Horace Whitlow asked me yesterday. He didn't bring a little boy.'",
 "<b>Harriet and Solomon returned to Los Angeles</b> on October 11. Amond agreed to call on Sundays. Harriet: 'Your father would have been so proud of you, it would have been unbearable.' Amond thanked Solomon for the photo. Robert has a copy of Harriet's list. Amond watched a mitral repair from the gallery against orders, and Big Ray told Robert.",
 "<b>Curtis Lemieux</b> was discharged October 10. He and Odile played trombone and cooked red beans at 49th Avenue ('Just a Closer Walk with Thee').",
 "<b>Monty's 43rd birthday</b> party was October 11 at Monty's. Marc gave the toast. <b>New canon:</b> Monty never asked out Yvonne in 1987; she married a Bay Ridge firefighter. Gloria has had two husbands. Elxa got engaged to Russell at a Popeyes on Merrick Boulevard. Marc took Simone Pettigrew to the Collegiate spring formal in 10th grade.",
 "<b>Booker Haines</b> is pain-free 8 days after surgery and shaved both sides of his face for the first time since 1999. Mae kissed his right cheek."])
CONT.append(p("Knowledge Tracker (as of October 11, 2005)", H2))
CONT.append(tbl([["Secret", "Who knows", "New pressure"],
 ["Marc is Natasha and Robert's son", "Family, Bernie, Graves, Gloria, Mrs. Truitt, Amond, Big Ray, Arianna, Esther", "<b>Whitlow has the yearbook</b> and is meeting Kittredge on October 17; Kennerly knows about Collegiate; Clayton, Raven and Harmony suspect"],
 ["Marc and Victor", "Same", "Raven and Harmony saw Victor on October 8"],
 ["Esther and Clayton reconciling", "Public (the blog)", "-"],
 ["Raven and Arianna dating", "Marc, Amond, Harmony", "-"],
 ["Harmony and Camille's date", "Raven, Marc, Amond", "-"]],
 [1.8*inch, 2.5*inch, 2.1*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Nikki Chambers", "8/2/1998 (7)", "Congenital insensitivity to pain with anhidrosis (CIPA); open radius and ulna fracture about 18 h old; hyperthermia 105.4; febrile seizure", "Active cooling, lorazepam; I&D, radial ORIF, ulnar IM rod (Camille; Crump; Harmony, Marc)", "Afebrile; HSS follow-up in November; CIPA family network"],
 ["Mitral patient", "-", "P2 prolapse", "Triangular resection repair (Robert)", "Uncomplicated"],
 ["Booker Haines", "5/16/1941 (64)", "Post-MVD, day 8", "Clinic (Esther)", "Pain-free"]],
 [1.05*inch, 0.85*inch, 1.9*inch, 1.65*inch, 1.0*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Nikki Chambers</b> (b. August 2, 1998) and <b>LaTonya Chambers</b> (b. January 15, 1974), a school bus driver.",
 "<b>Rev. Isaac Ashworth</b> (b. March 30, 1937), QGH trustee and pastor of Greater Bethel Baptist Church, St. Albans (a swing vote)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["The Angels eliminated the Yankees 5-3 in ALDS Game 5 on October 10, 2005. The October 2005 rains eased around October 11-12. Collegiate School is on the Upper West Side, and Dalton is on the Upper East Side.",
 "Medicine: CIPA (HSAN type IV, an NTRK1 mutation) causes absent pain and anhidrosis, with hyperthermia, self-mutilation (tongue injuries in infancy), unnoticed fractures and Charcot joints. Patients still need general anesthesia because of autonomic responses. "
 "An open fracture needs urgent irrigation and debridement, antibiotics and fixation. Fever in anhidrosis needs external cooling, since antipyretics are of limited help. Hospital for Special Surgery is in Manhattan."])
