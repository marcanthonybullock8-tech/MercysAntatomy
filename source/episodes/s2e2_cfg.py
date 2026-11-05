from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

import os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E02_Say_When.pdf')
PARTS = [D + 's2e2_part1.txt', D + 's2e2_part2.txt', D + 's2e2_part3.txt']
EP = date(2005, 10, 3)
CODE = '2x02'
SEASON_LINE = 'Season 2, Episode 2'
TITLE = 'Say When'
COUNTERPART = "Episode 2x02. The counterpart of <i>Grey's Anatomy</i> 2x02."
DATES = 'Monday, October 3, 2005, 5:12 AM through 11:52 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x01'
AGES_ON = 'Monday, October 3, 2005'

CAST = [
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)), ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)),
 ("Dr. Elxa Bullock", "Surgical Resident (21.5 weeks pregnant)", date(1977,8,29)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)), ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)),
 ("Dr. Isaiah Crump", "Chief of Pediatric Surgery", date(1944,3,11)), ("Franklin Bassett, Esq.", "General Counsel", date(1958,10,28)),
 ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)),
 ("Dr. Horace Whitlow (on-screen debut)", "Chief of Medicine", date(1949,9,19)), ("Dr. Clayton Hartwell", "Fetal Surgeon; Esther's husband", date(1971,3,3)),
 ("Curtis Lemieux", "Patient: post-transplant rejection", date(1961,4,9)), ("Lt. Tanisha 'Tee' Rollins", "FDNY EMS Lieutenant", date(1976,8,16)),
 ("Tyrell 'Bird' Pickens (new)", "Patient: GSW, liver", date(1989,6,7)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Booker Haines (new)", "Patient: trigeminal neuralgia", date(1941,5,16)), ("Mae Haines (new)", "Booker's wife", date(1943,2,8)),
 ("Lula Pickens (new)", "Tyrell's grandmother; MTA station agent", date(1941,2,11)), ("Kordell Pickens (new)", "Tyrell's brother", date(1994,3,2)),
 ("Nadia Ellerbe (new)", "Patient: fetal SCT, mirror syndrome", date(1977,4,25)), ("Malik Ellerbe (new)", "Nadia's husband; Con Ed lineman", date(1975,1,30)),
 ("Odile Lemieux", "Curtis's mother", date(1936,3,19)), ("Mrs. Evangeline Truitt", "QGH board member", date(1934,12,1)),
 ("Det. Lawrence Fyffe (new)", "NYPD 113th Precinct", date(1966,11,21)), ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)),
 ("Dr. Paulette Greenidge (new)", "Couples therapist, Brooklyn Heights", date(1955,8,1)), ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)),
 ("Daniella (new)", "Fordham Law student at Monty's", date(1978,7,9)), ("Russell Jeffries", "Elxa's husband", date(1975,4,3)),
]
ALSO = ("<i>Also appearing: FDNY paramedic Andre Fontaine, a circulating nurse, an L&D nurse, a fetal cardiologist, two anesthesiologists, "
        "the NICU team, a scrub nurse and Monty's patrons. Mentioned: Barry Marshall and Robin Warren (Nobel laureates), Rev. Ashworth, Judge Kittredge, "
        "Aunt Bernadine (Rocky Mount, NC), Ahmad Cummings, Malcolm Sloan and Lionel Lemieux.</i>")

MEDIA = [
 ("NOBELPRIZE.ORG: The Nobel Prize in Physiology or Medicine 2005", "Monday, October 3, 2005",
  ["\"The Nobel Assembly at Karolinska Institutet has today decided to award the Nobel Prize in Physiology or Medicine for 2005 jointly to Barry J. Marshall and J. Robin Warren "
   "for their discovery of the bacterium Helicobacter pylori and its role in gastritis and peptic ulcer disease.\""]),
 ("ASSOCIATED PRESS: \"BUSH NOMINATES WHITE HOUSE COUNSEL MIERS TO HIGH COURT\"", "Monday, October 3, 2005",
  ["\"WASHINGTON (AP) -- President Bush on Monday nominated White House counsel Harriet Miers, a longtime confidante who has never been a judge, to replace retiring Justice Sandra Day O'Connor on the Supreme Court...\""]),
 ("NY1: on-screen chyron", "Monday, October 3, 2005, 8:15 AM",
  ["\"SOUTH JAMAICA: TEEN SHOT NEAR BAISLEY PARK HOUSES; THIRD TIME HE HAS BEEN WOUNDED, POLICE SAY\""]),
 ("QueensGraceConfidential (Blogger)", "Monday, October 3, 2005, 4:30 PM",
  ["<i>\"FIRST IN QUEENS: an OPEN FETAL SURGERY at Grace today. They took a 26-week baby halfway out of his mother, removed a tumor the size of a softball and PUT HIM BACK. "
   "Our spies in OR 5 say the new Boston surgeon and Dr. X were on the same side of the table, and that Dr. X caught something that 'saved the whole thing.' "
   "The new Boston surgeon reportedly said 'good catch.' Out loud. In front of witnesses. We don't know what to do with this information either.\"</i> Comments (412)."]),
 ("Medical Executive Committee: draft minutes (Bernadette Watkins)", "Monday, October 3, 2005, 6:30 AM",
  ["<b>Item 4.</b> Dr. Whitlow proposed that the Board of Trustees authorize a review of all Victor Donohue Foundation gifts, visits and relationships with QGH medical staff. "
   "Dr. Donohue noted twenty-seven years of Foundation grants predating her appointment. Mr. Bassett advised that the Board must authorize any review. "
   "<b>Action:</b> to the Board of Trustees, Thursday, October 20, 2005."]),
 ("SMS, Motorola RAZR (Raven Ellison and Arianna Cummings)", "Monday, October 3, 2005, 11:02 PM",
  ["<b>Raven:</b> \"you were good today. with tyrell\"", "<b>Arianna:</b> \"you held a pringle for 16 min. your hand still shaking?\"",
   "<b>Raven:</b> \"a little\"", "<b>Arianna:</b> \"ice it\"", "<b>Raven:</b> \"thats it? ice it?\"", "<b>Arianna:</b> \"...and you were good too. go to sleep ellison\""]),
 ("AIM: away message, AortaOrBust79 (Amond Baker)", "Monday, October 3, 2005, 11:55 PM",
  ["\"Asleep.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x02", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>Clayton's 30 days</b> (Sept 12 to Oct 11): day 22 is October 3. Sessions with <b>Dr. Paulette Greenidge, LCSW-R</b> (Montague Street, Brooklyn Heights) are Mondays and Thursdays at 6:30 PM; session 7 was October 3. <b>Revealed:</b> Clayton and Malcolm Sloan's affair was not one night but <b>six weeks</b>, from New Year's Eve 2004 (a party in Milton) to February 11, 2005. Esther: 'Stupid.' Clayton: 'Ashamed.' Clayton: 'We're the same kind of coward.' Esther wrote a draft text telling Marc and didn't send it.",
 "<b>Marc's 'Enough'</b> (11:12 AM, Elevator 4): no more one-ring calls at 2 AM (Esther had called and hung up at least three times), no more hallway looks. 'Decide it for you. Not for him. And not for me.' Marc turned down Daniella at Monty's ('half my attention'). He has run along Gantry Plaza every morning since September 12.",
 "<b>Marc and Clayton</b> did the first open fetal surgery in Queens: resection of a type I sacrococcygeal teratoma at 26 weeks 1 day (Crump; Clayton; Marc). <b>Marc caught a compressed umbilical cord</b> under the retractor during fetal bradycardia. Clayton: 'Good catch.' 'You're very good, Bullock.' 'That's inconvenient for both of us.' A professional truce.",
 "<b>Dr. Horace Whitlow</b> (Chief of Medicine) makes his on-screen debut. He moved that the Board review all Foundation relationships with QGH staff; the vote is <b>Thursday, October 20, 2005</b>. Count: 3 (Whitlow: Hollingsworth, Edmonds, a new bank trustee) to 3 (Natasha, including Mrs. Truitt), with <b>Rev. Ashworth and Judge Kittredge undecided</b>. Kittredge resents Victor over a 1994 Columbia gift. Whitlow requested the August 9 loading dock log and footage. <b>The dock camera has been broken since July</b> (work order on file; Big Ray did not break it). Whitlow saw 'BULLOCK, M. - PGY-1' in the directory and dismissed it ('a common name') for now. He gave Clayton his card, and Clayton kept it.",
 "<b>Big Ray</b> will not lie under oath (20 years NYPD), and Natasha will never ask him to. Robert urged that Marc decide when to reveal himself: 'Not your father's. Not the policy's. His.'",
 "<b>Amond:</b> pain 5-6/10. Hgb 12.1, down from 14.6 in July. <b>11:52 PM: he saw evidence of GI bleeding</b> (implied melena) and didn't call Robert. Odile: 'The water don't read the calendar.' Arianna, Robert, Lowery and Odile know he's sick; Monty knows about the blood count. <b>This sets up the Meckel's bleed in 2x03.</b>",
 "<b>Curtis Lemieux:</b> ISHLT grade 3A acute cellular rejection on his October 3 biopsy, treated with Solu-Medrol 1 g/day for 3 days. Odile Lemieux arrived from Houston (fig preserves from Baton Rouge for Amond), and Robert brought her red beans and cornbread.",
 "<b>Elxa</b> (21.5 weeks): Marc felt the baby kick from the outside, and then Russell did.",
 "<b>Harmony and Esther:</b> asked if she loves Marc, Harmony said 'Enough, Esther.' Harmony to Marc: 'Nobody believed me, so I hurt myself to prove it' was about 'a lot of people,' including Marc, Amond, Esther and herself.",
 "<b>Raven and Arianna:</b> 'You'd visit.' 'I'd bring beer.' Amond noticed.",
 "<b>Mrs. Truitt</b> confirms the 1990 punch story: Marc spilled it, and she took the blame."])
CONT.append(p("Knowledge Tracker (as of October 3, 2005)", H2))
CONT.append(tbl([["Secret", "Who knows", "New pressure"],
 ["Marc's family / Victor", "Family, Bernie, Graves, Gloria, Mrs. Truitt, Amond, Big Ray, Arianna, Esther", "<b>Whitlow</b> is investigating the August 9 visit. Clayton suspects; Monty suspects"],
 ["Affair lasted six weeks", "Esther, Clayton, Dr. Greenidge (and Malcolm)", "Marc doesn't know"],
 ["Amond's bleeding", "Amond only (as of 11:52 PM)", "Robert, Arianna, Odile, Lowery know he's sick"],
 ["Harmony loves Marc", "Raven, Esther (suspects strongly)", "Marc is starting to wonder"]],
 [1.8*inch, 2.6*inch, 2.0*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Tyrell Pickens", "6/7/1989 (16)", "GSW right upper quadrant (third GSW); grade IV liver laceration; bullet near the IVC", "Damage-control laparotomy, Pringle 16 min, packing (Elxa; Raven, Arianna)", "Alive. Second look in 48 h. Family moving to Rocky Mount, NC"],
 ["Booker Haines", "5/16/1941 (64)", "Trigeminal neuralgia, V2-V3, 12 years", "Microvascular decompression; superior cerebellar artery padded with Teflon (Graves; Esther)", "Pain-free"],
 ["Nadia Ellerbe / fetus", "4/25/1977 (28)", "Type I sacrococcygeal teratoma, 10 cm, with high-output failure, early hydrops and maternal mirror syndrome", "Open fetal debulking at 26w1d (Crump; Clayton; Marc)", "Pregnant; BP 138/88; FHR 148"],
 ["Curtis Lemieux", "4/9/1961 (44)", "ISHLT 3A acute rejection", "Endomyocardial biopsy; pulse Solu-Medrol (Robert; Amond)", "Treated; repeat biopsy next week"]],
 [1.05*inch, 0.9*inch, 1.65*inch, 1.75*inch, 1.0*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Tyrell 'Bird' Pickens</b> (b. June 7, 1989), <b>Kordell Pickens</b> (b. March 2, 1994) and <b>Lula Pickens</b> (b. February 11, 1941), an MTA station agent. Tyrell's mother was killed in 2001.",
 "<b>Booker Haines</b> (b. May 16, 1941), a retired A-train conductor, and <b>Mae Haines</b> (b. February 8, 1943).",
 "<b>Nadia Ellerbe</b> (b. April 25, 1977), an MTA bus operator; <b>Malik Ellerbe</b> (b. January 30, 1975), a Con Ed lineman; fetus 'Malik Jr.'",
 "<b>Dr. Paulette Greenidge</b> (b. August 1, 1955), couples therapist. <b>Det. Lawrence Fyffe</b> (b. November 21, 1966), 113th Precinct. <b>Daniella</b> (b. 1978), a Fordham Law student. Trustees named but unseen: Hollingsworth, Edmonds, Rev. Ashworth and Judge Kittredge."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["October 3, 2005: Marshall and Warren won the Nobel Prize for <i>H. pylori</i>; Marshall drank a culture in 1984. President Bush nominated Harriet Miers to the Supreme Court. The Yankees-Angels ALDS opened October 4. Baisley Park Houses (South Jamaica) is in the NYPD 113th Precinct.",
 "Medicine: open fetal resection of sacrococcygeal teratoma for high-output failure and hydrops was performed at a handful of centers (CHOP, UCSF) before 2005, and mirror (Ballantyne) syndrome is an indication. "
 "Damage-control laparotomy with a Pringle maneuver and perihepatic packing is standard; retained bullets near the IVC are left alone. Microvascular decompression (Jannetta) for trigeminal neuralgia uses Teflon felt. "
 "ISHLT 1990 grade 3A rejection was treated with pulse methylprednisolone. Meckel's diverticulum with ectopic gastric mucosa can cause painless or painful lower-GI bleeding."])
